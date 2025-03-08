#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil

def executar_comando(comando, descricao):
    """Executa um comando no terminal e captura a saída"""
    print(f"🔹 {descricao}...")
    try:
        resultado = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro durante {descricao}:")
        print(e.stderr)
        sys.exit(1)

def compilar():
    """Executa o CMake e Make, monitorando erros"""
    os.makedirs("build", exist_ok=True)
    os.chdir("build")

    executar_comando("cmake ..", "Configuração do CMake")
    executar_comando("make -j4", "Compilação")

    # Verifica se o arquivo UF2 foi gerado
    uf2_file = None
    for file in os.listdir("."):
        if file.endswith(".uf2"):
            uf2_file = file
            break

    if uf2_file:
        print(f"✅ Compilação bem-sucedida: {uf2_file}")
        return uf2_file
    else:
        print("❌ Erro: Arquivo UF2 não foi gerado!")
        sys.exit(1)

def flash(uf2_file):
    """Copia o arquivo UF2 para a Pico"""
    user = os.environ.get("USER") or os.environ.get("LOGNAME") or os.environ.get("USERNAME")
    pico_path = f"/media/{user}/RPI-RP2"

    if not os.path.exists(pico_path):
        print("❌ Raspberry Pi Pico não encontrada! Conecte a placa no modo bootloader.")
        sys.exit(1)

    print(f"📂 Copiando '{uf2_file}' para a Pico...")
    shutil.copy(uf2_file, pico_path)
    print("✅ Upload concluído!")

if __name__ == "__main__":
    uf2 = compilar()
    flash(uf2)
