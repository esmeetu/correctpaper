#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  import sys
import json
import os
import json
import uuid
import base64
import requests
from .sympy_proof import *


# Define print results under different subject##########
def out_print(rate, j, written_ans):
    if rate < 0.1:
        print("书写不清楚，请重新提交答案")
        return json.dumps({'answer': '书写不清楚，请重新提交答案'})
    else:
        get_number = ChooseSubject(j)
        get_number.answer_number()
        if j in [1, 2, 3]:
            get_anw = ComAnw(written_ans, get_number.express_1, get_number.express_2, get_number.final)
            get_anw.splitting()
            get_anw.grade()
            print(get_anw.math_formal[0])
            print(get_number.express_1)
            print('$', get_anw.step[0], '$')
            print(get_anw.print_out_1)
            print('$', get_anw.step[len(get_anw.step) - 1], '$')
            print(get_anw.print_out_2)
            print(get_anw.print_out_3, get_anw.score)
            res = {'totalScore': get_anw.score,
                   'step1_tex': get_anw.step[0],
                   'step1': get_anw.print_out_1,
                   'step2_tex': get_anw.step[len(get_anw.step) - 1],
                   'step2': get_anw.print_out_2,
                   'step3': get_anw.print_out_3}
        else:
            proof = ProofAnw(written_ans, get_number.express_1, get_number.express_2, get_number.final)
            proof.splitting()
            proof.grade()
            print_out = [proof.print_out_1, proof.print_out_2, proof.print_out_3]
            i = 0
            for lli in proof.step:
                print('$', lli, '$')
                print(print_out[i])
                i += 1
                print(proof.score)
            res = {'totalScore': proof.score,
                   'step1_tex': proof.step[0],
                   'step1': proof.print_out_1,
                   'step2_tex': proof.step[1],
                   'step2': proof.print_out_2,
                   'step3_tex': proof.step[2],
                   'step3': proof.print_out_3}
        res['answer'] = written_ans
        return json.dumps(res)
# recognize image and print out results
# put desired file path here
# accuracy of handwriting recognition#
# j present the number of subject

# 输入要选择得题目类型: proof or
# 输出题号

# classify = raw_input("您要选择的题目类型(print proof_ or com_) :")
# number = raw_input("您要选择的题号(输入1－4) :")
#
# try:
#     file_path = classify+str(number)+'.jpg'
#     image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read())
#     r = requests.post("https://api.mathpix.com/v3/latex",
#                       data=json.dumps({'src': image_uri}),
#                       headers={"app_id": '',
#                                "app_key": '',
#                                "Content-type": "application/json"})
#     re_rate = json.loads(r.text)['latex_confidence']
#     put = json.loads(r.text)['latex']
#
# except TypeError:
#     print("TypeError:请重写答案!")
# except ValueError:
#     print("ValueError:请重写答案!")
# except IOError:
#     print("IOErrors:请重写答案!")
# else:
#     out_print(re_rate, int(number), put)

