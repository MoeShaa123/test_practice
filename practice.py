

# numbers = [2, 5, 7, 8, 9]
#
# def findlargest(numbers):
#     return max(numbers)
#
# print(f"The largest number is {findlargest(numbers)}")
#
#
# def isTwin(a,b):
#     if sorted(a) == sorted(b):
#         return True
#     else:
#         return False
#
# print(isTwin("silent", "listen"))
#
# def isgood(password):
#     if len(password) < 5:
#         return "Your password is too short"
#     elif len(password) > 20:
#         return "Your password is too long and may be forgetten"
#     else:
#         return "Your password is an acceptable length"
#
#
# password = input()
# print(isgood(password))

def new(string):
    nstring = string.replace(" ", "\n")
    print(nstring)


string = "Hello World"
new(string)

def adult(x):
    return "Hello" if x > 18 else "Noman"

print(adult(5))



items = ["Bob", "Luke", "Mess", "john", "Bob"]

print(items.count("Bob"))
print(items[1],items[3])


# def showNum(limit):
#     for x in range(0,limit):
#         if x % 2 == 0:
#             print (f"{x} EVEN")
#         else:
#             print (f"{x} ODD")
#
# showNum(8)

def odd_even_counter(number):
    list = []
    for x in range(0,number+1):
        if x % 2 == 0:
            list.append(x)
    return sum(list)
    for x in range(1,number):
        if x % 2 != 0:
            list.append(x)
    return sum(list)

print(odd_even_counter(6))
