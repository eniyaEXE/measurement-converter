# measurement converter
import itertools

red = "\033[31m"        # ANSI color codes borrowed from graphing-calculator
blue = "\033[34m"
magenta = "\033[35m"
clear = "\033[0m"

units = ["Liter", "Mililiter", "Gallon", "Fluid ounce", "Kilogram", "Pound", "Centimeter", "Inch", "Degrees Celsius", "Degrees Fahrenheit"]

# Values for calculating the conversions.
conversionValues = {"liter-mililiter": 1000,
                    "liter-gallon": 0.2641721769,
                    "liter-fluid ounce": 33.814038638,
                    "mililiter-liter": 0.001,
                    "mililiter-gallon": 0.0002641722,
                    "mililiter-fluid ounce": 0.0338140386,
                    "gallon-liter": 3.78541,
                    "gallon-mililiter": 3785.41,
                    "gallon-fluid ounce": 128,
                    "fluid ounce-liter": 0.0295735156,
                    "fluid ounce-mililiter": 29.573515625,
                    "fluid ounce-gallon": 0.0078125,
                    "kilogram-pound": 2.2046244202,
                    "pound-kilogram": 0.453592,
                    "centimeter-inch": 0.3937007874,
                    "inch-centimeter": 2.54,
                    "celsius-fahrenheit": 1.8,
                    "fahrenheit-celsius": 0.555555555,
                    "degrees celsius-degrees fahrenheit": 1.8,
                    "degrees fahrenheit-degrees celsius": 0.555555555}

# Corrections for temperature, since 0C =/= 0F, to convert them you cannot simply multiply by a number.
tempCorrections = {"celsius-fahrenheit": 32,
                   "fahrenheit-celsius": -17.77777777,
                   "degrees celsius-degrees fahrenheit": 32,
                   "degrees fahrenheit-degrees celsius": -17.77777777}

for _ in itertools.count():
    print(f"\n{blue}List of available units (v2.2){clear}:")
    for item in units:
        print(item)
    fromUnit = input(f"\n{blue}please choose the first unit{clear}: ").lower()
    toUnit = input(f"{blue}please choose the second unit{clear}: ").lower()
    
    # This concatenates the units to get the key to the values.
    conversionKey = fromUnit + "-" + toUnit

    conversionValue = conversionValues.get(conversionKey)
    tempCorrection = tempCorrections.get(conversionKey, 0)

    # When attempting to convert a unit to itself or to something not compatible (liter to kilogram for example), this will stop you.
    if conversionValue == None:
        print(f"{red}invalid conversion{clear}")
        input("press enter to continue")
        continue

    measure = input(f"\n{blue}please input your measurement in {magenta}{fromUnit} {blue}here{clear}: ")
    try:
        measure = float(measure)
    except:
        print("please try again.")
        continue
    
    # Calculates the output. When the units converted are not temperatures, tempCorrection will be 0, thus doing nothing to the answer.
    output = measure * conversionValue + tempCorrection

    print(f"\n{measure} {magenta}{fromUnit}{clear} = {round(output, 2)} {magenta}{toUnit}{clear}")
    input("press enter to continue")