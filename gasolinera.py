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
        self.__nombre=nombre
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
        if not nuevo_nombre:
            raise ValueError("el nombre no puede quedar vacio")
        else:
            self.__nombre=nuevo_nombre
    def mostrar_cajero(self):
        print("ID: ",self.id_empleado)
        print("Nombre: ",self.nombre)
        print("-============================")

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
class Pago(Bomba, Cliente):
    def __init__(self, idbomba, tipo_servicio, tipo_combustible, tipo_servicio_cliente, tipo_combustible_cliente, precio, cantidad, pago_recibido):
        Bomba.__init__(self, idbomba, tipo_servicio, tipo_combustible, precio)
        Cliente.__init__(self, tipo_servicio_cliente, tipo_combustible_cliente, cantidad)
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
                tipo_combustible = "Super"
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
            capacidad=bomba.capacidad

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
                pago = Pago(idbomba, tipo_servicio_bomba, tipo_combustible, tipo_servicio_cliente, tipo_cliente,precio,cantidad, pago)
                if capacidad==0 or capacidad<pago.calcular_total():
                    print("no hay combustible disponible en la bomba: ", idbomba)
                    break
                else:
                    for b in bombas:
                        if b.id==idbomba:
                            b.capacidad=capacidad-pago.calcular_total()
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

bombas=[]
id_bomba=1
def crear_bomba():
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
def crear_empleado():
    while True:
        try:
            nombre=input("ingrese nombre: ")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            cajero=Cajero(id_empleado,nombre)
            break
        except ValueError as e:
            print(e)

while True:
    print("1. ingreso de cliente")
    print("2. atender cliente")
    print("3. mostrar cola de clientes")
    print("4. ver todas las bombas")
    print("5. ver al al ultimo cliente atendido")
    print("6. ver ultima factura hecha")
    print("7. llenar bomba")
    print("8. ver ultima bomba llenada")
    print("9. ver historial de llenado")
    print("10. ver historial de facturacion")
    print("11. ver historial de clientes")
    print("12. borrar todos los historiales")
    print("13. crear una nueva bomba")
    print("14. crear empleado")
    print("15. salir")
    opcion=input("\n ingrese una opcion: ")
    match opcion:
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
            if len(bombas)==0:
                print("no hay bombas creadas")
            else:
                for b in bombas:
                    b.mostrar_bomba()
        case "5":
            if historial_clientes.vacia():
                print("historial vacio")
            else:
                elemento = historial_clientes.mirar_ultimo_elemento()
                print(elemento.mostrar_cliente())
        case "6":
            if historial_faturacion.vacia():
                print("no hay facturas realizadas")
            else:
                elemento=historial_faturacion.mirar_ultimo_elemento()
                print(elemento.mostrar_factura())
        case "7":
            llenar_bomba()
        case "8":
            if historial_llenado.vacia():
                print("no hay historial de llenado")
            else:
                elemento=historial_llenado.mirar_ultimo_elemento()
                print("---------ultima bomba llenada----------")
                print(elemento.mostrar_bomba())
        case "9":
            if historial_llenado.vacia():
                print("historial vacio")
            else:
                for l in historial_llenado.historial:
                    print("==========historial de llenado==========")
                    print(l.mostrar_bomba())
        case "10":
            if historial_faturacion.vacia():
                print("historial vacio")
            else:
                for f in historial_faturacion.historial:
                    print("==========historial de llenado==========")
                    print(f.mostrar_factura())
        case "11":
            if historial_clientes.vacia():
                print("historial vacio")
            else:
                for c in historial_clientes.historial:
                    print("==========historial de llenado==========")
                    print(c.mostrar_cliente())
        case "12":
            historial_faturacion.vaciar_hitorial()
            historial_clientes.vaciar_hitorial()
            historial_llenado.vaciar_hitorial()
            print("historiales eliminados con exito")
        case "13":
            crear_bomba()
            id_bomba=id_bomba+1
        case "14":
            crear_empleado()
        case "15":
            break