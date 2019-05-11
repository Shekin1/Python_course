class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")

    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    

class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False   # Al añadir dos guiones '__' delante del atributo trabajando convertimos este atributo en
                                    # privado, esto significa que si quiero modificarlo desde el terminal o desde fuera de esta
                                    # clase debo poner 'nombreObjetoPerro'_PerroAsistencia__trabajando = False
                                    # Como poner todo esto resulta muy largo, también puedo crear un método llamado setter
                                    # para cambiar el valor o getter si quiero recuperar el valor de __trabajando. 
    
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{}: ayudo a mi dueño {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.trabajando:
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
    
    # Este metodo es a la vez getter y setter.
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando    # Como estamos dentro de la clase PerroAsistencia aunque __trabajando es un 
                                        # atributo privado desde aquí la forma de acceder a él es self.__trabajando                                        
                                        # Esta sería la parte getter de la función trabajando() en ella obtenemos
                                        # el contenido del atributo __trabajando
        else:
            self.__trabajando = valor   # Esta sería la parte setter porque modifica el atributo __trabajando

# Este sería un método setter
def setTrabajandoTrue(PerroAsistencia):
    # Aquí ya estamos fuera de las clases Perro y PeroAsistencia así que self.__trabajando = True
    # no funciona y hay que hacerlo igual que si escribiésemos desde la terminal
    PerroAsistencia._PerroAsistencia__trabajando = True
    
    
## En la terminal
    
# rantanplan = PerroAsistencia('Ran Tan Plan', 4, 8, 'Lucky Luke')   # Creo la instancia rantanplan
# rantanplan._PerroAsistencia__trabajando                            # Accedo a __trabajando sin método getter 
#   False
# setTrabajandoTrue(rantanplan)                          # Método setter para cambiar el estado de __trabajando a True
# rantanplan.trabajando()                                # Accedo a __trabajando con método getter
#   True
# rantanplan.trabajando(False)                           # setter
# rantanplan.trabajando()                                # getter
#   False