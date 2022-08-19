import redis
red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)

def user_counter():
    sub = red.pubsub()
    sub.subscribe('usernames')

    for message in sub.listen():
        if message is not None and isinstance(message, dict):
            username = message.get('data')
            print('Username ', username)

if __name__ == "__main__":
    while True:
        user_counter()