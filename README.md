<div align="center">

# Gestor Livre

![GitHub top language](https://img.shields.io/github/languages/top/MauricioPaivadaSilva/GestorLivre) ![GitHub language count](https://img.shields.io/github/languages/count/MauricioPaivadaSilva/GestorLivre) ![GitHub License](https://img.shields.io/github/license/MauricioPaivadaSilva/GestorLivre) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/MauricioPaivadaSilva/GestorLivre/main) ![GitHub repo size](https://img.shields.io/github/repo-size/MauricioPaivadaSilva/GestorLivre)


</div>

---

<div align="justify">

## Sobre o projeto

Este projeto trata-se de um gerenciador de acervo para bibliotecas pessoais, desta forma, seu dimêncionamento não foi planejado para a carga de uma biblioteca de médio/grande porte, como:
- Bibliotecas
  - Institucionais;
  - Públicas;
  - Com empréstimos ([Ler nota 1](#1))

**Obs.: Este é um projeto pessoal, desta forma compreende-se que as escolhas tomadas no projeto podem não ser as melhores.**

## O que há no projeto atualmente?

Para as informações não selecionadas, [olhar nota 2](#2)

- [x] Tela de cadastro;
  - [x] Inserir dados mínimos conforme norma ABNT/NBR 6023;
  - [ ] Inserir dados opcionais como: ISSN, ISBN, CDD,...;
  - [ ] Inserir resumo;
  - [ ] Inserir o documento digital para ser armazenado no próprio projeto.
- [x] Tela de procura;
  - [ ] Sujestões de leitura.
- [x] Ver detalhadamente:
- [ ] Login de usuários e suas permissões;
  - [ ] Estatística dos empréstimos;
  - [ ] Maiores empréstimos;
  - [ ] Sujestões personalizadas para cada usuário.

## Organização do projeto

O projeto conta com um _Data base_ (DB), que encontra-se em `C:\GestorLivre`. Este DB é utilizado para armazenar os dados da biblioteca em uma tabela, esta tabela chama-se `docs`. Cada tabela será criada tendo como nome a versão atual do projeto, também haverá a tabela de 2 versões estáveis anteriores, para que possam ser utilizadas como _backup_.

## Notas

### 1
Ainda será adicionado ao projeto a função de empréstimos.

### 2
Demais funções serão adicionadas em versões posteriores. As funções planejadas para cada versão podem ser observadas nas [issues](https://github.com/MauricioPaivadaSilva/GestorLivre/issues) do projeto.

</div>