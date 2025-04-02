import streamlit as st
import random

# ページ設定
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
    3. 回答予想欄に数字を入力し、「結果確認」ボタンを押してください。
    4. 予想が正しい場合、ヒット(位置も数字も正解)とブロー(位置は違うが数字は正解)の数が表示されます。
    5. 予想を繰り返しランダムな数を充てることが出来ればあなたの勝利です。
    """)

# ゲームの状態を保持するためのセッション状態
if "secret" not in st.session_state:
    st.session_state.secret = None
    st.session_state.guesses = []
    st.session_state.game_started = False  # ゲーム開始フラグ
    st.session_state.n = None  # 桁数の初期化

# ゲームが開始していなければ桁数入力とゲーム開始ボタンを表示
if not st.session_state.game_started:
    n = int(st.number_input("桁数", min_value=1, step=1))

    if st.button("ゲームを開始"):
        # ランダムな数を生成
        st.session_state.secret = random.sample('123456789', n)
        st.session_state.secret = ''.join(st.session_state.secret)  # リストを文字列に変換
        st.session_state.guesses = []  # ゲーム開始時にリセット
        st.session_state.game_started = True  # ゲーム開始フラグをTrueに設定
        st.session_state.n = n  # 入力された桁数をセッション状態に保存
else:
    st.write(f"ゲームが開始されました。桁数: {st.session_state.n}桁")

    # 予想入力フォームと結果確認ボタン
    guess = st.text_input("予想を入力してください", max_chars=st.session_state.n)
    submit_button = st.button("結果確認")

    # ヒットとブローを計算する関数
    def check_hit_and_blow(secret, guess):
        hit = 0
        blow = 0
        secret_list = list(secret)  # secretをリストに変換

        # ヒットの判定
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                hit += 1
                secret_list[i] = None  # ヒットした位置は無効化

        # ブローの判定
        for i in range(len(guess)):
            if guess[i] != secret[i] and guess[i] in secret_list:
                blow += 1
                secret_list[secret_list.index(guess[i])] = None  # ブローの位置も無効化

        return hit, blow

    # エラーチェック
    def validate_guess(guess, n):
        if len(guess) != n:
            return False, "予想が桁数に足りていません。もう一度入力してください。"
        if not guess.isdigit():
            return False, "数字以外の文字が含まれています。数字のみを入力してください。"
        return True, ""

    # 結果の表示
    if submit_button:
        is_valid, error_message = validate_guess(guess, st.session_state.n)
        if not is_valid:
            st.error(error_message)  # エラーメッセージを表示
        else:
            hit, blow = check_hit_and_blow(st.session_state.secret, guess)
            st.write(f"ヒット: {hit}, ブロー: {blow}")
            st.session_state.guesses.append((guess, hit, blow))  # 予想履歴に追加

            # ゲームが終わった場合
            if hit == st.session_state.n:
                st.write("おめでとうございます！正解です！")
            else:
                st.write("引き続き予想してください。")

    # ゲーム履歴
    if st.session_state.guesses:
        st.write("予想履歴:")
        for idx, (guess, hit, blow) in enumerate(st.session_state.guesses, 1):
            st.write(f"{idx}. 予想: {guess} → ヒット: {hit}, ブロー: {blow}")
