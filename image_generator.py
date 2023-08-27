import openai
import requests
from PIL import Image
from io import BytesIO
import os

# We need to set up this variables to run script
openai.api_key = "Your API key"
image_name = "sample_image.png"
user_prompt = "Generate star wars scene with droids"

# Next we use OpenAi Api to generate our image
response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"  
)

# Now we have url to image
image_url = response['data'][0]['url']
response = requests.get(image_url)

# We try to download image
if response.status_code == 200:

    # If we get image, then we open it
    image_content = response.content
    image_data = BytesIO(image_content)
    img = Image.open(image_data)

    # Increase the resolution by resizing the image. 
    img = img.resize((6000, 6000)) # Size in pixels

    # Next we save image with 300 dpi
    img.save(image_name, dpi=(300,300))

    print("success")
else:
    print("Failed to fetch the image.")
