def segundos_a_minutos(segundo):
    return segundo /60

def segundo_a_horas(segundo):
    return segundo /3600

def minutos_a_horas(minutos):
    return minutos /60

if __name__== "__main__":
    segundos= 150
    minutos= segundos_a_minutos(segundos)
    print(f"{segundos} segundos son equivalentes a {minutos} minutos")