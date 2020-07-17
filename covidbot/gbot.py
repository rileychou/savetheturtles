from flask import Flask
import random

app = Flask(__name__)

@app.route('/covidbot', methods=['POST'])

def covidbot():
    joke = random.choice(["If Hogwarts was in the ocean, they would play squidditch!",\
                          "Whose music do fish listen to the most? Frank Ocean", \
                          "I’m shore we will need sunscreen on the beach, it is hot as shell!", \
                          "Where do you fuel a submarine? Shell gas station.",\
                          "Is there a beach nearby? I'm in need of some Vitamin Sea", \
                          "We otter go for a swim, sea ya later!",\
                          "Keep your friends close, and your anemones closer",
                          "Lost at sea? I'm not shore.",\
                          "Life's a beach. Enjoy the waves.",\
                          "What did the ocean say to the other ocean? Nothing, it just waved."])
    return {
        'actions':[
            {'say': joke}
        ]
    }
