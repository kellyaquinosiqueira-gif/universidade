

Modelagem em Orientação à Objetos
das Entidades Alunos, Cursos e 
Turmas.

## Casos de Uso
```mermaid
flowchart LR

    Usuario([Secretaria])
    UC1((Cadastrar alunos))
    UC2((Editar alunos))
    UC3((Transferir alunos))
    
    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3

```

## Diagrama de Classes
```mermaid
classDiagram
    class Aluno{
        - Nome
        - Email
        - CPF
        - Telefone
        - Endereço
        - Matrícula
        + cadastrar()
        + editar()
        + transferir()
      
        
    }
```

## Dependências
- **VSCode**: IDE (Interface de Desenvolvimento)

- **Mermaid**: Linguagem para 
confecção de Diagramas em 
documentos MD (Mark Down)

- **Material Icon Theme**:Tema para as Colorir as 
pastas.

- **GIt Lens**: Interface gráfica para o
versionamento .git integrado ao VSCode. 
