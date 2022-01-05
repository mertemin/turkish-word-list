#!/usr/bin/python
# -*- coding: utf8 -*-

import requests
import re


alphabet = "ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"


def read_page(letter):
    url = f"http://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_({letter})"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Charset": "ISO-8859-9,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "none",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive",
    }

    req = requests.get(url.encode("utf-8"), headers=headers)
    content = req.text

    words = re.findall("<li><a[^>]*>([^<]+)<\/a>", content, flags=0)
    words.pop()
    print("Read the letter ", letter)
    return words


def get_word_list():
    words = []
    for letter in alphabet:
        words += read_page(letter)
    return words


def write_to_file(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(get_word_list()))


write_to_file("words.txt")
