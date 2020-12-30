print('SHA1')
# import
import hashlib

# create sha1 object
sha1 = hashlib.sha1()
# encrypt this string by update fuc
sha1.update('You are the best to solve this'.encode('utf-8'))
# print cipher text
print(sha1.hexdigest())

from random import randint
from sympy import *  # 引入包


def play():
    random_int = randint(0, 100)
    while True:
        user_guess = int(input('What number did we guess (0-100)?'))
        if user_guess == random_int:
            print(f'You found the number({random_int}).Congrats!')
            break
        if user_guess < random_int:
            print('Your number is less than the number we guessed.')
            continue
        if user_guess > random_int:
            print('Your number is more than the number we guessed.')
            continue


def Just_Kidding():
    Choice = input('Do you wanna know this equation of answer? (Y/N)\n'
                   '--> x + y + 2 * x * y = 83\n'
                   '--> solve x + y\n')
    over = [[0] * 3 for i in range(2000)]
    idx = 0
    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            if x + y + 2 * x * y == 83:
                idx += 1
                over[idx][0] = f'x + y = {x + y}'
                over[idx][1] = f'x = {x}'
                over[idx][2] = f'y = {y}'
    # NewList = [x for x in OldList if x]  # 删除空列表[]
    # filter(lambda x: x != [0, 0, 0], over)

    over_ptr = over[:]
    for Ready2Del in over_ptr:
        if Ready2Del == [0, 0, 0]:
            over.remove(Ready2Del)
    del over_ptr

    if Choice == 'Y':
        for LineFeed in range(0, len(over), 1):
            print(f' ***** {over[LineFeed]} ***** ')
    else:
        print('GO TO THE HELL!')

    # print(over)


class Calories:
    def __init__(calories, date, breakfast, lunch, dinner, snack):
        calories.date = date
        calories.breakfast = breakfast
        calories.lunch = lunch
        calories.dinner = dinner
        calories.snack = snack

    def dailyTotalCalories(self):
        sum = self.breakfast + self.lunch + self.dinner + self.snack
        print('Calorie content for', self.date, ':', sum)


if __name__ == '__main__':
    # play()
    # Just_Kidding()

    # below are 20201024 pm test
    # follow the microsoft learning to practice
    print('fuck')
    print('which one do you fuck, please input her name')
    name = input()
    if name == 'no':
        print('no no no no no no no')
    else:
        print('this is who you are ready to fuck -> ', name)

    print('please input first number')
    firstNum = int(input())
    print('then please input next number')
    secondNum = int(input())
    sum = firstNum + secondNum
    print('your input num sum is -> ', sum)

    print('Today\'s date?')
    date = input()
    print('Breakfast calories?')
    breakfast = int(input())
    print('Lunch calories?')
    lunch = int(input())
    print('Dinner calories?')
    dinner = int(input())
    print('Snack calories?')
    snack = int(input())

    total = Calories(date, breakfast, lunch, dinner, snack)
    total.dailyTotalCalories()

    # test end

    x = symbols('x')  # 声明变量'x'
    expr = exp(exp(x))
    i_expr = integrate(expr, x)
    # print(Eq(a, a.doit()))
    print(i_expr)

    # print(Ei(exp(2))).n(chop=True)
