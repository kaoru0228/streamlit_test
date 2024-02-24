import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')


# 表の挿入  API refernce の Data elements
df1 = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})
st.write('DataFrame')
# st.write(df1) # ソートが可能（動的）
# st.dataframe(df1.style.highlight_max(axis=0), width=500, height=200)
st.table(df1.style.highlight_min(axis=0))  # 静的


# グラフ  Chart elements
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.write('Line chart')
st.line_chart(df2)
st.write('Area chart')
st.area_chart(df2)
st.write('Bar chart')
st.bar_chart(df2)


# マップ  Chart elements
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.write('Map')
st.map(df3)


# 画像  Media elements
st.write('Display Image')
img = Image.open('ResNet50.png')
st.image(img, caption='ResNet50', use_column_width=True)

# 音声  Media elements
# st.write('Audio')
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

# 動画  Media elements
# st.write('Video')
# st.video(data, format="video/mp4", start_time=0)

# マークダウン  Text elements
"""
# 見出し1
## 見出し2
### 見出し3

*Itaric*と**Bold**

- 箇条書きリスト1
- 箇条書きリスト2

1. 番号付きリスト1
2. 番号付きリスト2

リンク\n
[Google](https://www.google.com)

画像の挿入\n
![画像]('ResNet50.png')

`インラインコード  pip install streamlit`

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
