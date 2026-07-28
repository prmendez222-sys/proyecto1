from collections import deque
#clase historial
class Historial:
    def __init__(self):
        self.historial=[]
    def vacia(self):
        return len(self.historial)==0
    def agregar_historial(self,elemento):
        self.historial.append(elemento)
        print("elemento agrado al historial con exito")
    def mirar_ultimo_elemento(self):
        if self.vacia():
            print("el historial esta vacio")
            return None
        else:
            elemento=self.historial[-1]
            return elemento
    def retirar_del_historial(self):
        if self.vacia():
            print("el historial esta vacio")
            return None
        else:
            return self.historial.pop()
    def mostrar_historial(self):
        if self.vacia():
            print("el historial esta vacio")
        else:
            for e in reversed(self.historial):
                print(e)
                print("========================")
    def vaciar_hitorial(self):
        self.historial.clear()
    def cantidad_elementos(self):
        return len(self.historial)

#clase cola
class Cola:
    def __init__(self):
        self.cola=deque()

    def agregar(self,elemento):
            self.cola.append(elemento)
            print('elemento agregado a la cola')
    def mostrar_primer_elemento(self):
        if not self.cola:
            print("no hay elementos")
            return None
        else:
            return self.cola[0]
    def eliminar_primer_elemento(self):
        if not self.cola:
            print("no hay elementos")
            return None
        else:
            elemento=self.cola.popleft()
            return elemento
    def vaciar_cola(self):
        if not self.cola:
            print("no hay elementos")
        else:
            self.cola.clear()
    def cantidad_en_cola(self):
        return len(self.cola)
    def mostrar_cola(self):
        if not self.cola:
            print("no hay elementos")
        else:
            for e in self.cola:
                print(e)
                print("=====================")

#clase cajero
class Cajero:
    def __init__(self, id_empleado,nombre):
        self.__id_empleado=id_empleado
        self.nombre=nombre
        print("cajero creado con exito")
    @property
    def id_empleado(self):
        return self.__id_empleado
    @id_empleado.setter
    def id_empleado(self, nuevo_id):
        if isinstance(nuevo_id,int):
            self.__id_empleado=nuevo_id
        else:
            raise ValueError("el Id debe ser un numero")
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre.strip())==0:
            raise ValueError("el nombre no puede quedar vacio")
        else:
            self.__nombre=nuevo_nombre
    def mostrar_cajero(self):
        print("ID: ",self.id_empleado)
        print("Nombre: ",self.nombre)

#clase bomba
class Bomba:
    def __init__(self, idbomba, tipo_servicio, tipo_combustible, precio):
        self.__id_bomba=idbomba
        self.__tipo_servicio=tipo_servicio
        self.__tipo_combustible=tipo_combustible
        self.__capacidad=1000
        self.__precio=precio
    @property
    def id(self):
        return self.__id_bomba
    @id.setter
    def id(self, nuevo_id):
        if isinstance(nuevo_id,int):
            self.__id_bomba=nuevo_id
        else:
            raise ValueError("el Id debe ser un numero")
    @property
    def tipo_servicio(self):
        return self.__tipo_servicio
    @tipo_servicio.setter
    def tipo_servicio(self,nuevo_tipo):
        self.__tipo_servicio=nuevo_tipo
    @property
    def tipo_combustible(self):
        return self.__tipo_combustible
    @tipo_combustible.setter
    def tipo_combustible(self,nuevo_tipo):
        self.__tipo_combustible=nuevo_tipo
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self,nuevo_precio):
        if isinstance(nuevo_precio,(int,float)):
            self.__precio=nuevo_precio
        else:
            raise ValueError("solo se permiten numeros decimales")
        return
    @property
    def capacidad(self):
        return self.__capacidad
    @capacidad.setter
    def capacidad(self,nueva_capacidad):
            self.__capacidad=nueva_capacidad

    def llenar_bomba(self,cantidad):
        self.__capacidad=self.__capacidad+cantidad
        
    def mostrar_bomba(self):
        print("========================")
        print("Id: ",self.id)
        print("tipo de servicio: ",self.tipo_servicio)
        print("tipo de combustible: ",self.tipo_combustible)
        print("desponible: ",self.capacidad," galones")
        print("Precio: ",self.precio)
        print("=====================================")
