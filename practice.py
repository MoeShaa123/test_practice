

numbers = [2, 5, 7, 8, 9]

def findlargest(numbers):
    return max(numbers)

print(f"The largest number is {findlargest(numbers)}")


def isTwin(a,b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(isTwin("silent", "listen"))

def isgood(password):
    password = input()
    if len(password) < 5:
        return "Your password is too short"
    elif len(password) > 20:
        return "Your password is too long and may be forgetten"
    else:
        return "Your password is an acceptable length"

print(isgood(mohamed))
