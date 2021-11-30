API URL used for getting exchange price from BTC to USD:
https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=demo

API URL used to fetch BTC price in USD market:
https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=demo

API_KEY to be used to make GET/POST reuqets on URL 'api/v1/quotes/' : TECH@QUYTECH

GET request: it will fetch the exchange rate from alpha vantage and give jSON response.

POST request: it will fetch the data from database and return JSON response.

Scheduled Task: After every hour, the api will fetch the BTC price in USD market and store it to the database, which can be accessed via POST reuqest made to the url as mentioned above. The first hour will start after one hour passed by the project running on server.
 
