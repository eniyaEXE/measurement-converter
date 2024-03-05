# measurement converter
import itertools

def FahrToCels():
    output = (measure - 32) / 1.8
    roundedOutput = round(output, 2)
    print("{0}Fahrenheit = {1}Celsius".format(measure, roundedOutput))

def CelsToFahr():
    output = (measure * 1.8) + 32
    roundedOutput = round(output, 2)
    print("{0}Celsius = {1}Fahrenheit".format(measure, roundedOutput))

def CentToInch():
    output = measure / 2.54
    roundedOutput = round(output, 2)
    print("{0}Centimeter(s) = {1}Inch(es)".format(measure, roundedOutput))

def InchToCent():
    output = measure * 2.54
    roundedOutput = round(output, 2)
    print("{0}Inch(es) = {1}Centimeter(s)".format(measure, roundedOutput))

def KiloToPoun():
    output = measure * 2.2046244202
    roundedOutput = round(output, 2)
    print("{0}Kilogram(s) = {1}Pound(s)".format(measure, roundedOutput))

def PounToKilo():
    output = measure * 0.453592
    roundedOutput = round(output, 2)
    print("{0}Pound(s) = {1}Kilogram(s)".format(measure, roundedOutput))

conversionDict = {"A": FahrToCels,
                  "B": CelsToFahr,
                  "C": CentToInch,
                  "D": InchToCent,
                  "E": KiloToPoun,
                  "F": PounToKilo}

for _ in itertools.count():
    conversion = input("\nplease choose your conversion\n A - Fahrenheit to Celsius\n B - Celsius to Fahrenheit\n C - Centimeters to Inches\n D - Inches to Centimeters\n E - Kilogram to Pound\n F - Pound to Kilogram\n ")

    measure = input("\nplease input your measure here: ")
    try:
        measure = float(measure)
    except:
        print("please try again.")
        continue

    try:
        conversionDict.get(conversion)()
    except:
        print("invalid conversion")
        continue