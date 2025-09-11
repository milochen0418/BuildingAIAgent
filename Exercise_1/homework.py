from openai import OpenAI

# Point the client to your local server and use any placeholder API key
client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk-local-123",  # llamafile doesn't validate this
)

# Find your model id via GET /v1/models
# Example: model_name = "ModelName"  # use the id returned by /v1/models
model_name = "your-model-id-from-/v1/models"
#model_name = "Qwen2.5-0.5B-Instruct-Q6_K"

resp = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give me a 2-sentence summary of llamafile."},
    ],
    temperature=0.7,
)

print(resp.choices[0].message.content)