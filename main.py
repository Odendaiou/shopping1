import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
import io
import time

# モールス信号の辞書
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

# 文字からモールス信号に変換
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

# モールス信号から文字に変換
def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(code, '') for code in morse.split())

# モールス信号の音声を再生
def play_morse_sound(morse):
    dot = AudioSegment.silent(duration=100) + AudioSegment.sine(frequency=700, duration=100)
    dash = AudioSegment.silent(duration=100) + AudioSegment.sine(frequency=700, duration=300)
    silence = AudioSegment.silent(duration=100)
    
    sound = AudioSegment.silent(duration=0)
    for symbol in morse:
        if symbol == '.':
            sound += dot + silence
        elif symbol == '-':
            sound += dash + silence
        elif symbol == ' ':
            sound += silence * 2  # 単語間の区切り
    
    buffer = io.BytesIO()
    sound.export(buffer, format="wav")
    buffer.seek(0)
    play(sound)

# Streamlit UI
st.title("モールス信号変換アプリ")

option = st.radio("変換モードを選択", ("文字 → モールス信号", "モールス信号 → 文字"))

if option == "文字 → モールス信号":
    text_input = st.text_input("文字を入力してください:")
    if st.button("変換"):
        morse_code = text_to_morse(text_input)
        st.write("モールス信号:", morse_code)
        if st.button("音を再生"):
            play_morse_sound(morse_code)

elif option == "モールス信号 → 文字":
    morse_input = st.text_input("モールス信号を入力してください（スペース区切り）:")
    if st.button("変換"):
        st.write("変換後の文字:", morse_to_text(morse_input))