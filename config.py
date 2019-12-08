# Tags e definições de produtos
products = {
    'x-bacon':     {
        'nome':      'X-Bacon',
        'tipo':      'hamburguer',
        'preco':     1400,
        'descricao': 'Hamburguer de 180g com 5 fatias de bacon e maionese da casa',
        'tags':      ['xbacon', 'xbacons'],
    },
    'x-burguer':   {
        'nome':      'X-Burguer',
        'tipo':      'hamburguer',
        'preco':     1100,
        'descricao': 'Hamburguer de 180g com queijo e maionese da casa',
        'tags':      ['xburguer', 'burguer']
    },
    'x-tudo':      {
        'nome':      'X-Tudo',
        'tipo':      'hamburguer',
        'preco':     1800,
        'descricao': 'Hamburguer de 220g com 5 fatias de bacon, ovo, alface, tomate, salsicha e maionese da casa',
        'tags':      ['xtudo'],
    },
    'refri-lata':  {
        'nome':      'Refrigerante Lata',
        'tipo':      'bebida',
        'preco':     400,
        'descricao': 'Lata de 350ml',
        'tags':      ['coca', 'cocas', 'coca-cola', 'guarana', 'fanta'],
    },
    'suco':        {
        'nome':  'Garrafa de Suco',
        'tipo':  'bebida',
        'preco': 600,
        'tags':  ['suco', 'polpa', 'laranja'],
    },
    'refri-litro': {
        'nome':  'Refrigerante Litro',
        'tipo':  'bebida',
        'preco': 900,
        'tags':  [],
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
