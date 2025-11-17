# import random
# import string
# # N = 10_000
# # file_to_save = "task_1.txt"
# # def generate_random_letters():
# #     return random.choices(string.ascii_letters)
# with open("task_1.txt", "w", encoding="utf-8") as f:
#     for i in range(10_000):
#         letters = ''.join(random.choices(string.ascii_letters))
#         f.write(letters + "\n")

# # 3 task
# Letters={}
# with open("task_1.txt", "r", encoding="utf-8") as f:
#     letter = f.readlines()
#    " key 

# Task 1. Read first 3 rows from amazon.csv, display columns \
import csv
with open("data/amazon.csv", "r", encoding="utf-8") as f:
    for i in range(3):
        row = f.readline()
        print(row)
 
# # Task 2. Calculate image_url and display stats
# image_url_count = 0
# with open("data/amazon.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if row['image_url']:
#             image_url_count += 1