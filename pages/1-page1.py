import streamlit as st

# 출력 메서드
st.text('Tushar-Aggarwal.com') # 화면에 출력 또는 입력을 받는다
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''') # 수식을 출력하는 문법
st.write('Supreme Applcations by Tushar Aggarwal') # 알아서 안에 있는 내용을 변환
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')

# * optional kwarg unsafe_allow_html = True
hello = 1
st.title('hello')

# 입력 메서드
st.button('Demo') 

import pandas as pd

df = pd.DataFrame({'keys':[1, 2, 3]})
st.data_editor(df) 
st.checkbox('Option 1') # 여러문항 중 여러 개 선택(중복), checkbox
st.radio('Pick Country:', ['France','Germany'])  # 여러문항 중 단일 항목 선택, radio button
st.selectbox('Select', [1,2,3]) 
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
# 완전히 정해진 옵션 중의 하나
st.text_input('Enter Article')
st.number_input('Enter required number')
st.text_area('Entered article text')
# 긴문자열을 받을 때 text_area
st.date_input('Select date')
st.time_input('Select Time')
st.file_uploader('File CSV uploader')
data = '안녕하세요'
st.download_button('Download Source data', data)

data = st.camera_input('Click a Snap')
if data: # 데이터의 값이 있으면 
    with open(data, "rb") as file:
        st.download_button(
            label="Download image",
            data=file,
            file_name="my_picture.png",
            mime="image/png",
        )


st.color_picker('Pick a color')

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

st.image('https://i.imgur.com/MDKQoDc.jpg',width=300)
