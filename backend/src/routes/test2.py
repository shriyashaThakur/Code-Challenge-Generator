from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

with open('/Users/shriyashathakur/Documents/college/college-project/major-project/nextjs-react/fast-nextjs-v2/public/terna-logo.png', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()
print(client)
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
        'give colour of logo '
    ]
)

print(response.text)