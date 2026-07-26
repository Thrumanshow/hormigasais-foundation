# 03. Arquitectura

- Nodo A16 (primario): ejecuta la colonia completa vía Termux.
- Nodo A20 (shadow/relay): respaldo y continuidad operativa.
- Protocolo LBH v2.0: SDKs publicados en Python y JavaScript.
- Capa de coordinación pública: Cloudflare Workers/KV/Pages, ligera y no
  crítica para el núcleo del sistema.
- Agentes de decisión: vocero, asesor semántico, árbitro, saneador de
  perímetro, bus de memoria química.