#clase cliente
class Cliente:
    def __init__(self,tipo_servicio,tipo_combustible,cantidad):
        self.__tipo_servicio=tipo_servicio
        self.__tipo_combustible=tipo_combustible
        self.__cantidad=cantidad
    @property
    def tipo_servicio(self):
        return self.__tipo_servicio
    @tipo_servicio.setter
    def tipo_servicio(self,nuevo_tipo):
        self.__tipo_servicio=nuevo_tipo
    @property
    def tipo_combustible(self):
        return self.__tipo_combustible
    @tipo_combustible.setter
    def tipo_combustible(self,nuevo_tipo):
        self.__tipo_combustible=nuevo_tipo
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,nueva_cantidad):
        if isinstance(nueva_cantidad,(int,float)):
            self.__cantidad=nueva_cantidad
        else:
            raise ValueError("la cantidad debe ser un numero entero o decimal")
    def mostrar_cliente(self):
        print("===================cliente=========================")
        print("tipo servicio: ",self.tipo_servicio)
        print("tipo combustible: ",self.tipo_combustible)
        print("cantidad: ",self.cantidad)
        print("------------------------------------------------")
#clase pago
class Pago(Bomba, Cliente,Cajero):
    def __init__(self, idbomba, tipo_servicio, tipo_combustible, tipo_servicio_cliente, tipo_combustible_cliente, precio, cantidad, pago_recibido, id_cajero, nombre_cajero):
        Bomba.__init__(self, idbomba, tipo_servicio, tipo_combustible, precio)
        Cliente.__init__(self, tipo_servicio_cliente, tipo_combustible_cliente, cantidad)
        Cajero.__init__(self,id_cajero,nombre_cajero)
        self.pago = pago_recibido
        print("cliente atendido con exito")

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, nuevo_pago):
        if not isinstance(nuevo_pago, (int, float)):
            raise ValueError("el pago debe ser entero o decimal")
        elif nuevo_pago < self.cantidad:
            raise ValueError("el pago debe ser mayor o igual a la cantidad pedida")
        else:
            self.__pago = nuevo_pago

    def calcular_total(self):
        return self.cantidad / self.precio

    def calcular_vuelto(self):
        return self.pago - self.cantidad

    def mostrar_factura(self):
        print("==================")
        print("ID de bomba: ", self.id)
        print("cajero que lo atendio: ",self.nombre)
        print("tipo servicio: ", self.tipo_servicio)
        print("tipo combustible: ", self.tipo_combustible)
        print("precio por galon: ", self.precio)
        print("cantidad despachada: ", round(self.calcular_total(), 2))
        print("pago recibido: ", self.pago)
        print("vuelto: ", round(self.calcular_vuelto(), 2))
        print("==============================================")

cola_bomba=Cola()
def agregar_cliente():
    print("=======cliente en cola=========")
    while True:
        print("-------ingrese tipo de servicio-------")
        print("1. servicio Completo")
        opcion1=input("ingrese una opcion: ")
        match opcion1:
            case "1":
                tipo_servicio="servicio_completo"
                break
            case _:
                print("opcion no valida")

    while True:
        print("-------------tipo de combustible----------")
        print("1. regular")
        print("2. diesel")
        print("3. super")
        opcion2 = input("ingrese una opcion: ")
        match opcion2:
            case "1":
                tipo_combustible = "regular"
                break
            case "2":
                tipo_combustible = "diesel"
                break
            case "3":
                tipo_combustible = "super"
                break
            case _:
                print("opcion no valida")

    while True:
        try:
            cantidad=float(input("ingrese la cantidad (Q.): "))
            break
        except ValueError:
            print("error: cantidad no aceptada")

    while True:
        try:
            cliente1=Cliente(tipo_servicio,tipo_combustible,cantidad)
            cola_bomba.agregar(cliente1)
            break
        except ValueError as e:
            print("error: ",e)

