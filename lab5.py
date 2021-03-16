# Метод Фібоначчі із затримуванням.
# Розподіл на площині (елементи попарно обробляються як координати точок (x, y).
# Тест на найдовшу послідовність одиниць.

#lags
import mpmath
import matplotlib.pyplot as plt


def main():
    A = 17
    B = 5
    elmtArr = [0.2, 0.9, 0.1, 0.5, 0.1, 0.5, 0.3, 0.7, 0.9, 0.1, 0.2, 0.8, 0.7, 0.1, 0, 0.2, 0.4]

    answer = input("Do you want to use your values? ")

    if answer.lower() in ["y", "yes"]:
        A = int(input("Enter lag A: "))
        B = int(input("Enter lab B: "))

        num = (A if A > B else B)

        elmtArr.clear()
        print("Enter start value: ")
        for i in range(num):
            while True:
                tmp = float(input())
                if (tmp < 1 and tmp >= 0):
                    break

                print("Enter element from 0 to <1: ")
            
            elmtArr.append(tmp)   
    
    N = int(input("Number of elements: "))

    start = (A if A > B else B)

    for i in range(start, start + N):
        fibonacci(i, A, B, elmtArr)
    
    for i in range(start, start + N):
        print(elmtArr[i])

    print()
    nist(elmtArr)
    graphic(elmtArr)


def fibonacci(N, A, B, elmtArr):
    result = elmtArr[N - A] - elmtArr[N - B]
    result = round(result, 1)
    elmtArr.append(result + 1 if result < 0 else result ) 

def nist(arr):
    M = 8  
    numV = 4
    V = [0, 0, 0, 0]
    for i in arr:
        tmp =  str(i).split('.') 
        if (len(tmp) > 1):
            dec = int(tmp[1]) 
            res = bin(dec)
            string = str(res)[2:]
            maximum = 0
            count = 0

            for j in string:
                if j == '1':
                    count += 1
                    if count > maximum:
                        maximum = count
                else:
                    count = 0

            if maximum > numV:
                V[numV - 1] += 1
            else:
                maximum -= 1
                if maximum < 0:
                    V[0] += 1
                else:
                    V[maximum] += 1
    
    p =[0.2148, 0.3672, 0.2305, 0.1875]

    K = 3
    R = 16
    x = 0

    for i in range(4):
        up = (V[i] - (R * p[i]))**2
        down = R * p[i]
        res = up / down
        x += res

    P = mpmath.gammainc(K/2, x/2)

    print(P)

def graphic(arr):
    i = 1
    x = []
    y =[]
    while i < len(arr):
        x.append(arr[i-1])
        y.append(arr[i])
        i += 2 

    plt.plot(x, y, 'ro')
    plt.show()
    
main()
