def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()

print(odd())
print(odd())
print(odd())

odd2 = calculate()
print(odd2())