historial_faturacion=Historial()
historial_clientes=Historial()
def atender_cliente():
    while True:
        if cola_bomba.cantidad_en_cola()==0 or len(bombas) == 0:
            print("no hay bombas o no hay cola de clientes")
            break
        else:
            while True:
                try:
                    id_e=int(input("ingrese su ID: "))
                    break
                except ValueError:
                    print("tipo de dato no correcto")

            if id_e in cajeros:
                elemento = cola_bomba.mostrar_primer_elemento()
                if elemento.tipo_combustible == "regular":
                    for b in bombas:
                        if b.id == 1:
                            bomba = b
                elif elemento.tipo_combustible == "diesel":
                    for b in bombas:
                        if b.id == 2:
                            bomba = b
                elif elemento.tipo_combustible == "super":
                    for b in bombas:
                        if b.id == 3:
                            bomba = b
                tipo_servicio_cliente = elemento.tipo_servicio
                tipo_cliente = elemento.tipo_combustible
                cantidad = elemento.cantidad
                idbomba = bomba.id
                tipo_servicio_bomba = bomba.tipo_servicio
                tipo_combustible = bomba.tipo_combustible
                precio = bomba.precio
                capacidad = bomba.capacidad
                id_cajero=cajeros[id_e].id_empleado
                nombre_cajero=cajeros[id_e].nombre

                print("----------CAJA--------------")
                print("tipo de combustible: ", tipo_combustible)
                print("tipo de servicio: ", tipo_servicio_bomba)
                print("cantidad: ", cantidad)
                print("precio por galon: ", precio)
                print("=======================================")
                while True:
                    try:
                        pago = float(input("ingrese el pago: "))
                        break
                    except ValueError:
                        ValueError("el precio debe ser entero o decimal")

                try:
                    pago = Pago(idbomba, tipo_servicio_bomba, tipo_combustible, tipo_servicio_cliente, tipo_cliente,
                                precio, cantidad, pago,id_cajero,nombre_cajero)
                    if capacidad == 0 or capacidad < pago.calcular_total():
                        print("no hay combustible disponible en la bomba: ", idbomba)
                        break
                    else:
                        for b in bombas:
                            if b.id == idbomba:
                                b.capacidad = capacidad - pago.calcular_total()
                    historial_faturacion.agregar_historial(pago)
                    historial_clientes.agregar_historial(elemento)
                    cola_bomba.eliminar_primer_elemento()
                    factura = historial_faturacion.mirar_ultimo_elemento()
                    print("============Factura==================")
                    factura.mostrar_factura()
                    print("-------------------------")
                    break
                except ValueError as e:
                    print("error: ", e)
            else:
                print("cajero no encontrado")

id_bomba=1
bombas=[]
def crear_bomba():
    global id_bomba
    while True:
        print("==================")
        print("----------ingrese el tipo de servicio-------")
        print("1. servicio completo")
        opcion1=input("ingrese una opcion: ")
        match opcion1:
            case "1":
                tipo_servicio="servicio completo"
                break
                break
            case _:
                print("opcion no valido")

    while True:
        print("-------------ingrese el tipo de combustible-------------")
        print("1. regular")
        print("2. diesel")
        print("3. super")
        opcion2=input("ingrese una opcion: ")
        match opcion2:
            case "1":
                tipo_combustible="regular"
                break
            case "2":
                tipo_combustible="diesel"
                break
            case "3":
                tipo_combustible="super"
                break
            case _:
                print("opcion no valida")
    while True:
        try:
           precio=float(input("ingrese precio por galon: "))
           break
        except ValueError:
            ValueError("el numero debe ser entero o dec")

    while True:
        try:
            bomba1=Bomba(id_bomba,tipo_servicio,tipo_combustible,precio)
            bombas.append(bomba1)
            print("bomba creada con exito")
            id_bomba+=1
            break
        except ValueError as e:
            print("error: ",e)

historial_llenado=Historial()
def llenar_bomba():
    while True:
        try:
            idbomba=int(input("ingrese el Id de bomba: "))
            break
        except ValueError:
            ValueError("el id debe ser un numero entero")
    if len(bombas)==0:
        print("no hay bombas registradas")
    else:
        for lb in bombas:
            if lb.id == idbomba:
                bomba = lb
                existe = True
                lb.mostrar_bomba()
            else:existe=False

        if existe:
            cantidad_anterior = bomba.capacidad
            while True:
                try:
                    nueva_cantidad = float(input("ingrese la nueva cantidad: "))
                    for b in bombas:
                        if b.id == idbomba:
                            b.llenar_bomba(nueva_cantidad)
                    historial_llenado.agregar_historial(bomba)
                    print("___________bomba llenada con exito------------")
                    print("cantidad anterior: ", cantidad_anterior)
                    print("cantidad actual: ", nueva_cantidad)
                    break
                except ValueError as e:
                    print("error: ", e)
        else:
            print("bomba no econtrada")
