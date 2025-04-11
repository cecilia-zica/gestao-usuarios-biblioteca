from funcionario import Funcionario

class Administrativo(Funcionario):
    def __init__(self, departamento: str, cpf: int):
        super().__init__(departamento, cpf, dias_de_emprestimo=10)

    def emprestar(self, titulo_livro: str):
        return f'Funcionario administrativo do departamento "{self._departamento}" pegou emprestado o livro: {titulo_livro} com {self._dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro: str):
        return f'Funcionario administrativo do departamento "{self._departamento}" devolveu o livro: {titulo_livro}'
