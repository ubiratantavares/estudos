import math
from ponto3d import Ponto3D

class Vetor3D:

    def __init__(self, ponto_origem: Ponto3D, ponto_extremo: Ponto3D):
        self.__ponto_origem = ponto_origem
        self.__ponto_extremo = ponto_extremo

    @property
    def ponto_origem(self):
        return self.__ponto_origem
    
    @property
    def ponto_extremo(self):
        return self.__ponto_extremo
    
    def calcular_modulo(self):
        """Calcula o módulo (magnitude) do vetor, que é a distância entre o ponto de origem e o ponto extremo."""
        return self.ponto_origem.calcular_distancia_ate_ponto(self.ponto_extremo)
    
    def calcular_direcao(self):
        """Calcula os ângulos que o vetor forma com os eixos x, y e z."""
        direcao = self.ponto_extremo - self.ponto_origem
        modulo = self.calcular_modulo()
        
        if modulo == 0:
            raise ValueError("Vetor nulo não possui direção.")
        
        cos_alpha = direcao.x / modulo
        cos_beta = direcao.y / modulo
        cos_gamma = direcao.z / modulo
        
        alpha = math.degrees(math.acos(cos_alpha))
        beta = math.degrees(math.acos(cos_beta))
        gamma = math.degrees(math.acos(cos_gamma))
        
        return alpha, beta, gamma

    def vetor_unitario(self):
        """Retorna o vetor unitário, que é o vetor com o mesmo sentido, mas com comprimento 1."""
        if self.eh_vetor_nulo():
            raise ValueError("O vetor de módulo 0 não tem vetor unitário.")
        direcao = self.ponto_extremo - self.ponto_origem
        modulo = self.calcular_modulo()
        return Vetor3D(Ponto3D(), direcao.multiplicar_por_um_valor_escalar(1 / modulo))
    
    def eh_vetor_nulo(self):
        """Verifica se o vetor é nulo (origem e extremo coincidem)."""
        return self.ponto_origem.x == self.ponto_extremo.x and \
               self.ponto_origem.y == self.ponto_extremo.y and \
               self.ponto_origem.z == self.ponto_extremo.z
    
    def produto_escalar(self, outro_vetor):
        direcao1 = self.ponto_extremo - self.ponto_origem
        direcao2 = outro_vetor.ponto_extremo - outro_vetor.ponto_origem
        return (direcao1.x * direcao2.x) + (direcao1.y * direcao2.y) + (direcao1.z * direcao2.z)
    
    def produto_vetorial(self, outro_vetor):
        direcao1 = self.ponto_extremo - self.ponto_origem
        direcao2 = outro_vetor.ponto_extremo - outro_vetor.ponto_origem
        x = direcao1.y * direcao2.z - direcao1.z * direcao2.y
        y = direcao1.z * direcao2.x - direcao1.x * direcao2.z
        z = direcao1.x * direcao2.y - direcao1.y * direcao2.x
        return Vetor3D(Ponto3D(), Ponto3D(x, y, z))
    
    def vetor_simetrico(self):
        """Retorna o vetor simétrico, que tem a mesma magnitude, mas direção oposta."""
        direcao = self.ponto_extremo - self.ponto_origem
        return Vetor3D(Ponto3D(), direcao.multiplicar_por_um_valor_escalar(-1))

    def sao_colineares(self, outro_vetor):
        """Verifica se dois vetores são colineares (produto vetorial = vetor nulo)."""
        produto_vet = self.produto_vetorial(outro_vetor)
        return produto_vet.eh_vetor_nulo()

    def sao_coplanares(vetor1, vetor2, vetor3):
        """Verifica se três vetores são coplanares (produto misto = 0)."""
        produto_vet = vetor1.produto_vetorial(vetor2)
        return produto_vet.produto_escalar(vetor3) == 0

    def sao_iguais(self, outro_vetor):
        """Verifica se dois vetores são iguais (mesma direção e magnitude)."""
        direcao1 = self.ponto_extremo - self.ponto_origem
        direcao2 = outro_vetor.ponto_extremo - outro_vetor.ponto_origem
        return direcao1.x == direcao2.x and direcao1.y == direcao2.y and direcao1.z == direcao2.z

    def sao_paralelos(self, outro_vetor):
        """Verifica se dois vetores são paralelos."""
        direcao1 = self.ponto_extremo - self.ponto_origem
        direcao2 = outro_vetor.ponto_extremo - outro_vetor.ponto_origem
        proporcao_x = direcao1.x / direcao2.x if direcao2.x != 0 else None
        proporcao_y = direcao1.y / direcao2.y if direcao2.y != 0 else None
        proporcao_z = direcao1.z / direcao2.z if direcao2.z != 0 else None
        
        return proporcao_x == proporcao_y == proporcao_z

    def sao_ortogonais(self, outro_vetor):
        """Verifica se dois vetores são ortogonais (produto escalar = 0)."""
        return self.produto_escalar(outro_vetor) == 0
    
    def multiplicar_por_escalar(self, escalar):
        direcao = self.ponto_extremo - self.ponto_origem
        resultado = direcao.multiplicar_por_um_valor_escalar(escalar)
        return Vetor(Ponto3D(), resultado)

    def normalizar(self):
        modulo = self.calcular_modulo()
        if modulo == 0:
            raise ValueError("Não é possível normalizar um vetor nulo.")
        return self.multiplicar_por_escalar(1 / modulo)

    def angulo_entre_vetores(self, outro_vetor):
        produto_escalar = self.produto_escalar(outro_vetor)
        modulo1 = self.calcular_modulo()
        modulo2 = outro_vetor.calcular_modulo()
        if modulo1 == 0 or modulo2 == 0:
            raise ValueError("Não é possível calcular o ângulo com um vetor nulo.")
        cos_theta = produto_escalar / (modulo1 * modulo2)
        return math.acos(cos_theta)

    def projetar_sobre(self, outro_vetor):
        produto_escalar = self.produto_escalar(outro_vetor)
        modulo_outro_vetor = outro_vetor.calcular_modulo()
        fator = produto_escalar / (modulo_outro_vetor ** 2)
        return outro_vetor.multiplicar_por_escalar(fator)

    def refletir_sobre(self, vetor_normal):
        produto_escalar = self.produto_escalar(vetor_normal)
        vetor_normal_unitario = vetor_normal.vetor_unitario()
        return self.subtrair_vetor(vetor_normal_unitario.multiplicar_por_escalar(2 * produto_escalar))

    def __add__(self, outro_vetor):
        direcao1 = self.ponto_extremo - self.ponto_origem
        direcao2 = outro_vetor.ponto_extremo - outro_vetor.ponto_origem
        resultado = direcao1 + direcao2
        return Vetor3D(Ponto3D(), resultado)
    
    def __sub__(self, outro_vetor):
        direcao1 = self.ponto_extremo - self.ponto_origem
        direcao2 = outro_vetor.ponto_extremo - outro_vetor.ponto_origem
        resultado = direcao1 - direcao2
        return Vetor3D(Ponto3D(), resultado)

    def __str__(self):
        return f"Vetor3D({self.ponto_origem}, {self.ponto_extremo})"
