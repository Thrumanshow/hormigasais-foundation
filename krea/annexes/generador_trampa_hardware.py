#!/usr/bin/env python3
"""
Generador de diagrama técnico - HormigasAIS Trampa de Mosquitos
Nodo A16 · Protocolo LBH v2.0 - v2 corregida
"""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1400, 1000
BG_COLOR = (15, 20, 30)
CYAN = (0, 220, 220)
WHITE = (240, 245, 250)
LIGHT_GRAY = (180, 190, 200)
YELLOW = (255, 220, 50)
GREEN = (50, 220, 120)

def get_font(size):
    paths = [
        "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans.ttf",
        "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
        "/system/fonts/Roboto-Regular.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def create_diagram():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    font_title = get_font(42)
    font_subtitle = get_font(22)
    font_section = get_font(20)
    font_normal = get_font(16)
    font_small = get_font(14)

    draw.text((WIDTH//2, 40), "HORMIGASAIS FOUNDATION - NODO A16",
              fill=CYAN, font=font_title, anchor="mt")
    draw.text((WIDTH//2, 90), "PROTOCOLO LBH v2.0 - Trampa de Mosquitos Autonoma (IoT Edge)",
              fill=WHITE, font=font_subtitle, anchor="mt")

    left_x = 80
    y = 160
    draw.text((left_x, y), "Vista Funcional del Dispositivo", fill=CYAN, font=font_section)
    y += 45

    components_left = [
        ("[ENTRADA DE AIRE / PERIMETRO]", None),
        ("UV LED 5mm", "Atraccion visual nocturna"),
        ("SENSOR PIR HC-SR501", "Detecta paso o corte optico"),
        ("SENUELO TERMICO", "Resistencia IR 5V - Gradiente 36.5C"),
        ("Ventilador 40mm 5V", "Extractor mecanico - flujo invertido"),
        ("[MALLA MOSQUITERA / CAMARA DE RETENCION]", "Neutralizacion pasiva"),
    ]

    box_h = 70
    gap = 25
    total_boxes_height = len(components_left) * (box_h + gap)
    contenedor_bottom = y + 20 + total_boxes_height + 10

    draw.rounded_rectangle([left_x-20, y-10, 620, contenedor_bottom],
                           radius=15, outline=CYAN, width=2)

    box_y = y + 20
    for i, (title, desc) in enumerate(components_left):
        draw.rounded_rectangle([left_x+20, box_y, 560, box_y+box_h], radius=8,
                               outline=LIGHT_GRAY, width=1)
        draw.text((left_x+40, box_y+12), title, fill=WHITE, font=font_normal)
        if desc:
            draw.text((left_x+40, box_y+38), desc, fill=LIGHT_GRAY, font=font_small)

        if i < len(components_left)-1:
            draw.line([(left_x+290, box_y+box_h), (left_x+290, box_y+box_h+20)], fill=CYAN, width=2)
            draw.polygon([(left_x+280, box_y+box_h+15), (left_x+300, box_y+box_h+15),
                          (left_x+290, box_y+box_h+25)], fill=CYAN)
        box_y += box_h + gap

    right_x = 700
    y = 160
    draw.text((right_x, y), "Mapping de la Protoboard", fill=CYAN, font=font_section)
    y += 45

    draw.rounded_rectangle([right_x-20, y-10, 1340, contenedor_bottom],
                           radius=15, outline=CYAN, width=2)

    draw.rounded_rectangle([right_x+280, y+30, right_x+480, y+160], radius=10,
                           fill=(30, 60, 100), outline=CYAN, width=2)
    draw.text((right_x+380, y+50), "NodeMCU", fill=CYAN, font=font_normal, anchor="mt")
    draw.text((right_x+380, y+80), "ESP8266", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+380, y+110), "D5 <- PIR", fill=YELLOW, font=font_small, anchor="mt")
    draw.text((right_x+380, y+130), "D1/D2 -> Relays", fill=YELLOW, font=font_small, anchor="mt")

    draw.rounded_rectangle([right_x+40, y+40, right_x+220, y+140], radius=10,
                           fill=(40, 40, 40), outline=GREEN, width=2)
    draw.text((right_x+130, y+55), "HC-SR501", fill=GREEN, font=font_normal, anchor="mt")
    draw.text((right_x+130, y+85), "PIR Sensor", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+130, y+110), "OUT -> D5", fill=YELLOW, font=font_small, anchor="mt")

    draw.rounded_rectangle([right_x+40, y+200, right_x+260, y+320], radius=10,
                           fill=(40, 40, 40), outline=YELLOW, width=2)
    draw.text((right_x+150, y+215), "2-Channel 5V", fill=YELLOW, font=font_normal, anchor="mt")
    draw.text((right_x+150, y+245), "Relay Module", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+150, y+270), "IN1 -> Fan", fill=LIGHT_GRAY, font=font_small, anchor="mt")
    draw.text((right_x+150, y+290), "IN2 -> IR Resistance", fill=LIGHT_GRAY, font=font_small, anchor="mt")

    draw.rounded_rectangle([right_x+300, y+220, right_x+520, y+320], radius=10,
                           fill=(30, 50, 40), outline=GREEN, width=2)
    draw.text((right_x+410, y+240), "OTG USB", fill=GREEN, font=font_normal, anchor="mt")
    draw.text((right_x+410, y+270), "Android A16", fill=WHITE, font=font_small, anchor="mt")
    draw.text((right_x+410, y+295), "+ Fuente 5V Externa", fill=LIGHT_GRAY, font=font_small, anchor="mt")

    draw.line([(right_x+220, y+90), (right_x+280, y+90)], fill=CYAN, width=2)
    draw.line([(right_x+380, y+160), (right_x+380, y+220)], fill=CYAN, width=2)

    draw.text((right_x+40, y+360), "Conexiones principales:", fill=CYAN, font=font_normal)
    pines = [
        "- PIR VCC -> 3.3V / GND -> GND / OUT -> D5",
        "- Relay IN1 -> D1 (Ventilador)",
        "- Relay IN2 -> D2 (Resistencia IR)",
        "- Alimentacion: OTG USB (Android A16) + 5V externa",
        "- Negativos del ventilador y resistencia -> GND comun"
    ]
    py = y + 395
    for p in pines:
        draw.text((right_x+40, py), p, fill=LIGHT_GRAY, font=font_small)
        py += 28

    resumen_top = contenedor_bottom + 40
    resumen_bottom = resumen_top + 110
    draw.rounded_rectangle([60, resumen_top, 1340, resumen_bottom], radius=12, outline=CYAN, width=2)

    pos_text = [
        "Ecosistema de inteligencia distribuida basado en agentes ligeros e hiper-eficientes bajo el Protocolo LBH.",
        "Automatizacion, monitoreo y procesamiento Edge con consumo minimo y soberania total de datos.",
        "Nodo Maestro A16 - San Miguel, El Salvador"
    ]
    ty = resumen_top + 20
    for line in pos_text:
        draw.text((WIDTH//2, ty), line, fill=WHITE, font=font_normal, anchor="mt")
        ty += 28

    draw.text((WIDTH//2, resumen_bottom + 30),
              "HormigasAIS Foundation (c) 2026 | Evidencia Tecnica - Hardware Real | Verificable en hormigasais.com",
              fill=LIGHT_GRAY, font=font_small, anchor="mt")

    output = "hormigasais_trampa_nodo_a16_lbh_v2.png"
    img.save(output, "PNG")
    print("Imagen generada:", os.path.abspath(output))
    return output

if __name__ == "__main__":
    create_diagram()
