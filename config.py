# Tags e definições de produtos
products = {
    'x-bacon':            {
        'nome':      'X-Bacon',
        'tipo':      'hamburguer',
        'preco':     1400,
        'descricao': 'Hamburguer de 180g com 5 fatias de bacon e maionese da casa',
        'tags':      ['xbacon', 'xbacons', 'x-bacon', 'x-bacons'],
    },
    'x-burguer':          {
        'nome':      'X-Burguer',
        'tipo':      'hamburguer',
        'preco':     1100,
        'descricao': 'Hamburguer de 180g com queijo e maionese da casa',
        'tags':      ['xburguer', 'burguer', 'xburguers', 'burguers']
    },
    'x-tudo':             {
        'nome':      'X-Tudo',
        'tipo':      'hamburguer',
        'preco':     1800,
        'descricao': 'Hamburguer de 220g com 5 fatias de bacon, ovo, alface, tomate, salsicha e maionese da casa',
        'tags':      ['xtudo', 'xtudos'],
    },
    'x-podrao':           {
        'nome':      'X-Podrão',
        'tipo':      'hamburguer',
        'preco':     2400,
        'descricao': 'Dois hamburgueres de 220g com 10 fatias de bacon, maionese da casa, alface, tomate e cebola.',
        'tags':      ['xpodrao', 'xpodroes', 'x-podrao', 'x-podroes'],
    },
    'refri-lata-coca':    {
        'nome':      'Coca-Cola Lata',
        'tipo':      'bebida',
        'preco':     400,
        'descricao': 'Lata de 350ml',
        'tags':      ['coca', 'cocas', 'coca-cola', 'guarana', 'fanta'],
    },
    'refri-lata-guarana': {
        'nome':      'Guaraná Lata',
        'tipo':      'bebida',
        'preco':     350,
        'descricao': 'Lata de 350ml',
        'tags':      ['guarana', 'guaranas'],
    },
    'suco':               {
        'nome':  'Garrafa de Suco',
        'tipo':  'bebida',
        'preco': 600,
        'tags':  ['suco', 'polpa'],
    },
    'agua':               {
        'nome':  'Garrafa de Água',
        'tipo':  'bebida',
        'preco': 900,
        'tags':  ['agua', 'aguas'],
    },
    'cha':                {
        'nome':  'Latinha de Chá Gelado',
        'tipo':  'bebida',
        'preco': 450,
        'tags':  ['cha', 'chas']
    },
}

# Tags para números
number_tags = {
    1: ['1', 'um', 'uns', 'uma', 'umas'],
    2: ['2', 'dois', 'duas'],
    3: ['3', 'tres'],
    4: ['4', 'quatro'],
    5: ['5', 'cinco'],
    6: ['6', 'seis'],
}

# Tags para pagamento
payment_tags = {
    'credit': ['credito'],
    'debit':  ['debito'],
    'cash':   ['dinheiro', 'troco'],
}

# Tags para envio
shipping_tags = {
    'self':   ['retirada', 'retirar', 'pegar'],
    'direct': ['entrega', 'entregue', 'envio', 'entregar'],
}

# Minutos de preparos para cada item
min_per_item = 5

# X TODO: persistencia
# X TODO: fazer o bot perguntar mais coisas
# X TODO: melhorar as mensagens
# X TODO: finalizacao do pedido (mostrar resumo)
# X TODO: logging
# X TODO: /reset
# TODO: Dockerfile
# TODO: testar
# TODO: backend
