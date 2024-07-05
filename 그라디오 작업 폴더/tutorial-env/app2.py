# gradio library를 가져온다. gr로 줄여서 칭한다.
import gradio as gr

# gradio 내부에서 사용할 함수다.
def update(name): 
    return f"Welcome to Gradio, {name}!"

with gr.Blocks() as iface:
    gr.Markdown("Hello, World! I’m yelling in gradio!")
    with gr.Row():
        inp = gr.Textbox(placeholder="이름이 무엇인가요?")
        out = gr.Textbox()
    btn = gr.Button("제출")

    # 버튼에 이벤트 리스너를 추가한다. 
    # 버튼 클릭시 update함수를 호출하고, inp에 입력된 문자열을 파라미터로 보낸다. 함수의 반환값은 out에 출력한다.
    btn.click(fn=update, inputs=inp, outputs=out)

iface.launch()