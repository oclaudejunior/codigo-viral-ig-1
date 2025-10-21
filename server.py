#!/usr/bin/env python3
"""
Servidor HTTP Simples para o Código Viral IG
Execute este arquivo para visualizar a landing page localmente
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Configurações
PORT = 8000
DIRECTORY = Path(__file__).parent

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def end_headers(self):
        # Adiciona headers para evitar problemas de CORS
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print("🚀 CÓDIGO VIRAL IG - Servidor Local")
        print("=" * 60)
        print(f"\n✅ Servidor rodando em: {url}")
        print(f"\n📂 Diretório: {DIRECTORY}")
        print("\n🌐 Abrindo navegador automaticamente...")
        print("\n⚠️  Para parar o servidor: pressione CTRL+C")
        print("=" * 60)

        # Abre o navegador automaticamente
        webbrowser.open(url)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor encerrado pelo usuário")
            print("=" * 60)

if __name__ == "__main__":
    main()
