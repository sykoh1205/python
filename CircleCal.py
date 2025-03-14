import math
circle_r = float(input("반지름의 길이를 입력하십시오.\n>"))
circumference = circle_r * math.pi * 2
circleextent = circle_r ** 2 *math.pi
print("반지름이", circle_r, "인 원의 둘레는", circumference, '이며, 넓이는', circleextent, "입니다.")