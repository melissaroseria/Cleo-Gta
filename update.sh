#!/bin/bash
# update.sh - Termux için otomatik güncelleme ve çalıştırma scripti

# Renkli çıktı için
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[+] Repo güncelleniyor...${NC}"

# Eğer repo yoksa klonla, varsa güncelle
if [ ! -d "Cleo-Gta" ]; then
    git clone https://github.com/melissaroseria/Cleo-Gta.git
else
    cd Cleo-Gta
    git pull
    cd ..
fi

echo -e "${GREEN}[+] main.py çalıştırılıyor...${NC}"

# Python ile main.py çalıştır
cd Cleo-Gta
python3 main.py
