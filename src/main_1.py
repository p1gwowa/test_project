import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')                                  # page layout

page_bg_img = '''
<style>
    .stApp {
        background-color: rgb(255, 204, 153);
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


col1, col2 = st.columns([0.35, 0.65], vertical_alignment='center')   # page layout

col1.header(':blue[_Welcome to_]', anchor=False)
col1.title(':blue[Customer Outflow Analyzer!]', anchor=False)

with col1:
  in_col1_1, in_col2_1 = st.columns([0.35, 0.65], vertical_alignment='center')

inst_button = in_col1_1.button('View instructions 📄')               # instruction button
start_button = in_col2_1.button('Start Analysis! 🚀')                # start button

img = Image.open('src/logo.png')

with col2:
  in_col1_2, in_col2_2, in_col3_2 = st.columns([1, 2, 1], vertical_alignment='center')  # page layout

for _ in range(9):
  in_col2_2.write('')

in_col2_2.image(img, width=350, output_format="PNG", use_column_width=False)    # team logo
in_col2_2.header('Group Name QWERTY', anchor=False)   # team name

for _ in range(8):
  in_col2_2.write('')

@st.dialog("Instruction")          # instruction dialog window
def inst():
  with open('src/Instructions_for_the_User.txt', 'r', encoding='utf-8') as file:
    instructions = file.read()
    st.write(instructions)
    
if inst_button:
  inst()
    
if start_button:
  st.switch_page('pages/analysis.py')

