import redis
from faker import Faker
import time

red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
fake = Faker()
def stream():
        username = fake.name()
        hashtags = '#'+username
        red.publish('usernames', username)
        red.publish('hashtags', hashtags)
        print('Published ', username, ' and ', hashtags)
        print('sleeping for 2 second')
        time.sleep(2)

if __name__ == "__main__":
    while True:
        stream()