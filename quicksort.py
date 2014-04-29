#! /usr/bin/env python2.7

""" 快速排序的练习程序
"""

class QuickSort(object):
    """ 快速排序类
    """

    def __init__(self, data = ()):
        if data: self.data = list(data)

    def sort(data = ()):
        """ 实际排序
            Args:
                data: 调用者可以给出需要排序的数列，如果为空则默认在对象实例初始化
                    之时已经给出了输入数列

            Returns:
                返回排好序的结果，list 数据格式

            Raises:
                IOError: 如果没有给出输入数列，直接报错
        """

        if data:
            self.data = None    # 置空之前的数列
            self.data = list(data)

        if self.data.count() == 0:
            raise IOError

        # TODO: TDD 先
        
