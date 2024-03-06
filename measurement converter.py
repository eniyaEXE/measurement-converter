# measurement converter
import itertools

# Values for calculating the conversions.
conversionValues = {12: 1000,
                    13: 0.2641721769,
                    14: 33.814038638,
                    21: 0.001,
                    23: 0.0002641722,
                    24: 0.0338140386,
                    31: 3.78541,
                    32: 3785.41,
                    34: 128,
                    41: 0.0295735156,
                    42: 29.573515625,
                    43: 0.0078125,
                    56: 2.2046244202,
                    65: 0.453592,
                    78: 0.3937007874,
                    87: 2.54,
                    910: 1.8,
                    109: 0.555555555}

# Corrections for temperature, since 0C =/= 0F, to convert them you cannot simply multiply by a number.
tempCorrections = {910: 32,
                   109: -17.77777777}

# Assigning integers to the units.
unitDict = {"Liter": 1,
            "Mililiter": 2,
            "Gallon": 3,
            "Fluid ounce": 4,
            "Kilogram": 5,
            "Pound": 6,
            "Centimeter": 7,
            "Inch": 8,
            "Degrees Celsius": 9,
            "Degrees Fahrenheit": 10,
            "Celsius": 9,
            "Fahrenheit": 10}

for _ in itertools.count():
    print("\nList of available units (v2.0):\n\nLiter\nMililiter\nGallon\nFluid ounce\nKilogram\nPound\nCentimeter\nInch\nDegrees Celsius\nDegrees Fahrenheit")
    fromUnit = input("\nplease choose the first unit: ")
    toUnit = input("\nplease choose the second unit: ")
    
    # This concatenates the units' numbers to get the key to the values.
    conversionKey = int(str(unitDict.get(fromUnit, 0)) + str(unitDict.get(toUnit, 0)))

    conversionValue = conversionValues.get(conversionKey)
    tempCorrection = tempCorrections.get(conversionKey, 0)

    # When attempting to convert a unit to itself or to something not compatible (liter to kilogram for example), this will stop you.
    if conversionValue == None:
        print("invalid conversion")
        input("Enter 1 to continue: ")
        continue

    measure = input(f"\nplease input your measurement in {fromUnit} here: ")
    try:
        measure = float(measure)
    except:
        print("please try again.")
        continue
    
    # Calculates the output. When the units converted are not temperatures, tempCorrection will be 0, thus doing nothing to the answer.
    output = measure * conversionValue + tempCorrection

    print(f"\n{measure} {fromUnit} = {round(output, 2)} {toUnit}")
    input("Enter 1 to continue: ")