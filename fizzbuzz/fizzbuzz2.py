# While better than v1, still is repeating code. Can be improved.
def FizzBuzz(num):
    for x in range(1, num+1):
        
        output = ""

        if (x % 3 == 0): output += "Fizz"
        if (x % 5 == 0): output += "Buzz"
        if (x % 7 == 0): output += "Fuzz"
        if (x % 11 == 0): output += "Bizz"
        if (x % 13 == 0): output += "Biff"
        if output == "":
            output = x

        print(output)


FizzBuzz(100)
