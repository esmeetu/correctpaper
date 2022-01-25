#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sympy import *
from .right_answer import *
import re
from latex2sympy.process_latex import process_sympy
f, x, t, exp = symbols('f x t exp')


class ComAnw(object):
    step = []
    separate = []
    formal = []
    score = 0
    print_out_1 = ''
    print_out_2 = ''
    print_out_3 = ''

    def __init__(self, draft, express_1, express_2, final):
        self.draft = draft
        self.express_1 = express_1
        self.express_2 = express_2
        self.final = final
        self.split_str = []
        self.math_formal = []

    def splitting(self):
        self.draft = self.draft.replace("\operatorname { cos }", "\\cos")
        self.draft = self.draft.replace("\operatorname { sin }", "\\sin")
        self.draft = self.draft.replace("- \\int x d \\cos x", " \\int x \\sin x d x")
        self.draft = self.draft.replace(" \\int x d \\cos x", " -\\int x \\sin x d x")
        self.draft = self.draft.replace("f ^ { \prime } ( x )",  "\\frac{df(x)}{dx}")
        self.draft = self.draft.replace("e ^ { x }", "\exp(x)")
        self.draft = self.draft.replace("\\operatorname { log } x", "\\ln x")
        self.step = re.split(r",", self.draft)
        self.separate = re.split(r"=", self.draft)
        for ne in self.separate:
            lie = re.split(r",", ne)
            for self.i in lie:
                self.split_str.append(self.i)
            print(self.split_str)
    def grade(self):
        for self.line in self.split_str:
            self.formal = process_sympy(self.line)
            self.math_formal.append(self.formal)
        if (simplify(self.math_formal[1].doit()) == simplify(self.express_2)) & (
                simplify(self.math_formal[0].doit()) == simplify(self.express_1)):
            self.print_out_1 = '第一步正确，得2分'
            self.score = 2
            if simplify(self.math_formal[len(self.math_formal)-1].doit()) == simplify(self.final):
                self.print_out_2 = '第二步正确，得2分'
                self.print_out_3 = '所有步骤都正确，总得分:'
                self.score += 2
            else:
                self.print_out_2 = '第二步错误，得0分'
                self.print_out_3 = '没有完全正确，总得分:'
                self.score = 2
        else:
            self.print_out_1 = '第一步错误，得0分'
            self.print_out_2 = '第二步错误，得0分'
            self.print_out_3 = '全错，总得分:'
            self.score = 0


if __name__ == "__main__":
    ComAnw()
