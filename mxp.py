import http.server
import socketserver
import random

def run_code(num):
    # Jogo ímpar ou par
    r = random.randint(1, 99)
    f = r % 2

    # Checa se o usuário ganhou ou perdeu
    if (f == 0 and num == "impar") or (f == 1 and num == "par"):
        resultado = "Voce perdeu"
    else:
        resultado = "Voce ganhou"

    # Retorna o resultado formatado como uma string
    return ('<h2>Jogo impar ou Par</h2>'
            '<p>Numero escolhido pelo computador: {}.</p>'
            '<p>Resultado: {}</p>').format(r, resultado)

# Criando o servidor
PORT = 2020 # Porta que o servidor irá escutar

# Função para lidar com as solicitações
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Configura a resposta do servidor
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Formulário HTML
        html = '''
        <html>
        <body>
            <h1>Jogo Impar ou Par</h1>
            <form method="post">
                <label for="num">Escolha impar ou par:</label>
                <select id="num" name="num">
                  <option value="impar">Impar</option>
                  <option value="par">Par</option>
                </select>
                <input type="submit" value="Jogar">
            </form>
        </body>
        </html>
        '''
        self.wfile.write(html.encode())

    def do_POST(self):
        # Recebe os dados do formulário
        content_length = int(self.headers['Content-Length'])
        raw_post_data = self.rfile.read(content_length).decode()
        num = raw_post_data.split('=')[1]

        # Roda o jogo ímpar ou par
        response = run_code(num)

        # Configura a resposta do servidor com o resultado do jogo
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Envia a resposta do servidor com o resultado do jogo
        self.wfile.write(response.encode())

# Cria o servidor na porta especificada com o manipulador de solicitações personalizado
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Servidor rodando na porta", PORT)
    httpd.serve_forever()
