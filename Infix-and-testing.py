# Please feel free to do additional testing in the terminal
# - it is made easily possible, just enter your calculation
# All other tests being automated are at the bottom


ops = ["+", "-", "*", "/"]

def listify (inp):
    # puts all the "words" within parentheses into a list
    # separated based on the spaces (and removes the spaces)
    # also removes parentheses
    if inp == "":
        return ([])
    lst = [inp[0]]
    for i in range(1, len(inp)):
        if inp[i] == " ":
            continue
        elif inp[i - 1] == " ":
            lst.append(inp[i])
        else:
            lst[len(lst) - 1] += inp[i]
    return lst

def calc (inp):
    # takes any basic ["(", int, operator, int, ")"] list and makes it into
    # an int
    a = 0
    b = 0
    c = ""
    try:
        a = float(inp[1])
        b = float(inp[3])
        c = inp[2]
    except:
        return ("Failure: something went wrong")
    if c == "+":
        return int(a + b)
    elif c == "-":
        return int(a - b)
    elif c == "*":
        return int(a * b)
    elif c == "/":
        if b == 0:
            return ("Failure: something went wrong")
        return float(a / b)
    else:
        return ("Failure: something went wrong")

def rempar (inp):
    # removes the first available set of parentheses (innermost)
    start = 0
    end = 0
    ln = len(inp)
    for i in range(len(inp)):
        if inp[i] == "(":
            start = i
        elif inp[i] == ")":
            return (rempar (inp[0:start] + [str(calc(inp[start:i + 1]))] +
                    inp[i + 1:ln]))
    if ln == 1:
        ans = inp[0]
        try:
            if float(ans) - round(float(ans)) == 0:
                return int(float(ans))
            return float(ans)
        except:
            return ("Failure: something went wrong")
    else:
        return ("Failure: something went wrong")
    
def run():
    inf = str(input())
    print(rempar(listify(inf)))

def testcases(args):
    for i in args:
        if not i:
            return ("Some test failed")
    else:
        return ("All tests passed")

# here are the testcases:
print(testcases([rempar(listify("3")) == 3, # just an int
                 rempar(listify("( 1 + 2 )")) == 3, # sum
                 rempar(listify("( 1 - 4 )")) == -3, # subtract
                 rempar(listify("( 3 * 5 )")) == 15, # times
                 rempar(listify("( 0 * 3 )")) == 0, # times 0
                 rempar(listify("( 6 / 2 )")) == 3, # div
                 rempar(listify("( 5 / 0 )")) == "Failure: something went wrong", #div by 0
                 rempar(listify("( 1 + ( 2 * 3 ) )")) == 7, # complex 1
                 rempar(listify("( ( 1 * 2 ) + 3 )")) == 5, # complex 2
                 rempar(listify("( ( 10 / ( 1 + 1 ) ) - ( 1 * 2 ) )")) == 3, # complex 3
                 rempar(listify("( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )")) == -1, # complex 4
                 rempar(listify("( 3 / 2 )")) == 1.5, # not-nice div
                 rempar(listify("( 4 + a )")) == "Failure: something went wrong", # some letters
                 rempar(listify("( adsafsd )")) == "Failure: something went wrong" # nonsense
                 ]))

while True:
    run()
