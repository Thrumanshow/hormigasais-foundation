#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

REPO_HOME="$HOME/hormigasais-foundation"
KREA_DIR="$REPO_HOME/krea"
REPORT_DIR="$REPO_HOME/reports"
REPORT_FILE="$REPORT_DIR/krea_audit_report.md"

mkdir -p "$REPORT_DIR"

DOCS=(01_problema.md 02_solucion.md 03_arquitectura.md 04_evidencia_tecnica.md \
      05_mercado_objetivo.md 06_modelo_negocio.md 07_roadmap_30000.md 08_impacto_social.md)
FOLDERS=(architecture financial market impact annexes media)

{
  echo "# 🐜 HormigasAIS KREA Audit"
  echo
  echo "_Generado: $(date '+%Y-%m-%d %H:%M:%S')_"
  echo
  echo "## Documentos"
  echo '```'
  for doc in "${DOCS[@]}"; do
      f="$KREA_DIR/$doc"
      if [ -f "$f" ]; then
          lines=$(wc -l < "$f")
          if [ "$lines" -eq 0 ]; then
              printf "%-28s ⚠️  VACÍO (0 líneas)\n" "$doc"
          else
              printf "%-28s OK  %s líneas\n" "$doc" "$lines"
          fi
      else
          printf "%-28s FALTA\n" "$doc"
      fi
  done
  echo '```'
  echo
  echo "## README"
  echo '```'
  if [ -f "$KREA_DIR/README.md" ]; then echo "OK"; else echo "FALTA"; fi
  echo '```'
  echo
  echo "## Carpetas"
  echo '```'
  for folder in "${FOLDERS[@]}"; do
      if [ -d "$KREA_DIR/$folder" ] && [ -f "$KREA_DIR/$folder/README.md" ]; then
          echo "${folder}/   OK"
      elif [ -d "$KREA_DIR/$folder" ]; then
          echo "${folder}/   ⚠️  sin README.md"
      else
          echo "${folder}/   FALTA"
      fi
  done
  echo '```'
  echo
  echo "## one-pager / pitch-deck"
  echo '```'
  for f in one-pager.md pitch-deck.md; do
      lines=$(wc -l < "$KREA_DIR/$f" 2>/dev/null || echo 0)
      if [ "$lines" -eq 0 ]; then
          printf "%-28s ⚠️  VACÍO\n" "$f"
      else
          printf "%-28s OK  %s líneas\n" "$f" "$lines"
      fi
  done
  echo '```'
  echo
  echo "## Estado"
  echo '```'
  MISSING=0
  for doc in "${DOCS[@]}"; do
      f="$KREA_DIR/$doc"
      if [ ! -f "$f" ] || [ "$(wc -l < "$f")" -eq 0 ]; then
          MISSING=1
      fi
  done
  [ -f "$KREA_DIR/README.md" ] || MISSING=1
  if [ "$MISSING" -eq 0 ]; then
      echo "READY FOR REVIEW"
  else
      echo "INCOMPLETO — revisar elementos marcados arriba"
  fi
  echo '```'
} > "$REPORT_FILE"

echo "[OK] Reporte generado: $REPORT_FILE"
cat "$REPORT_FILE"
