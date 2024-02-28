# measurement converter
import itertools

def FahrToCels():
    output = (measure - 32) / 1.8
    roundedOutput = round(output, 2)
    print("{0}F is {1}C".format(measure, roundedOutput))

def CelsToFahr():
    output = (measure * 1.8) + 3
    roundedOutput = round(output, 2)
    print("{0}C is {1}F".format(measure, roundedOutput))

def CentToInch():
    output = measure / 2.54
    roundedOutput = round(output, 2)
    print("{0}CM is {1}inches".format(measure, roundedOutput))

def InchToCent():
    output = measure * 2.54
    roundedOutput = round(output, 2)
    print("{0}Inches is {1}CM".format(measure, roundedOutput))

conversionDict = {"A": FahrToCels,
                  "B": CelsToFahr,
                  "C": CentToInch,
                  "D": InchToCent}

for _ in itertools.count():
    conversion = input("\nplease choose your conversion\n A - Fahrenheit to Celsius\n B - Celsius to Fahrenheit\n C - Centimeters to Inches\n D - Inches to Centimeters\n ")

    measure = input("\nplease input your measure here: ")
    try:
        measure = float(measure)
    except:
        print("please try again.")
        continue

    conversionDict.get(conversion)()