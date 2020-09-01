"""
@project: FM
@author: fanjinding
@time: 2020/1/14 11:46
"""
import doctest
def multiply(a, b):
    """
    fuction: 两个数相乘
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
if __name__ == '__main__':
    doctest.testmod(verbose=True)