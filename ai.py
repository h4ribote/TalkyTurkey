import openai
import json


def talk(user_input: str) -> str:

    openai.api_key = "API_KEY"

    # 会話内容を復元
    with open("db/conversation.json", 'r') as file:
        conversation = json.load(file)

    conversation.append({"role": "user", "content": user_input})

    # 回答を取得
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=200,
        n=1
        )

    ai_response = response['choices'][0]['message']['content']

    conversation.append({"role": "assistant", "content": ai_response})

    # 会話内容を保存
    with open("db/conversation.json", 'w') as file:
        json.dump(conversation, file)
    
    return ai_response