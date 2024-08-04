from config import load_config
from fed_messages_pb2 import Exchange, Side
from portfolio_manager_pb2 import Fill
from trader_pb2 import Order


def main():
    yaml_file_path = './config.yaml'
    configs = load_config(yaml_file_path)


    


    fill = Fill(exchange=Exchange.DBT, symbol='BTC-PERPETUAL', price=50000, amount=0.001)

    if Fill.side == Side.BUY:


        spread = configs[fill.symbol].spreadbps * 1000.0
        price = fill.price + 2.0 * spread  
        side = Side.SELL 

        order = Order()

    else:
        spread = configs[fill.symbol].spreadbps * 1000.0
        price = fill.price - 2.0 * spread  
        side = Side.BUY 

        order = Order()








if __name__ == "__main__":
    main()
