#!/data/data/com.termux/files/usr/bin/bash

# ============================================
# Script: Actualizar imagen de Hardware Real
# HormigasAIS - Nodo A16 - Trampa de Mosquitos
# Reemplaza también Foto_3_Arquitectura...
# ============================================

set -e

REPO_DIR="$HOME/hormigasais-foundation"
IMAGE_SOURCE="/sdcard/Download/hormigasais_trampa_nodo_a16_lbh.png"
TARGET_DIR="$REPO_DIR/krea/annexes"
TARGET_NAME="Foto_Hardware_Trampa_Mosquitos_LBH_NodoA16.png"
OLD_IMAGE_NAME="Foto_3_Arquitectura_Nodos_Kit_EdTech.png"
EVIDENCE_README="$REPO_DIR/evidence/README.md"

echo "🔍 Verificando imagen fuente..."
if [ ! -f "$IMAGE_SOURCE" ]; then
    echo "❌ No se encontró la imagen en:"
    echo "   $IMAGE_SOURCE"
    exit 1
fi

echo "✅ Imagen encontrada:"
ls -lh "$IMAGE_SOURCE"

# Entrar al repositorio
cd "$REPO_DIR" || exit 1

# Crear directorio si no existe
mkdir -p "$TARGET_DIR"

# 1. Copiar la nueva imagen con nombre descriptivo
echo "📦 Copiando nueva imagen de hardware..."
cp "$IMAGE_SOURCE" "$TARGET_DIR/$TARGET_NAME"
echo "✅ Nueva imagen guardada como: krea/annexes/$TARGET_NAME"

# 2. Reemplazar la imagen vieja Foto_3_Arquitectura...
echo ""
echo "🔄 Reemplazando imagen antigua ($OLD_IMAGE_NAME)..."
cp "$IMAGE_SOURCE" "$TARGET_DIR/$OLD_IMAGE_NAME"
echo "✅ $OLD_IMAGE_NAME ha sido reemplazada con la nueva imagen de hardware"

# Mostrar ambas
echo ""
echo "📁 Imágenes actuales en krea/annexes/:"
ls -lh "$TARGET_DIR"/Foto_*

# Calcular hash de la nueva
echo ""
echo "🔐 SHA256 de la nueva imagen:"
sha256sum "$TARGET_DIR/$TARGET_NAME"

# Preguntar si desea actualizar evidence/README.md
echo ""
read -p "¿Deseas agregar/actualizar la entrada en evidence/README.md? (s/n): " RESP

if [[ "$RESP" == "s" || "$RESP" == "S" ]]; then
    echo ""
    echo "📝 Agregando entrada en evidence/README.md..."

    cat >> "$EVIDENCE_README" << EOF

## Imagen — Hardware Real: Trampa de Mosquitos IoT (Nodo A16)

| Campo | Valor |
|---|---|
| Archivo | \`krea/annexes/$TARGET_NAME\` |
| También reemplaza | \`krea/annexes/$OLD_IMAGE_NAME\` |
| Tipo | Diagrama técnico de hardware real |
| Componentes | ESP8266 NodeMCU + PIR HC-SR501 + Resistencia IR + Ventilador 40mm + Relay 5V |
| Generado | Script \`crear_trampa_lbh.py\` (Termux) |
| Fecha | $(date +%Y-%m-%d) |
| Nodo | A16 · San Miguel, El Salvador |
| Protocolo | LBH v2.0 |
| Estado | ✅ Hardware documentado y versionado |

EOF

    echo "✅ evidence/README.md actualizado"
fi

# Mostrar estado de git
echo ""
echo "📊 Estado actual de Git:"
git status

echo ""
echo "============================================"
echo "✅ Proceso completado"
echo ""
echo "Se realizaron estos cambios:"
echo "  • Nueva imagen: krea/annexes/$TARGET_NAME"
echo "  • Imagen antigua reemplazada: krea/annexes/$OLD_IMAGE_NAME"
echo ""
echo "Próximos pasos recomendados:"
echo "1. git add krea/annexes/ evidence/README.md"
echo "2. git commit -m \"docs: replace architecture image with real hardware diagram - Trampa Mosquitos IoT Nodo A16\""
echo "3. git push origin main"
echo "============================================"
