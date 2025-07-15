#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import math
import time

class AnimacionesCyberpunk:
    def __init__(self):
        self.ventana = Gtk.Window()
        self.ventana.set_app_paintable(True)
        self.ventana.set_type_hint(Gtk.WindowType.DOCK)
        self.ventana.set_keep_above(True)
        
        # Configurar transparencia
        screen = self.ventana.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.ventana.set_visual(visual)
        
        # Variables de animación
        self.angulo = 0
        self.pulso = 0
        self.tiempo_inicio = time.time()
        
        # Colores neón
        self.colores = [
            (1, 0, 0.5),  # Rosa neón
            (0, 1, 1),    # Cian neón
            (0.2, 1, 0.08) # Verde neón
        ]
        
        # Conectar señales
        self.ventana.connect('draw', self.dibujar)
        self.ventana.connect('destroy', Gtk.main_quit)
        
        # Iniciar animación
        GLib.timeout_add(50, self.actualizar)
        
    def dibujar(self, widget, contexto):
        # Obtener dimensiones
        ancho = self.ventana.get_allocated_width()
        alto = self.ventana.get_allocated_height()
        
        # Limpiar fondo
        contexto.set_operator(cairo.OPERATOR_CLEAR)
        contexto.paint()
        contexto.set_operator(cairo.OPERATOR_OVER)
        
        # Dibujar efectos de onda
        for i in range(3):
            contexto.set_line_width(2)
            contexto.set_source_rgb(*self.colores[i])
            
            # Crear patrón de onda
            for x in range(0, ancho, 20):
                y = alto/2 + math.sin(x/30 + self.angulo + i*2) * 10
                if x == 0:
                    contexto.move_to(x, y)
                else:
                    contexto.line_to(x, y)
            
            # Dibujar línea con brillo
            contexto.stroke()
            
            # Efecto de brillo
            contexto.set_line_width(1)
            contexto.set_source_rgba(*self.colores[i], 0.5)
            contexto.stroke()
        
        # Efecto de pulso
        radio = 20 + math.sin(self.pulso) * 5
        for i in range(3):
            contexto.arc(ancho-30, alto/2, radio-i*5,
                        0, 2*math.pi)
            contexto.set_source_rgba(*self.colores[i], 0.3)
            contexto.fill()
    
    def actualizar(self):
        self.angulo += 0.1
        self.pulso += 0.15
        self.ventana.queue_draw()
        return True

def main():
    app = AnimacionesCyberpunk()
    app.ventana.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()