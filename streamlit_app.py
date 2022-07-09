import streamlit.components.v1 as components  # Import Streamlit
import requests as r
import streamlit as st

# print ('http://localhost:8501?q=drill+bits')
# print ('http://localhost:8501?q=drill+bits&url=https://www.mscdirect.com/browse/tn/tn?mscNew=true&searchterm=')

params_dict = st.experimental_get_query_params()
print (f"{params_dict = }")
query = 'drill+bits'

try:
    query = params_dict['q'][0]
except:
    pass
print (f"{query = }")

st.set_page_config(page_title='Test', layout='wide')
# st1, st2 = st.columns(2)


endpoint = 'https://www.bing.com/search?q='
endpoint = 'https://www.mscdirect.com/browse/tn/tn?mscNew=true&searchterm='

url = f"{endpoint}{query}"
# user_agent = 'user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
# req = r.get(url, headers={user_agent})

components.iframe(url, width=1900, height=1200, scrolling=True)



