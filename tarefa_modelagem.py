#primeira parte - abstração

class MembroUepa:

    def __init__(self, nome, matricula, email):

        self.nome = nome
        self.matricula  = matricula
        self.email = email
    
    def apresentar(self):
        return f"Nome:{self.nome}, Matrícula:{self.matricula}, Email:{self.email}"
    
#segunda parte -herança

class Aluno(MembroUepa):

    def __init__(self, nome, matricula, email, curso):
        super().__init__(nome, matricula, email)
        self.curso = curso

    def verificar_notas(self):
        return f"Aluno: {self.nome}, Curso: {self.curso}"
    
    def apresentar(self):
        return f"Aluno: {self.nome}, matrícula {self.matricula} do curso {self.curso}"
    
class Professor(MembroUepa):

    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento

    def lancar_frequencia(self):
        return f"Professora {self.nome} do departamento {self.departamento} emitiu a frequência."
    
    def apresentar(self):
        return f"Professora: {self.nome}, Matrícula {self.matricula}, Departamento {self.departamento}."
    
#Testes

if __name__ ==  "__main__":

    aluno1 = Aluno("Juliana Solano", "20250923", "juliana@uepa.br", "Letras - Português")
    print(aluno1.apresentar())
    print(aluno1.verificar_notas())

    print("-" * 30)

    professor1 = Professor("Ketelen Souza", "23092025", "ketelen.mlbb@uepa","Linguística")
    print(professor1.apresentar())
    print(professor1.lancar_frequencia())




