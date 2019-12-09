# coding=utf-8
from functools import reduce
from matplotlib import pylab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, precision_score, accuracy_score, confusion_matrix
from sklearn.model_selection import LeaveOneOut
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
import telegram
import logging
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import config
import helpers as h

# Inicializa vetorizador
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, strip_accents='unicode')

# Carrega dataset
csv = pd.read_csv('./dataset.csv')

# Separa textos e intenções do dataset
x = vectorizer.fit_transform(csv['text'].values)
y = csv['intention'].values

# Inicializa classificadores a serem utilizados
classifiers = {
    'knn':        KNeighborsClassifier(n_neighbors=3),
    'svm':        SVC(gamma=2, C=1),
    'tree':       DecisionTreeClassifier(max_depth=5),
    'regression': LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial'),
}
'''
# Aumenta o tamanho das imagens (matrizes de confusão)
pylab.rcParams['figure.figsize'] = (16, 10)

# Itera classificadores
for name, classifier in classifiers.items():
    # Inicializa vetores dos resultados dos testes
    # Cada teste do LeaveOneOut será armazenado para poder gerar métricas em seguida
    trues = []
    preds = []

    # Iniciaza o LeaveOneOut
    loo = LeaveOneOut()

    # Realiza a divisão dos dados
    for train, test in loo.split(csv.values):
        # Separa parte de treino e parte de teste
        train = csv.iloc[train]
        test = csv.iloc[test]

        # Separa texto e intenção do treino
        x = vectorizer.fit_transform(train['text'])
        y = train['intention']

        # Separa texto e intenção do teste
        a = test['text']
        b = test['intention']

        # Realiza o treino do classificador
        classifier.fit(x, y)

        # Vetoriza o teste
        test = vectorizer.transform(a)

        # Prediz o teste com o classificador
        pred = classifier.predict(test)

        # Separa o valor real
        true = b.values

        # Adiciona na lista de predições
        # TODO: mudar para tuplas
        trues.append(true[0])
        preds.append(pred[0])

    print('#################################################')
    print('Estatísticas para %s' % name)
    print('Recall=', recall_score(trues, preds, average='weighted'))
    print('Precision=', precision_score(trues, preds, average='weighted'))
    print('Accuracy=', accuracy_score(trues, preds))

    # Lista de todos as classes sem repetição
    labels = list(set(trues))

    # Gera matriz de confusão
    matrix = confusion_matrix(trues, preds, labels=labels)

    # Inicia plot para matriz de confusão
    ax = plt.subplot()
    sns.heatmap(matrix, annot=True, ax=ax)  # annot=True to annotate cells

    # labels, title and ticks
    ax.set_title('Confusion Matrix')

    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')

    ax.xaxis.set_ticklabels(labels)
    ax.yaxis.set_ticklabels(labels)

    # Printa matriz em texto
    print(matrix)

    # Mostra matriz imagem
    # plt.show()
'''


# Treina modelo da regressão e classifica uma mensagem
def predict_action(message):
    model = classifiers['regression']
    x = vectorizer.fit_transform(csv['text'])
    y = csv['intention']

    model.fit(x, y)

    test = vectorizer.transform([message])

    pred = model.predict(test)

    return pred[0]


# Lógica para intenção de `cardapio`
def cardapio(message, user_data):
    response = '*Nosso cardápio de hamburgueres:* \n\n'

    # Lista todos os produtos do tipo hamburguer
    for cod, info in config.products.items():
        if info['tipo'] == 'hamburguer':
            response += "🍔 *%s:* `R$ %.2f`\n" % (info['nome'], info['preco'] / 100)

    return response


# Lógica para intenção `bebidas`
def bebidas(message, user_data):
    response = '*Nosso cardário de bebidas:* \n\n'

    # Lista todos os produtos do tipo bebida
    for cod, info in config.products.items():
        if info['tipo'] == 'bebida':
            response += "🥤 *%s:* `R$ %.2f`\n" % (info['nome'], info['preco'] / 100)

    return response


# Lógica para intenção `conta`
def conta(message, user_data):
    response = ''
    order = user_data['order']

    # Calcula custo total da conta
    valor_conta = reduce(lambda cur, x: cur + x[1] * config.products[x[0]]['preco'], order.items(), 0)

    response += "*Valor total da conta:* `R$ %.2f`\n\n" % (valor_conta / 100)

    # Lista todos os produtos adicionados na conta do usuário
    for cod, quant in order.items():
        product = config.products[cod]
        response += "*%d* `%s`\n" % (quant, product['nome'])
    response += "\nComo será o meio de pagamento?"

    return response


# Lógica para intenção `tempo`
def tempo(message, user_data):
    order = user_data['order']
    # Soma quantidade de itens
    items = reduce(lambda cur, x: cur + x, list(order.values()), 0)
    return "Tempo estimado para entrega: %dmin" % (items * config.min_per_item + 20)


# Resposta para quando não existe resposta para a intenção classificada
def nao_entendi(message, user_data):
    return "Nao entendi o que você disse, pode tentar de outra forma?"


