#celcius to farenheit and vice versa
celcius = float(input("enter temperature in celcius "))
celcius_to_farenheit = celcius*1.8+32
farenheit = float(input("enter temperature in farenheit "))
farenheit_to_celcius = (farenheit - 32) * 5 / 9
print("celcius to farenheit is ",celcius_to_farenheit)
print("farenheit to celcius is ",farenheit_to_celcius)
