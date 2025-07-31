import gradio as gr
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def ags_response(user_input):
    if not user_input.strip():
        return "Please enter a message."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=ags_response,
    inputs="text",
    outputs="text",
    title="🧠 AGS: Voice + Reasoning System",
    description="Multilingual AI agent with reasoning and memory"
)

demo.launch()
