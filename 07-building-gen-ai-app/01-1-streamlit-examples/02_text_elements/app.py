import streamlit as st 

st.caption("This is written small caption")
st.code("a=1234")
st.text("Hello world")

st.divider()
st.write("This is code will be printed 1")
st.latex("\int a x^2 \,dx")
st.divider()
 
def get_user_name():
    return 'John'

with st.echo():
    ## 이 블록 안의 모든 내용이 화면에 인쇄되고 실행된다.
    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# 이제 다시 화면에 인쇄하지 않는 것으로 돌아갑니다.
st.write('Done!') 