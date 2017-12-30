from jinja2 import nodes, contextfunction
from jinja2.ext import Extension

class NotesExtension(Extension):
    tags = set(['topic', 'topicl', 'tag'])

    def __init__(self, environment):
        super().__init__(environment)
        self.active_tags = []

    def parse(self, parser):
        current_tag = next(parser.stream)
        end_tag = "end" + current_tag.value
        lineno = current_tag.lineno

        # Get topic name.
        if current_tag.value.startswith("topic"):
            topic = parser.parse_expression()
        else:
            topic = nodes.Const(None)

        # Get topic tags.
        if parser.stream.skip_if("comma") or current_tag.value == "tag":
            topic_tags =  parser.parse_expression()
        else:
            topic_tags = nodes.List([])

        # Update active tag list.
        if not topic.value:
            self.active_tags.extend(map(lambda x: x.value, topic_tags.items))

        # Get bodym if any.
        if current_tag.value == "topicl":
            body = []
        else:
            body = parser.parse_statements(["name:" + end_tag], drop_needle=True)

        # Get parsed node.
        return_value = nodes.CallBlock(self.call_method("_notes_helper", [topic, topic_tags]), [], [], body).set_lineno(lineno)

        # Update active tag list.
        if not topic.value:
            self.active_tags = self.active_tags[:-len(topic_tags.items) or None]

        return return_value

    def _notes_helper(self, topic, tags, caller):
        if topic:
            tags_string = ""
            if tags:
                tags_string += ",".join(map(lambda x: "[{0}]".format(x), tags)) + ","
            if self.active_tags:
                tags_string += ",".join(map(lambda x: "[{0}]".format(x), self.active_tags))
            if tags_string:
                tags_string = "<sub><sup>Tags: {0}</sup></sub>\n".format(tags_string)
            # Perhaps tags should not be added to the document.
            tags_string = ""

            topic_header = "## {0}\n{1}".format(topic, tags_string)

            # Indent text by a level
            text = caller().replace("\n", "\n> ")[:-2]
            if text:
                text = "> " + text

            return topic_header + text
        return "" + caller()
