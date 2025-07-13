# AlphaTrend Telegram Bot

A Telegram bot that receives TradingView webhook alerts and sends buy/sell signals **only for cryptocurrencies** to subscribed users.

## Features
- ✅ Multi-user support
- ✅ Webhook listener for TradingView
- ✅ Filters signals by trusted crypto exchanges
- ✅ Sends alerts to Telegram
- ✅ Uses `.env` for token security

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env`
```env
BOT_TOKEN=your_telegram_bot_token_here
```

### 3. Run the Bot Locally
```bash
python bot.py
```

### 4. Set Telegram Webhook
```bash
https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=<YOUR_DOMAIN>/<YOUR_TOKEN>
```

### 5. TradingView Alert Example
Send alerts with JSON body like:
```json
{
  "ticker": "BINANCE:BTCUSDT",
  "action": "BUY",
  "price": "62000"
}
```

## Notes
- Only tickers from approved crypto exchanges are accepted:
  `BINANCE`, `COINBASE`, `BYBIT`, `KRAKEN`, `BITSTAMP`, `CRYPTO`, `CRYPTOCAP`, `OKX`

## License
MIT
