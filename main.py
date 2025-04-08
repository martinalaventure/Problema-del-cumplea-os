import random

def problema_cumpleaños (cant_personas : int) :
    cumpleaños = set() # Usamos un conjunto para almacenar los cumpleaños únicos
    
    for _ in range(cant_personas):
        dia = random.randint(1, 365)
        if dia in cumpleaños:
            # Si el día ya está en el conjunto, significa que hay una coincidencia
            return True
        cumpleaños.add(dia)

    return False  # No hay coincidencias de cumpleaños

def jugadas (cant_personas : int, repeticiones: int) :
    victorias = 0
    derrotas = 0

    for _ in range(repeticiones):
        if problema_cumpleaños(cant_personas):
            victorias += 1
        else:
            derrotas += 1

    print(f"Para {cant_personas} personas:")
    print(f"Victorias (coincidencias de cumpleaños): {victorias}")
    print(f"Derrotas (sin coincidencias de cumpleaños): {derrotas}")
    print(f"Probabilidad de coincidencia: {victorias / repeticiones:.2%}")

cantidades = [10, 20, 30, 40, 50]
repeticiones = [1000, 10000, 100000]

# print("Simulación del problema de cumpleaños")
# for cant_personas in cantidades:
#     print(f"\nPara {cant_personas} personas:")
#     print(problema_cumpleaños(cant_personas))

# print("\nEjecutando simulaciones para diferentes cantidades de personas y repeticiones")
# for rep in repeticiones:
#     print(f"\nSimulando {rep} repeticiones")
#     for cant_personas in cantidades:
#         jugadas(cant_personas, rep)


def probabilidad_teorica(m):
    if m > 365:
        return 1.0
    prob = 1.0
    for i in range(m):
        prob *= (365 - i) / 365
    return 1 - prob

def jugadas_con_comparacion (cant_personas : int, repeticiones: int) :
    victorias = 0

    for _ in range(repeticiones):
        if problema_cumpleaños(cant_personas):
            victorias += 1
    
    empírica = victorias / repeticiones
    teórica = probabilidad_teorica(cant_personas)

    print(f"Para {cant_personas} personas | Repeticiones {repeticiones}:")
    print(f"Prob. empírica: {empírica:.4f}")
    print(f"Prob. teórica : {teórica:.4f}")
    print(f"Diferencia     : {abs(empírica - teórica):.4f}")
    print("-------------------------------------------------------------------")

print("\nEjecutando simulaciones con comparaciones para diferentes cantidades de personas y repeticiones")
for rep in repeticiones:
    for cant_personas in cantidades:
        jugadas_con_comparacion(cant_personas, rep)