id_empleado=1
cajeros={}
def crear_empleado():
    global id_empleado
    while True:
        try:
            nombre=input("ingrese nombre: ")
            cajero=Cajero(id_empleado,nombre)
            cajeros[id_empleado]=cajero
            id_empleado+=1
            break
        except ValueError as e:
            print(e)

def sub_menu1():
    while True:
        print("===========procesos administrativos========")
        print("1. crear cajero")
        print("2. ver a todos los cajeros")
        print("3. crear una nueva bomba")
        print("4. ver todas las bombas")
        print("5. llenar bomba")
        print("6. Menu Principal")
        sub1=input("ingrese una opción: ")
        match sub1:
            case "1":
                crear_empleado()
            case "2":
                for e in cajeros.values():
                    e.mostrar_cajero()
                    print("========================")
            case "3":
                crear_bomba()
            case "4":
                if len(bombas)==0:
                    print("no hay bombas creadas")
                else:
                    for b in bombas:
                        b.mostrar_bomba()
                break
            case "5":
                llenar_bomba()
            case "6":
                break
            case _:
                print("opción no valida")
def sub_menu2():
    while True:
        print("==============atención al cliente=========")
        print("1. ingresar de cliente")
        print("2. atender cliente")
        print("3. ver clientes en espera")
        print("4. Menu")
        sub2=input("ingrese una opción: ")
        match sub2:
            case "1":
                agregar_cliente()
            case "2":
                atender_cliente()
            case "3":
                if cola_bomba.cantidad_en_cola()==0:
                    print("no hay clientes en cola")
                else:
                    for c in cola_bomba.cola:
                        c.mostrar_cliente()
            case "4":
                break
            case _:
                print("opción no valida")
def sub_menu3():
    while True:
        print("1. ver al al ultimo cliente atendido")
        print("2. ver ultima factura hecha")
        print("3. ver ultima bomba llenada")
        print("4. ver historial de llenado")
        print("5. ver historial de facturación")
        print("6. ver historial de clientes")
        print("7. borrar todos los historiales")
        print("8. salir")
        sub3=input("ingrese una opción: ")
        match sub3:
            case "1":
                if historial_clientes.vacia():
                    print("historial vacio")
                else:
                    elemento = historial_clientes.mirar_ultimo_elemento()
                    print("---------ultima cliente atendido----------")
                    print(elemento.mostrar_cliente())
            case "2":
                if historial_faturacion.vacia():
                    print("no hay facturas realizadas")
                else:
                    elemento=historial_faturacion.mirar_ultimo_elemento()
                    print("---------ultima factura emitida----------")
                    print(elemento.mostrar_factura())
            case "3":
                if historial_llenado.vacia():
                    print("no hay historial de llenado")
                else:
                    elemento=historial_llenado.mirar_ultimo_elemento()
                    print("---------ultima bomba llenada----------")
                    print(elemento.mostrar_bomba())
            case "4":
                if historial_llenado.vacia():
                    print("historial vacio")
                else:
                    for l in historial_llenado.historial:
                        print("==========historial de llenado==========")
                        print(l.mostrar_bomba())
            case "5":
                if historial_faturacion.vacia():
                    print("historial vacio")
                else:
                    for f in historial_faturacion.historial:
                        print("==========historial de facturación==========")
                        print(f.mostrar_factura())
            case "6":
                if historial_clientes.vacia():
                    print("historial vacio")
                else:
                    for c in historial_clientes.historial:
                        print("==========historial de clientes==========")
                        print(c.mostrar_cliente())
            case "7":
                historial_faturacion.vaciar_hitorial()
                historial_clientes.vaciar_hitorial()
                historial_llenado.vaciar_hitorial()
                print("historiales eliminados con exito")
            case "8":
                break
            case _:
                print("opcion no valida")

while True:
    print("================MENU===================")
    print("1. procesos Administrativos")
    print("2. atención al cliente")
    print("3. historiales")
    print("4. salir")
    opcion=input("\ningrese una opción: ")
    match opcion:
        case "1":
            sub_menu1()
        case "2":
            sub_menu2()
        case "3":
            sub_menu3()
        case "4":
            break
        case _:
            print("opción no valida")