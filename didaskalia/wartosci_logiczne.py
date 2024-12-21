False, True


# wszelkie operacje z operatorami porówniania powinny zwrócić wartość logiczną

print(1 == 1)
print(1 == 2)
print(1 != 1)
print(1 != 2)
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)

print(1 == 1 and 2 == 2)
print(1 == 1 or 2 == 1) # True or False
print(not 1 == 1)

## ugolnione wartosci logiczne

print(bool(0))
print(bool(1))
print(bool(None))
print(bool(""))
print(bool(" "))
print(bool("False"))
print(bool([]))
print(bool([1, 2, 3]))
print(bool([False, False, False]))


wyrazenie = 1 > 0

if wyrazenie:  # it True
    print("Prawda")


if wyrazenie is True:  # it True
    print("Prawda")

# nie piszemy tak:

if wyrazenie == True:
    print("Prawda")


print("-" * 80)

wyrazenie = 1

if wyrazenie:  # if 1
    print("Prawda")


if wyrazenie is True:  # if i is True
    print("Prawda")

# nie piszemy tak:

if wyrazenie == True: # if 1 == True
    print("Prawda")

print("-" * 80)
wyrazenie = []


if wyrazenie:
    print("Lista nie jest pusta")
else:
    print("Lista jest pusta")


print("koszykarz")
print("koszykarz"[::-1])

def is_palindrome(word):

    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
    
def is_palindrome_2(word):
    reversed_word = word[::-1]
    return word == reversed_word


def is_palindrome_3(word):

    word = [w for w in word.casefold() if w.isalnum()]
    return word == word[::-1]

assert is_palindrome_3("kajak") is True
assert is_palindrome_3("kajak")
assert is_palindrome_3("Kajak") is True
assert is_palindrome_3("krowa") is False



print("ß", "ß".lower(), "ß".casefold())