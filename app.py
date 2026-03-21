from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Mantém a compatibilidade de URLs com ou sem barra final
app.url_map.strict_slashes = False

# ROTA PARA SERVIR O MODELO 3D E OUTROS ASSETS DA PASTA STATIC
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# ROTA PRINCIPAL - RENDERIZA O INDEX.HTML
@app.route('/')
def index():
    # Variáveis enviadas para o template caso precise usar caminhos dinâmicos
    config = {
        "modelo_3d": "/static/pote_maionese.glb.glb"
    }
    
    # Renderiza o arquivo que você renomeou para index.html
    return render_template('index.html', data=config)

# INICIALIZAÇÃO DO SERVIDOR
if __name__ == '__main__':
    # Configurado para rodar na porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
