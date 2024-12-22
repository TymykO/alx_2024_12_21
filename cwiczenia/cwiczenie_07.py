
def create_incrementator(value=1):

    counter = value
    
    def inner():
        # nonlocal counter
        to_return = inner.counter
        inner.counter = inner.counter + 1
        return to_return

    inner.counter = counter

    return inner



incrementator = create_incrementator(10)  # [10]

print(incrementator()) # 1   [10, 11]
print(incrementator()) # 2
print(incrementator()) # 3
print(incrementator()) # 4


print(incrementator.counter)
print(incrementator.counter)
print(incrementator.counter)
print(incrementator())
print(incrementator.counter)

