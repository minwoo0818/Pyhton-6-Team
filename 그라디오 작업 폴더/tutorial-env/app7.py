import gradio as gr

def submit(name, age, gender, preferred_hobby, non_preferred_hobby, *questions):
    responses = "\n".join([f"Q{i+1}: {q}" for i, q in enumerate(questions)])
    return (f"이름: {name}\n나이: {age}\n성별: {gender}\n"
            f"선호 취미: {preferred_hobby}\n비선호 취미: {non_preferred_hobby}\n"
            f"{responses}")

with gr.Blocks() as demo:
    gr.Markdown("# 취미 추천 서비스")
    
    with gr.Row():
        with gr.Column():
            name = gr.Textbox(label="이름")
            age = gr.Number(label="나이")
            gender = gr.Radio(label="성별", choices=["남성", "여성"])
            preferred_hobby = gr.Textbox(label="선호 취미")
            non_preferred_hobby = gr.Textbox(label="비선호 취미")
            
            questions = []
            for i in range(1, 9):
                questions.append(gr.Radio(label=f"질문 {i}", choices=["선택 1", "선택 2"]))

        with gr.Column():
            submit_btn = gr.Button("제출")
            output = gr.Textbox(label="결과")

    submit_btn.click(fn=submit, inputs=[name, age, gender, preferred_hobby, non_preferred_hobby] + questions, outputs=output)

if __name__ == "__main__":
    demo.launch()
