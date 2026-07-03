import argparse

from bot.logging_config import logger
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (Required for LIMIT order)"
    )

    return parser.parse_args()


def validate_inputs(args):
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)

    price = None

    if order_type == "LIMIT":
        if args.price is None:
            raise ValueError("Price is required for LIMIT orders.")
        price = validate_price(args.price)

    return side, order_type, quantity, price


def print_order_summary(symbol, side, order_type, quantity, price):
    print("\n========== ORDER SUMMARY ==========")
    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")

    if price is not None:
        print(f"Price       : {price}")

    print("===================================")


def print_order_response(response):
    print("\n========== ORDER RESPONSE ==========")
    print(f"Order ID      : {response.get('orderId')}")
    print(f"Status        : {response.get('status')}")
    print(f"Executed Qty  : {response.get('executedQty')}")
    print(f"Average Price : {response.get('avgPrice', 'N/A')}")
    print("====================================")


def main():
    try:
        args = parse_arguments()

        side, order_type, quantity, price = validate_inputs(args)

        logger.info(
            f"Request -> Symbol={args.symbol}, Side={side}, "
            f"Type={order_type}, Quantity={quantity}, Price={price}"
        )

        print_order_summary(
            args.symbol,
            side,
            order_type,
            quantity,
            price,
        )

        if order_type == "MARKET":
            response = place_market_order(
                args.symbol,
                side,
                quantity,
            )
        else:
            response = place_limit_order(
                args.symbol,
                side,
                quantity,
                price,
            )

        logger.info(f"Response -> {response}")

        print_order_response(response)

        print("\n✅ Order placed successfully!")

    except Exception as e:
        logger.error(str(e))
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()