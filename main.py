import grpc

import fed_messages_pb2
import portfolio_manager_pb2
import portfolio_manager_pb2_grpc
import trader_pb2_grpc
from config import load_config
from fed_messages_pb2 import Exchange, OrderType, PortfolioName, Side
from portfolio_manager_pb2 import Fill
from trader_pb2 import Order, OrderResponse


def main():
    yaml_file_path = "./config.yaml"
    configs = load_config(yaml_file_path)

    # connect to grpc server
    trader_channel = grpc.insecure_channel("localhost:50053")
    trader_stub = trader_pb2_grpc.TraderStub(trader_channel)
    profolio_manager_channel = grpc.insecure_channel("localhost:50052")
    pm_stub = portfolio_manager_pb2_grpc.PortfolioManagerStub(trader_channel)
    pm_stub.StreamFills

    stream_req = portfolio_manager_pb2.StreamFillsRequest(PortfolioName.DBT_SP)
    fill: Fill
    for fill in pm_stub.StreamFills(stream_req):
        if not isinstance(fill, Fill):
            continue

        # fill = Fill(
        # exchange=Exchange.DBT, symbol="BTC-PERPETUAL", price=50000, amount=0.001
        # )

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
            order_type=OrderType.LIMIT,
        )

        resp: OrderResponse
        resp = trader_stub.SubmitOrder(order)
        print(resp)


if __name__ == "__main__":
    main()
