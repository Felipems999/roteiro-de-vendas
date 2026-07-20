import os
import http.server as srv
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

class HTTPHandler(srv.BaseHTTPRequestHandler):
    def do_POST(self):
        if 'Content-Length' in self.headers:
            size = int(self.headers['Content-Length'])
            body_content = self.rfile.read(size).decode('utf-8')
        else:
            body_content = "{}"

        try:
            data = json.loads(body_content)

            api_key = os.getenv("GENAI_API_KEY")

            if api_key:
                client = genai.Client(api_key=api_key)

                ai_response = client.models.generate_content(
                            model="gemini-3-flash-preview",
                            contents=f"""
                            Escreva um roteiro de vendas com base nestes dados:
                            {data['nome_oferta']}, {data['resultado']} e {data['publico']}.
                            """,
                        )

                roteiro = ai_response.text if ai_response.text else "Houve um erro com a geração do roteiro!"

                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()


                response = {
                    "message": "Success",
                    "roteiro": roteiro,
                }

                self.wfile.write(json.dumps(response).encode("utf-8"))
            else:
                response = {
                    "message": "Error",
                    "roteiro": "Chave da API não configurada",
                }
        except Exception as e:
            print(e)

    def do_OPTIONS(self):
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()


def backend_service(port=8800):
    address = ("", port)
    server = srv.HTTPServer(address, HTTPHandler)

    server.serve_forever()

if __name__ == "__main__":
    backend_service()
