"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random

# สุ่มเลขระหว่าง 0 - 9
test_random = random.randint(1, 20)

print("-- เกมทายตัวเลข มาเดาใจคอมพิวเตอร์กันเถอะ --")
print("-- ทายเลขจำนวนเต็มตั้งแต่ 1 - 20 --")
print("-- คุณมีโอกาส 6 ครั้ง --")

for i in range(6):

    # รับค่าการทายเลขจากผู้ใช้
    print(f"ความพยายามครั้งที่ {i+1}")
    guess_number = int(input("What is your guess number (1-20)?: "))

    # condition ==> if-elif-else
    if test_random == guess_number:
        print("ยูเก่งมาก มั่วถูกตั้งแต่ครั้งแรกเลย เทพจริมๆ❤️")
        break
    elif guess_number < test_random:
        print("ผิดจ้า น้อยไปเนอะ 😒")
    elif  guess_number > test_random:
        print("ผิดจ้า มากไปหน่อย 🤣")
