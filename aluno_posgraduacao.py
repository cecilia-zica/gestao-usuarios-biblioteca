from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int, elaborando_tese: bool = True):
        self._elaborando_tese = elaborando_tese
        dias = dias_de_emprestimo * 2 if elaborando_tese else dias_de_emprestimo
        super().__init__(cpf, dias, matricula)

    @property
    def elaborando_tese(self):
        return self._elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, valor: bool):
        if isinstance(valor, bool):
            self._elaborando_tese = valor

    def emprestar(self, titulo_livro: str):
        return super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return super().devolver(titulo_livro)





