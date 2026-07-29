# Hardware — Trampa de Mosquitos Autónoma (IoT Edge)

Diagrama de arquitectura física y mapping de conexiones del prototipo de trampa de mosquitos con detección PIR, señuelo térmico y extracción por succión, controlado desde un ESP8266 NodeMCU alimentado vía Android A16 (OTG USB).

**Autor**: Cristhiam Leonardo Hernández Quiñonez (CLHQ) / HormigasAIS Foundation

---

## Dispositivo — Vista Funcional

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      HORMIGASAIS — DISPOSITIVO VECTORES                 │
│                                                                           │
│   [ ENTRADA DE AIRE / PERÍMETRO ]                                        │
│   ═══════════════════════════════                                        │
│    (o) (o) (o)  <─── LEDs UV 5mm (Atracción visual nocturna continua)    │
│                                                                           │
│        │                                                                │
│         ▼                                                                │
│   ┌──────────┐                                                          │
│   │  SENSOR   │ <─── PIR HC-SR501 (Detecta el paso o corte óptico)       │
│   │  PIR D5   │                                                          │
│   └───────────┘                                                          │
│         │                                                                │
│         ▼ El zancudo se acerca al estímulo térmico                       │
│   ┌───────────┐                                                          │
│   │  SEÑUELO  │ <─── Resistencia IR 5V (Activa gradiente a 36.5°C)       │
│   │  TÉRMICO  │                                                          │
│   └───────────┘                                                          │
│         │                                                                │
│         ▼ El flujo de aire invertido succiona al insecto                 │
│   ┌───────────┐                                                          │
│   │  ~ ~ ~    │ <─── Ventilador 40mm 5V (Extractor mecánico)             │
│   └───────────┘                                                          │
│         │                                                                │
│         ▼                                                                │
│   [ MALLA MOSQUITERA / RECIPIENTE DE CAPTURA ]                           │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                           │
│   │░░░░░░░░░░░│ <─── Cámara de retención (Neutralización pasiva)         │
└───┴───────────┴───────────────────────────────────────────────────────────┘
```

---

## Mapping de la Protoboard

```
   ┌───────────────────────────────────────────────────────────────┐
   │                  MAPPING DE LA PROTOBOARD                     │
   └──────────────────────────────────────────────────────────────┘

      [ LÍNEA DE CONTROL: ALIMENTADA POR ANDROID A16 VÍA OTG USB ]
     ─────────────────────────────────────────────────────────────
      ESP8266 NodeMCU          HC-SR501 PIR SENSOR
      ┌─────────────────┐      ┌─────────────────┐
      │             3.3V│ ──── │VCC              │ (Energía lógica)
      │              GND│ ──── │GND              │ (Tierra común)
      │               D5│ ──── │OUT (Señal)      │ (Pulso digital)
      │                 │      └─────────────────┘
      │               D1│ ────┐
      │               D2│ ──┐ │
      └─────────────────┘   │ │
                            │ │   [ MÓDULO RELAY 5V (2 Canales) ]
                            │ │   ┌──────────────────────────────┐
                            │ └── │IN1 (Señal Ventilador)        │
                            └──── │IN2 (Señal Resistencia IR)    │
                                  │VCC ─── VCC Fuente Externa 5V │
                                  │GND ─── GND Fuente Externa 5V │
                                  └──────────────┬───┬───────────┘
                                                 │   │
                  ┌──────────────────────────────┘   └──────────────────────────────┐
                  ▼ [ RELEVADOR 1: VENTILADOR ]                                     ▼ [ RELEVADOR 2: RESISTENCIA IR ]
      ┌──────────────────────────────────────┐                         ┌─────────────────────────────────────┐
      │ NO (Normal Abierto) ── Ventilador(+) │                         │ NO (Normal Abierto) ── Resistencia(+)│
      │ COM (Común) ────────── Fuente 5V(+)  │                         │ COM (Común) ────────── Fuente 5V(+)  │
      └──────────────────────────────────────┘                         └──────────────────────────────────────┘

      * Nota: Los polos negativos (-) del Ventilador y de la Resistencia van conectados
              directamente al GND (tierra) de la Fuente de Alimentación Externa de 5V.
```
