# _*_ coding: utf-8 _*_
__auther__ = "tanran"
__date__ = "2019/1/28 23:03"


def is_isbn_or_key(word):
    """
    :param word:判断是否是isbn
    :return:返回是否是isbn结果
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key