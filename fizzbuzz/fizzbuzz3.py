def FizzBuzz(num):
    for x in range(1, num+1):
        tests = {3: "Fizz", 5: "Buzz", 7: "Poop"}
        output = ""

        for key, value in tests.items():
            if (x % key == 0):
                output += value

        if output == "":
            output = x

        print(output)


FizzBuzz(100)
