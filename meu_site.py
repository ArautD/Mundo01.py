from flask import Flask
#AuladoLIra
app = Flask(__name__)

# Criar a 1ª pagina do site
# Rout -> hashtagetreinamentos.com/
# Função -> o que vc quer exibir naquela pagina

@app.route("/")
def homepage():
    return "esse é meu primeiro site"

@app.route("/contatos")
def contatos():
    return "Contato (91) 983585025"

# Colocar o site no ar
if __name__== "__main__":
    app .run(debug = True)
