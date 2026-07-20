import http.server as srv
import json

class HTTPHandler(srv.BaseHTTPRequestHandler):
    def do_POST(self):
        if 'Content-Length' in self.headers:
            size = int(self.headers['Content-Length'])
            body_content = self.rfile.read(size).decode('utf-8')
        else:
            body_content = "{}"

        data = json.loads(body_content)

        roterio = f"""Você, {data['publico']}, perde noites pensando na sua segurança financeira?\n
        Nós temos uma solução! Foi disponibilizado para você o {data['nome_oferta']}!\n Graças à ela,
        você {data['resultado']}"""

        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


        response = {
            "message": "Success",
            "roteiro": roterio,
        }

        self.wfile.write(json.dumps(response).encode("utf-8"))

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
