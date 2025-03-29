#Rose Goldberg
#CSC 2280 Project 1
#This program converts several types of units

def unitConverter():
    #functions for every kind of unit conversion
    #in order asked by program
    def lenConvert():
        convertDirect = input("Type m for meters to feet or "
                            "f for feet to meters.") #To check for direction of conversion
        if convertDirect == "m":
            givenLen = float(input("What length? It can have decimals.")) #Asks user for how much they want converted
            newLen = givenLen * 3.281
            return f"Your new distance is {newLen} feet." #Calculation is done and returned to user
        elif convertDirect == "f":
            givenLen = float(input("What length? It can have decimals."))
            newLen = givenLen / 3.281
            return f"Your new distance is {newLen} meters."
    def massConvert():
        convertDirect = input("Type k for kilos to pounds or"
                            " p for pounds to kilos.")
        if convertDirect == "k":
            givenMass = float(input("What mass? It can have decimals."))
            newMass = givenMass * 2.205
            return f"Your new Mass is {newMass} pounds."
        elif convertDirect == "p":
            givenMass = float(input("What mass? It can have decimals."))
            newMass = givenMass / 2.205
            return f"Your new Mass is {newMass} kilograms."
    def tempConvert():
        convertDirect = input("Type C to convert Celcius to Fahrenheit or"
                            "Type F to convert Fahrenheit to Celcius.")
        if convertDirect == "C":
            givenTemp = float(input("What temperature? It can have decimals."))
            newTemp = (givenTemp * (9/5)) + 32
            return f"Your new temperature is {newTemp} degrees Fahrenheit."
        elif convertDirect == "F":
            givenTemp = float(input("What temperature? It can have decimals."))
            newTemp = float((givenTemp - 32) * (5/9))
            return f"Your new temperature is {newTemp} degrees Celcius."
    def speedConvert(): 
        convertDirect = input("Type mph to convert mph to kph or"
                            "Type kph to convert kph to mph.")
        if convertDirect == "mph":
            givenSpeed = float(input("What speed? It can have decimals."))
            newSpeed = givenSpeed * 1.609
            return f"Your new speed is {newSpeed}kph."
        elif convertDirect == "kph":
            givenSpeed = float(input("What speed? It can have decimals."))
            newSpeed = givenSpeed / 1.609
            return f"Your new speed is {newSpeed}mph."
    def volConvert():
        convertDirect = input("Type g for gallons to liters or"
                            " l for liters to gallons.")
        if convertDirect == "g":
            givenVol = float(input("What volume? It can have decimals."))
            newVol = givenVol * 3.785
            return f"Your new volume is {newVol} liters."
        if convertDirect == "l":
            givenVol = float(input("What volume? It can have decimals."))
            newVol = givenVol / 3.785
            return f"Your new volume is {newVol} gallons."
    typeUnit = 1
    while typeUnit != 0: #Used to continue asking for conversions until the user quits
        typeUnit = int(input("Type 1: Length, Type 2: Mass, Type 3: Temp,"
                    "Type 4: Speed, Type 5: Volume, Type 0: Quit Program"))
        if typeUnit == 1:
            print(lenConvert())
        elif typeUnit == 2:
            print(massConvert())
        elif typeUnit == 3:
            print(tempConvert())
        elif typeUnit == 4:
            print(speedConvert())
        elif typeUnit == 5:
            print(volConvert())
    return "Thank you for using the program. Closing now."
print(unitConverter())
        