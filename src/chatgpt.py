from openai import OpenAI
import config


# OpenAIクラスのインスタンスを生成する
client = OpenAI(
    api_key=config.OPEN_AI_KEY
)
# 役割(role)やコンテンツ(content)、モデル(model)の設定をする
response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Pythonの概要について教えてください。"}],
    model="gpt-3.5-turbo",
)
# APIで生成されるテキストを取得する
generated_text = response.choices[0].message.content
print(generated_text)