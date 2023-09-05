import openai
import streamlit as st
import json
from datetime import datetime
import config
st.title("Yatırım Finansman Chatbot")
openai.api_key = config.api_key
# Veriyi yükle
with open('C:\\Users\\enes.uzun\\PycharmProjects\\YF_cbot\\training_data.json', 'r', encoding='utf-8') as f:
    veri = json.load(f)
with open('C:\\Users\\enes.uzun\\PycharmProjects\\YF_cbot\\Kurumsal_Iletisim_SSS.json', 'r', encoding='utf-8') as r:
    veri2 = json.load(r)
with open('C:\\Users\\enes.uzun\\PychrmProjects\\YF_cbot\\website_SSS.json', 'r', encoding='utf-8') as r:
    veri3 = json.load(r)
with open('C:\\Users\\enes.uzun\\PycharmProjects\\YF_cbot\\YFHatırlatma.json', 'r', encoding='utf-8') as r:
    veri4 = json.load(r)


def chat_with_gpt3(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": veri},
            {"role": "system", "content": veri2},
            {"role": "system", "content": veri3},
            {"role": "system", "content": veri4},
            {"role": "system",
             "content": "Sen bir Yatırım Finansman Mobil App Chat botusun. Tüm cevapları ona göre vermelisin."},
            {"role": "user", "content": message}
        ],
        temperature=0.4,
        max_tokens=1000
    )
    return response.choices[0].message['content']


# Ayarlar sayfası için gerekli kodlar

st.config.show_settings = True

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Selam! Nasıl yardımcı olabilirim?"):
    start_time = datetime.now()

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_content = chat_with_gpt3(prompt)

        elapsed_time = datetime.now() - start_time
        response_seconds = elapsed_time.total_seconds()

        apology_message = "Biraz uzun sürdüğü için kusura bakmayın.<br>" if response_seconds > 5 else ""

        response_for_display = f"{response_content}<br><div style='text-align:right; font-size:0.8em;'>{apology_message} {response_seconds:.2f} saniye</div>"
        st.markdown(response_for_display, unsafe_allow_html=True)

        response_for_state = f"{response_content} {apology_message} {response_seconds:.2f} saniye"
        st.session_state.messages.append({"role": "assistant", "content": response_for_state})
