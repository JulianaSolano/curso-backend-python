from abc import ABC, abstractmethod
import random
import time

class Personagem(ABC):

    def __init__(self, nome, vida, ataque_base):
        self.nome = nome
        self._vida = vida
        self._ataque_base = ataque_base

    def receber_dano(self, dano):
        "Reduz a vida do personagem ao receber dano."
        self._vida = max(0, self._vida - dano)
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self._vida}")

    def esta_vivo(self):
        "Verifica se o personagem ainda está vivo."
        return self._vida > 0 
    @abstractmethod
    def atacar(self, alvo):
        "Método abstrato para atacar outro personagem - implementado nas subclasses."
        pass

class Guerreiro(Personagem):

    def __init__(self, nome, vida, ataque_base, furia):
        super().__init__(nome, vida, ataque_base)
        self.__furia = furia

    def __usar_furia(self, valor):
        if self.__furia >= valor:
            self.__furia -= valor
            return True
        return False 
    
    def __ganhar_furia(self, valor):
        self.__furia += valor
        if self.__furia > 100:
            self.__furia = 100
    
    def atacar(self, alvo):
        "Ataque do guerreiro com chance de crítico."
        dano = self._ataque_base + random.randint(0, 10)
        alvo.receber_dano(dano)
        self.__ganhar_furia(10)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")

    def ataque_especial(self, alvo):
        "Ataque especial que consome fúria."
        if self.__usar_furia(30):
            dano = self._ataque_base * 2 + random.randint(5, 10)
            alvo.receber_dano(dano)
            print(f"{self.nome} usou ATAQUE ESPECIAL em {alvo.nome} causando {dano} de dano!")
        else:
            print(f"{self.nome} tentou usar ATAQUE ESPECIAL, mas não tinha fúeria suficiente!")

class Mago(Personagem):

    def __init__(self, nome, vida, ataque_base, mana):
        super().__init__(nome, vida, ataque_base)
        self.__mana = mana 

    def __gastar_mana(self, valor):
        if self.__mana >= valor:
            self.__mana -= valor
            return True 
        return False 
    
    def __regenerar_mana(self, valor):
        self.__mana += valor
        if self.__mana > 100:
            self.__mana = 100

    def atacar(self, alvo):
        "Ataque mágico consome mana."
        if self.__gastar_mana(20):
            dano = self._ataque_base + random.randint(5, 15)
            alvo.receber_dano(dano)
            print(f"{self.nome} lançou um feitiço em {alvo.nome} causando {dano} de dano!")
        else: 
            print(f"{self.nome} está sem mana e não pode atacar!")
            self.__regenerar_mana(10)

 #simulação batalha

if __name__ == "__main__":
    guerreiro = Guerreiro("Terizla", vida=120, ataque_base=15, furia=50)
    mago = Mago("Vexana", vida=100, ataque_base=12, mana=100)

    turno = 1 
    print("Início da batalha nas terras do Rio Kádia")

    while guerreiro.esta_vivo() and mago.esta_vivo():
        print(f"\n--- TURNO {turno} ---")

        if random.random() < 0.5:
            guerreiro.ataque_especial(mago)
        
        else:
            guerreiro.atacar(mago)
        
        if not mago.esta_vivo():
            print(f"\n {mago.nome} foi derrotado! {guerreiro.nome} venceu!")
            break

        time.sleep(1)

        mago.atacar(guerreiro)

        if not guerreiro.esta_vivo():
            print(f"\n {guerreiro.nome} foi derrotado!{mago.nome} venceu!")
            break

        turno += 1
        time.sleep(1)

    print ("\n Batalha encerrada.")
