#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
cd "$HOME/hormigasais-foundation"

cp krea/01_problema.md krea/01_problema.md.bak
cat > krea/01_problema.md << 'EOF'
# 01. Problema

Los sistemas de inteligencia artificial modernos dependen casi por completo
de infraestructura cloud centralizada — costosa, sujeta a proveedores
extranjeros, y frágil ante fallas de conectividad o restricciones
regulatorias.

Para instituciones, PYMEs y desarrolladores en economías emergentes como
El Salvador, esto crea una barrera estructural: no hay soberanía real
sobre su propia infraestructura de IA. El costo se factura en moneda
extranjera, los datos salen del país, y la continuidad del servicio
depende de terceros fuera de control local.
EOF

cp krea/02_solucion.md krea/02_solucion.md.bak
cat > krea/02_solucion.md << 'EOF'
# 02. Solución

HormigasAIS es un ecosistema de agentes inteligentes que corre íntegramente
en el borde (Edge Computing), sin depender de un VPS ni de infraestructura
cloud centralizada.

Su protocolo propio, LBH (Lenguaje Binario HormigasAIS), coordina una
colonia de agentes especializados — inspirados en el comportamiento de
hormigas — que operan de forma resiliente, auditable y verificable,
incluso desde un único dispositivo Android.
EOF

cp krea/03_arquitectura.md krea/03_arquitectura.md.bak
cat > krea/03_arquitectura.md << 'EOF'
# 03. Arquitectura

- Nodo A16 (primario): ejecuta la colonia completa vía Termux.
- Nodo A20 (shadow/relay): respaldo y continuidad operativa.
- Protocolo LBH v2.0: SDKs publicados en Python y JavaScript.
- Capa de coordinación pública: Cloudflare Workers/KV/Pages, ligera y no
  crítica para el núcleo del sistema.
- Agentes de decisión: vocero, asesor semántico, árbitro, saneador de
  perímetro, bus de memoria química.
EOF

cp krea/04_evidencia_tecnica.md krea/04_evidencia_tecnica.md.bak
cat > krea/04_evidencia_tecnica.md << 'EOF'
# 04. Evidencia técnica

Ver tabla completa en evidence/README.md.

Resumen:
- SDK LBH (Python, PyPI): publicado
- SDK LBH (JavaScript, npm): publicado
- LBH_SPEC_v2.0: DOI registrado en Zenodo
- hormigasais-edge-starter: producto comercial activo
- blog.hormigasais.com: en producción
- Nodo A16: ejecución en vivo, verificado
EOF

echo "[OK] 01-04 escritos"
for f in 01_problema.md 02_solucion.md 03_arquitectura.md 04_evidencia_tecnica.md; do
    echo "$f -> $(wc -l < "krea/$f") líneas"
done
