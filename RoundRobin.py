class Proceso:
    def __init__(self):
        self.nombre = ""
        self.llegada = 0
        self.cpu_original = 0  # Duración original del proceso
        self.cpu = 0           # Duración restante del proceso
        self.instante = -1
        self.t_fin = -1
        self.t_e = 0
        self.t_r = 0
        self.penalizacion = 0.0

# Función de comparación para ordenar procesos
def comparar_procesos(a, b):
    return a.llegada - b.llegada

def main():
    num_procesos = int(input("Ingrese el numero de procesos: "))
    quantum = int(input("Ingrese el quantum: "))

    procesos = [Proceso() for _ in range(num_procesos)]

    # Ingresar información de los procesos
    for i in range(num_procesos):
        procesos[i].nombre = chr(ord('A') + i)
        procesos[i].llegada = int(input(f"Ingrese la hora de llegada del proceso {procesos[i].nombre}: "))
        procesos[i].cpu_original = int(input(f"Ingrese la duración del proceso {procesos[i].nombre}: "))
        procesos[i].cpu = procesos[i].cpu_original
        procesos[i].instante = -1
        procesos[i].t_fin = -1
        procesos[i].t_e = 0
        procesos[i].t_r = 0
        procesos[i].penalizacion = 0.0

    # Ordenar los procesos por hora de llegada
    procesos.sort(key=lambda x: x.llegada)

    tiempo_actual = 0
    proceso_actual = 0
    procesos_terminados = 0

    while procesos_terminados < num_procesos:
        p = procesos[proceso_actual]

        if p.cpu > 0 and p.llegada <= tiempo_actual:
            if p.instante == -1:
                p.instante = tiempo_actual
                p.t_e = p.instante - p.llegada
                p.t_r = p.t_e + p.cpu
                p.penalizacion = p.t_r / p.t_e if p.t_e != 0 else 0.0

            if p.cpu <= quantum:
                tiempo_actual += p.cpu
                p.t_fin = tiempo_actual
                p.cpu = 0
                procesos_terminados += 1
            else:
                tiempo_actual += quantum
                p.cpu -= quantum

        proceso_actual = (proceso_actual + 1) % num_procesos

        if proceso_actual == 0:
            # Si hemos recorrido todos los procesos, volvemos a verificar si hay procesos pendientes
            todos_terminados = all(p.cpu == 0 for p in procesos)
            if todos_terminados:
                break

    print("+---------+---------+-----+----------+-------+------+-------+--------------+")
    print("| proceso | llegada | cpu | t.inicio | t.fin | t.e  |  t.r  | penalizacion |")
    print("+---------+---------+-----+----------+-------+------+-------+--------------+")

    for p in procesos:
        if p.t_fin != -1:
            print(f"|    {p.nombre}    |    {p.llegada:2d}   |  {p.cpu_original:2d} |    {p.instante:3d}   |  {p.t_fin:3d}  |  {p.t_e:2d}  |  {p.t_r:3d}  |     {p.penalizacion:.8f}   |")

    print("+---------+---------+-----+----------+-------+------+-------+--------------+")

if __name__ == "__main__":
    main()