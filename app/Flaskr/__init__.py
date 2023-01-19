from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
    poke_name = request.form['poke_name']
    try:
        poke_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_name}').json()
        poke_types = [t['type']['name'] for t in poke_data['types']]
        return render_template('pokemon.html', name=poke_data['name'], types=poke_types)
    except:
        return render_template('error.html')

@app.route('/pokemon_list')
def pokemon_list():
    poke_list = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151').json()['results']
    return render_template('pokemon_list.html', poke_list=poke_list)

if __name__ == '__main__':
    app.run(debug=True)



