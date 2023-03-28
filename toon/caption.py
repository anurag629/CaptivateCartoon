import openai
import requests
from io import BytesIO

# Set up OpenAI API credentials
openai.api_key = process.env.OPENAI_API_KEY

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
