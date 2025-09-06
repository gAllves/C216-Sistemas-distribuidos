alunos = []
cursos = ["GES", "GEC", "GEA", "GEB", "GET", "GEE", "GEP"]
numero_matricula = {curso: 0 for curso in cursos}

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno (GES, GEC, GEA, GEB, GET, GEE, GEP): ").upper()

    while(1):
        if curso not in cursos:
            print("Curso inválido. Por favor, digite um curso listado.")
            curso = input("Digite o curso do aluno novamente (GES, GEC, GEA, GEB, GET, GEE, GEP): ").upper()
        else:
            break

    numero_matricula[curso] += 1
    matricula = f"{curso}-{numero_matricula[curso]}"

    alunos.append({"nome": nome, "email": email, "curso": curso, "matricula": matricula})
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    print("\nLista de Alunos Cadastrados:")
    print(f"Matricula, Nome, Email, Curso")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"\n{aluno['nome']}, {aluno['email']}, {aluno['curso']}, {aluno['matricula']}")

def atualizar_aluno():
    matricula = input("Digite a matrícula do aluno que deseja atualizar (EX: 'GES-10'): ").upper()
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            
            if input(f"Deseja atualizar o nome do aluno? (S - Sim; N - Não): ").upper() == "S":
                aluno["nome"] = input("Digite o novo nome: ")

            if input("Deseja atualizar o email do aluno? (S - Sim; N - Não): ").upper() == "S":
                aluno["email"] = input("Digite o novo email: ")

            if input("Deseja atualizar o curso do aluno? (S - Sim; N - Não): ").upper() == "S":
                novo_curso = input("Digite o novo curso (GES, GEC, GEA, GEB, GET, GEE, GEP): ")
                while(1):
                    if novo_curso not in cursos:
                        print("Curso inválido. Por favor, digite um curso listado.")
                        novo_curso = input("Digite o curso do aluno novamente (GES, GEC, GEA, GEB, GET, GEE, GEP): ").upper()
                    else:
                        break
                aluno["curso"] = novo_curso
                numero_matricula[novo_curso] += 1
                aluno["matricula"] = f"{novo_curso}-{numero_matricula[novo_curso]}"

            print("Aluno atualizado com sucesso!")

            return
    print("Aluno não encontrado.")

def remover_aluno():
    matricula = input("Digite a matrícula do aluno que deseja remover: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula and input(f"Tem certeza que deseja remover o aluno {aluno['nome']}? (S - Sim; N - Não): ").upper() == "S":
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")

def main():

    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Site seguro academico - Instituto Nacional de Telecomunicações")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Finalizando sistema")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()