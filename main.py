# Now, if you are aware of the FastAPI architecture, 
# we will require a data class for the inputs. 
# This data class allows FastAPI to validate the inputs to be sent to the model and if any wrong input is given,
# it simply raises the error without giving it to the model.

# Creating a data class is pretty straightforward and requires only the parameters to be accepted along with the data type. To further customize, you can also add a custom example to quickly test out the results. The code for this class is:

# Now, we need to create an endpoint where all the requests will be served. The endpoint creation in FastAPI is very similar to the flask and only requires the endpoint function to take in the data class for validation.

from fastapi import FastAPI
import pickle

from pydantic import BaseModel



app = FastAPI()

### load the model
@app.on_event("startup")
def load_model():
    global model
    model = pickle.load(open("model_tree.pkl", "rb"))

@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}

# define the model input, schema, data type etc.
class Music(BaseModel):
    acousticness: float 
    danceability: float 
    energy: float 
    instrumentalness: float 
    liveness: float 
    speechiness: float 
    tempo: float 
    valence: float
    class Config:
        schema_extra = {
            "example": {
                "acousticness": 0.838816, 
                "danceability": 0.542950, 
                "energy": 0.669215,
                "instrumentalness": 0.000006,
                "liveness": 0.105610,
                "speechiness": 0.391221,
                "tempo": 111.894,
                "valence": 0.796073
            }
        }


## http post operation, the ML part
@app.get('/predict')  # can use either get or post

# this original function uses hard-coded model input
#def get_music_category(data: Music):
    #received = data.dict()
    #acousticness = received['acousticness']
    #danceability = received['danceability']
    #energy = received['energy']
    #instrumentalness = received['instrumentalness']
    #liveness = received['liveness']
    #speechiness = received['speechiness']
    #tempo = received['tempo']
    #valence = received['valence']

# This modified function can let user to input any numbers in the UI.
# We can also use prompt functionality to prompt user to enter input.
def get_music_category(
    acousticness: float = 0.838816,
    danceability: float = 0.542950,
    energy: float = 0.669215,
    instrumentalness: float = 0.000006,
    liveness: float = 0.105610,
    speechiness: float = 0.391221,
    tempo: float = 111.894,
    valence: float = 0.796073
):


    pred_name = model.predict([[acousticness, danceability, energy,
                                instrumentalness, liveness, speechiness, tempo, valence]]).tolist()[0]
    return {'prediction': pred_name}