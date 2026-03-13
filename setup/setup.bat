@echo off
REM 1. Créer le virtual environment
python -m venv venv

REM 2. Activer le venv
call venv\Scripts\activate

REM 3. Mettre à jour pip
python -m pip install --upgrade pip

REM 4. Installer les dépendances depuis requirements.txt
pip install -r requirements.txt

echo Venv créé et dépendances installées !
echo Pour activer le venv plus tard : call venv\Scripts\activate
pause