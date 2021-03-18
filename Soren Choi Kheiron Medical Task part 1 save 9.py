# Please feel free to do additional testing in the terminal
# - it is made easily possible, just enter your calculation
# All other tests being automated are at the bottom


ops = ["+", "-", "*", "/"]

def despace (inp):
    # takes the spaces off the start of a string
    count = 0
    for char in inp:
        if char == " ":
            count += 1
        else:
            break
    outp = inp[count:len(inp)]
    return outp

def listify (inp):
    # puts all the "words" of a string into a list
    # separated based on the spaces (and removes the spaces)
    dsp_inp = despace(inp)
    lst = [dsp_inp[0]]
    for i in range(1, len(dsp_inp)):
        if dsp_inp[i] == " ":
            continue
        elif dsp_inp[i - 1] == " ":
            lst.append(dsp_inp[i])
        else:
            lst[len(lst) - 1] += dsp_inp[i]
    return lst

def split (inp):
    # takes a list of the form we want and finds out at what
    # point the end of the first half of the first operation
    # occurs
    # e.g. with ["/", "+", "3", "4", "/", "1", "4"]
    # it will split it between the 4 and the /
    # returns this as the integer 4 since the 4th element
    # is the first one after the split
    count = 0
    val = len(inp)
    if val == 3:
        return 2
    for i in range(1, len(inp)):
        elt = inp[i]
        if elt in ops:
            count += 1
        else:
            try:
                int(elt)
                count -= 1
            except:
                return 0
        if count == -1:
            return (i + 1)
    return 0

def calc (inp):
    # recursively calculates the whole string
    # essentially it splits each suffix to an operation
    # into the first and second halves and calculates
    # each one individually
    spl = split(inp)
    if len(inp) == 1:
        try:
            return int(inp[0])
        except:
            return ("Failure: something went wrong")
    if spl == 0:
        return ("Failure: something went wrong")
    a = calc(inp[1:spl])
    b = calc(inp[spl:len(inp)])
    c = inp[0]
    try:
        # make sure we have integers or floats (not a string)
        a + b
    except:
        return ("Failure: something went wrong")
    if c == "+":
        return (a + b)
    elif c == "-":
        return (a - b)
    elif c == "*":
        return (a * b)
    elif c == "/":
        if b == 0:
            return ("Failure: something went wrong")
        return (a / b)
    else:
        return ("Failure: something went wrong")
    
def run ():
    pref = str(input())
    print(calc(listify(pref)))

def testcases(args):
    for i in args:
        if not i:
            return ("Some test failed")
    else:
        return ("All tests passed")

# here are the testcases:
print(testcases([calc(listify("3")) == 3, # just an int
                 calc(listify("+ 1 2")) == 3, # sum
                 calc(listify("- 1 4")) == -3, # subtract
                 calc(listify("* 3 5")) == 15, # times
                 calc(listify("* 0 3")) == 0, # times 0
                 calc(listify("/ 6 2")) == 3, # div
                 calc(listify("/ 5 0")) == "Failure: something went wrong", #div by 0
                 calc(listify("+ 1 * 2 3")) == 7, # complex 1
                 calc(listify("+ * 1 2 3")) == 5, # complex 2
                 calc(listify("- / 10 + 1 1 * 1 2")) == 3, # complex 3
                 calc(listify("/ 3 2")) == 1.5, # not-nice div
                 calc(listify("+ 4 a")) == "Failure: something went wrong", # some letters
                 calc(listify("adsafsd")) == "Failure: something went wrong" # nonsense
                 ]))

while True:
    run()
