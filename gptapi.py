import openai
from config import key_for_openia

openai.api_key=key_for_openia

messages =  []

def start_dialog_gpt(text):
    try:
        messages.append({'role':'user','content': text})
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages= messages
            )
        
        response=response.choices[0].message.content

        #добавляем ответ gpt в историию диалога
        messages.append({'role': 'assistant', 'content':response})

        
        #обработаный текст ответа отправляем на озвучку
        return response
    except:
        return "ошибка"

if __name__=="__main__":
    data = input(">>>>")
    assist=start_dialog_gpt(data)
    
    print(f"gpt anser{assist}")






