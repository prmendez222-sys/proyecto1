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
            return self.historial[-1]
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
            return self.cola.popleft()
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
#clase empleado
class Empleado:
    def __init__(self,id_empleado,nombre):
        self.__id_empleado=id_empleado
        self.__nombre=nombre
    @property
    def id(self):
        return self.__id_empleado
    @id.setter
    def id(self,nuevo_id):
        if isinstance(nuevo_id,int):
            self.__id_empleado=nuevo_id
        else:
            raise ValueError("el Id debe se un numero entero")
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("el nombre no puede quedar vacio")
        else:
            self.__nombre=nuevo_nombre
    def mostrar_empleado(self):
        print("=====================================")
        print("ID: ",self.id)
        print("Nombre: ",self.nombre)
#clase gasolinero
class Gasolinero(Empleado):
    def __init__(self, id_gasolinero, nombre, bomba_que_atiende):
        super().__init__(id_gasolinero, nombre)
        self.__bomba_que_atiende=bomba_que_atiende
    @property
    def bomba_que_atiende(self):
        return self.__bomba_que_atiende
    @bomba_que_atiende.setter
    def bomba_que_atiende(self,nueva_bomba):
        if isinstance(nueva_bomba,int):
            self.__bomba_que_atiende=nueva_bomba
        else:
            raise ValueError("el numero de bomba debe ser entero")
    def mostrar_gasolinero(self):
        super().mostrar_empleado()
        print("bomba que atiende: ",self.bomba_que_atiende)
        print("=====================================")
#clase cajero
class Cajero(Empleado):
    def __init__(self,id_cajero,nombre,numero_caja):
        super().__init__(id_cajero,nombre)
        self.__numero_de_caja=numero_caja
    @property
    def numero_caja(self):
        return self.__numero_de_caja
    @numero_caja.setter
    def numero_caja(self,nueva_caja):
        if isinstance(nueva_caja,int):
            self.__numero_de_caja=nueva_caja
        else:
            raise ValueError("el numero de caja debe ser entero")
    def mostrar_cajero(self):
        super().mostrar_empleado()
        print("numero de caja: ",self.numero_caja)
        print("===================================")
#clase bomba
class Bomba:
    def __init__(self,id_bomba,tipo_servicio,tipo_combustible,precio):
        self.__id_bomba=id_bomba
        self.__tipo_servicio=tipo_servicio
        self.__tipo_combustible=tipo_combustible
        self.__capacidad=1000
        self.__precio=precio
        print("bomba creada con exito")
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
        if not isinstance(nueva_capacidad,int):
            raise ValueError("la capacidad debe ser expresada en numeros enteros")
        elif nueva_capacidad>1000:
            raise ValueError("la cantidad no debe ser mayor a 1000 galones")
        elif nueva_capacidad<0:
            raise ValueError("la cantidad no puede ser negativa")
        else:
            self.__capacidad=nueva_capacidad

    def llenar_bomba(self,cantidad):
        self.__capacidad=self.__capacidad+cantidad
        
    def mostrar_bomba(self):
        print("========================")
        print("Id: ",self.id)
        print("tipo de servicio: ",self.tipo_servicio)
        print("tipo de combustible: ",self.tipo_combustible)
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
#clase pago
class Pago(Bomba, Cliente):
    def __init__(self, id_bomba, tipo_servicio, tipo_combustible, tipo_servicio_cliente, tipo_combustible_cliente, precio, cantidad, pago_recibido):
        Bomba.__init__(self, id_bomba, tipo_servicio, tipo_combustible, precio)
        Cliente.__init__(self, tipo_servicio_cliente, tipo_combustible_cliente, cantidad)
        self.pago = pago_recibido

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

cola_bomba_1=Cola()
cola_Bomba_2=Cola()
Cola_bomba_3=Cola()

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
            if tipo_combustible=="regular":
                cola_bomba_1.agregar(cliente1)
            elif tipo_combustible=="diesel":
                cola_Bomba_2.agregar(cliente1)
            elif tipo_combustible=="super":
                Cola_bomba_3.agregar(cliente1)
            break
        except ValueError as e:
            print("error: ",e)


bombas=[]
id_bomba=0
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
            break
        except ValueError as e:
            print("error: ",e)

while True:
    print("1. ingreso de cliente")
    print("2. atender cliente")
    print("3. ver al al ultimo cliente atendido")
    print("4. ver ultima factura hecha")
    print("5. llenar bomba")
    print("6. ver ultima bomba llenada")
    print("7. ver historial de llenado")
    print("8. ver historial de facturacion")
    print("9. ingresar empleado")
    print("10. crear una nueva bomba")
    print("11. salir")
    opcion=input("\n ingrese una opcion: ")
    match opcion:
        case "1":
            agregar_cliente()
        case "2":
            for b in bombas:
                b.mostrar_bomba()
        case "10":
            crear_bomba()
            id_bomba=id_bomba+1
        case "11":
            break