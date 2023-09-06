import temperatura
import masa
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen =="celcius" and unidad_destino == "fahrenheit":
        return  temperatura.celcius_a_fahrenheit(valor)
    else:
        return None
    
def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen =="kilogramos" and unidad_destino == "gramos":
        return  masa.kilogramos_a_gramos(valor)
    else:
        return None

def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen =="segundo" and unidad_destino == "minutos":
        return  tiempo.segundos_a_minutos(valor)
    else:
        return None
    
if __name__=="__main__":
    valor = 20
    unidad_origen= "celcius"
    unidad_destino= "fahrenheit"
    resultado= convertir_temperatura(valor,unidad_origen,unidad_destino)
    print(f"{valor} de {unidad_origen} son equivalentes a {resultado:.2f} {unidad_destino}")

    valor = 120
    unidad_origen= "segundo"
    unidad_destino= "minutos"
    resultado= convertir_tiempo(valor,unidad_origen,unidad_destino)
    print(f"{valor} de {unidad_origen} son equivalentes a {resultado:.2f} {unidad_destino}")

    valor = 100
    unidad_origen= "kilogramos"
    unidad_destino= "gramos"
    resultado= convertir_masa(valor,unidad_origen,unidad_destino)
    print(f"{valor} de {unidad_origen} son equivalentes a {resultado:.2f} {unidad_destino}")