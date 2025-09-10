# Cadastro - Alunos 2025/2026
print("Bem-vindo ao sistema de cadastro de alunos!")

def Consulta_ao_Sistema():
    print("\n1. Cadastrar Novo Aluno")
    print("2. Listar Alunos Cadastrados")
    print("3. Buscar Aluno por Matrícula")
    print("4. Sair")

def Cadastrar_Novo_Aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")

    try:
        matricula = int(input("Digite a matrícula do aluno (número inteiro): "))
    except ValueError:
        print("Matrícula inválida. Digite apenas números.")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("Matrícula já cadastrada. Tente novamente.")
            return

    aluno = {"nome": nome, "matricula": matricula, "curso": curso}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def Listar_Alunos_Cadastrados(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- Lista de Alunos ---")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Curso: {aluno['curso']}")

def Buscar_Aluno_por_Matricula(alunos):
    try:
        matricula = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida. Digite apenas números.")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"Aluno encontrado: Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Curso: {aluno['curso']}")
            return

    print("Aluno não encontrado.")

def main():
    alunos = []

    while True:
        Consulta_ao_Sistema()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            Cadastrar_Novo_Aluno(alunos)
        elif opcao == "2":
            Listar_Alunos_Cadastrados(alunos)
        elif opcao == "3":
            Buscar_Aluno_por_Matricula(alunos)
        elif opcao == "4":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
