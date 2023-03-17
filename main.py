import openai
OPENAI_API_KEY="sk-xxxxxxxx"

openai.api_key = OPENAI_API_KEY

"""response = openai.Completion.create(model="text-davinci-003",\
                                    prompt="Necesito nombres para gatos",\
                                    temperature=0, max_tokens=256)"""

with open("video.mp4", "rb") as audio_file:
    trascript = openai.Audio.transcribe("whisper-1", audio_file)          
    print(trascript)
