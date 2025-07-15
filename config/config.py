# -*- coding: utf-8 -*-
import os
import subprocess
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# Colores Cyberpunk
colores = {
    'neon_rosa': '#FF0080',
    'neon_azul': '#00FFFF',
    'neon_verde': '#39FF14',
    'neon_amarillo': '#FFE900',
    'negro': '#000000',
    'gris_oscuro': '#1A1A1A',
    'morado': '#9D00FF'
}

# Configuración de Mod key
mod = "mod4"
terminal = "alacritty"

# Atajos de teclado personalizados
keys = [
    # Controles básicos
    Key([mod], "Return", lazy.spawn(terminal), desc="Lanzar terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Cambiar distribución"),
    Key([mod], "w", lazy.window.kill(), desc="Cerrar ventana activa"),
    Key([mod, "control"], "r", lazy.restart(), desc="Reiniciar Qtile"),
    
    # Controles de animaciones
    Key([mod], "a", lazy.group.cmd_toggle_animations(), desc="Alternar animaciones"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Alternar ventana flotante"),
    
    # Navegación
    Key([mod], "h", lazy.layout.left(), desc="Mover foco a la izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover foco a la derecha"),
    Key([mod], "j", lazy.layout.down(), desc="Mover foco abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover foco arriba"),
]

# Configuración de grupos
groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc=f"Cambiar al grupo {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc=f"Mover ventana al grupo {i.name}"),
    ])

# Diseños
layouts = [
    layout.Columns(
        border_focus=colores['neon_rosa'],
        border_normal=colores['gris_oscuro'],
        border_width=2,
        margin=8,
    ),
    layout.Max(),
]

# Widgets y configuración de la barra
widget_defaults = dict(
    font='JetBrainsMono Nerd Font',
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=colores['neon_azul'],
                    inactive=colores['gris_oscuro'],
                    highlight_method='line',
                    highlight_color=[colores['negro'], colores['negro']],
                    this_current_screen_border=colores['neon_rosa'],
                ),
                widget.WindowName(
                    foreground=colores['neon_verde'],
                ),
                widget.CPU(
                    format='CPU {load_percent}%',
                    foreground=colores['neon_amarillo'],
                ),
                widget.Memory(
                    format='RAM {MemPercent}%',
                    foreground=colores['neon_azul'],
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    foreground=colores['neon_rosa'],
                ),
                widget.Systray(),
            ],
            24,  # altura de la barra
            background=colores['negro'],
            opacity=0.8,  # transparencia
            margin=[5, 10, 0, 10],  # márgenes [top, right, bottom, left]
        ),
    ),
]

# Reglas de ventanas flotantes
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colores['neon_rosa'],
    border_normal=colores['gris_oscuro'],
)

# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# Otras configuraciones
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"