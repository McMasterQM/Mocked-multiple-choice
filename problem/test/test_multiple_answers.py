# from ..m_choice import *
import numpy as np
import re
from numpy.testing import assert_equal, assert_allclose



d_pat = r'\d+.\d*'
let_pat = r'[A-Z]'
right_answers = [
    {'a', 'b', 'e'},
    {'a', 'c', 'e', 'f'},
    3.336e-10
]

i = 0
score = 0
answer = '**Answer**'
with open(r"../m_choice.py", 'r') as f:
    for line in f.readlines():
        if answer in line:
            ind = line.find(answer) + len(answer)
            new_line = line.upper()[ind:]
            answers_digits = [float(x) for x in re.findall(d_pat, new_line)]
            answers_letters = set(re.findall(let_pat, new_line))

            if answers_letters == right_answers[i] or\
                (len(answers_digits)>0 and np.allclose(answers_digits, right_answers[i])):
                score += 1
            i += 1

print(f"Your score is {score}/{len(right_answers)}")


