number = 212122
digits = str(number)
if len(digits) == 6:
    if sum(map(int, digits[:3])) == sum(map(int, digits[3:])):
        print("Счастливый билет")
    else:
        print("Несчастливый билет")
else:
    print("Введите шестизначное число.")