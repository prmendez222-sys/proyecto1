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
class Empleado():
    def __init__(self,id,nombre,bomba_asignada):
        self.__id=id
        self.__nombre=nombre
        self.__bomba_asignada=bomba_asignada
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,nuevo_id):
        if isinstance(nuevo_id,int):
            self.__id=nuevo_id
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
    @property
    def bomba_asignada(self):
        return self.__bomba_asignada
    @bomba_asignada.setter
    def bomba_asignada(self,nueva_asignacion):
        if isinstance(nueva_asignacion,int):
            self.__bomba_asignada=nueva_asignacion
        else:
            raise ValueError("el numero de bomba debe ser entero")
    def mostrar_empleado(self):
        print("=====================================")
        print("ID: ",self.id)
        print("Nombre: ",self.nombre)
        print("bomba_asignada: ",self.bomba_asignada)
        print("=====================================")

class Bomba:
    def __init__(self,id,tipo_servicio,tipo_combustible,precio):
        self.__id=id
        self.__tipo_servicio=tipo_servicio
        self.__tipo_combustible=tipo_combustible
        self.__capacidad=1000
        self.__precio=precio
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, nuevo_id):
        if isinstance(nuevo_id,int):
            self.__id=nuevo_id
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
        if isinstance(nuevo_precio,float):
            self.__precio=nuevo_precio
        else:
            raise ValueError("solo se permiten numeros decimales")