import gradio as gr

def submit(name, age, gender, preferred_hobby, non_preferred_hobby, q1, q2, q3, q4, q5, q6, q7, q8):
    responses = (f"Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\n"
                 f"Q5: {q5}\nQ6: {q6}\nQ7: {q7}\nQ8: {q8}")
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
            
            q1 = gr.Radio(label="질문 1: 아침에 주로 무엇을 드시나요?", choices=["빵", "밥"])
            q2 = gr.Radio(label="질문 2: 주말에 어떤 활동을 선호하시나요?", choices=["운동", "독서"])
            q3 = gr.Radio(label="질문 3: 여행을 간다면?", choices=["산", "바다"])
            q4 = gr.Radio(label="질문 4: 주로 어떤 음악을 듣나요?", choices=["클래식", "팝"])
            q5 = gr.Radio(label="질문 5: 어떤 영화 장르를 좋아하시나요?", choices=["액션", "로맨스"])
            q6 = gr.Radio(label="질문 6: 어떤 음료를 좋아하시나요?", choices=["커피", "차"])
            q7 = gr.Radio(label="질문 7: 어떤 옷을 주로 입으시나요?", choices=["정장", "캐주얼"])
            q8 = gr.Radio(label="질문 8: 어떤 동물을 좋아하시나요?", choices=["고양이", "강아지"])

        with gr.Column():
            submit_btn = gr.Button("제출")
            output = gr.Textbox(label="결과")

    submit_btn.click(fn=submit, inputs=[name, age, gender, preferred_hobby, non_preferred_hobby, q1, q2, q3, q4, q5, q6, q7, q8], outputs=output)

if __name__ == "__main__":
    demo.launch(share=True)
