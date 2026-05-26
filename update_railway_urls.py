import json
import re

RAILWAY_DOMAIN = "https://bot-inspire-production-84c7.up.railway.app"
OLD_PATTERNS = [
    "http://localhost:5680",
    "http://localhost:5678",
    "http://localhost:3000",
    "https://localhost:5680",
    "https://localhost:5678",
    "http://127.0.0.1:5680",
    "http://127.0.0.1:5678",
    # ngrok antigo
    "https://tuneable-gertie-unflamboyantly.ngrok-free.dev",
    "https://bot-inspire-production.up.railway.app",
    "http://bot-inspire-production.up.railway.app",
]

FILES = [
    "agente-clinica-inspire-feegow-v3.json",
    "Agente Clinica Inspire — Feegow v3_SEM_CALENDARIO.json",
]

def update_file(filename):
    print(f"\n[Processando]: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    replacements = 0

    for old in OLD_PATTERNS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, RAILWAY_DOMAIN)
            print(f"  [OK] Substituido '{old}' -> {count}x")
            replacements += count

    if replacements == 0:
        print("  [WARN] Nenhuma URL encontrada para substituir.")
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [SAVE] Arquivo salvo com {replacements} substituicoes.")

    # Verificação: mostrar todas as URLs que ficaram
    remaining = re.findall(r'https?://[^\s\\\'"]+', content)
    unique_urls = sorted(set(remaining))
    print(f"\n  [INFO] URLs no arquivo apos atualizacao:")
    for url in unique_urls:
        if "feegow" in url or "railway" in url or "localhost" in url or "ngrok" in url:
            print(f"     {url}")

for fname in FILES:
    update_file(fname)

print("\n[OK] Concluido!")
