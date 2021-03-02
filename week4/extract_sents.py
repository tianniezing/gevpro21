#!/bin/python3
# Program: extract_sents.py
# Author: Tian Niezing
# Date: 02-03-2021


import gzip
import sys
import re


def line_to_sentence_string(inp):
    """This function makes a list of the lines from the \
    input file and returns the sentences as a text"""
    line_list = []
    for line in inp:
        line = line.replace('\n', '')
        line_list.append(line)
    without_intro_outro = line_list[4:-7]
    text = ''.join(without_intro_outro)
    split_sentences = re.compile('[^.!?]*[.!?]', re.DOTALL)
    sentence_text = ''.join(split_sentences.findall(text))
    return sentence_text


def make_sentence_per_line(inp):
    """This function uses the output of the line_to_sentence_string function \
     as input and places spaces around punctuation marks and digits"""
    sentences = line_to_sentence_string(inp)
    sentence_string = ''.join(sentences)
    words = re.compile(r'([0-9]|[a-zA-Z]+\'s|[a-zA-Z]+|[^\s\w])')
    sentence_string_with_space = ' '.join(words.findall(sentence_string))
    return sentence_string_with_space


def exception_rules(inp):
    """This function deals with the special exeptions"""
    split_text = make_sentence_per_line(inp)
    newline = re.compile(r'([.?])\s(")|([.?])\s')
    digits = re.compile(r'([0-9])\s')
    digit_with_char = re.compile('([0-9])([a-zA-Z])')
    punct_after_digit = re.compile('([0-9]+)([.?,])')
    indent_digit = re.compile(r'\s([0-9]-|[a-zA-Z]-)\s')
    indent_char = re.compile(r'\s(-)\s')
    indent_w_space = re.compile(r'(-)\s([0-9])')
    letter_dot_space_quote = re.compile(r'([a-zA-Z])([.?!])\s')
    fixed = re.compile('([.])\n(["])')

    newline = re.sub(newline, r'\3\2\n', split_text)
    digits = re.sub(digits, r'\1', newline)
    digit_with_char = re.sub(digit_with_char, r'\1 \2', digits)
    punct_after_digit = re.sub(punct_after_digit, r'\1 \2', digits)
    indent_digit = re.sub(indent_digit, r'\1', digit_with_char)
    indent_char = re.sub(indent_char, r'\1', indent_digit)
    indent_w_space = re.sub(indent_w_space, r'\1\2', indent_char)
    letter_dot_space_quote = re.sub(letter_dot_space_quote, r'\1\2\n', newline)
    fixed = re.sub(fixed, r'\1\2', indent_w_space) + '\n'
    return fixed


def main(argv):
    """This function converts a txt file to a gzip and uses that as input, \
    also this function checks if the cmd arguments are equal to 2 or not"""
    with gzip.open(sys.argv[1], 'rt', encoding='utf8') as inp:
        if len(argv) != 2:
            print("The amount of arguments are not equal to 2, \
            you have to have the program name as first argument \
            and the file name as second argument.".format(file=sys.stderr))
            exit(-1)
        else:
            print(exception_rules(inp))


if __name__ == '__main__':
    main(sys.argv)
