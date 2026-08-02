import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

# Leer el evento real del log (no fabricado)
LOG_PATH = os.path.expanduser("~/hormigasais-core/logs/pheromone_stream.log")
with open(LOG_PATH, "r") as f:
    lineas = f.readlines()
evento_real = lineas[-1].strip() if lineas else "Sin datos disponibles"

# Extraer timestamp real del JSON y convertirlo a fecha legible
import json
try:
    data = json.loads(evento_real)
    ts = data.get("timestamp")
    fecha_legible = subprocess.check_output(["date", "-d", f"@{ts}"]).decode().strip()
except Exception:
    fecha_legible = "Fecha no disponible"

# Dimensiones del lienzo (16:9 HD)
width, height = 1200, 675
bg_color = (15, 23, 42)
text_color = (248, 250, 252)
accent_cyan = (56, 189, 248)
accent_green = (74, 222, 128)
box_bg = (30, 41, 59)
border_color = (51, 65, 85)

img = Image.new('RGB', (width, height), color=bg_color)
draw = ImageDraw.Draw(img)

FONT_DIR = "/data/data/com.termux/files/usr/share/fonts/TTF/"
font_large = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 26)
font_medium = ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", 19)
font_code_small = ImageFont.truetype(FONT_DIR + "DejaVuSansMono.ttf", 14)
font_small = ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", 14)

draw.rectangle([0, 0, width, 70], fill=(30, 41, 59))
draw.text((30, 20), "HORMIGASAIS FOUNDATION — NODO A16", font=font_large, fill=accent_cyan)
draw.text((850, 25), "PROTOCOLO LBH v2.0", font=font_medium, fill=accent_green)
draw.line([(0, 70), (width, 70)], fill=accent_cyan, width=2)

draw.rectangle([50, 110, 550, 340], fill=box_bg, outline=border_color, width=2)
draw.text((70, 125), "NODO MAESTRO A16 (San Miguel, SV)", font=font_medium, fill=accent_cyan)
draw.text((70, 160), "• Sede Operativa & Certificación LBH", font=font_small, fill=text_color)
draw.text((70, 185), "• Control Criptográfico & Veto CTO", font=font_small, fill=text_color)
draw.text((70, 210), "• Bus Feromonas: XOXO-BUS (Master)", font=font_small, fill=text_color)
draw.text((70, 240), "Status: ACTIVE | Mode: MASTER", font=font_code_small, fill=accent_green)

draw.rectangle([650, 110, 1150, 340], fill=box_bg, outline=border_color, width=2)
draw.text((670, 125), "NODOS EDGE / KITS EDTECH & IOT", font=font_medium, fill=accent_cyan)
draw.text((670, 160), "• Trampas Inteligentes (Vector Control)", font=font_small, fill=text_color)
draw.text((670, 185), "• Sensores Ambientales / Microcontroladores", font=font_small, fill=text_color)
draw.text((670, 210), "• Procesamiento Local (Sin Nube)", font=font_small, fill=text_color)
draw.text((670, 240), "Resiliencia: EXTREMA | Energía: LOW", font=font_code_small, fill=accent_green)

draw.line([(550, 225), (650, 225)], fill=accent_cyan, width=4)
draw.polygon([(645, 218), (660, 225), (645, 232)], fill=accent_cyan)
draw.text((560, 195), "LBH Protocol", font=font_code_small, fill=accent_cyan)

dots_x = range(100, 1120, 40)
for x in dots_x:
    draw.ellipse([x-4, 375, x+4, 383], fill=accent_cyan)

draw.rectangle([50, 410, 1150, 570], fill=(15, 23, 42), outline=accent_cyan, width=2)
draw.text((70, 425), "[EVENTO REAL — pheromone_stream.log]", font=font_code_small, fill=accent_cyan)
draw.text((70, 465), evento_real, font=font_code_small, fill=text_color)
draw.text((70, 495), f"Fecha real: {fecha_legible}", font=font_code_small, fill=accent_green)
draw.text((70, 525), "Certificación Criptográfica LBH: https://hormigasais.com (Nodo A16 · El Salvador)", font=font_code_small, fill=accent_cyan)

draw.text((50, 640), "HormigasAIS Foundation © 2026 — Infraestructura Distribuida y Soberana", font=font_small, fill=(148, 163, 184))

output_path = "krea/annexes/Foto_3_Arquitectura_Nodos_Kit_EdTech_v2.png"
img.save(output_path)
print(f"✅ Imagen generada con datos reales: {output_path}")
print(f"Evento usado: {evento_real}")
print(f"Fecha real: {fecha_legible}")
