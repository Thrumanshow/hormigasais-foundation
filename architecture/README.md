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
