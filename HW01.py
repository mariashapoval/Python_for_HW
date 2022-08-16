#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("My name is ", name, "my age is ", age)

#2. Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time = int(input("Enter time in seconds: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes *60)
print(f"time format hh:mm:ss {hours} : {minutes} : {seconds}")

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input("Enter the number: "))
summ = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Summ of numbers is n + nn + nnn - %d" % summ)

#4. Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = input("Enter number: ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(x)

#5. Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
profit = float(input("Revenue of the firm "))
costs = float(input("Costs of the firm "))
if profit > costs:
    print(f"Firm has benefits. profitability of revenue is  {profit / costs:.2f}")
    workers = int(input("Employees  "))
    print(f"Profit per one employee is  {profit / workers:.2f}")
elif profit == costs:
    print("There is no revenue and costs")
else:
    print("Firm has losses")

#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = float(input("Enter start: "))
b = float(input("Enter finish: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)

