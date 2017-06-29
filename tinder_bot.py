import pynder
import random
import time
import urllib
import requests
import json

# To get toke: https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd

facebook_id = ""
facebook_auth_token = ""

initial_id = 1
images_path = "images/"

class JsonData(object):
    DATA_BASE = "tinder_bot_data.json"
    DATA_TEMPLATE = {
        "match_couter": 0,
        "matches": [],
        "last_id": 1
    }

    def __init__(self):
        try:
            initial_data = self.get_json()
        except Exception:
            self.save(self.DATA_TEMPLATE)
            initial_data = self.get_json()

        self.current_id = initial_data["last_id"]
        self.next_id = self.current_id + 1
        self.match_couter = initial_data["match_couter"]

    def match_ser(self, user):
        return {
            "id": self.next_id,
            "name": user.name,
            "bio": user.bio,
            "age": user.age,
            "ping_time": user.ping_time,
            "distance_km": user.distance_km,
            "tinder_id": user.id
        }

    def add_to_match_counter(self):
        self.match_couter += 1

        self.set("match_couter", self.match_couter)
        return self.match_couter

    def get(self, key):
        return self.get_json()[key]

    def set(self, key, data):
        json_data = self.get_json()
        json_data[key] = data
        self.save(json_data)

    def add_user(self, user):
        user_ser = self.match_ser(user)

        data = self.get_json()

        data["matches"].append(user_ser)

        self.save(data)
        self.current_id += 1
        self.next_id = self.current_id + 1

        self.set("last_id", self.current_id)

        return self.current_id

    def save(self, data):
        data_base = open(self.DATA_BASE, "+w")
        data_base.write(json.dumps(data, indent=4))
        data_base.close()

        return data

    def get_json(self):
        data_base = open(self.DATA_BASE, "r")
        _json = json.loads(data_base.read())
        data_base.close()

        return _json

def waitABit(minTime, maxTime):
    wait = random.uniform(minTime, maxTime)
    print("WAIT: %i - %i: %s \n" % (minTime, maxTime, str(wait)))
    time.sleep(wait)


if __name__ == '__main__':
    session = pynder.Session(facebook_id=facebook_id, facebook_token=facebook_auth_token)
    data_base = JsonData()

    while True:
        try:
            generator = session.nearby_users()
        except KeyError:
            continue

        for user in generator:
            pk = initial_id
            print("%s - %i " % (user.name, data_base.match_couter))

            x = 0
            for photo in user.get_photos(width="640"):
                file_name = "%i_%s_%i.jpg" % (data_base.next_id, user.name, x)
                file_path = "%s%s" % (images_path, file_name)

                f = open(file_path,'wb')
                f.write(requests.get(photo).content)
                f.close()

                x += 1

            user.like()
            data_base.add_user(user)
            data_base.add_to_match_counter()
            waitABit(0.25 * 5, 0.5 * 5)

        print("End of generator.")
        waitABit(0.25 * 15, 0.5 * 15)
)
        return self.match_couter

    def get(self, key):
        return self.get_json()[key]

    def set(self, key, data):
        json_data = self.get_json()
        json_data[key] = data
        self.save(json_data)

    def add_user(self, user):
        user_ser = self.match_ser(user)

        data = self.get_json()

        data["matches"].append(user_ser)

        self.save(data)
        self.current_id += 1
        self.next_id = self.current_id + 1

        self.set("last_id", self.current_id)

        return self.current_id

    def save(self, data):
        data_base = open(self.DATA_BASE, "+w")
        data_base.write(json.dumps(data, indent=4))
        data_base.close()

        return data

    def get_json(self):
        data_base = open(self.DATA_BASE, "r")
        _json = json.loads(data_base.read())
        data_base.close()

        return _json

def waitABit(minTime, maxTime):
    wait = random.uniform(minTime, maxTime)
    print("WAIT: %i - %i: %s \n" % (minTime, maxTime, str(wait)))
    time.sleep(wait)


if __name__ == '__main__':
    session = pynder.Session(facebook_id=facebook_id, facebook_token=facebook_auth_token)
    data_base = JsonData()

    while True:
        for user in session.nearby_users():
            pk = initial_id
            print("%s - %i " % (user.name, data_base.match_couter))

            x = 0
            for photo in user.get_photos(width="640"):
                file_name = "%i_%s_%i.jpg" % (data_base.next_id, user.name, x)
                file_path = "%s%s" % (images_path, file_name)

                f = open(file_path,'wb')
                f.write(requests.get(photo).content)
                f.close()

                x += 1

            user.like()
            data_base.add_user(user)
            data_base.add_to_match_counter()
            waitABit(0.25 * 5, 0.5 * 5)

        print("End of generator.")
        waitABit(0.25 * 15, 0.5 * 15)
