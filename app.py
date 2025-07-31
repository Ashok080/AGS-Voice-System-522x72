import gradio as gr

def greet(name):
    return f"Hello, {name}! I am AGS — your voice-powered assistant."

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="🗣 Enter your name"),
    outputs=gr.Textbox(label="🧠 AGS Response"),
    title="AGS Voice System",
    description="Multilingual reasoning system trained on 522 datasets and 72 notebooks."
)

demo.launch()
