# measurement converter
import itertools

# Values for calculating the conversions.
conversionValues = {"LiterMililiter": 1000,
                    "LiterGallon": 0.2641721769,
                    "LiterFluid ounce": 33.814038638,
                    "MililiterLiter": 0.001,
                    "MililiterGallon": 0.0002641722,
                    "MililiterFluid ounce": 0.0338140386,
                    "GallonLiter": 3.78541,
                    "GallonMililiter": 3785.41,
                    "GallonFluid ounce": 128,
                    "Fluid ounceLiter": 0.0295735156,
                    "Fluid ounceMililiter": 29.573515625,
                    "Fluid ounceGallon": 0.0078125,
                    "KilogramPound": 2.2046244202,
                    "PoundKilogram": 0.453592,
                    "CentimeterInch": 0.3937007874,
                    "InchCentimeter": 2.54,
                    "CelsiusFahrenheit": 1.8,
                    "FahrenheitCelsius": 0.555555555,
                    "Degrees CelsiusDegrees Fahrenheit": 1.8,
                    "Degrees FahrenheitDegrees Celsius": 0.555555555}

# Corrections for temperature, since 0C =/= 0F, to convert them you cannot simply multiply by a number.
tempCorrections = {"CelsiusFahrenheit": 32,
                   "FahrenheitCelsius": -17.77777777,
                   "Degrees CelsiusDegrees Fahrenheit": 32,
                   "Degrees FahrenheitDegrees Celsius": -17.77777777}

for _ in itertools.count():
    print("\nList of available units (v2.1):\n\nLiter\nMililiter\nGallon\nFluid ounce\nKilogram\nPound\nCentimeter\nInch\nDegrees Celsius\nDegrees Fahrenheit")
    fromUnit = input("\nplease choose the first unit: ")
    toUnit = input("\nplease choose the second unit: ")
    
    # This concatenates the units to get the key to the values.
    conversionKey = str(fromUnit) + str(toUnit)

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