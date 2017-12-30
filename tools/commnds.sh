# Temporarily saving commands here.
python build.py
pandoc $(find ./topics -name "*.md") -o topics.pdf
