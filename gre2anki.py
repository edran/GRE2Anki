#!/usr/bin/python
"""
Overview
========
Chooses a GRE word from a list of nearly 4000 words and outputs its
description. You can then copy that in Anki or other SRS software.
Every time you run the script, the random word will be added to
`archive.txt`, which will stop the word from appearing again. In case
you want to start over, just delete `archive.txt`.

Usage
=====
`$ python gre2anki.py`
--------------------
"""
import argparse
import random


class BCS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class GRE2Anki(object):
    """
    Takes random word from list and adds it to deck
    """
    def __init__(self):
        self.lines = None
        self.word = None
        self.description = None
        self.path_archive = "archive.txt"
        self.load_archived()

    def load(self, path):
        """
        Load file and split the lines.
        """
        try:
            f = open(path)
        except IOError:
            print("{} not found".format(path))
        self.lines = f.readlines()

    def load_archived(self, path_archive="default"):
        """
        Load list of archived words into class.
        """
        if path_archive == "default":
            path_archive = self.path_archive
        print("Loading archive at {}".format(path_archive))
        self.word_archive = open(path_archive, "a+")
        al = self.word_archive.readlines()
        self.archived_words = [w.split(None, 1)[0] for w in al]

    def random_word(self):
        """
        Select a random word out of the loaded list.
        Exceptions can be added through the word_archive file.
        """
        try:
            random_pair = random.choice(self.lines)
        except:
            print("File has to be loaded first!")
        self.word, self.description = random_pair.split(None, 1)
        if self.word in self.archived_words:
            print(BCS.FAIL
                  + "{} has already been archived. Loading other word.".format(
                      self.word)
                  + BCS.ENDC)
            self.random_word()

    def archive_word(self):
        """
        Archive previously found random word.
        """
        s = self.word + "\t" + self.description
        self.word_archive.write(s)
        print("{} has been archived in {}".format(self.word,
                                                  self.path_archive))

    def __str__(self):
        s = BCS.WARNING + "===================" + BCS.ENDC + "\n"
        s += "The random word is: " + BCS.OKGREEN + self.word + BCS.ENDC + "\n"
        s += "Its description is: " + BCS.OKBLUE + self.description + BCS.ENDC
        s += BCS.WARNING + "===================" + BCS.ENDC
        return s


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
    pass


def parse_input():
    """
    Parses command line and returns path string.
    Expected `python -f input.txt`.
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=CustomFormatter)
    parser.add_argument('-f', '--file',
                        dest='file',
                        required=False,
                        help='Path of file to analyse',
                        default="share/GRE_WORDS.txt")
    args = parser.parse_args()
    return (args.file)


def main():
    path = parse_input()
    g = GRE2Anki()
    g.load(path)
    g.random_word()
    g.archive_word()
    print(g)
    # copy to xclip

if __name__ == "__main__":
    main()
