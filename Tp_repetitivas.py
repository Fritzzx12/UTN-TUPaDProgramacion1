print("--- SISTEMA DE VENTAS ---")
nom = ""
while nom == "" or not nom.isalpha():
    nom = input("Nombre del cliente: ")
    if not nom.isalpha():
        print("Error: Solo letras.")

cant_prod = ""
while not cant_prod.isdigit() or int(cant_prod) <= 0:
    cant_prod = input("¿Cuantos productos lleva?: ")

cant = int(cant_prod)
tot_sin = 0
tot_con = 0

for i in range(cant):
    print("Producto", i + 1)
    
    pre_str = ""
    while not pre_str.isdigit():
        pre_str = input("Precio: ")
    
    precio = int(pre_str)
    tot_sin = tot_sin + precio
    
    t_desc = ""
    while t_desc != "s" and t_desc != "n":
        t_desc = input("¿Descuento? (s/n): ").lower()
    
    if t_desc == "s":
        precio_final = precio * 0.9
        tot_con = tot_con + precio_final
    else:
        tot_con = tot_con + precio

ahorro = tot_sin - tot_con
prom = tot_con / cant

print("\nRESULTADOS:")
print("Total sin desc: $", tot_sin)
print(f"Total con desc: ${tot_con:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio: ${prom:.2f}")


#Actividad 2
u_ok = "alumno"
p_ok = "python123"
intentos = 0
entró = False

while intentos < 3 and entró == False:
    intentos = intentos + 1
    print("Intento:", intentos)
    u = input("User: ")
    p = input("Pass: ")
    
    if u == u_ok and p == p_ok:
        entró = True
        print("Bienvenido!")
    else:
        print("Mal ingresado.")

if entró:
    op = ""
    while op != "4":
        print("\n1-Estado 2-Clave 3-Frase 4-Salir")
        op = input("Elegir: ")
        
        if not op.isdigit():
            print("Poner un numero.")
        elif op == "1":
            print("Estado: Inscripto")
        elif op == "2":
            n_clave = input("Nueva clave (6 min): ")
            if len(n_clave) >= 6:
                conf = input("Repita clave: ")
                if n_clave == conf:
                    p_ok = n_clave
                    print("Clave cambiada.")
                else:
                    print("No coinciden.")
            else:
                print("Muy corta.")
        elif op == "3":
            print("¡Sigue estudiando que te va a ir bien!")
        elif op == "4":
            print("Saliendo...")
        else:
            print("Opción no existe.")
else:
    print("Cuenta bloqueada.")


#Actividad 3
l1 = ""; l2 = ""; l3 = ""; l4 = ""
m1 = ""; m2 = ""; m3 = ""

op_nom = ""
while not op_nom.isalpha():
    op_nom = input("Nombre operador: ")

