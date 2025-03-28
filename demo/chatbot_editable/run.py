import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        chatbot = gr.Chatbot(value=[], type="messages", editable="user")
        chatbot2 = gr.Chatbot(value=[], type="tuples", editable="user")
    add_message_btn = gr.Button("Add Message")
    add_user_message_btn = gr.Button("Add User Message")

    with gr.Row():
        concatenated_text1 = gr.Textbox(label="Concatenated Chat 1")
        concatenated_text2 = gr.Textbox(label="Concatenated Chat 2")
        edited_messages = gr.Textbox(label="Edited Message")

    def add_message(history: list, history2: list[list[str]]):
        usr_msg = "I'm a user"
        bot_msg = "I'm a bot"
        history.append({"role": "user", "content": usr_msg})
        history.append({"role": "assistant", "content": bot_msg})
        history2.append([usr_msg, bot_msg])
        return history, history2
    
    def add_user_message(history: list, history2: list[list[str]]):
        usr_msg = "I'm a user"
        history.append({"role": "user", "content": usr_msg})
        history2.append([usr_msg, None])
        return history, history2
    
    add_message_btn.click(add_message, [chatbot, chatbot2], [chatbot, chatbot2])
    add_user_message_btn.click(add_user_message, [chatbot, chatbot2], [chatbot, chatbot2])
    chatbot.change(lambda m: "|".join(m["content"] for m in m), chatbot, concatenated_text1)
    chatbot2.change(lambda m: "|".join("|".join(filter(None, (x if x is not None else "" for x in m))) for m in m), chatbot2, concatenated_text2)

    def edit_message(edited_message: gr.EditData):
        return f"from {edited_message.previous_value} to {edited_message.value} at {edited_message.index}"
    
    chatbot.edit(edit_message, None, edited_messages)
    chatbot2.edit(edit_message, None, edited_messages)

if __name__ == "__main__":
    demo.launch()
