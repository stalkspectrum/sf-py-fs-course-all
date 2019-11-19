import os
import json

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request


RESOURCES_PATH = "users/"

def save_user(user_data):
    first_name = user_data["first_name"]
    last_name = user_data["last_name"]
    filename = "{}-{}.json".format(first_name, last_name)
    if not os.path.exists(RESOURCES_PATH):
        os.makedirs(RESOURCES_PATH)

    with open(filename, "w") as fd:
        json.dump(user_data, fd)
    return filename


@route("/user", method="POST")
def user():
    user_data = {
        "first_name": request.forms.get("first_name"),
        "last_name": request.forms.get("last_name"),
        "birthdate": request.forms.get("birthdate")
    }
    resource_path = save_user(user_data)
    print("User saved at: ", resource_path)

    return "Данные успешно сохранены"


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
