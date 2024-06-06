# AIGEN
 This project aims to develop an application that generates images and music based on user input using pre-trained deep learning models through an Application Programming Interface (API). The application will allow users to input text and the pre-trained deep learning models will generate a corresponding image and music track. 

## WORKING ⚔️
The system is divided into two parts: Getting the input from the user, Display the generated output to the user. 

The music and image is generated using publicly available __pre-trained models__ through Inference API from __HuggingFace__.

Image Generating Model: __Stable Diffusion__ is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input

Music Generating Model: __Riffusion__ is a latent text-to-image diffusion model capable of generating spectrogram images given any text input. These spectrograms can be converted into audio clips.
![image](https://github.com/Gowtham58/AiGEN/assets/75661938/bcf53544-9c7a-4abf-b61c-ace96fe70709)

## OUTPUT 👍
### APPLICATION HOMEPAGE
![image](https://github.com/Gowtham58/AiGEN/assets/75661938/4c18cb4c-b84b-4d9f-9b0d-d619ff8a8cc7)
### APPLICATION DISPLAY PAGE
SAMPLE 1 : Input ‘Boat with sunrise’ and ‘Pleasant heavy metal’

![image](https://github.com/Gowtham58/AiGEN/assets/75661938/72cf1d9e-5b8c-4b28-a504-340264af8aae)

SAMPLE 2 : Input ‘Sparrow in tree abstract’ and ‘fun disco’

![image](https://github.com/Gowtham58/AiGEN/assets/75661938/1b1c5a23-b1ae-484a-b1d2-888f37c9a868)


## TO RUN LOCALLY 👇
1. Download the repository or clone it locally
2. Create a python virtual environment using ```python -m venv```
3. Once Created Activate the virtual environment
4. Install the packages from the requierments.txt
5. Run the application using ```flask --app aigen run```

 
