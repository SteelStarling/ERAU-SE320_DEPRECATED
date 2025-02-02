mylist = [1, 2, 3, 4, 5]

print("==EX01==")

lx = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, mylist)))

print(lx)

lx = [x * x for x in mylist if x % 2 == 1]

print(lx)

print("==EX02==")

print([2 ** x for x in mylist])

print(list(map(lambda x: 2 ** x, mylist)))

print("==EX03==")

x = [i**3 for i in range(4)] 
print(x)

print("==EX04==")

print(list(filter(lambda a : a % 3==0, [0,1,2,3,4,5,6,7,8,9])))

print("==EX05==")

from math import sqrt
print(list(map(str,map(sqrt, [4,9,16,25]))))

print("==EX06==")
x = [5*3 for i in range(4)] 
print(x)

print("==EX07==")
import math
lx = [math.sqrt(y) for y in range(5)]
print(lx)

lx = list(map(math.sqrt, range(5)))
print(lx)

print("==EX08==")
names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    if i == 1:
       print(i, name, age)

print("==EX09==")

stocks = ['AAPL', 'TSLA']
prices = [130.19, 111.7]

new_dict = {stocks:prices for stocks, prices in zip(stocks, prices)}
print(new_dict)

print("==EX10==")
def count_down(number):
    while number > 0:
        yield number
        number -= 1

for count in count_down(5):
    print(count)

def count_down(number):
    for i in range(number):
        return i

for count in count_down(5):
    print(count)