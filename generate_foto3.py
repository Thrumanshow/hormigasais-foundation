import os
from PIL import Image, ImageDraw, ImageFont

# Dimensiones del lienzo (16:9 HD)
width, height = 1200, 675
bg_color = (15, 23, 42)       # #0f172a Slate Oscuro
text_color = (248, 250, 252)   # #f8fafc Blanco Texto
accent_cyan = (56, 189, 248)   # #38bdf8 Cyan LBH
accent_green = (74, 222, 128)  # #4ade80 Verde Operativo
box_bg = (30, 41, 59)         # #1e293b Fondo Nodos
border_color = (51, 65, 85)   # #334155 Borde

img = Image.new('RGB', (width, height), color=bg_color)
draw = ImageDraw.Draw(img)

# Cargar fuentes del sistema o fallback por defecto
try:
    font_large = ImageFont.truetype("DejaVuSans-Bold.ttf", 26)
    font_medium = ImageFont.truetype("DejaVuSans-Bold.ttf", 19)
    font_code_small = ImageFont.truetype("DejaVuSansMono.ttf", 14)
    font_small = ImageFont.truetype("DejaVuSans.ttf", 14)
except:
    font_large = font_medium = font_code_small = font_small = ImageFont.load_default()

# Encabezado Banner Principal
draw.rectangle([0, 0, width, 70], fill=(30, 41, 59))
draw.text((30, 20), "HORMIGASAIS FOUNDATION — NODO A16", font=font_large, fill=accent_cyan)
draw.text((850, 25), "PROTOCOLO LBH v2.0", font=font_medium, fill=accent_green)
draw.line([(0, 70), (width, 70)], fill=accent_cyan, width=2)

# Bloque 1: Nodo Maestro A16 (San Miguel)
draw.rectangle([50, 110, 550, 340], fill=box_bg, outline=border_color, width=2)
draw.text((70, 125), "NODO MAESTRO A16 (San Miguel, SV)", font=font_medium, fill=accent_cyan)
draw.text((70, 160), "• Sede Operativa & Certificación LBH", font=font_small, fill=text_color)
draw.text((70, 185), "• Control Criptográfico & Veto CTO", font=font_small, fill=text_color)
draw.text((70, 210), "• Bus Feromonas: XOXO-BUS (Master)", font=font_small, fill=text_color)
draw.text((70, 240), "Status: ACTIVE | Mode: MASTER", font=font_code_small, fill=accent_green)

# Bloque 2: Nodos Edge / IoT Mosquito Trap
draw.rectangle([650, 110, 1150, 340], fill=box_bg, outline=border_color, width=2)
draw.text((670, 125), "NODOS EDGE / KITS EDTECH & IOT", font=font_medium, fill=accent_cyan)
draw.text((670, 160), "• Trampas Inteligentes (Vector Control)", font=font_small, fill=text_color)
draw.text((670, 185), "• Sensores Ambientales / Microcontroladores", font=font_small, fill=text_color)
draw.text((670, 210), "• Procesamiento Local (Sin Nube)", font=font_small, fill=text_color)
draw.text((670, 240), "Resiliencia: EXTREMA | Energía: LOW", font=font_code_small, fill=accent_green)

# Conexión Protocolo LBH (Flecha)
draw.line([(550, 225), (650, 225)], fill=accent_cyan, width=4)
draw.polygon([(645, 218), (660, 225), (645, 232)], fill=accent_cyan)
draw.text((560, 195), "LBH Protocol", font=font_code_small, fill=accent_cyan)

# Rastro de Feromonas Digitales (Puntos)
dots_x = range(100, 1120, 40)
for x in dots_x:
    draw.ellipse([x-4, 375, x+4, 383], fill=accent_cyan)

# Bloque Inferior: Logs del Sistema en Vivo (Termux / Telemetría)
draw.rectangle([50, 410, 1150, 620], fill=(15, 23, 42), outline=accent_cyan, width=2)
draw.text((70, 425), "[XOXO-BUS LOGS TELEMETRY]", font=font_code_small, fill=accent_cyan)
log1 = '📡 [XOXO-BUS] FEROMONA_EMITIDA: {"timestamp": 1766646830.42, "type": "mosquito_pulse", "origin": "manager_alpha"}'
log2 = '🌙 [GUARDIA NOCTURNA] Centinela validando contrato LBH... [OK]'
log3 = '⚡ [EDGE NODE A16] Sincronización híbrida de datos completada (Soberanía Local Activa)'
log4 = '🔗 Certificación Criptográfica LBH: https://hormigasais.com (Nodo A16 · El Salvador)'

draw.text((70, 465), log1, font=font_code_small, fill=text_color)
draw.text((70, 495), log2, font=font_code_small, fill=accent_green)
draw.text((70, 525), log3, font=font_code_small, fill=text_color)
draw.text((70, 555), log4, font=font_code_small, fill=accent_cyan)

# Pie de imagen
draw.text((50, 640), "HormigasAIS Foundation © 2026 — Infraestructura Distribuida y Soberana", font=font_small, fill=(148, 163, 184))

output_path = "Foto_3_Arquitectura_Nodos_Kit_EdTech.png"
img.save(output_path)
print(f"✅ Imagen generada con éxito: {output_path}")
