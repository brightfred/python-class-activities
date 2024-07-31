def get_guess():
    result = None
    while True:
        try:
            test = input("Guess a number> ")
            result = float(test)
            break
        except ValueError:
            print(f'"{test}" is not a number')
    print("You entered:", result)
    return result


if __name__ == "__main__":
    print('Your number is {}'.format(get_guess()))