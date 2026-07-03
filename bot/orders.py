from binance.exceptions import BinanceAPIException

from bot.client import get_client


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order.
    """
    client = get_client()

    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        print("DEBUG RESPONSE:", response)
        return response

    except BinanceAPIException as e:
        raise Exception(f"Binance API Error: {e.message}")

    except Exception as e:
        raise Exception(f"Error: {str(e)}")


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order.
    """
    client = get_client()

    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        
        return response

    except BinanceAPIException as e:
        raise Exception(f"Binance API Error: {e.message}")

    except Exception as e:
        raise Exception(f"Error: {str(e)}")