#!/data/data/com.termux/files/usr/bin/bash

set -e

echo
echo "=========================================="
echo " HormigasAIS Foundation"
echo " KREA Structure Generator v0.4.0"
echo "=========================================="
echo

if [ ! -f README.md ]; then
    echo "[ERROR] Ejecuta este script desde la raíz del repositorio."
    exit 1
fi

mkdir -p \
krea \
krea/architecture \
krea/impact \
krea/market \
krea/financial \
krea/media \
krea/annexes

create_if_missing(){

FILE="$1"

if [ ! -f "$FILE" ]; then
cat > "$FILE"
fi

}

create_if_missing krea/README.md <<'EOT'
# 🚀 KREA Data Room

Centro documental para convocatorias, aceleradoras,
fondos de innovación e inversionistas.

Esta carpeta reúne toda la documentación institucional
de HormigasAIS Foundation.
EOT

create_if_missing krea/application.md <<'EOT'
# Application

Documento principal de postulación.
EOT

create_if_missing krea/one-pager.md <<'EOT'
# One Pager

Resumen ejecutivo de una página.
EOT

create_if_missing krea/pitch-deck.md <<'EOT'
# Pitch Deck

Presentación institucional.
EOT

create_if_missing krea/business-model.md <<'EOT'
# Business Model

Modelo de negocio.
EOT

create_if_missing krea/architecture/README.md <<'EOT'
# Arquitectura

Diagramas técnicos y arquitectura del ecosistema.
EOT

create_if_missing krea/impact/README.md <<'EOT'
# Impacto

Impacto social, educativo y tecnológico.
EOT

create_if_missing krea/market/README.md <<'EOT'
# Mercado

Clientes objetivo, posicionamiento y oportunidades.
EOT

create_if_missing krea/financial/README.md <<'EOT'
# Financial

Costos, proyecciones y sostenibilidad.
EOT

create_if_missing krea/media/README.md <<'EOT'
# Media

Logos, imágenes, infografías y recursos gráficos.
EOT

create_if_missing krea/annexes/README.md <<'EOT'
# Annexes

Documentación complementaria.
EOT

echo
echo "=========================================="
echo " KREA Data Room"
echo "=========================================="
echo

find krea | sort

echo
echo "[OK] Estructura creada correctamente."

