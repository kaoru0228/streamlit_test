import streamlit as st
from PIL import Image
import time

st.title('Streamlit Input widgets')
"""
`API reference : Input widgets`
"""

# プログレスバー
'Loading...'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.03)
'Done!!!'


# チェックボックス  Input widgets
st.sidebar.write('check box')
if st.sidebar.checkbox('Show Image'):
    img = Image.open('ResNet50.png')
    st.image(img, caption='ResNet50', use_column_width=True)

# セレクトボックス
st.sidebar.write('\nselect box')
option = st.sidebar.selectbox(
    '好きな数字',
    list(range(1, 10))
)
st.write((f'好きな数字：{option}'))

# テキストボックス
st.sidebar.write('\ntext box')
text = st.sidebar.text_input('趣味')
st.write((f'あなたの趣味：{text}'))

# スライダー
st.sidebar.write('\nslider')
condition = st.sidebar.slider('今日の調子', 0, 100, 50)
st.write((f'コンディション：{condition}'))


# レイアウト ------------------
# サイドバー 各所に実装
# st.sidebar.write('aaa')

# 2カラムレイヤー
# 2カラム  columns = st.columns(2)
# columns[0], columns[1]で参照
left_column, right_column = st.columns(2)
button = left_column.button('右カラムにテキストを表示')
if button:
    right_column.write('ここは右カラムです．')

# エキスパンダー
expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の解答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の解答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の解答')
