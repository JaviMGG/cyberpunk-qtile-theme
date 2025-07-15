#!/bin/bash

# Iniciar compositor para efectos de transparencia
picom --config ~/.config/picom/picom.conf &

# Establecer fondo de pantalla cyberpunk
feh --bg-fill ~/.config/qtile/themes/cyberpunk/wallpaper.jpg &

# Iniciar servicios de notificación
dunst &

# Iniciar polkit para permisos de sistema
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Iniciar applets de red y volumen
nm-applet &
pasystray &

# Establecer distribución de teclado
setxkbmap es &
