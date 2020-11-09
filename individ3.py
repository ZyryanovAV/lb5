#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    word = input("Введите слово: ")
    newWord = word[len(word) - 1] + word[:-1]
    print(newWord)
