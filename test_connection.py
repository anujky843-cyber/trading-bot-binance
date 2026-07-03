from bot.client import get_client

try:
    client = get_client()

    account = client.futures_account()

    print("✅ Connected Successfully!")
    print(account)

except Exception as e:
    print("❌ Connection Failed")
    print(e)