# response-time-py-redis

### NOTE: Use Python3

install dependencies:

```python
pip3 install -r requirements
```

# PeriodicService
Periodic service contains the component that handles the periodic service.


change the values in config.json to change the configuration.

```
{
    "end_point": "https://postman-echo.com/get",
    "interval": 30, // runs every 30secs
    "list_size": 50, // only 50 elements are stored in redis at a time
    "concurrency": 1000, // reduce the concurrency & interval for quick testing
    "redis_host": "localhost",
    "redis_port": 6379
}
```

Start the service:

```
python3 start.py // run in PeriodicService cause this looks for config.json in current directory
```

# Run the REST API Server

It is in REST API directory.

python3 app.py
