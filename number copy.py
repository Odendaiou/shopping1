import streamlit as st
import random 

st.set_page_config(
    page_title="ひまをつぶそう", 
    page_icon='🎮'
)

# タイトルと遊び方ボタン
st.write("## 数あてゲーム")
with st.expander("このページの使い方"):
    st.write("""
    ### 遊び方
    1. 1から9の数字を入力した状態で画面下部のボタンを押してゲームを開始してください。
    2. 私が考えた1-9の数字が使われたランダムな数を当ててください、桁数は前述で入力された数字です。
    3. 回答予想欄に数字を入力し、Enterキーを押してください。
    4. 予想が正しい場合、ヒット(位置も数字も正解)とブロー(位置は違うが数字は正解)の数が表示されます。
    5. 予想を繰り返しランダムな数を充てることが出来ればあなたの勝利です。
    """)

n = int(st.number_input("桁数", min_value=1, step=1))


def check_hit_and_blow(secret,guess):
#ユーザーの推測値と正解を比較し値を返す
    hit = 0
    blow = 0
    return hit, blow


