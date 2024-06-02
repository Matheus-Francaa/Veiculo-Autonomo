import random

class VeiculoAutonomo:
    def __init__(self, nome):
        self.nome = nome
        self.posicao = 0
        self.estado = "Parado"

    def detectar_obstaculo(self):
        
        return random.random() < 0.5

    def lidar_com_obstaculo(self):
        
        obstaculos = ["deslizamento", "estrada bloqueada", "pedestres"]
        obstaculo = random.choice(obstaculos)
        print(f"Obstáculo detectado: {obstaculo}")

        if obstaculo == "deslizamento":
            print("Desvio do deslizamento.")
        elif obstaculo == "estrada bloqueada":
            print("Calculando nova rota para evitar estrada bloqueada.")
        elif obstaculo == "pedestres":
            print("Parando para pedestres atravessarem.")
        self.estado = "Aguardando"
        self.aguardar()

    def aguardar(self):
        
        print("Aguardando para resolver o obstáculo...")
        for i in range(3):
            print(".")
        print("Obstáculo resolvido, continuando viagem.")

    def dirigir(self):
        while self.posicao < 10:
            self.estado = "Dirigindo"
            print(f"{self.nome} está dirigindo... Posição: {self.posicao}")

            if self.detectar_obstaculo():
                self.lidar_com_obstaculo()
            else:
                self.posicao += 1
                self.estado = "Em movimento"

        self.estado = "Chegou ao destino"
        print(f"{self.nome} chegou ao destino.")

# Simulação da história
print("Simulação do Veículo Autônomo")
veiculo = VeiculoAutonomo("Veículo Autônomo N5")
veiculo.dirigir()
