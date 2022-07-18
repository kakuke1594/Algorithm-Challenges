from itertools import groupby

def berserk(behelits):
    result = ''
    for i, behelit in enumerate(behelits):
        result += f'Case #{i+1}: {sacrifice(behelit)}\n' 
    return result

def sacrifice(behelit):
    result = ''
    red_behelit = [(key, sum(1 for _ in value)) for key, value in groupby(behelit)]
    if len(red_behelit) == 1:
        return behelit
    for idx in range(len(red_behelit) - 1):
        rate = 2 if red_behelit[idx][0] < red_behelit[idx + 1][0] else 1
        result += red_behelit[idx][0] * red_behelit[idx][1] * rate
    result += red_behelit[-1][0] * red_behelit[-1][1]
    return result

def is_valid_number_test_case(number):
    return number.isnumeric() and int(number) in range(1,101)

def is_valid_test_case(input):
    return input.isalpha() and input.isupper()

def input_number_test_case():
    counter = 0
    number = 0
    while counter < 3:
        number = input('Number of test case: ')
        counter += 1
        if is_valid_number_test_case(number):
            number = int(number)
            break
        print('Oops! Limit: 1 <= number <= 100')
    if counter > 2:
        print('Quit game!')
        exit()
    return number

def input_test_case():
    counter = 0
    test_case = ''
    while counter < 3:
        test_case = input(f'Test Case #{i+1}: ')
        counter += 1
        if is_valid_test_case(test_case):
            break
        print('Oops! Limit: test case contains only uppercase letters')
    if counter > 2:
        print('Quit game!')
        exit()
    return test_case

if __name__ == "__main__":
    behelits = []
    number = input_number_test_case()
    for i in range(number):
        test_case = input_test_case()
        behelits.append(test_case)
    
    print(berserk(behelits))
