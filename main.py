import openai
import json
import config
openai.api_key = config.api_key

with open('training_data.json', 'r',encoding='utf-8') as f:
  veri = json.load(f)
with open('Kurumsal_Iletisim_SSS.json', 'r', encoding='utf-8') as r:
  veri2=json.load(r)
with open('website_SSS.json', 'r', encoding='utf-8') as r:
  veri3=json.load(r)
with open('YFHatırlatma.json', 'r', encoding='utf-8') as r:
  veri4=json.load(r)

def chat_with_gpt3(message):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
      {"role": "system", "content":veri},
      {"role":"system","content":veri2},
      {"role": "system", "content": veri3},
      {"role": "system", "content": veri4},
      {"role": "system", "content": "Sen bir Yatırım Finansman Mobil App Chat botusun. Tüm cevapları ona göre vermelisin."},
      {"role": "user", "content": message}
    ],
    temperature=0.4,  # Bu parametre modelin çıktısının belirsizliğini kontrol eder.
    max_tokens=1000  # Bu parametre modelin üreteceği token sayısını sınırlar.
  )
  return response.choices[0].message['content']


while True:
  message = input("Sen: ")
  response = chat_with_gpt3(message)
  print("Yatırım Finansman ChatBot:", response)