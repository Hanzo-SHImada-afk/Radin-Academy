#1
lst=[15,18.5,16,13,19,11]
count = 0
for i in lst:
    if i >17:
        count+=1
print(count)

for i in range(len(lst)):
    lst[i] += 1
print(lst)

lst.pop(2)   
avg = sum(lst) / len(lst)
print(avg)
#2
lst = [67, 83, 55, 91, 64, 72, 89, 102]

new_lst = []

for i in lst:
    if 80 <= i <= 100:
        new_lst.append(i)

print(new_lst)

for i in lst:
    if i < 80:
        print("مجاز")
    elif i <= 100:
        print("اخطار")
    else:
        print("غیرمجاز")
#3
lst = [12, 16.5, 15, 18, 19, 17.25]

new_lst = []

for i in lst:
    if i < 18:
        new_lst.append(i)

print(new_lst)


bozorg = max(lst)
koochak = min(lst)

print(bozorg - koochak)


for i in range(len(lst)):
    lst[i] = lst[i] - 1

print(lst)
#4
for i in range(5, 31):
    if i % 2 == 1:
        print(i)
#5
sum_even = 0

for i in range(2, 21, 2):
    sum_even += i

print(sum_even)
#6
lst = []

for i in range(1, 21):
    lst.append(i)

avg = sum(lst) / len(lst)

print(lst)
print(avg)

#7
import random

lst = []

for i in range(40):
    lst.append(random.randint(1,100))

print(lst)

count = 0

for i in lst:
    if i % 3 == 0:
        count += 1

print(count)

#8
import random

dice = []

for i in range(100):
    dice.append(random.randint(1,6))

print(dice)

print(dice.count(6))

print(sum(dice))

count = 0

for i in dice:
    if i > 4:
        count += 1

print(count)

#9
n = int(input("عدد را وارد کنید: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)
#10
count = 0

for i in range(10):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    if d1 == 6 and d2 == 6:
        count += 1

print(count)

#11
s = 0

for i in range(2,101,2):
    s += i/(2*i)

print(s)

#12
num = int(input("عدد را وارد کنید: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)


#13
count = 0

for i in range(10):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    if d1 == 6 and d2 == 6:
        count += 1

print(count)

#14
s = 0

for i in range(2,101,2):
    s += i/(2*i)

print(s)

#15
def tedad_maghsom_alaih(n):
    count = 0

    for i in range(1,n+1):
        if n%i==0:
            count +=1

    print(count)

tedad_maghsom_alaih(12)

#16
def check(n):
    if n % 5 == 0:
        print("درست")
    else:
        print("نادرست")

check(20)

#17
def average(a,b,c,d):
    avg = (a+b+c+d)/4
    print(avg)

average(18,17,19,20)

#18
new_lst = []

for i in range(10):
    x = float(input("نمره: "))

    if x < 10:
        x = 10

    new_lst.append(x)

print(new_lst)

#19
def find_min_max(lst):

    maximum = lst[0]
    minimum = lst[0]

    for i in lst:
        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i

    print("بزرگترین:", maximum)
    print("کوچکترین:", minimum)

find_min_max([5,8,2,15,9])
#20
lst = []

for i in range(20):
    lst.append(random.randint(1,20))

print(lst)

repeat = 0

for i in set(lst):
    if lst.count(i) > 1:
        repeat += 1

print(repeat)

#21
import random

password = ""

for i in range(6):
    password += str(random.randint(0, 9))

print(password)

user = input("رمز را وارد کنید: ")

if user == password:
    print("درست")
else:
    print("اشتباه")

#22
# names = ["علی", "رضا", "سارا"]
grades = [18, 7, 9]

for i in range(3):
    if grades[i] < 10:
        print(names[i])

#23
import random

num = random.randint(1, 100)

guess = 0

while guess != num:
    guess = int(input("حدس بزن: "))

    if guess < num:
        print("بزرگ‌تر")
    elif guess > num:
        print("کوچک‌تر")

print("درست است")

#24
import random

count = 0
dice = 0

while dice != 6:
    dice = random.randint(1, 6)
    count += 1

print(count)


#24
text = input("رشته: ")

done = ""

for i in text:
    if text.count(i) > 1 and i not in done:
        print(i)
        done += i

#25
a = float(input("عدد اول: "))
op = input("عملگر: ")
b = float(input("عدد دوم: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("عملگر نامعتبر است")



#26
n = int(input("عدد را وارد کنید: "))

count = 0

for i in range(2, n + 1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        count += 1

print("تعداد اعداد اول:", count)




#27
text = input("رشته را وارد کنید: ")

big = 0
small = 0
number = 0
space = 0

for i in text:
    if i.isupper():
        big += 1
    elif i.islower():
        small += 1
    elif i.isdigit():
        number += 1
    elif i == " ":
        space += 1

print("حروف بزرگ:", big)
print("حروف کوچک:", small)
print("ارقام:", number)
print("فاصله‌ها:", space)

#28

numbers = input("اعداد را با فاصله وارد کنید: ").split()

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)

#29
grades = []

for i in range(10):
    grade = float(input("نمره را وارد کنید: "))
    grades.append(grade)

average = sum(grades) / 10

count = 0

for grade in grades:
    if grade > average:
        count += 1

print("میانگین:", average)
print("بیشترین:", max(grades))
print("کمترین:", min(grades))
print("تعداد بالاتر از میانگین:", count)



#30
text = input("متن را وارد کنید: ")

new_text = ""

for i in text:
    if i == "Z":
        new_text += "A"
    elif i == "z":
        new_text += "a"
    elif i.isalpha():
        new_text += chr(ord(i) + 1)
    else:
        new_text += i

print(new_text)


#31
import random

number = random.randint(1, 100)

while True:
    guess = int(input("حدس شما: "))

    if guess == number:
        print("درست حدس زدی!")
        break
    elif guess < number:
        print("عدد بزرگ‌تر است")
    else:
        print("عدد کوچک‌تر است")


#32


import random

dice = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    number = random.randint(1, 6)
    dice[number - 1] += 1

for i in range(6):
    print(i + 1, ":", dice[i])



