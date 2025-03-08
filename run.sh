# Instalar dependências
sudo apt-get install -y git cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib minicom

# Clonar o SDK do Raspberry Pi Pico
cd ~
git clone https://github.com/raspberrypi/pico-sdk.git --branch master
cd pico-sdk
git submodule update --init

# Criar pasta para scripts (melhor usar ~/.local/bin)
mkdir -p ~/.local/bin
cp setup_pico.py ~/.local/bin/
cp compile_pico.py ~/.local/bin/

# Dar permissão de execução
chmod +x ~/.local/bin/setup_pico.py
chmod +x ~/.local/bin/compile_pico.py

# Adicionar o PICO_SDK_PATH ao .bashrc
echo "export PICO_SDK_PATH=~/pico-sdk" >> ~/.bashrc

# Criar aliases para os scripts
echo "alias setup_pico='python3 ~/.local/bin/setup_pico.py'" >> ~/.bashrc
echo "alias compile_pico='python3 ~/.local/bin/compile_pico.py'" >> ~/.bashrc

# Atualizar o shell para aplicar as mudanças imediatamente
source ~/.bashrc
