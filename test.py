'''
print("hello, world")

x = 10
y = "hi"

num1 = 10 ** 3 #double * for exponent
num2 = 3
# double slash (/) for int division

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("equal")

# data structures
list = [10, "hi"]
phones = {"iphone" : "ios 13", "a50" : "pie"}
tuples = (0, 1, 2, 3)

print(list)
print(phones["iphone"])
#tuples[1] = 5 # will throw an error

gender = {"male" : "0", "female" : "1"}
print(gender["male"])

# looping through a list
for i in list:
    print(i)

# looping through a dictionary
for k, v in phones.items():
    print(k)
    print(v)
'''

str = "saurav mehta"
print(str[7 : ])

list = [10, "hi", 11, "bye"]
print(list[:2])

list2 = list[2:]
print(list2)
