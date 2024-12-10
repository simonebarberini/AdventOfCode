def checkSafe(value)-> int:
    isSafe = False
    mod = ""
    for x in range(len(value)-1):
        if value[x]> value[x+1] and mod == "inc" and 1<=abs(value[x]-value[x+1])<=3:
                isSafe = False
                break
        elif value[x] > value[x+1] and mod == "dec" and 1<=abs(value[x]-value[x+1])<=3:
                isSafe = True
        elif value[x] > value[x+1] and mod == "" and 1<=abs(value[x]-value[x+1])<=3:
                mod = "dec"
        elif value[x]< value[x+1] and mod == "dec" and 1<=abs(value[x]-value[x+1])<=3:
            isSafe = False
            break
        elif value[x] < value[x+1] and mod == "inc" and 1<=abs(value[x]-value[x+1])<=3:
            isSafe = True
        elif value[x] < value[x+1] and mod == "" and 1<=abs(value[x]-value[x+1])<=3:
            mod = "inc"
        elif value[x] == value[x+1]:
            isSafe = False
            break
        else: 
            isSafe = False
            break
    if(isSafe):
        return 1
    else:
        return 0
    