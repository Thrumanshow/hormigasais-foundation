#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "========================================="
echo " HormigasAIS Foundation v0.2.0 Bootstrap "
echo "========================================="

mkdir -p \
platform \
technology \
technology/lbh \
technology/sdk-python \
technology/sdk-javascript \
products \
products/edge-starter \
products/edu-lab \
products/lbh-protocol \
evidence \
evidence/github \
evidence/npm \
evidence/zenodo \
evidence/a16 \
institutionality

touch \
platform/README.md \
technology/README.md \
technology/lbh/README.md \
technology/sdk-python/README.md \
technology/sdk-javascript/README.md \
products/README.md \
products/edge-starter/README.md \
products/edu-lab/README.md \
products/lbh-protocol/README.md \
evidence/README.md \
evidence/github/README.md \
evidence/npm/README.md \
evidence/zenodo/README.md \
evidence/a16/README.md \
institutionality/README.md

echo
echo "Estructura creada correctamente."
echo
echo "Siguiente paso:"
echo "find ."
echo "git status"
