#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:apple
# datetime:18/10/19 上午11:45
# software: PyCharm
from sympy import *
f, x, exp, C = symbols('f x exp C')


class ChooseSubject(object):
    express_1 = x
    express_2 = x
    final = x
    content = x

    def __init__(self, i):
        self.i = i

    def answer_number(self):
        if self.i == 1:
            self.content = '已知 $f( x ) = e ^ { x } \operatorname { cos } x +\arctan x$,求$f(x)$ 的导数，以及 $f^\prime(0)=2$'
            self.express_1 = Derivative(f(x),x)
            self.express_2 = -exp(x)*sin(x) + exp(x)*cos(x) + 1/(x**2 + 1)
            self.final = 2
        elif self.i == 2:
            self.content = '求不定积分 $ \int x \operatorname { sin }x dx $'
            self.express_1 = simplify(integrate(x*sin(x),x))
            self.express_2 = simplify(integrate(cos(x), x)-x*cos(x))
            self.final = simplify(integrate(cos(x), x)-x*cos(x)+C)
        elif self.i == 3:
            self.content = '证明函数 $f(x) = 5x^2log(x)-11x^2$ 的二阶导数无界'
            self.express_1 = Derivative(f(x), x)
            self.express_2 = simplify(10 * x * log(x, E) + 5 * x - 22 * x)
            self.final = simplify((10 + 10 * log(x, E) + 5 - 22).doit())
        else:
            pass
            self.content = '证明函数 $f(x) = 5x^2log(x)-11x^2$ 的二阶导数无界'
            self.express_1 = 1
            self.express_2 = 1
            self.final = f(0)


if __name__ == "__main__":
    ChooseSubject()