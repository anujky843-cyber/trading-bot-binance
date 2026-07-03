# Binance Futures Trading Bot

A Python-based Binance Futures Trading Bot that connects to the Binance Futures Testnet/API and allows users to place **MARKET** and **LIMIT** orders through a command-line interface.

---

# Features

* Connects to Binance Futures API
* Place MARKET orders
* Place LIMIT orders
* Input validation
* Error handling and logging
* Modular Python code structure

---

# Project Structure

```text
trading-bot-binance/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── cli.py
├── test_connection.py
├── test_order_debug.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Requirements

* Python 3.10 or newer
* Binance Account
* Binance API Key
* Binance API Secret

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Setup

Clone the repository:

```bash
git clone https://github.com/anujky843-cyber/trading-bot-binance.git
```

Move into the project directory:

```bash
cd trading-bot-binance
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

---

# Running the Project

Run the CLI:

```bash
python cli.py
```

Check Binance connection:

```bash
python test_connection.py
```

Debug order placement:

```bash
python test_order_debug.py
```

---

# Example Usage

### Example MARKET Order

```text
Order Type : MARKET
Symbol     : BTCUSDT
Side       : BUY
Quantity   : 0.001
```

Expected Result:

```text
Market Order Executed Successfully
```

---

### Example LIMIT Order

```text
Order Type : LIMIT
Symbol     : BTCUSDT
Side       : SELL
Quantity   : 0.001
Price      : 120000
```

Expected Result:

```text
Limit Order Submitted Successfully
```

---

# Assumptions

* The user has a valid Binance account.
* API keys are configured correctly.
* Internet connection is available.
* The trading pair exists on Binance Futures.
* Sufficient balance is available before placing live orders.

---

# Logging

The project records order activity and errors using Python logging.

The submission includes logs for:

* MARKET order
* LIMIT order

Example:

```text
logs/
├── market_order.log
└── limit_order.log
```

---

# Future Improvements

* Stop Loss Orders
* Take Profit Orders
* Web Dashboard
* Strategy Automation
* Docker Support
* Unit Tests
* CI/CD using GitHub Actions

---

# Author

**Anuj Kumar**

GitHub: https://github.com/anujky843-cyber
