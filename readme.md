

Modelagem em Orientação à Objetos
das Entidades Alunos, Cursos e 
Turmas.

## Casos de Uso
```mermaid
flowchart LR

    Usuario([Secretaria])
    UC1(( alunos))
    UC2((Editar alunos))
    UC3((Transferir alunos))
    
    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3

```

## Diagrama de Classes
```mermaid
classDiagram
    class aluno{
        - nome
        - Eemail
        - cpf
        - telefone
        - endereço
        - matrícula
        + ()
        + editar()
        + transferir()
      
        
    }
```

## Bibliotecas Python

Este é um projeto desktop, utilizando as tecnologias:

- Python
- PySide6
- PyInstaller


# Funções MySQL

- CREATE - Cria tabelas dentro da base de dados.
- INSERT - Cria registros dentro das tabelas.

- SELECT - Permite visualizar os dados dentro das tabelas. Também permite filtrar os dados que quer visualizar.

- ALTER - Altera a estrutura das tabelas, adicionando ou removendo atributos(campos).
- UPDATE - Atualiza regristros dentro da tabela.

- DROP - Exclui a tabela ou a base de dados inteira.
- DELETE - Exclui registros dentro das tabelas.

# MySQL

- Banco de Dados: Programa hospedado na máquina, com objetivo de persistir os dados fisicamente no HD.

- Base de Dados: Conjunto de tabelas.

- Tabelas: Conjunto de registros.

- Registros: Uma linha na tabela, contendo a informação dos seus atributos.

- Atributos: Uma das caracteristicas da tabela (Colunas).

## Dependências
- **VSCode**: IDE (Interface de Desenvolvimento)

- **Mermaid**: Linguagem para 
confecção de Diagramas em 
documentos MD (Mark Down)

- **Material Icon Theme**:Tema para as Colorir as 
pastas.

- **GIt Lens**: Interface gráfica para o
versionamento .git integrado ao VSCode. 

- **MySQL**: SGBD (Sistema Gerenciador de Banco de Dados). Permite conectar o usuário com o servidor MySQL, possibilitando criar bases de dados, tabelas, incluir e modificar atributos e registros. 

