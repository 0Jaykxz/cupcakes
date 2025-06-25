from flask import Blueprint, render_template, request
import csv

user_route = Blueprint('user', __name__)

@user_route.route('/')
def user_main():
    sabores = ["Brigadeiro", "Leite ninho"]
    return render_template('pedidos.html', sabores=sabores)

@user_route.route('/pedidos', methods=['POST'])
def user_pedidos():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    sabor = request.form.get('sabor')
    quantidade = request.form.get('quantidade')

    # Descobre o próximo número de pedido
    try:
        with open('pedidos.csv', newline='') as file:
            reader = csv.reader(file)
            pedidos = list(reader)
            ultimo_num = int(pedidos[-1][0]) if pedidos else 0
    except FileNotFoundError:
        ultimo_num = 0

    numero_pedido = ultimo_num + 1

    # Grava o pedido com número
    with open('pedidos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([numero_pedido, nome, telefone, sabor, quantidade])

    return render_template('thank.html', nome=nome, numero_pedido=numero_pedido)

@user_route.route('/cancelar', methods=['GET', 'POST'])
def cancelar():
    mensagem = ""
    if request.method == 'POST':
        numero = request.form['numero']
        nome = request.form['nome'].strip().lower()

        try:
            with open('pedidos.csv', newline='') as file:
                pedidos = list(csv.reader(file))

            novos_pedidos = []
            cancelado = False
            for pedido in pedidos:
                if pedido[0] == numero and pedido[1].strip().lower() == nome:
                    cancelado = True
                    continue
                novos_pedidos.append(pedido)

            if cancelado:
                with open('pedidos.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(novos_pedidos)
                mensagem = "Pedido cancelado com sucesso."
            else:
                mensagem = "Pedido não encontrado."

        except FileNotFoundError:
            mensagem = "Nenhum pedido foi registrado ainda."

    return render_template('cancelar.html', mensagem=mensagem)