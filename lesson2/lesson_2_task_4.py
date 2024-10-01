def fizz_buzz(n):
    for i in range(1, n):
        result = ""
        if (i % 3 == 0):
            result = "Fizz"
        if (i % 5 == 0):
            result = result + "Buzz"
        if result == "":
            print(i)
        else:
            print(result)
    
fizz_buzz(20)