import chainlit as cl
# from chatbot import aibot
from async_agent import Aiagent

@cl.on_chat_start     # Use Decorator
async def on_chat_start():
    # Your custom logic goes here...
    await cl.Message(content = "I am your AI Assistant!").send()
    
@cl.on_message     # Use Decorator
async def main(message: cl.Message):
    user_input = message.content
    
    response = await Aiagent(user_input)
    # Send a response back to the user
    await cl.Message(content=f"Agent: {response}").send()
    