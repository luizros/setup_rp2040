# Instalar dependências
sudo apt-get install -y git cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib minicom

# Clonar o SDK do Raspberry Pi Pico se não existir
cd ~
if [ ! -d "pico-sdk" ]; then
    git clone https://github.com/raspberrypi/pico-sdk.git --branch master
    cd pico-sdk
    git submodule update --init
else
    echo "Diretório pico-sdk já existe. Pulando clonagem."
    cd pico-sdk
    git pull
    git submodule update --init
fi

# Criar pasta para scripts (melhor usar ~/.local/bin)
mkdir -p ~/.python_scripts

cd ~/setup_rp2040
cp ./setup_pico.py ~/.python_scripts/
cp ./compile_pico.py ~/.python_scripts/

# Dar permissão de execução
chmod +x ~/.python_scripts/setup_pico.py
chmod +x ~/.python_scripts/compile_pico.py

# Adicionar o PICO_SDK_PATH ao arquivo de configuração do shell
if [ "$SHELL" = "/bin/zsh" ] || [ "$SHELL" = "/usr/bin/zsh" ]; then
    echo "export PICO_SDK_PATH=~/pico-sdk" >> ~/.zshrc
    echo "alias setup_pico='python3 ~/.python_scripts/setup_pico.py'" >> ~/.zshrc
    echo "alias compile_pico='python3 ~/.python_scripts/compile_pico.py'" >> ~/.zshrc
elif [ "$SHELL" = "/bin/bash" ] || [ "$SHELL" = "/usr/bin/bash" ]; then
    echo "export PICO_SDK_PATH=~/pico-sdk" >> ~/.bashrc
    echo "alias setup_pico='python3 ~/.python_scripts/setup_pico.py'" >> ~/.bashrc
    echo "alias compile_pico='python3 ~/.python_scripts/compile_pico.py'" >> ~/.bashrc
else
    echo "Shell não suportado: $SHELL"
fi