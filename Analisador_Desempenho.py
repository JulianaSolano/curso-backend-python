#Análise de desempenho da turma

alunos = [
    {"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},
    {"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},
    {"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},
    {"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},
    {"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},
    {"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0, "status_matricula": "ativo"},
    {"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},
    {"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"}
]

alunos_ativos = list(filter(lambda aluno: aluno["frequencia"] >= 75.0 and aluno["status_matricula"] == "ativo",alunos))

print("\n Alunos Ativos (freq >= 75 e ativos):")
for aluno in alunos_ativos:
    print(f"{aluno['nome']} | Nota: {aluno['nota_final']} | Freq: {aluno['frequencia']}%")

alunos_com_bonus = list(map(lambda aluno: {**aluno,"nota_final": min(aluno["nota_final"] * 1.1, 10.0)},alunos_ativos))

print("\n Notas após aplicação do bônus (10%):")
for aluno in alunos_com_bonus:
    print(f"{aluno['nome']} | Nova Nota: {aluno['nota_final']:.2f}")

destaques = list(filter(lambda aluno: aluno["nota_final"] >= 9.0,alunos_com_bonus))

print("\n Alunos em destaque (nota >= 9.0):")
for aluno in destaques:
    print(f"{aluno['nome']} | Nota Final: {aluno['nota_final']:.2f}")
