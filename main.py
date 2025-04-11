from aluno_posgraduacao import AlunoPosGraduacao
from professor import Professor
from administrativo import Administrativo

def main():
    aluno_pg = AlunoPosGraduacao(cpf=123456789, dias_de_emprestimo=7, matricula=123, elaborando_tese=True)
    professor = Professor(departamento="Matemática", cpf=987654321)
    funcionario = Administrativo(departamento="Biblioteca", cpf=192837465)

    print(aluno_pg.emprestar("Algoritmos I"))
    print(professor.emprestar("Inteligência Artificial"))
    print(funcionario.emprestar("Gestão Pública"))

    print(aluno_pg.devolver("Algoritmos I"))
    print(professor.devolver("Inteligência Artificial"))
    print(funcionario.devolver("Gestão Pública"))

if __name__ == "__main__":
    main()
