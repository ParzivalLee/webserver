"""
@filename String.py
@author Parzival
@encoding utf-8
@date utf-8
@description 字符处理相关工具
"""
import random
import string

chars: str = string.ascii_letters + string.digits
byte_chars: bytes = (string.ascii_letters + string.digits).encode(encoding='utf-8')
byte_letters: bytes = string.ascii_letters.encode(encoding='utf-8')
byte_digits: bytes = string.digits.encode(encoding='utf-8')


# 获取随机字符串
def get_rand_str(size: int) -> str:
    """
    获取随机字符串
    :param size: 字符串长度
    :return: 随机字符串
    """
    rand_str: str = ''
    for i in range(size):
        rand_str += chars[random.randrange(0, 62)]
    return rand_str


# 获取随机数字字符串
def get_rand_digit(size: int) -> str:
    """
    获取随机数字字符串
    :param size: 字符串长度
    :return: 随机字符串
    """
    rand_str: str = ''
    for i in range(size):
        rand_str += string.ascii_letters[random.randrange(0, 10)]

    return rand_str


# 获取随机字母字节串
def get_rand_letters(size: int) -> str:
    """
    获取随机字母字节串
    :param size: 字节串长度
    :return: 随机字节串
    """
    rand_str: str = ''
    for i in range(size):
        rand_str += string.ascii_letters[random.randrange(0, 52)]

    return rand_str


# 获取随机字节串
def get_rand_bytes(size: int) -> bytes:
    """
    获取随机字节串
    :param size: 字节串长度
    :return: 随机字节串
    """
    rand_bytes: bytes = b''
    for i in range(size):
        rand_bytes += byte_chars[random.randrange(0, 62)]
    return rand_bytes


# 获取随机数字字节串
def get_rand_digit_bytes(size: int) -> bytes:
    """
    获取随机数字字节串
    :param size: 字符串长度
    :return: 随机字节串
    """
    rand_bytes: bytes = b''
    for i in range(size):
        rand_bytes += byte_digits[random.randrange(0, 10)]

    return rand_bytes


# 获取随机字母字节串
def get_rand_letters_bytes(size: int) -> bytes:
    """
    获取随机字母字节串
    :param size: 字节长度
    :return: 随机字节串
    """
    rand_bytes: bytes = b''
    for i in range(size):
        rand_bytes += byte_letters[random.randrange(0, 52)]

    return rand_bytes
