import config as c


# Verifica palavra por palavra por tags (como números, produtos, pagamentos, envios)
def get_tags(message):
    tags = {
        'nums':     [],
        'products': [],
        'payment':  '',
        'shipping': '',
    }

    for word in message.split(' '):
        # Produtos
        for cod, prod in c.products.items():
            if word in prod['tags']:
                tags['products'].append(cod)

        # Números
        for num, numtags in c.number_tags.items():
            if word in numtags:
                tags['nums'].append(num)

        # Pagamentos
        for pay, paytags in c.payment_tags.items():
            if word in paytags:
                tags['payment'] = pay

        # Envios
        for ship, shiptags in c.shipping_tags.items():
            if word in shiptags:
                tags['shipping'] = ship

    return tags
