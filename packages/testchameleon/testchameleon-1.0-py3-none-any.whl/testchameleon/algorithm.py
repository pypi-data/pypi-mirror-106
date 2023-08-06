# !/usr/bin/python3 
# -*- coding: utf-8 -*-

class AlgorithmDemo(object):

    def __init__(self):
        pass

    def demo_one(self):
        """
        冒泡排序用法
        :return:
        """
        data = [32,25,95,68,12,73,65]
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    def demo_two(self):
        pass


class RunDemo(AlgorithmDemo):

    def run_one(self):
        demo = self.demo_one()
        return demo

    def run_two(self):
        pass
