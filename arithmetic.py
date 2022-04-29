import random

count = 0
n = 0


def ask_user():
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    user_input = int(input())
    while user_input != 1 and user_input != 2:
        print('Incorrect format')
        user_input = int(input())
    return int(user_input)


def counter(good_bad):
    global count
    if good_bad:
        count += 1
    return 0


def is_numeric(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def eval_user(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Right!')
        counter(True)
    else:
        print('Wrong!')
        counter(False)


# def get_user_input():
#     user_input = input()
#     spited = user_input.split()
#     numbers = []
#     for e in spited:
#         if e.isnumeric():
#             numbers.append(int(e))
#     a, b = numbers
#     if '+' in user_input:
#         c = (a+b)
#     elif '-' in user_input:
#         c = (a-b)
#     elif '*' in user_input:
#         c = (a*b)
#     eval_user(c)

def get_user_input():
    user_input = input()
    while not is_numeric(user_input):
        print('Incorrect format')
        user_input = input()
    return int(user_input)  # problema posibila mai tarziu


def generate_random_problem():
    operator = ['+', '-', '*']
    if (user_type == 1):
        a, b = random.sample(range(2, 10), 2)
        random_op = random.sample(range(0, 3), 1)[0]
        random_operator = operator[random_op]
        print(a, random_operator, b)
        correct_answer = eval(f"{str(a)} {str(random_operator)} {str(b)}")
        return correct_answer
    else:
        a = random.sample(range(11, 30), 1)[0]
        print(a)
        return a * a

user_type = ask_user()

while (n < 5):
    eval_user(generate_random_problem(), get_user_input())
    n += 1

print(f"Your mark is {count}/5. Would you like to save the result? Enter yes or no.")
user_input = input().upper()
if(user_input == 'YES' or user_input == 'Y'):
    print("What is your name?")
    user_name = input()
    file = open('results.txt', 'a')
    if user_type == 1:
        user_type = '1 (simple operations with numbers 2-9)'
    else:
        user_type = '2 - integral squares 11-29'
    file.write(f'{user_name}: {count}/5 in level {user_type}')
    file.write("\n")
    file.close()
    print('The results are saved in "results.txt".')
