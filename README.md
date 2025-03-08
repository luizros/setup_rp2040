# Configuração de Ambiente para Projetos com a Raspberry Pi Pico RP2040

Este repositório auxilia na configuração do ambiente de desenvolvimento para projetos utilizando a **Raspberry Pi Pico RP2040**.

## 📌 Instalação  

Antes de começar, garanta que o script tenha permissão de execução:  

```bash
chmod +x run.sh
```

## 🚀 Criando um Novo Projeto  

Para criar um novo projeto, utilize o seguinte comando:  

```bash
setup_pico nome_do_projeto
```

Isso criará a estrutura de diretórios necessária para o desenvolvimento.  

## 🔧 Compilando o Projeto  

Após criar o projeto, navegue até a pasta `src/`, crie um arquivo `main.c` ou `main.cpp` e, em seguida, compile com:  

```bash
cd nome_do_projeto
compile_pico
```

Isso irá compilar e preparar o firmware para ser gravado na **Raspberry Pi Pico**.

## 📂 Estrutura do Projeto  

Após a criação do projeto, a estrutura de diretórios será semelhante a esta:  

```
nome_do_projeto/
│── build/
│── src/
│   ├── main.c  (ou main.cpp)
│── include/
│── CMakeLists.txt
```

## 📝 Observações  

- O script `setup_pico` cria a estrutura base do projeto.  
- O comando `compile_pico` compila e gera o arquivo `.uf2` para upload na Pico.  

