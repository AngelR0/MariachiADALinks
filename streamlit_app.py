import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

#st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://https://github.com/AngelR0/MariachiADALinks)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('pic.jpg'))

st.header('Mariachi Aguilas De America')

st.info('Adept for any type of events.')
st.info('Zelle: (469)734-7799   Ines Adrian Reyes')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/@mariachiaguilasdeamericade2728/videos', 'Mariachi Aguilas De America Youtube channel', icon_size)
st_button('venmo', 'https://venmo.com/u/MariachiADA', 'Tip or Pay via Venmo', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)