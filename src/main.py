from copy_to_source import *
from extract_title import *
from generate_page import *


def main():
    copy_to_source('./static','./public')
    generate_pages_recursive('./content', './template.html', './public')


if __name__ == "__main__":
    main()