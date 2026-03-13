#!/bin/bash

# 1. Créer le virtual environment
python -m venv venv

# 2. Activer le venv
source venv/bin/activate

# 3. Mettre à jour pip (optionnel mais conseillé)
pip install --upgrade pip

# 4. Installer les dépendances depuis requirements.txt
pip install -r requirements.txt

echo "Venv créé et dépendances installées !"
echo "Pour activer le venv plus tard : source venv/bin/activate"