# ChatBot - Hamburgueria
Um chatbot para atendimento de uma hamburgueria utilizando *sklearn*

## Requisitos

  - Python 3
  - Token de um bot do Telegram

## Instalação

Clone esse repositório
```console
git clone git@github.com:HugoJF/chatbot-hamburgueria.git
```

Instale os requisitos utilizando `pip3`
```console
pip3 install -r requirements.txt
```

Inicie o bot
```console
TELEGRAM_TOKEN=token python3 bot.py
```

## Instalação pelo Dockerfile

Clone esse repositório
```console
git clone git@github.com:HugoJF/chatbot-hamburgueria.git
```

Entre no diretório
```console
cd chatbot-hamburgueria
```

Construa a imagem 
```console
docker build -t chatbot .
```

Inicie um container com a imagem passando o token como variável de ambiente
```console
docker run -e TELEGRAM_TOKEN=my_token --name mybot chatbot:latest
```
## Variáveis de ambiente
```console
TELEGRAM_TOKEN=token_do_bot_do_telegram
```

