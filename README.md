# Biblioteca Universitária - Sistema de Empréstimos

Este projeto simula o controle de empréstimos de livros para diferentes tipos de usuários de uma biblioteca universitária.

## 📚 Classes

- `UsuarioBU`: Classe abstrata base para todos os usuários.
- `Funcionario`: Abstração de um funcionário da universidade.
- `Professor`: Herda de `Funcionario`, com regras específicas.
- `Administrativo`: Funcionário administrativo com tempo de empréstimo menor.
- `Aluno`: Classe abstrata para alunos.
- `AlunoPosGraduacao`: Aluno de pós-graduação com lógica especial se estiver elaborando tese.

## ⚙️ Funcionamento

Cada tipo de usuário tem uma política de empréstimo e devolução diferente.

### Exemplos:

```python
Aluno de matricula "123" pegou emprestado o livro: Algoritmos I com 14 dias de prazo
Professor do departamento "Matemática" pegou emprestado o livro: Inteligência Artificial com 20 dias de prazo
Funcionario administrativo do departamento "Biblioteca" pegou emprestado o livro: Gestão Pública com 10 dias de prazo
