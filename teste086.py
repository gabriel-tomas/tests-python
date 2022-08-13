class App:
    def __init__(self, cor) -> None:
        self.cor = cor
    def mudar_cor(self, cor_mudar, brilho):
        self.cor = cor_mudar
        self.brilho = brilho

cor1 = App("Azul")
print(cor1.cor)


cor1.mudar_cor("Amarelo", 23)
print(cor1.cor)
print(cor1.brilho)

