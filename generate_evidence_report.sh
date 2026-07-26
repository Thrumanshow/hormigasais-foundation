#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

REPO="$HOME/hormigasais-foundation"
EVIDENCE="$REPO/evidence"

mkdir -p "$EVIDENCE/reports"

echo "[INFO] Generando evidencia..."

############################################################
# runtime.txt
############################################################

{
echo "========================================"
echo "HormigasAIS Runtime Evidence"
echo "========================================"
echo
echo "Fecha:"
date
echo
echo "Hostname:"
hostname
echo
echo "Kernel:"
uname -sr
echo
echo "Arquitectura:"
uname -m
echo
echo "Uptime:"
uptime
echo
echo "Usuario:"
whoami
echo
echo "PWD:"
pwd
} > "$EVIDENCE/a16/runtime.txt"

############################################################
# termux-version.txt
############################################################

{
echo "========================================"
echo "Termux Environment"
echo "========================================"
echo

echo "Fecha:"
date
echo

echo "Android:"
getprop ro.build.version.release

echo
echo "SDK:"
getprop ro.build.version.sdk

echo
echo "Dispositivo:"
getprop ro.product.model

echo
echo "Fabricante:"
getprop ro.product.manufacturer

echo
echo "Kernel:"
uname -r

echo
echo "Bash:"
bash --version | head -n1

echo
echo "Git:"
git --version

echo
echo "Python:"
python --version 2>&1 || true

echo
echo "Node:"
node --version 2>/dev/null || true

echo
echo "npm:"
npm --version 2>/dev/null || true

echo
echo "Termux Packages:"
pkg list-installed 2>/dev/null || true

} > "$EVIDENCE/a16/termux-version.txt"

############################################################
# Reporte general
############################################################

REPORT="$EVIDENCE/reports/report-$(date +%Y%m%d-%H%M%S).md"

{
echo "# HormigasAIS Evidence Report"
echo
echo "**Fecha:** $(date)"
echo
echo "## Nodo"
echo
echo "- Host: $(hostname)"
echo "- Usuario: $(whoami)"
echo "- Arquitectura: $(uname -m)"
echo "- Kernel: $(uname -sr)"
echo
echo "## Evidencias disponibles"
echo
find "$EVIDENCE" -maxdepth 2 -type f | sed "s|$REPO/||"
echo
echo "## Estado"
echo
echo "✅ Runtime generado"
echo "✅ Información Termux actualizada"
echo "✅ Reporte generado automáticamente"
echo
echo "---"
echo
echo "HormigasAIS Foundation"
echo "Nodo Maestro A16"
} > "$REPORT"

############################################################
# Resumen
############################################################

echo
echo "======================================"
echo " Evidence Generated"
echo "======================================"

echo
echo "Runtime:"
echo "  $EVIDENCE/a16/runtime.txt"

echo
echo "Termux:"
echo "  $EVIDENCE/a16/termux-version.txt"

echo
echo "Reporte:"
echo "  $REPORT"

echo
echo "[OK] Evidencia actualizada."

