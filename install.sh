#!/bin/bash

# Colores para mensajes
VERDE="\033[0;32m"
AZUL="\033[0;34m"
NC="\033[0m" # Sin Color

echo -e "${AZUL}Instalando tema Cyberpunk para Qtile...${NC}"

# Crear directorios necesarios
mkdir -p ~/.config/qtile/themes/cyberpunk
mkdir -p ~/.config/picom

# Copiar archivos de configuración
cp -r config/* ~/.config/qtile/
cp config/picom.conf ~/.config/picom/

# Instalar dependencias
echo -e "${VERDE}Instalando dependencias...${NC}"
pacman -S --needed python-pip picom alacritty

# Instalar paquetes Python necesarios
pip install -r requirements.txt

# Dar permisos a los scripts
chmod +x ~/.config/qtile/autostart.sh

echo -e "${VERDE}¡Instalación completada!${NC}"
echo -e "${AZUL}Por favor, reinicia Qtile con Mod + Control + R${NC}"
