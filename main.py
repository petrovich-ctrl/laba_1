def parseEven(arr,number,p=5):
    res = []
    k=1
    if(number>=99):
        k=4
    elif(number>=9):
        k=2
    else:
        k=1
    for i in range(min(k,p), len(arr)):
        cond=(i % 2 == 0)
        if(p==1 and cond):
            res.append(arr[i])
        elif(k==1 and cond):
            res.append(arr[i])
        elif(k==2 and (not cond)):
            res.append(arr[i])
        elif(k==4 and cond):
            res.append(arr[i])
        elif(k==0 and cond):
            res.append(arr[i])
    return res;


def list(arr, symbolsAmount, length,):
    dictionary = []
    for w in range(0, symbolsAmount):  # Creating the dictionary of right size
        dictionary.append([])

    i = 0
    for t in range(0, len(arr) - 1, length + 1):  # Filling it
        for d in range(t + 1, t + length + 1):
            dictionary[i].append(arr[d])
        i += 1
    return dictionary;

def show(arr, horScale):
    arrWidth = 3 * horScale
    k = 1
    for i in range(0, len(arr), arrWidth):
        for j in range(i, i + arrWidth - 1):
            print(arr[j], end=' ')
        print(arr[arrWidth * k - 1])
        k += 1

def invert(arr):
    res=[]
    for i in range(0,len(res)):
        res.append(Xor(arr[i],1))
    return res

def maxInd(arr):
    max = arr[0]
    maxInd = 0
    for i in range(1, len(arr)):
        if (max < arr[i]):
            max = arr[i]
            maxInd = i
    return maxInd;


def UpScaleRowS(arr, scale, width=3):
    Rows = []
    for k in range(0, len(arr), width):
        tempRow = []

        for g in range(0, width):
            temp = [arr[k + g]]
            tempRow += temp * scale
        Rows.append(tempRow)
    return Rows;


def UpScale(arr, horScale, verScale, width=3, height=5):
    arrUpS = []
    Rows = UpScaleRowS(arr, horScale)
    # print(Rows)
    for i in range(0, height):
        arrUpS += Rows[i] * verScale
    return arrUpS;

def Xor(a,b):
    return int(a!=b)

from cmath import log

def find(x, y):
    for i in range(0, len(y)):
        if(x==y[i]):
            return i

def slog(x):
    if(x!=0):
        return log(x).real
    else:
        return float('-inf')

def best(x, y, p):
    if (len(x) != len(y)):
        return -1;
    prob = 0
    for i in range(0, len(x)):
        prob += Xor(x[i], y[i]) * (slog(p)) + Xor(1, Xor(x[i], y[i])) * (slog(1 - p))
    return prob;


def number(k):
    return im[k]

im=[]


im.append(['1', '1', '1',
        '1', '0', '1',
        '1', '0', '1',
        '1', '0', '1',
        '1', '1', '1'])

im.append(['0', '1', '0',
       '0', '1', '0',
       '0', '1', '0',
       '0', '1', '0',
       '0', '1', '0'])

im.append(['1', '1', '1',
       '0', '0', '1',
       '1', '1', '1',
       '1', '0', '0',
       '1', '1', '1'])

im.append(['1', '1', '1',
         '0', '0', '1',
         '1', '1', '1',
         '0', '0', '1',
         '1', '1', '1'])

im.append(['1', '0', '1',
        '1', '0', '1',
        '1', '1', '1',
        '0', '0', '1',
        '0', '0', '1'])

im.append(['1', '1', '1',
        '1', '0', '0',
        '1', '1', '1',
        '0', '0', '1',
        '1', '1', '1'])

im.append(['1', '1', '1',
       '1', '0', '0',
       '1', '1', '1',
       '1', '0', '1',
       '1', '1', '1'])

im.append(['1', '1', '1',
         '0', '0', '1',
         '0', '1', '0',
         '1', '0', '0',
         '1', '0', '0'])

im.append(['1', '1', '1',
         '1', '0', '1',
         '1', '1', '1',
         '1', '0', '1',
         '1', '1', '1'])

im.append(['1', '1', '1',
        '1', '0', '1',
        '1', '1', '1',
        '0', '0', '1',
        '0', '0', '1'])