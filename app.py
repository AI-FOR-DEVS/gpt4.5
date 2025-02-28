from openai import OpenAI
from playsound import playsound
import os

client = OpenAI()

# Create a directory for temporary audio files if it doesn't exist
if not os.path.exists("temp_audio"):
    os.makedirs("temp_audio")

while True:
    user_input = input("You: ")
    
    # Get text response from GPT
    response = client.chat.completions.create(
        model="gpt-4.5-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input
                    }
                ]
            },
        ],
        response_format={
            "type": "text"
        },
        temperature=1,
    )

    text_response = response.choices[0].message.content
    print(text_response)

    # Convert text to speech using OpenAI TTS
    speech_file_path = "temp_audio/response.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",  # You can choose from: alloy, echo, fable, onyx, nova, shimmer
        input=text_response
    )

    # Write the audio content to file
    with open(speech_file_path, "wb") as file:
        file.write(response.content)

    # Play the audio
    playsound(speech_file_path)