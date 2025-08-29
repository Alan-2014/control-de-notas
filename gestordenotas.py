# ===============================
# Sistema de Control de Notas (máximo 5)
# ===============================

notas = []  # Lista para almacenar las notas (máximo 5)

def registrar_notas():
    while len(notas) < 5:
        try:
            nota = float(input(f"Ingrese la nota {len(notas)+1} (0-100) o -1 para terminar: "))
            if nota == -1:
                break
            elif 0 <= nota <= 100:
                notas.append(nota)
                print("✅ Nota registrada.")
            else:
                print("⚠️ La nota debe estar entre 0 y 100.")
        except ValueError:
            print("⚠️ Entrada inválida, ingrese un número.")
    if len(notas) == 5:
        print("⚠️ Ya alcanzó el límite de 5 notas.")

def mostrar_notas():
    if len(notas) == 0:
        print("⚠️ No hay notas registradas.")
    else:
        print("📋 Notas registradas:")
        for i, n in enumerate(notas):
            estado = "Aprobado ✅" if n >= 60 else "Reprobado ❌"
            print(f"{i}. {n} - {estado}")

def calcular_promedio():
    if len(notas) == 0:
        print("⚠️ No hay notas registradas.")
    else:
        promedio = sum(notas) / len(notas)
        print(f"📊 El promedio general es: {promedio:.2f}")

def contar_aprobados_reprobados():
    aprobados = sum(1 for n in notas if n >= 60)
    reprobados = len(notas) - aprobados
    print(f"✅ Aprobados: {aprobados}")
    print(f"❌ Reprobados: {reprobados}")

def buscar_nota():
    if len(notas) == 0:
        print("⚠️ No hay notas registradas.")
        return
    try:
        valor = float(input("Ingrese la nota a buscar: "))
        if valor in notas:
            indice = notas.index(valor)  # búsqueda lineal
            print(f"🔍 Nota {valor} encontrada en la posición {indice}.")
        else:
            print("⚠️ Nota no encontrada.")
    except ValueError:
        print("⚠️ Entrada inválida.")

def actualizar_nota():
    if len(notas) == 0:
        print("⚠️ No hay notas registradas.")
        return
    try:
        mostrar_notas()
        indice = int(input("Ingrese la posición de la nota a actualizar: "))
        if 0 <= indice < len(notas):
            nueva = float(input("Ingrese la nueva nota: "))
            if 0 <= nueva <= 100:
                notas[indice] = nueva
                print("✅ Nota actualizada con éxito.")
            else:
                print("⚠️ La nota debe estar entre 0 y 100.")
        else:
            print("⚠️ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Entrada inválida.")

def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Registrar notas (máx 5)")
        print("2. Mostrar todas las notas")
        print("3. Calcular promedio")
        print("4. Contar aprobados y reprobados")
        print("5. Buscar nota")
        print("6. Actualizar nota")
        print("7. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_notas()
        elif opcion == "2":
            mostrar_notas()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            contar_aprobados_reprobados()
        elif opcion == "5":
            buscar_nota()
        elif opcion == "6":
            actualizar_nota()
        elif opcion == "7":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción inválida. Intente de nuevo.")

# Ejecutar menú principal
menu()