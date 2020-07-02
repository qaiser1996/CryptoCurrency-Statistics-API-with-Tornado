# Crypto Currency Statistics API with Tornado

## Tornado
Tornado is a Python web framework and asynchronous networking library,
that uses non-blocking network I/O which allows it to scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

## BeautifulSoup
The API uses BS4 to scrape currency data from the website https://walletinvestor.com/forecast/

## API Usage
 - `/getCurrencyData/[crypto-currency name]` retreives predictions of next 7 days and historical data of 14 days of the given crypto currency
 - `/about/` gets about info