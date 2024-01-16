import streamlit as st
import requests
import json

page=st.sidebar.selectbox('choose your page',['create task','list','test'])
API_URL="http://127.0.0.1:8000/tasks"

if page=='create task':
    st.title('create task')
    with st.form(key='registration'):
        content:str=st.text_input('memo',max_chars=100)
        data={
            'title':content
        }
        submit_button=st.form_submit_button(label='regist')

        if submit_button:
            res=requests.post(
                API_URL,
                data=json.dumps(data)
            )
            if res.status_code==200:
                st.success('success!')
            st.json(res.json())
elif page=='list':
    st.title('list')
    res=requests.get(API_URL)
    records=res.json()
    # for record in records:
    #     st.subheader('・'+record.get('title'))
    #st.subheader(records.get('title'))
    titles=[record['title'] for record in records]
    for record in records:
        title=record['title'] if record['title'] is not None else 'none'
        id=record['id']

        col1,col2=st.columns([3,1])
        col1.subheader('・'+title)
        if col2.button('delete',key=id):
            response=requests.delete(f"http://127.0.0.1:8000/tasks/{id}")            
            #st.write("hoge")
            if response.status_code == 200:
                st.write(f"Task with ID {id} deleted successfully.")
            else:
                st.write(f"Failed to delete task with ID {id}.")
elif page=='test':
    st.title('test')
    data=[1,2,3,4,1,6,8,4,8,4,5,6,9,5]
    st.line_chart(data)
    st.write(data)