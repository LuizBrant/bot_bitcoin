import json

import websocket
import bitstamp.client

CARTEIRA_USD = []
CARTEIRA_BTC = []

passagem = {
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}

def cliente():
    return bitstamp.client.Trading(username='999999', key='xxx', secret='xxx')


def comprar(quantidade):
    trading_client = cliente()
    trading_client.buy_market_order(quantidade)

def vender(quantidade):
    trading_client = cliente()
    trading_client.sell_market_order(quantidade)

def pesca(resposta):
    quantidade= float(resposta['data']['amount_str'])
    if quantidade >1 and quantidade < 2:
        print('Peixe grande')
    elif quantidade >=2 and quantidade <= 6:
        print('Tubarão')
    elif quantidade >6:
        print('baleia')
    elif quantidade >0.01:
        print('Peixe pequeno')
    else:
        pass


if __name__ == "__main__":

    try:
        ws = websocket.WebSocket()
        ws.connect('wss://ws.bitstamp.net')
    
        
        ws.send(json.dumps(passagem))
        while True:
            resposta = json.loads(ws.recv())
            if resposta.get("event") == "trade":
                print(f"Preço do Bitcoin: ${resposta['data']['price']} , Quantidade comprada: {resposta['data']['amount_str']}")
                pesca(resposta)
    except: KeyboardInterrupt

    finally:
        print("Bot encerrado")
        ws.close