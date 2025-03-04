import random
print("введите номер задания")
number_task=int(input())
match number_task:
    case 1:
        def dif(beg, end):
            h1,h2,m1,m2= "", "", "", ""
            found_colon1 = False
            for char in beg:
                if char == ":":
                    found_colon1 = True
                elif not found_colon1:
                    h2 += char
                else:
                    m2 += char

            h2 = int(h2)
            m2 = int(m2)

            found_colon2 = False
            for char in end:
                if char == ":":
                    found_colon2 = True
                elif not found_colon2:
                    h1 += char
                else:
                    m1 += char

            h1 = int(h1)
            m1 = int(m1)

            if(h1 > 23 or h1<0) or (h2 > 23 or h2<0) or (m1 > 60 or m1<0) or (m2 > 60 or m2<0):
                return print("ошибка формата времени")

            if h1>h2:
                if m1<m2:
                    h3=h1-h2-1
                    m3=m1+(60-m2)
                else:
                    h3=h1-h2
                    m3=m1-m2
            else:
                if m1<m2:
                    h3=24-h2+h1-1
                    m3=m1+(60-m2)
                else:
                    h3=24-h2+h1
                    m3=m1-m2

            return print("продолжительность события", h3,":",m3)

        print("введите начало события в формате часы:минуты")
        beg=input()
        print("введите конец события в формате часы:минуты")
        end=input()

        dif(beg, end)
    case 2:
        flag = 0
        while(flag == 0):
            print('введите два числа и операцию или "Stop", если хотите завершить процесс')
            a=input()
            if a == "Stop":
                print("вы завершили процесс")
                flag = 1
                break
            else:
                a=int(a)
                b=int(input())
                c=input()
                match c:
                    case '+':
                        print('результат операции a+b =', a+b)
                    case '-':
                        print('результат операции a-b =', a-b)
                    case '*':
                        print('результат операции a*b =', a*b)
                    case '/':
                        print('результат операции a/b =', a/b)
    case 3:
        flag = 0
        while(flag == 0):
            print('введите число или "Stop", если хотите завершить процесс')
            a=input()
            if a == "Stop":
                print("вы завершили процесс")
                flag = 1
                break
            else:
                a=int(a)
                if a%2 == 0:
                    print("число", a, "является четным")
                else:
                    print("число", a, "является нечетным")
    case 4:
        flag = 0
        sum = 0
        while(flag == 0):
            print('введите число или "Stop", если хотите завершить процесс')
            a=input()
            if a == "Stop":
                print("сумма введенных вами чисел =", sum)
                print("вы завершили процесс")
                flag = 1
                break
            else:
                a = int(a)
                sum +=a
    case 5:
        flag = 0
        def simple(n):
            sum=0
            for i in range(2, n):
                if n%i == 0:
                    sum+=1
                else:
                    sum+=0
            if sum == 0:
                return 0
            else:
                return 1

        while(flag == 0):
            print('введите число или "Stop", если хотите завершить процесс')
            a=input()
            if a == "Stop":
                print("вы завершили процесс")
                flag = 1
                break
            else:
                a = int(a)
                if a==1:
                    print("единица не относится к одной из этих категорий")
                else:
                    b = simple(a)
                    if b==0:
                        print("число", a, "простое")
                    else:
                        print("число", a, "составное")
    case 6:
        flag = 0
        def factorial(n):
            res=1
            for i in range(1, n+1):
                res*=i
            return res

        while(flag == 0):
            print('введите число или "Stop", если хотите завершить процесс')
            a=input()
            if a == "Stop":
                print("вы завершили процесс")
                flag = 1
                break
            else:
                a = int(a)
                b = factorial(a)
                print(a,"!", "=", b)
    case 7:
        random_num=random.randint(1,100)
        print("попробуйте угадать число от 1 до 100")
        user_num=int(input())
        while(user_num != random_num):
            if (user_num - random_num) < -20:
                print("ваше число слишком маленькое")
            elif ((user_num - random_num) < 0) and ((user_num - random_num) > -10):
                print("ваше число немного меньше заданного")
            elif (user_num - random_num) > 20:
                print("ваше число слишком большое")
            elif ((user_num - random_num) > 0) and ((user_num - random_num) < 10):
                print("ваше число немного большое заданного")

            user_num=int(input())
        if user_num==random_num:
            print("вы угадали число!")
    case 8:
        print("введите количество метров для перевода в различные единицы измерения")
        metr=float(input())
        print(metr, "м - это", metr*3.28, "футов")
        print(metr, "м - это", metr*39.37, "дюймов")
        print(metr, "м - это", metr*1.9, "ярдов")
    case 9:
        print("введите строчку")
        line = input()
        words = line.split()
        long_word = max(words, key=len)
        print("самое длинное слово в строке", long_word)
