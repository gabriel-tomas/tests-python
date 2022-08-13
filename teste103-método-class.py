class Carro:
    ano = 2022
    def __init__(self, cor, marca) -> None:
        self.cor = cor
        self.marca = marca
    def desc(self):
        return f"A cor do carro é {self.cor} e o ano é {self.ano}"
    
    @classmethod
    def edit_ano(cls, ano):
        cls.ano = ano
        print(f"Os carros agora vão ser do ano {ano}")
        
Carro.edit_ano(2000)