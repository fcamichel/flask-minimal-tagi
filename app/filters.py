from datetime import datetime
from app import app


def format_datetime(value):
    date = datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %z')
    return date.strftime("%H:%M - %d.%m")

def split_url(value):
    return value.split('/')[-1]

app.jinja_env.filters['datetime'] = format_datetime
app.jinja_env.filters['split'] = split_url
