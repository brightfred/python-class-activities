
def fizz_buzz(i,first,second):
    if i % 3 == 0 and i % 5 == 0 :
        answer = "FizzBuzz"
    elif i % 3 == 0:
        answer = "Fizz"
    elif i % 5 == 0 :
        answer = "Buzz"
    else:
        answer = str(i)
        
        print(i, answer)
        



def get_fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
       answer = "FizzBuzz"
    elif i % 3 == 0:
        answer = "Fizz"
    elif i % 5 == 0:
        answer = "Buzz"
    else:
        answer = str(i)
    return answer


def fizz_buzz_return_list(up_to_number):
    result_list = []
    answer = ""
    for i in range(up_to_number):
        answer = get_fizzbuzz(i)
       
        result_list  += [i,answer]


def fizz_buzz_comprehension(up_to_number):
    return [(i, get_fizzbuzz(i)) for i in range(up_to_number)]

if __name__ == "__main__":
    fizz_buzz(25)



