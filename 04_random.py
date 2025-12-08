# можливості імпортів модулів в Python в залежності від потреби
# ---------------------------------------------------------------
# import random # radom.randrange(5)
# import random as r # r.randrange(10)
# from random import * # randrange(20)
# from random import randrange, randint # randrange(30) можно імпортовати одразу декілька модулів чере
# from random import randrange as rr # rr(40)
# ---------------------------------------------------------------
# comp_choice = random.randint(1, 10) # випадкове число від 1 до 10 включно
# print("Загадано число від 1 до 10. Спробуйте вгадати його.")
# user_choice = int(input("Вгадайте число від 1 до 10: "))
# while user_choice != comp_choice:
#     if user_choice < comp_choice:
#         print("Ваше число менше за загаданого.")
#     elif user_choice > comp_choice:
#         print("Ваше число більше за загаданого.") 
#     try:
#         user_choice = int(input("Спробуйте ще раз: "))
#     except ValueError:
#         print("Будь ласка, введіть коректне ціле число.")
#         continue
# print("Вітаємо! Ви вгадали число:", comp_choice)



# Oksana
# ---------------------------------------------------------------
# іменем модуля називати файли - ЗАБОРОНЕНО!!!

import random  # random.randrange(5)
# import random as r  # r.randrange(5)
# from random import *  # randrange(5)
#### from numpy import *
# from random import randrange, randint  # randrange(5)
# from random import randrange as rr  # rr(5)

comp_choice = random.randint(0,100)
n_count = 0
# user_choice = -1
# while True:
while n_count < 3:
    try:
        user_choice = int(input("Enter your number: "))
    except ValueError:
        print("Uncorrect number!")
        continue
    else:
        print("Excelent! I remember your number")
    finally:
        n_count += 1
        print(f"Your attempt {n_count}")
        # print(f"Your choice")
        
    # if
    
    if user_choice == comp_choice:
        print("Congratulations")
        break
    # elif
    # else
    print("Try again!")