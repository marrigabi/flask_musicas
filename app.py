from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # importante para sessões

# Lista fictícia de usuários
usuarios = {
    "joao": "123",
    "maria": "456"
}

# Banco de músicas em memória
musicas = {
    "joao": [],
    "maria": []
}

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            flash("Usuário ou senha inválidos.")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', usuario=session['usuario'], musicas=musicas[session['usuario']])

@app.route('/musicas', methods=['GET', 'POST'])
def gerenciar_musicas():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    user = session['usuario']
    
    if request.method == 'POST':
        acao = request.form['acao']
        nome = request.form['nome']
        
        if acao == 'adicionar':
            musicas[user].append(nome)
        elif acao == 'remover' and nome in musicas[user]:
            musicas[user].remove(nome)
        elif acao == 'editar':
            antiga = request.form['antiga']
            if antiga in musicas[user]:
                musicas[user][musicas[user].index(antiga)] = nome
    
    return render_template('musicas.html', musicas=musicas[user])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
