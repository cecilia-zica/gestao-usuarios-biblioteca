from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU

class Funcionario(UsuarioBU, ABC):
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf)
        self._departamento = departamento
        self._dias_de_emprestimo = dias_de_emprestimo

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, departamento: str):
        if isinstance(departamento, str):
            self._departamento = departamento

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return f'do departamento "{self._departamento}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    @abstractmethod
    def devolver(self, titulo_livro: str):
        return f'do departamento "{self._departamento}" devolveu o livro: {titulo_livro}'
