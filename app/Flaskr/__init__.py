from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon/<name>')
def pokemon(name):
    try:
        poke_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
        poke_types = [t['type']['name'] for t in poke_data['types']]
        poke_abilities = [a['ability']['name'] for a in poke_data['abilities']]
        poke_stats = {s['stat']['name']: s['base_stat'] for s in poke_data['stats']}
        return render_template('pokemon.html', poke_data=poke_data, poke_types=poke_types, poke_abilities=poke_abilities, poke_stats=poke_stats)
    except:
        return render_template('error.html')

@app.route('/pokemons')
def pokemons():
    poke_list = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151').json()['results']
    return render_template('pokemons.html', poke_list=poke_list)

if __name__ == '__main__':
    app.run(debug=True)