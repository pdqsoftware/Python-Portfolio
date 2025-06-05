#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def fizzbuzz_1(starting_integer, ending_integer):

    result = []

    for number in range(starting_integer, ending_integer + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 5 == 0:
            result.append("Fizz")
        elif number % 3 == 0:
            result.append("Buzz")
        else:
            result.append((str(number)))

        sequence = ",".join(result)

    return sequence

def fizzbuzz_2(starting_integer, ending_integer):
    output = ",".join(
        "FizzBuzz" if number % 15 == 0 else
        "Fizz" if number % 3 == 0 else
        "Buzz" if number % 5 == 0 else
        str(number) for number in range(starting_integer, ending_integer + 1)
    )
    return output


#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

start = 11
end = 23
print(fizzbuzz_2(start, end))
print(fizzbuzz_2(start, end))