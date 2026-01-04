import random

def grade_random_func(score):
    if score>=90:
        print(f'you scored: {score}, and you got Grade A')
    elif score<90 and score>=70:
        print(f'you scored: {score}, and you got Grade B')
    else:
        print(f'Need Improvement, You scored {score} ')

for i in range(5):
    score = random.randint(1,100)
    grade_random_func(score)