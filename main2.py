import streamlit as st

st.set_page_config(
    page_title="安いものを買いたい", 
    page_icon='🍖'
)

# タイトルと「使い方」ボタン
st.write("## 値段比較アプリ")

# 「使い方」ポップアップ
with st.expander("このページの使い方"):
    st.write("""
    ### このアプリの使い方
    1. **単位を選択**: 商品の重さや個数などの単位を選択してください（例: g, ml, 個など）。
    2. **商品情報を入力**: 比較したい2つの商品について、それぞれ以下の情報を入力します。
    (★印は必須項目です)
       - 名前(商品を区別するためのメーカ名などの名称)
       - 値段★
       - 1パックあたりの内容量★
       - パック数（例: ベーコンの3枚入りパックなど）
    3. **比較ボタンを押す**: 入力が終わったら「比較」ボタンを押して、どちらの商品が1単位あたり安いかを確認してください。
    """)

# スーパーでよく使われる単位を選択
unit = st.selectbox("単位を選択してください", ["g", "kg", "ml", "L", "個", "枚", "パック", "束", "本", "箱"])

cols = st.columns(2)

# 商品1の情報入力
with cols[0]:
    st.write("### 商品1の情報")
    product1_name = st.text_input("商品1の名前", placeholder="例: 小岩井牛乳")
    if not product1_name:
        product1_name = "商品1"
    
    product1_price = st.number_input("★商品1の値段（円）", min_value=0, step=1)
    product1_pack_weight = st.number_input("★商品1の1パックあたりの内容量", min_value=0, step=1)
    product1_pack_count = st.number_input("商品1のパック数", min_value=1, step=1)
    # 合計内容量を自動計算
    product1_quantity = product1_pack_weight * product1_pack_count

# 商品2の情報入力
with cols[1]:
    st.write("### 商品2の情報")
    product2_name = st.text_input("商品2の名前", placeholder="例: 明治おいしい牛乳")
    if not product2_name:
        product2_name = "商品2"
    
    product2_price = st.number_input("★商品2の値段（円）", min_value=0, step=1)
    product2_pack_weight = st.number_input("★商品2の1パックあたりの内容量", min_value=0, step=1)
    product2_pack_count = st.number_input("商品2のパック数", min_value=1, step=1)
    # 合計内容量を自動計算
    product2_quantity = product2_pack_weight * product2_pack_count

# ボタンが押されたら計算を実行
if st.button("比較"):
    if product1_price <= 0 and product2_price <= 0:
        st.error("両方の商品について値段を入力してください。")
    elif product1_price <= 0:
        st.error("商品1の値段を正しく入力してください。")
    elif product2_price <= 0:
        st.error("商品2の値段を正しく入力してください。")
    elif product1_quantity <= 0 and product2_quantity <= 0:
        st.error("両方の商品について内容量を正しく入力してください。")
    elif product1_quantity <= 0:
        st.error("商品1の内容量を正しく入力してください。")
    elif product2_quantity <= 0:
        st.error("商品2の内容量を正しく入力してください。")
    else:
        # 1単位あたりの価格を計算
        price_per_unit1 = product1_price / product1_quantity
        price_per_unit2 = product2_price / product2_quantity

        # 結果の表示
        st.write(f"{product1_name} の1{unit}あたりの価格: {price_per_unit1:.2f}円/{unit}")
        st.write(f"{product2_name} の1{unit}あたりの価格: {price_per_unit2:.2f}円/{unit}")

        # どちらが安いかを判定
        if price_per_unit1 < price_per_unit2:
            st.success(f"{product1_name} の方が安いです！")
        elif price_per_unit1 > price_per_unit2:
            st.success(f"{product2_name} の方が安いです！")
        else:
            st.info("両方の商品は同じ単価です！")
