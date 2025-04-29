import logging
import random
from faker import Faker
# import os
import time
import traceback

logging.basicConfig(
    filename='app.log'
    , level=logging.INFO
    , format='%(asctime)s - %(levelname)s - %(message)s'
)

faker = Faker()


def write_to_file(data):
    print(data)
    try:
        if random.random() < 0.2:
            raise PermissionError(f"You can't do this: {data}")

        if random.random() > 0.2 and random.random() < 0.3:
            data = None

        with open('db.txt', 'a') as file:
            file.write(' | '.join(data) + '\n')

    except Exception as e:
        logging.error(f'Something wrong with append: {str(e)}')

        logging.error(f'Traceback is: {str(traceback.format_exc())}')

    else:
        logging.info('All done')


def generate_data():
    user = faker.first_name()
    email = faker.email()
    active = ['read', 'go to db', 'buy', 'cancelled', 're-do']

    return [user, email, active[random.randint(0, 4)]]


while True:
    data = generate_data()
    write_to_file(data)
    time.sleep(4)

#
#
# try:
#     number = int(input('Enter you number: '))
#     print(10 / number)
# except Exception as e: # Zero
#     print(f'Something wrong in user int value. Error is {e}')
#
# import logging
#
# logging.info()
# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s %(traceback)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
#
#
# def task1():
#     logging.info('Start function1')
#     pass
#     logging.info('End function 1')
#
#
# def task2():
#     pass
#
# age = 1
# if age < 0:
#     raise ValueError("Вік не може бути від'ємним")
#
#
# # password = 'password123'
# #
# # class MyCustomError(Exception): # version lib, error, user, date,
# #     pass
# #
# #
# # if password == "password123":
# #     raise MyCustomError("Занадто простий пароль!")
#
# # class EmptyListError(Exception):
# #     pass
# #
# # def process_list(data):
# #     if not data: # len(data) > 0, None
# #         raise EmptyListError("Список порожній")
# #
# # try:
# #     process_list([])
# # except TypeError as e:
# #     raise EmptyListError("Передано не список") from e
#
#
# class MyCustomError(Exception):
#     pass
#
#
# class ValueTooSmallError(Exception):
#     def __init__(self, value, limit):
#         self.value = value
#         self.limit = limit
#         message = f"Значення {value} менше допустимого {limit}" # 120 60
#         super().__init__(message)
#
#
# def check_age(age):
#     if age < 18:
#         raise ValueTooSmallError(age, 18)
#
# # try:
# #     check_age(15)
# # except ValueTooSmallError as e:
# #     print(e)
