from flask import Blueprint, render_template, request
import csv

admin_route = Blueprint('admin', __name__)

@admin_route.route('/login')
def login():
    return render_template('login.html')

@admin_route.route('/admin', methods=['GET', 'POST'])
def admin():
    pedidos = []
    mensagem = ""

    try:
        with open('pedidos.csv', newline='') as file:
            reader = csv.reader(file)
            pedidos = list(reader)
    except FileNotFoundError:
        pass

    # Verifica se veio uma requisição para deletar
    if request.method == 'POST':
        numero_a_cancelar = request.form['numero']
        novos_pedidos = [p for p in pedidos if p[0] != numero_a_cancelar]
        if len(novos_pedidos) < len(pedidos):
            with open('pedidos.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(novos_pedidos)
            mensagem = f"Pedido #{numero_a_cancelar} cancelado com sucesso."
            pedidos = novos_pedidos
        else:
            mensagem = f"Pedido #{numero_a_cancelar} não encontrado."

    return render_template('admin.html', pedidos=pedidos, mensagem=mensagem)