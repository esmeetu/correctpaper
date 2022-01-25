#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:apple
# datetime:18/10/30 上午12:34
# software: PyCharm

from .sympy_com import *


class ProofAnw(ComAnw):
    split_str = []

    def __init__(self, draft, express_1, express_2, final):
        super(ProofAnw, self).__init__(draft, express_1, express_2, final)

    def splitting(self):
        self.draft = self.draft.replace("\\operatorname { sin }", "\\sin")
        self.draft = self.draft.replace("\\left. \\begin{array} { l } ", ' ')
        self.draft = self.draft.replace("\\end{array} \\right.", ' ')
        self.step = re.split(r"\\\\", self.draft)
        print(self.step)
        self.separate = self.step
        for ne in self.separate:
            lin = re.split(r"=", ne)
            self.split_str.append(lin[-1])
        print(self.split_str)

    def grade(self):
        return super(ProofAnw, self).grade()


if __name__ == "__main__":
    ProofAnw()
