#!/usr/bin/env python3
"""
Generador de diagrama técnico - HormigasAIS Trampa de Mosquitos
Nodo A16 · Protocolo LBH v2.0
Optimizado para Termux
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuración de la imagen
WIDTH, HEIGHT = 1400, 900
BG_COLOR = (15, 20, 30)          # Fondo oscuro
CYAN = (0, 220, 220)
WHITE = (240, 245, 250)
LIGHT_GRAY = (180, 190, 200)
YELLOW = (255, 220, 50)
GREEN = (50, 220, 120)

def get_font(size, bold=False):
    """Intenta cargar una fuente del sistema, si no usa la default"""
    try:
        # Fuentes comunes en Termux/Android
        paths = [
            "/system/fonts/Roboto-Regular.ttf",
            "/system/fonts/Roboto-Bold.ttf",
            "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans.ttf",
            "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
        ]
        for p in paths:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    except:
        pass
    return ImageFont.load_default()

def create_diagram():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Fuentes
    font_title = get_font(42)
    font_subtitle = get_font(22)
    font_section = get_font(20)
    font_normal = get_font(16)
    font_small = get_font(14)

    # ========== TÍTULO ==========
    draw.text((WIDTH//2, 40), "HORMIGASAIS FOUNDATION — NODO A16", 
              fill=CYAN, font=font_title, anchor="mt")
    draw.text((WIDTH//2, 90), "PROTOCOLO LBH v2.0 · Trampa de Mosquitos Autónoma (IoT Edge)", 
              fill=WHITE, font=font_subtitle, anchor="mt")

    # ========== COLUMNA IZQUIERDA: Vista Funcional ==========
    left_x = 80
    y = 160

    draw.text((left_x, y), "Vista Funcional del Dispositivo", fill=CYAN, font=font_section)
    y += 45

    # Caja contenedora izquierda
    draw.rounded_rectangle([left_x-20, y-10, 620, 620], radius=15, outline=CYAN, width=2)

    components_left = [
        ("[ENTRADA DE AIRE / PERÍMETRO]", None),
        ("UV LED 5mm", "Atracción visual nocturna"),
        ("SENSOR PIR HC-SR501", "Detecta paso o corte óptico"),
        ("SEÑUELO TÉRMICO", "Resistencia IR 5V → Gradiente 36.5°C"),
        ("Ventilador 40mm 5V", "Extractor mecánico - flujo invertido"),
        ("[MALLA MOSQUITERA / CÁMARA DE RETENCIÓN]", "Neutralización pasiva"),
    ]

    box_y = y + 20
    for i, (title, desc) in enumerate(components_left):
        # Caja
        draw.rounded_rectangle([left_x+20, box_y, 560, box_y+70], radius=8, 
                               outline=LIGHT_GRAY, width=1)
        
        draw.text((left_x+40, box_y+12), title, fill=WHITE, font=font_normal)
        if desc:
            draw.text((left_x+40, box_y+38), desc, fill=LIGHT_GRAY, font=font_small)
        
        # Flecha hacia abajo (excepto el último)
        if i < len(components_left)-1:
            draw.line([(left_x+290, box_y+70), (left_x+290, box_y+90)], fill=CYAN, width=2)
            draw.polygon([(left_x+280, box_y+85), (left_x+300, box_y+85), (left_x+290, box_y+95)], fill=CYAN)
        
        box_y += 95

    # ========== COLUMNA DERECHA: Mapping ==========
    right_x = 700
    y = 160

    draw.text((right_x, y), "Mapping de la Protoboard", fill=CYAN, font=font_section)
    y += 45

    # Caja contenedora derecha
    draw.rounded_rectangle([right_x-20, y-10, 1340, 620], radius=15, outline=CYAN, width=2)

    # ESP8266 NodeMCU
    draw.rounded_rectangle([right_x+280, y+30, right_x+480, y+160], radius=10, 
                           fill=(30, 60, 100), outline=CYAN, width=2)
    draw.text((right_x+380, y+50), "NodeMCU", fill=CYAN, font=font_normal, anchor="mt")
    draw.text((right_x+380, y+80), "ESP8266", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+380, y+110), "D5 ← PIR", fill=YELLOW, font=font_small, anchor="mt")
    draw.text((right_x+380, y+130), "D1/D2 → Relays", fill=YELLOW, font=font_small, anchor="mt")

    # PIR Sensor
    draw.rounded_rectangle([right_x+40, y+40, right_x+220, y+140], radius=10, 
                           fill=(40, 40, 40), outline=GREEN, width=2)
    draw.text((right_x+130, y+55), "HC-SR501", fill=GREEN, font=font_normal, anchor="mt")
    draw.text((right_x+130, y+85), "PIR Sensor", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+130, y+110), "OUT → D5", fill=YELLOW, font=font_small, anchor="mt")

    # Relay Module
    draw.rounded_rectangle([right_x+40, y+200, right_x+260, y+320], radius=10, 
                           fill=(40, 40, 40), outline=YELLOW, width=2)
    draw.text((right_x+150, y+215), "2-Channel 5V", fill=YELLOW, font=font_normal, anchor="mt")
    draw.text((right_x+150, y+245), "Relay Module", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+150, y+270), "IN1 → Fan", fill=LIGHT_GRAY, font=font_small, anchor="mt")
    draw.text((right_x+150, y+290), "IN2 → IR Resistance", fill=LIGHT_GRAY, font=font_small, anchor="mt")

    # OTG / Alimentación
    draw.rounded_rectangle([right_x+300, y+220, right_x+520, y+320], radius=10, 
                           fill=(30, 50, 40), outline=GREEN, width=2)
    draw.text((right_x+410, y+240), "OTG USB", fill=GREEN, font=font_normal, anchor="mt")
    draw.text((right_x+410, y+270), "Android A16", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+410, y+295), "+ Fuente 5V Externa", fill=LIGHT_GRAY, font=font_small, anchor="mt")

    # Líneas de conexión (simples)
    draw.line([(right_x+220, y+90), (right_x+280, y+90)], fill=CYAN, width=2)  # PIR → NodeMCU
    draw.line([(right_x+380, y+160), (right_x+380, y+220)], fill=CYAN, width=2)  # NodeMCU → Relay/OTG

    # Texto de pines
    draw.text((right_x+40, y+360), "Conexiones principales:", fill=CYAN, font=font_normal)
    pines = [
        "• PIR VCC → 3.3V / GND → GND / OUT → D5",
        "• Relay IN1 → D1 (Ventilador)",
        "• Relay IN2 → D2 (Resistencia IR)",
        "• Alimentación: OTG USB (Android A16) + 5V externa",
        "• Negativos del ventilador y resistencia → GND común"
    ]
    py = y + 395
    for p in pines:
        draw.text((right_x+40, py), p, fill=LIGHT_GRAY, font=font_small)
        py += 28

    # ========== TEXTO DE POSICIONAMIENTO ==========
    draw.rounded_rectangle([60, 680, 1340, 790], radius=12, outline=CYAN, width=2)
    
    pos_text = [
        "Ecosistema de inteligencia distribuida basado en agentes ligeros e hiper-eficientes bajo el Protocolo LBH.",
        "Automatización, monitoreo y procesamiento Edge con consumo mínimo y soberanía total de datos.",
        "Nodo Maestro A16 · San Miguel, El Salvador"
    ]
    
    ty = 700
    for line in pos_text:
        draw.text((WIDTH//2, ty), line, fill=WHITE, font=font_normal, anchor="mt")
        ty += 28

    # Footer
    draw.text((WIDTH//2, 850), 
              "HormigasAIS Foundation © 2026  |  Evidencia Técnica · Hardware Real  |  Verificable en hormigasais.com", 
              fill=LIGHT_GRAY, font=font_small, anchor="mt")

    # Guardar
    output = "hormigasais_trampa_nodo_a16_lbh.png"
    img.save(output, "PNG", quality=95)
    print(f"\n✅ Imagen generada exitosamente: {output}")
    print(f"   Ruta completa: {os.path.abspath(output)}")
    return output

if __name__ == "__main__":
    create_diagram()
