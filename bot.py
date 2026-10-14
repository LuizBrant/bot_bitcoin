import json

import websocket

passagem = {
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}

if __name__ == "__main__":

    try:
        ws = websocket.WebSocket()
        ws.connect('wss://ws.bitstamp.net')
    
        
        ws.send(json.dumps(passagem))
        while True:
            resposta = json.loads(ws.recv())
            if resposta.get("event") == "trade":
                print(f"Preço do Bitcoin: ${resposta['data']['price']} , Quantidade comprada: {resposta['data']['amount_str']}")
            
    except: KeyboardInterrupt

    finally:
        print("Bot encerrado")
        ws.close