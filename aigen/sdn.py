import requests
import io
from PIL import Image


API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def getimg(prompt):
	image_bytes = query({
	"inputs": f"{prompt}",
	"options":{"wait_for_model":True}
	})
	#print(image_bytes)
	image = Image.open(io.BytesIO(image_bytes))
	image.save(f"py\static\img.png")
	
	return None

	