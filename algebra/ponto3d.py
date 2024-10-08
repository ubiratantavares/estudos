class Ponto3D:

    def _init_(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def z(self):
        return self.__z

    def calcular_distancia_ate_ponto(self, outro):
        return ((self.x - outro.x) * 2 + (self.y - outro.y) * 2 + (self.z - outro.z) * 2) * 0.5

    def multiplicar_por_um_valor_escalar(self, fator):
        return Ponto3D(self.x * fator, self.y * fator, self.z * fator)
    
    def __str__(self) -> str:
        return f"Ponto({self.x}, {self.y}, {self.z})"
    
    def __add__(self, outro):
        return Ponto3D(self.x + outro.x, self.y + outro.y, self.z + outro.z)

    def __sub__(self, outro):
        return Ponto3D(self.x - outro.x, self.y - outro.y, self.z - outro.z)
    
