# example/views.py
import base64
import openai
import requests
from io import BytesIO
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from datetime import datetime

from django.http import HttpResponse

def index(request):
    '''Return a simple HTML page.'''

    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello, I am Anurag Verma.</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)



# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Set up the OpenAI model you want to use
model_engine = "text-davinci-002"

# Function to generate a caption/tagline for a given image
def generate_caption(image_url):
    # Download the image and convert it to base64 encoding
    response = requests.get(image_url)
    image = response.content
    encoded_image = base64.b64encode(image).decode("utf-8")

    # Generate a prompt to feed to GPT-3
    prompt = f"Generate a caption/tagline for this image: {encoded_image}"

    # Use GPT-3 to generate the caption/tagline
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated caption/tagline from the API response
    caption = response.choices[0].text.strip()
    return caption

def home(request):
    if request.method == 'POST' and request.FILES['face_image']:
        # Handle uploaded image
        face_image = request.FILES['face_image']
        fs = FileSystemStorage()
        filename = fs.save(face_image.name, face_image)
        uploaded_file_url = fs.url(filename)
        # Generate cartoon and tagline here
        cartoon_image = generate_cartoon(uploaded_file_url)
        tagline = generate_caption(uploaded_file_url)
        # Pass data to template
        return render(request, 'result.html', {
            'uploaded_file_url': uploaded_file_url,
            'cartoon_image': cartoon_image,
            'tagline': tagline,
        })
    return render(request, 'home.html')
