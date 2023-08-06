import os
import flask

def serve_local_model():
  # check that files exist
  try:
    from predictor import Predictor
  except Exception as e:
    print('Could not load predictor.py')

  loaded_predictor = Predictor()

  try:
    print('Calling predictor.load()')
    loaded_predictor.load()
  except Exception as e:
      print('An error occurred while loading your model with Preditor.load:')
      print(str(e))
      sys.exit()

  # instantiate flask
  app = flask.Flask(__name__)

  @app.route('/', methods=['POST'])
  def predict():
    data = {"success": False}
    body = flask.request.json
    print('Request coming in. Body is:')
    print(flask.jsonify(body))
    
    try:
      data = userProvidedPredictor.predict(body)
    except Exception as e:
      data["message"] = "There was an error while running your model: " + str(e)

    return flask.jsonify(data)

  # start the flask app, allow remote connections
  print('Local server is running on port 3005')
  app.run(host='0.0.0.0', port=3005)