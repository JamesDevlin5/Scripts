#!/usr/bin/env python3

import argparse
import urllib.request as req
from collections import defaultdict
from html.parser import HTMLParser


def create_arg_parser():
    parser = argparse.ArgumentParser(
        description="Get information regarding a websites HTML structure."
    )
    parser.add_argument(
        "--all", "-a", action="store_true", help="print all information available"
    )
    parser.add_argument(
        "--tag",
        "-t",
        action="append",
        metavar="TAG",
        dest="tags",
        help="get information regarding the target HTML tag(s) (repeatable for multiple search targets)",
    )
    parser.add_argument(
        "--summary",
        "-s",
        action="store_true",
        help="print a short summary of the information found",
    )
    parser.add_argument(
        "--sort",
        choices=["tag", "count", "none"],
        default="none",
        help="the means of sorting this report (default is none)",
    )
    parser.add_argument(
        "urls",
        nargs="+",
        metavar="URL",
        help="the URL to download the HTML file from",
    )
    return parser


def get_page(target):
    with req.urlopen(target) as t:
        return str(t.read())[2:-1]


class WebParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dict = defaultdict(lambda: 0)

    def handle_starttag(self, tag, attrs):
        self.dict[tag] += 1

    def handle_endtag(self, tag):
        # print("Encountered end: ", tag)
        pass

    def handle_data(self, data):
        # print("Encountered data: ", data)
        pass


class Printer:
    def __init__(self, left_len, right_len):
        self._l_len = left_len
        self._r_len = right_len

    def _print_row(self, left, right):
        print(f" | {left}|{right} | ")

    def _print_div(self, ch="="):
        print(" ", ch * (self._l_len + self._r_len + 4))

    def print_items(self, left, right):
        self._print_row(left.ljust(self._l_len), right.rjust(self._r_len))

    def print_title(self, left, right):
        self._print_div()
        self.print_items(left, right)
        self._print_div("-")

    def print_footer(self):
        self._print_div()


def parse_page(target):
    parser = WebParser()
    parser.feed(get_page(target))
    parser.close()
    return parser.dict


def summary(stats):
    print("  ", "Number of unique tags:".ljust(25), len(stats))
    print("  ", "Total number of tags:".ljust(25), sum(stats.values()))
    mode = max(stats.values())
    for attr, count in stats.items():
        if count >= mode:
            print(
                "  ", "Most common tag:".ljust(25), f"{attr}    ({count} occurrences)"
            )


def count_tags(urls):
    def merge_dict(acc, copy):
        for attr, count in copy.items():
            acc[attr] += count

    total = defaultdict(lambda: 0)
    for url in urls:
        merge_dict(total, parse_page(url))

    return total


def print_table(counts, targets, p_all):
    MIN_WIDTH = 10
    TAG_WIDTH = max(MIN_WIDTH, max(len(tag) for tag in counts.keys()) + 1)
    COUNT_WIDTH = max(MIN_WIDTH, max(len(str(count)) for count in counts.values()) + 1)

    out = Printer(TAG_WIDTH, COUNT_WIDTH)

    def p_items(attr, count):
        out.print_items(attr, str(count))

    out.print_title("Tag", "Count")
    if p_all:
        for attr, count in counts.items():
            p_items(attr, count)
    elif targets:
        for tag in targets:
            p_items(tag, counts[tag])
    else:
        p_items("none", 0)

    out.print_footer()


def run():
    args = create_arg_parser().parse_args()
    tag_count = count_tags(args.urls)

    if args.sort == "tag":
        tag_count = {
            k: v for k, v in sorted(tag_count.items(), key=lambda item: item[0])
        }
        if args.tags:
            args.tags = sorted(args.tags)
            print(args.tags)

    elif args.sort == "count":
        tag_count = {
            k: v for k, v in sorted(tag_count.items(), key=lambda item: item[1])[::-1]
        }
        if args.tags:
            pass

    print_table(tag_count, args.tags, args.all)

    if args.summary:
        summary(tag_count)


run()
