#!/usr/bin/env python3
import os
import sys

def criar_estrutura(nome_projeto, type_project):
    if not nome_projeto:
        print("❌ Você deve fornecer um nome para o projeto!")
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

    print(f"✅ Estrutura do projeto '{nome_projeto}' criada com sucesso!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: setup_project.py <nome_do_projeto>")
        sys.exit(1)

    criar_estrutura(sys.argv[1])
    if len(sys.argv) < 3:
        print("Uso: setup_project.py <nome_do_projeto> <tipo>")
        sys.exit(1)

    type_project = sys.argv[2]
    if type_project not in ["c", "cpp"]:
        print("❌ Tipo de projeto inválido! Use 'c' ou 'cpp'.")
        sys.exit(1)

    criar_estrutura(sys.argv[1], type_project)
