# Binance Futures Trading Bot

A Python-based Binance Futures Trading Bot that securely connects to the Binance Futures API, validates user input, and places market orders through a simple command-line interface.

## 🚀 Features

* 🔐 Secure Binance Futures API integration
* 📈 Place Buy and Sell Market Orders
* ✅ Input validation for trading parameters
* 📝 Centralized logging for debugging
* ⚡ Simple and easy-to-use CLI
* 🧩 Modular project structure for easy maintenance

## 📂 Project Structure

```text
trading_bot/
│── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
│── cli.py
│── requirements.txt
│── test_connection.py
│── test_order_debug.py
│── README.md
│── .gitignore
```

## 🛠️ Technologies Used

* Python 3.x
* Binance Futures API
* python-binance
* Logging
* Virtual Environment (venv)

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/anujky843-cyber/trading-bot-binance.git
```

Move into the project directory:

```bash
cd trading-bot-binance
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file in the project root and add your Binance API credentials:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

**Never commit your API keys to GitHub.**

## ▶️ Running the Project

Run the command-line interface:

```bash
python cli.py
```

Test the Binance API connection:

```bash
python test_connection.py
```

## 📌 Future Improvements

* Web Dashboard
* Streamlit Interface
* FastAPI REST API
* Telegram Bot Integration
* Trading Strategies
* Risk Management
* Docker Support
* GitHub Actions CI/CD

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Anuj Kumar**

* GitHub: https://github.com/anujky843-cyber
* Email: [anujky843@gmail.com](mailto:anujky843@gmail.com)
