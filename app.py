import streamlit as st
view = {'1월':100, '2월':150, '3월':30, '4월':145, '5월':23, '6월':45, '7월':76, '8월':90, '9월':127, '10월':100, '11월':124, '12월':60}
st.write('# Youtube View')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview