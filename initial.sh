#!/bin/sh
set -e

if [ ! -f /app/database/crm.db ]; then
    echo "Database başlatılıyor..."
    python database/init_db.py
else
    echo "Database zaten aktif."
fi

exec python run.py
