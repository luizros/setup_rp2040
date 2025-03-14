#!/usr/bin/env python3
import os
import sys
import argparse

def criar_estrutura(nome_projeto, type_project):
    if not nome_projeto:
        print("❌ Você deve fornecer um nome para o projeto!")
        sys.exit(1)

    if type_project not in ["c", "cpp"]:
        print("❌ Tipo de projeto inválido! Use 'c' ou 'cpp'.")
        sys.exit(1)

    estrutura = [
        f"{nome_projeto}/build",
        f"{nome_projeto}/src",
        f"{nome_projeto}/include"
    ]

    for pasta in estrutura:
        os.makedirs(pasta, exist_ok=True)

    # Criar um CMakeLists.txt básico
    cmake_content = f"""\
cmake_minimum_required(VERSION 3.13)
include($ENV{{PICO_SDK_PATH}}/external/pico_sdk_import.cmake)

project({nome_projeto})

pico_sdk_init()

add_executable({nome_projeto} src/main.{type_project})
target_include_directories({nome_projeto} PRIVATE include)
target_link_libraries({nome_projeto} pico_stdlib)
pico_add_extra_outputs({nome_projeto})

# Habilita USB para saída padrão (printf)
pico_enable_stdio_usb({nome_projeto} 1)
pico_enable_stdio_uart({nome_projeto} 0) # Opcional: Desativa a saída pela UART
"""

    with open(f"{nome_projeto}/CMakeLists.txt", "w") as f:
        f.write(cmake_content)

    # Criar um arquivo main.c ou main.cpp com um script simples de "Hello World"
    hello_world_content = ""
    if type_project == "c":
        hello_world_content = """\
#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    stdio_init_all();
    printf("Hello, world!\\n");
    while (1) {
        sleep_ms(1000);
    }
    return 0;
}
"""
    elif type_project == "cpp":
        hello_world_content = """\
#include <iostream>
#include "pico/stdlib.h"

int main() {
    stdio_init_all();
    std::cout << "Hello, world!" << std::endl;
    while (1) {
        sleep_ms(1000);
    }
    return 0;
}
"""

    with open(f"{nome_projeto}/src/main.{type_project}", "w") as f:
        f.write(hello_world_content)

    print(f"✅ Estrutura do projeto '{nome_projeto}' criada com sucesso!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para criar a estrutura de um projeto para o Raspberry Pi Pico.")
    parser.add_argument("-n", "--nome", type=str, help="Nome do projeto")
    parser.add_argument("-t", "--tipo", type=str, choices=["c", "cpp"], help="Tipo do projeto (c ou cpp)")
    parser.add_argument("nome_projeto", nargs="?", type=str, help="Nome do projeto (argumento posicional)")
    parser.add_argument("type_project", nargs="?", type=str, choices=["c", "cpp"], help="Tipo do projeto (c ou cpp, argumento posicional)")

    args = parser.parse_args()

    nome_projeto = args.nome or args.nome_projeto
    type_project = args.tipo or args.type_project

    if not nome_projeto or not type_project:
        parser.print_help()
        sys.exit(1)

    criar_estrutura(nome_projeto, type_project)
