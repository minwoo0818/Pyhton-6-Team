import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)
# Share your demo with just 1 extra parameter 🚀-- 이렇게 실행하면 웹사이트 링크 생성
demo.launch(share=True)  