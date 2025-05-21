import litellm

def aibot(user_query):
    response = litellm.completion(
    model="gemini/gemini-2.0-flash-exp",
    messages=[{"role": "user", "content": user_query}],
    api_key = "AIzaSyBUSK_NAtwOojuNOfA47eVQORR1y-412pw"  
)
    return(response['choices'][0]['message']['content'])

print(aibot("hello"))
