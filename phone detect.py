from pyexpat import model


//write code to import a keras model
import keras
from keras.models import load_model
def load_model():
    model = load_model('model.h5')
    return model
