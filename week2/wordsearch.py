#!/bin/python3
# Program: wordsearch.py
# Author: Tian Niezing
# Date: 14-02-2021
#

import json
import argparse


def solve(puzzle_file, json_file):
    with open(json_file) as inp:
        possible_words = json.load(inp)

    with open(puzzle_file) as puzzle:
        puzzle_words = puzzle.read().lower()
        puzzle_words_list = puzzle_words.split()

    word_list_casesensitive = list(possible_words['words'])
    word_list = [word.lower() for word in word_list_casesensitive]

    vert_list = []
    horiz_list = [word.upper() for word in word_list if word in puzzle_words]

    for i in range(len(puzzle_words_list)):
        first_letters = ''.join([letters[i] for letters in puzzle_words_list])
        for i in word_list:
            if i in first_letters.lower():
                vert_list.append(i.upper())

    return set(horiz_list + vert_list)


def main(puzzle_file, json_file):
    print(solve(puzzle_file, json_file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Finds words \
        from a word puzzle horizontally and vertically')
    parser.add_argument('puzzle_file', help='Puzzle file name in .txt')
    parser.add_argument('json_file', nargs='?', help='File with \
        possible words in .json', default='words.json')
    args = parser.parse_args()
    main(args.puzzle_file, args.json_file)