# Lógica para intenção `pagamento`
def pagamento(message, user_data):
    response = ''

    # Processa tags da mensagem (e cria "atalho" para tags de pagamento)
    tags = h.get_tags(message)
    pay = tags['payment']

    # Seta tipo de pagamento do pedido
    user_data['payment_method'] = pay

    # Monta resposta dependente do tipo de pagamento
    if pay == 'credit':
        response += 'Enviaremos uma máquina para pagamento com cartão de crédito.'
    elif pay == 'debit':
        response += 'Enviaremos uma máquina para pagamento com cartão de débito.'
    elif pay == 'cash':
        response += 'Seu pedido foi registrado para pagamento em dinheiro.'
    else:
        # Reseta tipo de pagamento
        user_data['payment_method'] = None
        return 'Como voce deseja pagar seu pedido?'

    response += '\n\nDeseja que seu pedido seja entregue ou para retirada?'
    return response


# Lógica para intenção `entrega`
def entrega(message, user_data):
    # Processa tags
    tags = h.get_tags(message)
    shipping = tags['shipping']

    # Seta tipo de entrega
    user_data['shipping_method'] = shipping

    if shipping == 'self':
        return "Pedido para retirada!"
    elif shipping == 'direct':
        return 'Pedido para entrega!'
    else:
        user_data['shipping_method'] = None
        return "Deseja que seu pedido seja retirado ou entregue?"


def informacao(message, user_data):
    response = ''
    tags = h.get_tags(message)

    prods = tags['products']

    for prod in prods:
        p = config.products[prod]
        nome = p['nome']
        desc = p['descricao']
        response += 'Informacoes sobre o %s: \n\n*%s*\n' % (nome, desc)

    return response


def pedido(message, user_data):
    order = user_data['order']
    response = ''
    tags = h.get_tags(message)

    if len(tags['nums']) != len(tags['products']):
        return 'Por favor mencione a quantidade e o produto em seguida!'

    for i in range(len(tags['nums'])):
        quant = tags['nums'][i]
        cod = tags['products'][i]
        nome = config.products[cod]['nome']

        if cod not in order:
            order[cod] = 0

        order[cod] += quant

        response += "*%d* `%s` %s ao seu pedido!\n" % (quant, nome, ('adicionado', 'adicionados')[quant > 1])
    response += '\n✅ Deseja mais algo?'
    return response


def done(user_data):
    return user_data['order'] and user_data['shipping_method'] and user_data['payment_method']


def finish(user_data):
    response = ''
    order = user_data['order']

    response += '*Resumo do seu pedido*\n'

    for cod, quant in order.items():
        p = config.products[cod]
        response += "*%d* `%s`\n" % (quant, p['nome'])

    pay = user_data['payment_method']
    valor_conta = reduce(lambda cur, x: cur + x[1] * config.products[x[0]]['preco'], order.items(), 0)
    if pay == 'credit':
        payment_method = 'Cartão de Crédito'
    elif pay == 'debit':
        payment_method = 'Cartão de Débito'
    else:
        payment_method = 'Dinheiro'
    shipping_method = ('Retirada', 'Entrega')[user_data['shipping_method'] == 'direct']

    response += '\n*O valor total:* `R$ %.2f`' % (valor_conta / 100)
    response += '\n*Meio de pagamento:* %s' % payment_method
    response += '\n*Pedido para:* %s\n' % shipping_method
    response += '\n*Seu pedido foi registrado!*'

    user_data['order'] = {}
    user_data['payment_method'] = None
    user_data['shipping_method'] = None

    return response


print('Polling Telegram')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def text_message(update, context):
    message = update.message.text
    print('Received message: %s' % message)
    intention = predict_action(message)

    actions = {
        'cardapio':   cardapio,
        'conta':      conta,
        'entrega':    entrega,
        'tempo':      tempo,
        'bebidas':    bebidas,
        'informacao': informacao,
        'pagamento':  pagamento,
        'pedido':     pedido,
    }

    if intention in actions:
        call = actions[intention]
    else:
        call = nao_entendi

    print('Itention: %s' % intention)
    print(h.get_tags(message))

    user_data = context.user_data

    if 'order' not in user_data:
        user_data['order'] = {}
    if 'payment_method' not in user_data:
        user_data['payment_method'] = ''
    if 'shipping_method' not in user_data:
        user_data['shipping_method'] = ''

    print('Calling intention')
    response = call(message, user_data)
    print('Response: %s' % response)
    update.message.reply_text(response, parse_mode=telegram.ParseMode.MARKDOWN)

    if done(user_data):
        response = finish(user_data)
        update.message.reply_text(response, parse_mode=telegram.ParseMode.MARKDOWN)


def bot_help(update, context):
    update.message.reply_text("Para começar um pedido, basta me informar quais itens do cardápio você tem interesse!\n"
                              "Exemplos:\n"
                              "- *Por favor me mande o cardárpio*\n"
                              "- *Eu quero um X-Bacon e 2 cocas*\n"
                              "- *O que tem de bebida?*", parse_mode=telegram.ParseMode.MARKDOWN)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"' % (update, context.error))


updater = Updater(os.environ['TELEGRAM_TOKEN'], use_context=True)

updater.dispatcher.add_handler(CommandHandler('ajuda', bot_help))
updater.dispatcher.add_handler(CommandHandler('start', bot_help))
updater.dispatcher.add_handler(CommandHandler('iniciar', bot_help))
updater.dispatcher.add_handler(MessageHandler(Filters.update.message, text_message))
updater.dispatcher.add_error_handler(error)

updater.start_polling()
updater.idle()
