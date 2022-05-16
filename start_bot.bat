@echo off

call %~dp0SendBot\venv\Scripts\activate

cd %~dp0SendBot

set TOKEN=5391966554:AAEj7xmOwJEtjFWeYRf9u3xdSoyg_OFqY4o

python bot_telegram.py

pause
