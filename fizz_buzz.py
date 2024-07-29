def fizz_buzz(up_to_number) :
    for i in range(1, up_to_number + 1) :
        if i % 3 == 0 and i % 5 == 0 :
            answer = "FizzBuzz"
        elif i % 3 == 0 :
            answer = "Fizz"
        elif i % 5 == 0 :
            answer = "Buzz"
        else :
            answer = i
        print(answer)