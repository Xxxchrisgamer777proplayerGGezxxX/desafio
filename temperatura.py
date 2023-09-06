def celcius_a_fahrenheit(celsius):
    return (celsius *9/5) +32

def celcius_a_kelivn(celcius):
    return celcius + 273.5

def kelvin_a_celcius(kelvin):
    return kelvin_a_celcius -273.15

if __name__=="__main__":
    celcius = 25
    fahrenheit = celcius_a_fahrenheit(celcius)
    print(f"{celcius} grados celcius son equivalentes a {fahrenheit} grados fahrenheit")