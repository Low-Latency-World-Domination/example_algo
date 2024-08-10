from config import load_config
from fed_messages_pb2 import Exchange, Side, OrderType
from portfolio_manager_pb2 import Fill
from trader_pb2 import Order
import trader_pb2_grpc
import portfolio_manager_pb2_grpc
import grpc


def main():
    yaml_file_path = './config.yaml'
    configs = load_config(yaml_file_path)


    # connect to grpc server
    trader_channel = grpc.insecure_channel('localhost:50051')
    trader_stub = trader_pb2_grpc.TraderStub(trader_channel)

    


    fill = Fill(exchange=Exchange.DBT, symbol='BTC-PERPETUAL', price=50000, amount=0.001)

    if Fill.side == Side.BUY:


        spread = configs[fill.symbol].spreadbps * 1000.0
        price = fill.price + 2.0 * spread  
        side = Side.SELL 

    else:
        spread = configs[fill.symbol].spreadbps * 1000.0
        price = fill.price - 2.0 * spread  
        side = Side.BUY 

    order = Order(
        exchange=fill.exchange,
        symbol=fill.symbol,
        side=side,
        price=price,
        amount=fill.amount,
        order_type=OrderType.LIMIT
        )


    resp = trader_stub.SubmitOrder(order)








if __name__ == "__main__":
    main()
