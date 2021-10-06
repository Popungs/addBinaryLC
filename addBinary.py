def binToInt(bin):
    bin = int(bin)
    retVal = i = n = 0
    while (bin != 0):
        a = bin % 10
        retVal = retVal + a * pow(2, i)
        bin = bin // 10
        i += 1
    print(retVal)
    return retVal


def addBinary(a, b):
    inta = binToInt(a)
    intb = binToInt(b)
    intc = inta + intb
    res = ""
    while intc > 0:
        if intc % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
        intc = intc // 2
    return(res)


a1 = "11"
b = "1"

print(addBinary(a1, b))
