import requests
from PIL import Image
import io
from riffusion.spectrogram_params import SpectrogramParams
from riffusion.spectrogram_image_converter import SpectrogramImageConverter
API_URL = "https://api-inference.huggingface.co/models/riffusion/riffusion-model-v1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
params = SpectrogramParams()
converter = SpectrogramImageConverter(params)


def getaudio(prmpt, dur = 8):
    image_bytes = query({
	"inputs": f"{prmpt}",
    "parameters":{"width": dur*80},
    "options":{"wait_for_model":True}
    })
    
    image = Image.open(io.BytesIO(image_bytes))
    wav1 = converter.audio_from_spectrogram_image(image)
    wav1.export('py\static\output.wav', format='wav')
    return None
    


