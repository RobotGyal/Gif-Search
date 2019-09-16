from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


#Function and Route to generate trending gifs
@app.route('/')
def index():
    """Return homepage."""
    # Extract the query term from url using request.args.get()
    query = request.args.get('query')

    params = {
        'q' : query,
        'key' : 'UZ3H7US8OGBS',
        'limit' : '10'
    }

    # Make an API call to Tenor using the 'requests' library.
    result = requests.get('https://api.tenor.com/v1/search', params=params)

    # Use the '.json()' function to get the JSON of the returned response object
    result_json = result.json()

    # Get the 'results' field of the JSON, which contains the GIFs as a list
    result_gif = result_json['results']
    

    #Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'
    if (len(result_gif) != 0):
        gifs = render_template('index.html', 
            query = query, 
            result_gif = result_gif)
    else:
        print("No gifs found")
    return gifs

#Function and Route to generate trending gifs
@app.route('/trending')
def trending():

    params = {
        'key' : 'UZ3H7US8OGBS',
        'limit' : '10'
    }

    #API call to Tenor
    result = requests.get('https://api.tenor.com/v1/trending', params=params)
    trending_gifs = json.loads(result.content)['results']

    if (len(trending_gifs) != 0):
        gifs = render_template('index.html', trending_gifs=trending_gifs)    
    else:
        print("No gifs found")
    return gifs

#Function and Route to generate random gifs
@app.route('/random')
def random():

    params = {
        'q':'random',
        'key' : 'UZ3H7US8OGBS',
        'limit' : '10'
    }

    #API call to Tenor
    result = requests.get('https://api.tenor.com/v1/random', params=params)
    random_gifs = json.loads(result.content)['results']
    
    if (len(random_gifs) != 0):
        gifs = render_template('index.html', random_gifs=random_gifs, params=params)
    else:
            print("No gifs found")
    return gifs

if __name__ == '__main__':
    app.run(debug=True)
