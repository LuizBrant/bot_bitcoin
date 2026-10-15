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
def comprar_e_vender():

    pass

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