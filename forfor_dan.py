#변수 설정
i, k, dan = 0, 0, ""

#구구단_제목
for i in range(2,10):
    dan = dan + (" #  %d단  #" %i)
print(dan)

#구구단_바깥for문
for i in range(1,10):
    dan = ""
    #구구단_안쪽for문
    for k in range(2,10):
        dan = dan + str("%2dX %2d= %2d" %(k, i, k*i))
    print(dan)