n = int(input('Input a number:'))
n += 1
while True:
    flag = 1
    if len(str(n)) >= 2:
        for i in range(1,len(str(n))):
            if str(n)[i] < str(n)[i-1]:
                flag = 0
                break
        if flag:
            print(f'Next growing number is:{n}')
            break
    n += 1
