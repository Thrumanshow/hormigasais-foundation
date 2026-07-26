#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

# Convención LBH: nunca /tmp, siempre rutas absolutas
REPO_HOME="$HOME/hormigasais-foundation"
EVIDENCE_ASSETS="$REPO_HOME/evidence/assets"
IMG_DEST="$EVIDENCE_ASSETS/architecture-overview-v0.2.0.png"

# 1. Permisos de almacenamiento
termux-setup-storage
sleep 1

mkdir -p "$EVIDENCE_ASSETS"

# 2. Buscar imagen nativa en almacenamiento local
IMG_SOURCE=$(find "$HOME/storage/pictures" "$HOME/storage/downloads" \
    "$HOME/storage/dcim" -iname "1000080409.png" 2>/dev/null | head -n1)

if [ -z "$IMG_SOURCE" ]; then
    echo "[ERROR] No se encontró 1000080409.png en almacenamiento interno." >&2
    exit 1
fi

cp "$IMG_SOURCE" "$IMG_DEST"

# 3. Verificación de copia
if [ -f "$IMG_DEST" ]; then
    echo "[OK] Evidencia copiada: $IMG_DEST"
    ls -la "$IMG_DEST"
else
    echo "[ERROR] Falló la copia." >&2
    exit 1
fi
