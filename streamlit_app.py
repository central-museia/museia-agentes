from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>MuseIA</title>

<style>
body {
    font-family: Arial, sans-serif;
    background: #ffffff;
    max-width: 700px;
    margin: auto;
    padding: 20px;
    color: #111;
}

h1 {
    font-size: 28px;
}

.subtitle {
    color: #555;
    margin-bottom: 20px;
}

.price {
    font-size: 26px;
    font-weight: bold;
    margin: 20px 0;
}

button {
    width: 100%;
    padding: 15px;
    font-size: 16px;
    background: black;
    color: white;
    border: none;
    border-radius: 6px;
    margin-top: 10px;
    cursor: pointer;
}

button:hover {
    opacity: 0.9;
}

.section {
    margin-top: 40px;
}

ul {
    padding-left: 20px;
}

hr {
    margin: 40px 0;
}
</style>

</head>
<body>

<h1>Novos Agentes de Automação disponíveis</h1>
<div class="subtitle">Implemente IA generativa no seu dia</div>

<hr>

<input type="text" placeholder="O que você está procurando?" style="width:100%; padding:10px;">

<hr>

<p>
Pare de perder tempo com tarefas repetitivas.  
Use automações simples e recupere horas do seu dia com a MuseIA.
</p>

<button>Comece agora gratuitamente</button>

<hr>

<h2>Kit Inicial MuseIA</h2>

<p>
Seu primeiro passo para automatizar seu dia sem precisar entender tecnologia.
</p>

<ul>
<li>Organize tarefas automaticamente</li>
<li>Responda mensagens com mais agilidade</li>
<li>Evite esquecimentos e retrabalho</li>
<li>Ganhe tempo no seu dia</li>
</ul>

<div class="price">R$ 69,90</div>

<button>Comprar agora</button>

<hr>

<p>
Pare de perder tempo com tarefas repetitivas.  
Use automações simples e recupere horas do seu dia com a MuseIA.
</p>

<button>Simplificar meu dia agora</button>

<hr>

<h3>Por que usar a MuseIA?</h3>

<ul>
<li>Assinatura mensal</li>
<li>Central de Agentes MuseIA</li>
<li>Aceleração de Vendas</li>
<li>Inteligência de Dados</li>
<li>Gestão de Pessoas & Feedback</li>
<li>Consistência de Marca</li>
</ul>

<hr>

<h3>Perguntas frequentes</h3>

<p><strong>1. O que é a MuseIA Digital?</strong><br>
Central de agentes de automação com instruções práticas.</p>

<p><strong>2. Quanto custa?</strong><br>
R$ 69,90. Assinatura futura: R$ 79,90/mês.</p>

<p><strong>3. Onde posso usar?</strong><br>
No seu dia a dia, vendas e organização.</p>

<p><strong>4. Posso cancelar?</strong><br>
Sim.</p>

<hr>

<p style="color:#777;">
Home • Central de Automação • Sobre a MuseIA
</p>

<p style="color:#777;">
Desenvolvido por MuseIA © 2026
</p>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
