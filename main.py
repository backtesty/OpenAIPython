import openai
OPENAI_API_KEY="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"

openai.api_key = OPENAI_API_KEY

response = openai.Completion.create(model="text-davinci-003",\
                                    prompt="Necesito nombres para gatos",\
                                    temperature=0, max_tokens=256)

print(response)
text = response['choices'][0]['text']
print(text)