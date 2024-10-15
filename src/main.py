from copy_to_source import *
from extract_title import *
from generate_page import *


def main():
    copy_to_source('./static','./public')
    generate_page('./content/index.md', './template.html', './public/index.html')


if __name__ == "__main__":
    main()