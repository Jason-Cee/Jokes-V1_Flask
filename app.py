from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Random joke from chuck norris: </strong> </br> {}".format(response["value"])+ \
           "</br> <a href='https://vast-plateau-73090.herokuapp.com/categories'><button>Categories</button>"



@app.route('/categories/', methods=['GET'])
def get_chuck_norris_categories():
    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()

    return "<strong>Chuch Norris' Joke Categories: </strong> </br> {}".format(response) + \
           "</br> <a href='https://vast-plateau-73090.herokuapp.com//info/'><button>Info</button>" + \
           "<a href='https://vast-plateau-73090.herokuapp.com/'><button>Back</button>"


@app.route('/info/', methods=['GET'])
def get_chuck_norris_info():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Developer Stuff: </strong> </br> " + str(response) + \
           "</br> <a href='https://vast-plateau-73090.herokuapp.com//categories'><button>Back</button>"


if __name__ == "__main__":
    app.debug = True
    app.run()