m_turno = ""
while m_turno != "5":
    print("\n--- AGENDA ---")
    print("1-Reservar 2-Cancelar 3-Ver Dia 4-Resumen 5-Cerrar")
    m_turno = input("Opcion: ")
    
    if m_turno == "1":
        dia = input("Dia (1=Lun, 2=Mar): ")
        p_nom = input("Paciente: ")
        if p_nom.isalpha():
            if dia == "1":
                if p_nom == l1 or p_nom == l2 or p_nom == l3 or p_nom == l4:
                    print("Ya tiene turno.")
                elif l1 == "": l1 = p_nom
                elif l2 == "": l2 = p_nom
                elif l3 == "": l3 = p_nom
                elif l4 == "": l4 = p_nom
                else: print("Lunes lleno.")
            elif dia == "2":
                if p_nom == m1 or p_nom == m2 or p_nom == m3:
                    print("Ya tiene turno.")
                elif m1 == "": m1 = p_nom
                elif m2 == "": m2 = p_nom
                elif m3 == "": m3 = p_nom
                else: print("Martes lleno.")
        else:
            print("Nombre mal.")
            
    elif m_turno == "2":
        dia = input("Dia (1 o 2): ")
        p_nom = input("Nombre a borrar: ")
        if dia == "1":
            if l1 == p_nom: l1 = ""
            elif l2 == p_nom: l2 = ""
            elif l3 == p_nom: l3 = ""
            elif l4 == p_nom: l4 = ""
        elif dia == "2":
            if m1 == p_nom: m1 = ""
            elif m2 == p_nom: m2 = ""
            elif m3 == p_nom: m3 = ""
            
    elif m_turno == "3":
        dia = input("Dia a ver (1 o 2): ")
        if dia == "1":
            t1 = l1; t2 = l2; t3 = l3; t4 = l4
            if t1 == "": t1 = "(libre)"
            if t2 == "": t2 = "(libre)"
            if t3 == "": t3 = "(libre)"
            if t4 == "": t4 = "(libre)"
            print(f"Lunes: 1:{t1} 2:{t2} 3:{t3} 4:{t4}")
        else:
            t1 = m1; t2 = m2; t3 = m3
            if t1 == "": t1 = "(libre)"
            if t2 == "": t2 = "(libre)"
            if t3 == "": t3 = "(libre)"
            print(f"Martes: 1:{t1} 2:{t2} 3:{t3}")
            
    elif m_turno == "4":
        ocu_l = 0
        if l1 != "": ocu_l += 1
        if l2 != "": ocu_l += 1
        if l3 != "": ocu_l += 1
        if l4 != "": ocu_l += 1
        
        ocu_m = 0
        if m1 != "": ocu_m += 1
        if m2 != "": ocu_m += 1
        if m3 != "": ocu_m += 1
        
        print(f"Lunes: {ocu_l} ocupados. Martes: {ocu_m} ocupados.")
        if ocu_l > ocu_m: print("Mas turnos: Lunes")
        elif ocu_m > ocu_l: print("Mas turnos: Martes")
        else: print("Empate.")


#Actividad 4
e = 100
t = 12
cer = 0
alarm = False
cod = ""
racha = 0

nom_ag = ""
while not nom_ag.isalpha():
    nom_ag = input("Agente: ")

while e > 0 and t > 0 and cer < 3 and not (alarm and t <= 3):
    print(f"\n[E:{e} T:{t} C:{cer}]")
    print("1-Forzar 2-Hackear 3-Descansar")
    acc = input("¿Que hacer?: ")
    
    if acc == "1":
        racha = racha + 1
        e = e - 20
        t = t - 2
        if racha == 3:
            alarm = True
            print("¡Trampa! Alarma prendida.")
        elif e < 40:
            ries = input("Cuidado, elegi 1, 2 o 3: ")
            if ries == "3": alarm = True
        
        if alarm == False:
            cer = cer + 1
            print("Abriste una!")
            
    elif acc == "2":
        racha = 0
        e = e - 10
        t = t - 3
        for i in range(4):
            print("Cargando...")
            cod = cod + "X"
        if len(cod) >= 8:
            cer = cer + 1
            print("Hackeado con exito.")
            
    elif acc == "3":
        racha = 0
        e = e + 15
        if e > 100: e = 100
        t = t - 1
        if alarm: e = e - 10

if cer == 3:
    print("Ganaste!")
elif alarm and t <= 3:
    print("Perdiste: Bloqueado.")
else:
    print("Perdiste: Sin recursos.")


#Actividad 5
hp_j = 100
hp_e = 100
pocs = 3
atq_p = 15
atq_e = 12

g_nom = ""
while not g_nom.isalpha():
    g_nom = input("Tu nombre: ")

while hp_j > 0 and hp_e > 0:
    print(f"\n{g_nom}: {hp_j} HP | Enemigo: {hp_e} HP | Pociones: {pocs}")
    print("1-Ataque Pesado 2-Rafaga 3-Curar")
    elegir = input("Accion: ")
    
    if elegir == "1":
        daño = float(atq_p)
        if hp_e < 20:
            print("¡CRITICO!")
            daño = daño * 1.5
        hp_e = hp_e - int(daño)
        print("Pegaste:", daño)
    elif elegir == "2":
        print("Rafaga!!")
        for j in range(3):
            hp_e = hp_e - 5
            print("> 5 de daño")
    elif elegir == "3":
        if pocs > 0:
            hp_j = hp_j + 30
            pocs = pocs - 1
            print("Te curaste.")
        else:
            print("No tenes mas.")
            
    if hp_e > 0:
        hp_j = hp_j - atq_e
        print("El enemigo te pego 12.")

if hp_j > 0:
    print("VICTORIA!")
else:
    print("DERROTA...")