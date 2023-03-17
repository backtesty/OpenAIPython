import os, openai

OPENAI_API_KEY="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"
openai.api_key = OPENAI_API_KEY
response = openai.Image.create_edit(
    image=open("johnmendoza.png", "rb"),
     mask= open("mask.png", "rb"),
    prompt="Create a avatar fushion both images: image and mask",
    n=2, 
    size="512x512"
)
print(response)
