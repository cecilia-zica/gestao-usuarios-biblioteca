from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU

class Aluno(UsuarioBU, ABC):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        self._matricula = matricula


    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor: int):
        if isinstance(valor, int):
            self._matricula = valor

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return f'Aluno de matricula "{self._matricula}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    @abstractmethod
    def devolver(self, titulo_livro: str):
        return f'Aluno de matricula "{self._matricula}" devolveu o livro: {titulo_livro}'

