from bot.client import get_client

client = get_client()

order = client.futures_create_order(
    symbol="BTCUSDT",
    side="BUY",
    type="MARKET",
    quantity=0.001
)

print(order)