#!/usr/bin/python3

import sys
import argparse
import random


class GRE2Anki(object):
    """
    Takes random word from list and adds it to deck
    """
    def __init__(self):
        self.lines = None
        self.word = None
        self.description = None
        # self.archived_words = self.load_archived()

    def load(self, path):
        try:
            f = open(path)
        except IOError:
            print("%s not found".format(path))
        self.lines = f.readlines()

    def load_archived(self, archive="archive.txt"):
        self.archive = open(archive, "rw+")

    def random_word(self):
        """
        Select a random word out of the loaded list.
        Exceptions can be added through the archive file.
        """
        try:
            random_pair = random.choice(self.lines)
        except:
            print("File has to be loaded first!")
        self.word, self.description = random_pair.split(None, 1)


def parse_file():
    """
    Parses command line and returns path string.
    Expected `python -f input.txt`.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        dest='file',
                        required=True,
                        help='Path of file to analyse')
    args = parser.parse_args()
    return (args.file)


def main():
    path = parse_file()
    g = GRE2Anki()
    g.load(path)
    g.random_word()
    print(g.word)
    print(g.description)
    # g.archive()
    # copy to xclip

if __name__ == "__main__":
    main()
