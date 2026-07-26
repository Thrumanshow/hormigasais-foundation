#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
cd "$HOME/hormigasais-foundation"

cat > architecture/README.md << 'EOF'
# 🏛 Architecture — HormigasAIS

Arquitectura técnica del ecosistema HormigasAIS.

- **Nodo A16 (primario):** ejecuta la colonia completa vía Termux, sin VPS
  ni cloud centralizado como dependencia crítica.
- **Nodo A20 (shadow/relay):** respaldo y continuidad operativa.
- **Protocolo LBH v2.0:** especificación con DOI en Zenodo, SDKs en
  Python y JavaScript.
- **Capa de coordinación pública:** Cloudflare Workers/KV/Pages — ligera,
  no crítica para el núcleo del sistema.
- **Jerarquía de agentes:** vocero, asesor semántico, árbitro, saneador
  de perímetro, bus de memoria química.

Ver también: [krea/03_arquitectura.md](../krea/03_arquitectura.md)
EOF

cat > institutionality/README.md << 'EOF'
# 🏛 Institutionality — HormigasAIS

Marco de identidad legal e institucional del proyecto.

- **Identidad:** Cristhiam Leonardo Hernández Quiñonez (CLHQ), fundador
  y arquitecto — Nodo A16-SanMiguel-SV, El Salvador.
- **Arquitectura legal:** marco de custodia digital bajo Protocolo LBH,
  con validación criptográfica SHA-256 + HMAC-SHA256.
- **Propiedad intelectual:** protocolo, especificación LBH_SPEC_v2.0,
  SDKs y metodología interna en titularidad exclusiva de CLHQ salvo
  cesión expresa por escrito.
- **Marco legal de referencia:** Decreto 722, Decreto 234, Decreto 643
  (El Salvador); GDPR, EU-US DPF, Principios WIPO (internacional).

Documentación legal completa: docs.hormigasais.com/legal.html
EOF

cat > platform/README.md << 'EOF'
# 🏛 Platform — HormigasAIS Foundation

Plataforma soberana de agentes inteligentes de borde (Edge Computing).

Estructura:
- [technology/](../technology/README.md) — protocolo, SDKs, cómputo de borde
- [products/](../products/README.md) — oferta comercial
- [evidence/](../evidence/README.md) — trazabilidad pública
- [institutionality/](../institutionality/README.md) — identidad y marco legal
EOF

cat > roadmap/README.md << 'EOF'
# 🏛 Roadmap — HormigasAIS

- **Fase actual:** fundación técnica e institucional completa (SDKs, DOI,
  legal, sitio, blog).
- **0–6 meses:** primeros pilotos de consultoría pagados; formalización
  de casos de uso reales.
- **6–24 meses:** escalamiento de Edge Starter; exploración de modelo SaaS.

Ver también: [krea/07_roadmap_30000.md](../krea/07_roadmap_30000.md)
EOF

cat > products/README.md << 'EOF'
# 🏛 Products — HormigasAIS

- **hormigasais-edge-starter:** producto comercial activo, punto de
  entrada productizado a la arquitectura de agentes de borde.
- **Edu Lab:** laboratorio educativo (ESP8266/Termux) para formación
  práctica en IA de borde y protocolo LBH.
EOF

cat > technology/README.md << 'EOF'
# 🏛 Technology — HormigasAIS

- **LBH Protocol:** Lenguaje Binario HormigasAIS v2.0 — DOI en Zenodo.
- **SDK Python:** publicado en PyPI.
- **SDK JavaScript:** publicado en npm.
- **Edge Computing:** ejecución soberana en Nodo A16 (Android/Termux),
  sin VPS ni cloud centralizado.
- **Autonomous Agents:** jerarquía de agentes especializados coordinados
  vía el protocolo LBH.
EOF

cat > business/README.md << 'EOF'
# 🏛 Business — HormigasAIS

**Modelo actual:** consultoría e implementación a medida del protocolo
LBH y arquitectura de agentes de borde, por proyecto.

**Ruta de crecimiento:** hacia oferta productizada (Edge Starter) y,
a mediano plazo, modelo SaaS.

Ver también: [krea/06_modelo_negocio.md](../krea/06_modelo_negocio.md)
EOF

echo "[OK] READMEs raíz escritos"
for d in architecture institutionality platform roadmap products technology business; do
    echo "$d/README.md -> $(wc -l < "$d/README.md") líneas"
done
