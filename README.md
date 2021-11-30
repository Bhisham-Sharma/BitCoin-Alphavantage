# BitCoin-Alphavantage
Fetching API data using celery worker. Project setup on docker.

# Technologies Used
- Django
- Celery
- Redis for Celery Broker
- Postgres
- Docker
- Docker Compose
- Rest Framework

# API Debugging Tools
- POSTMAN

# Authentication
- API key is set to authenticate the GET and POST requests made to our REST API.

# Third Party API used To Fetch Data:
- AlphaVantage API

# What this API does
This API have a url api/v1/quotes/ on which both GET and POST request will be made. The GET request will return the JSON response of the current exchnage price of BTC in USD market. The POST request will fetch the daily historical price stored by the celery-workers in backend and return JSON response. Celery-workers are scheduled to fetch data at every 1 hour from AlphaVantage.
