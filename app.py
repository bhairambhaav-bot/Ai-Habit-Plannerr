import http.server
import socketserver
import webbrowser
import os

PORT = 5000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 70)
        print("🧠 NEUROPLAN AI ULTIMATE (v5) — HYBRID OFFLINE STUDY OS 🧠")
        print(f"🚀 Live at: {url}")
        print("✅ Online Syllabus Ingestion -> 100% Offline Execution (PWA Ready)")
        print("=" * 70)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        httpd.serve_forever()
