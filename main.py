# color palette: https://coolors.co/e2f1af-e3d888-84714f-5a3a31-31231e
from pyscript import display, document

def adding_numbers(e):
    document.getElementById('result').innerHTML = " " # clears the previous
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    # "+" sign indicates to add the first and second number
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}', target='result')


def subtracting_numbers(e):
    document.getElementById('result').innerHTML = " " # clears the previous
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    # "-" sign indicates to subtract the first and second number
    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is {difference}', target='result')

def multiplying_numbers(e):
    document.getElementById('result').innerHTML = " " # clears the previous
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    # "*" sign indicates to multiply the first and second number
    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} is {product}', target='result')

def dividing_numbers(e):
    document.getElementById('result').innerHTML = " " # clears the previous
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    # "/" sign indicates to divide the first and second number
    quotient = first_number / second_number

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='result')

def dividinground_numbers(e):
    document.getElementById('result').innerHTML = " " # clears the previous
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    # "//" sign indicates to divide the first and second number and showcase its rounded off value
    quotientround = first_number // second_number

    display(f'The rounded-off quotient of {first_number} and {second_number} is {quotientround}', target='result')

def remainder_numbers(e):
    document.getElementById('result').innerHTML = " " # clears the previous
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    # "%" sign indicates to get the remainder after dividing the first and second number
    remainer = first_number % second_number

    display(f'The remainder of {first_number} and {second_number} is {remainer}', target='result')


