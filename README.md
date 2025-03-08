# Configuração de Ambiente para Projetos com a Raspberry Pi Pico RP2040

Este repositório auxilia na configuração do ambiente de desenvolvimento para projetos utilizando a **Raspberry Pi Pico RP2040**.


## 📌 Instalação  

Para começar, clone este repositório e navegue até o diretório:

```bash
cd ~
git clone https://github.com/luizros/setup_rp2040
cd setup_rp2040
```

Antes de começar, garanta que o script tenha permissão de execução:  

```bash
chmod +x run.sh
```

## Prepando o Ambiente

Para preparar o ambiente, execute o seguinte comando:

```bash
./run.sh
```

## Atualizar o bashrc

Para atualizar o arquivo .bashrc, execute o seguinte comando:

```bash
source ~/.bashrc
```

## 🚀 Criando um Novo Projeto  

Para criar um novo projeto, utilize os seguintes comandos:  

```bash
cd ~
setup_pico nome_do_projeto tipo
```

No lugar de tipo, coloque `c` para C ou `cpp` para C++.

Isso criará a estrutura de diretórios necessária para o desenvolvimento.  

## 🔧 Compilando o Projeto  

Primeiro, certifique-se de estar na pasta do projeto. Em seguida, coloque a placa na porta USB no modo bootsel e execute os seguintes comandos:

```bash
cd nome_do_projeto
compile_pico
```

Isso irá compilar o projeto e gerar o arquivo `.uf2` necessário para upload na **Raspberry Pi Pico**.

## 📂 Estrutura do Projeto  

Após a criação do projeto, a estrutura de diretórios será semelhante a esta:  

```bash
nome_do_projeto/
│── build/
│── src/
│   ├── main.c  (ou main.cpp)
│── include/
│── CMakeLists.txt
```

## 📝 Observações  

- O script `setup_pico` cria a estrutura base do projeto.  
- O comando `compile_pico` compila e gera o arquivo `.uf2` e faz upload automático na Pico caso ela esteja conectada no modo bootsel.  
