def printFun(i):
    if i < 1:
        print(end="<=PUSH(i) POP(i)=>")
        return
    else:

        print(i, end=" ")
        printFun(i - 1)  # statement 2
        print(i, end=" ")
        return

i = 3
printFun(i)
