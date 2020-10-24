#from PIL import Image
import pandas as pd
import numpy as np
import streamlit as st



def image_resize(image, bw):
    """
        Resizes image to a balanced pixel ratio considering a 
        pixel basewith wb alocated by the user
    """
    basewidth = bw
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    image = image.resize((basewidth,hsize))

    return image

#logo_loc = 'C:/ML Analytics/00 - ML Stuff/98 - ML Analytics Branding/'   

#mlanalytics_logo = Image.open(logo_loc + 'logo_transparent_background.png')
#mlanalytics_logo = image_resize( mlanalytics_logo, 500 )

#st.image(mlanalytics_logo )

# Ainda não é possível alinhar objectos( imagens, gráficos, selectboxes )
# à esquerda/direita/centro/etc.
# https://discuss.streamlit.io/t/how-to-center-images-latex-header-title-etc/1946

# Também não é permitido mudar a cor de background da webpage.
# https://github.com/streamlit/streamlit/issues/585

# Há limitações no uso de tags HTML em text markdown
# https://discuss.streamlit.io/t/are-you-using-html-in-markdown-tell-us-why/96

# Há limitações para a partilha de streamlit apps
# Varios utilizadores tiveram problemas a compilar um ficheiro executavel
# O utilizador final tem de ter Python instalado na maquina local também
# https://discuss.streamlit.io/t/how-to-most-easily-share-your-streamlit-app-locally/1751/12
# Uma opção passa por usar docker containers
# https://towardsdatascience.com/sharing-streamlit-apps-securely-with-your-clients-a34bf0f9e00c


""" 
# This is ML Analytics first streamlit app!
## Welcome!  :heart: :smiley_cat: :rocket:
"""

st.markdown(
"<span style='color:blue'><br> Let's start by adding an interactive dataframe below, where the user can \
chose the mean and the standard deviation of a Normal distribution  \
that generates the dataframe. The user can also chose column and row \
quantity to display in the data frame (check hidden side bar).  \
<br><br></span>",
unsafe_allow_html=True
)


mu = st.sidebar.selectbox(
    label = 'Select the mean.',
    options = [5, 10, 20]
)
sigma = st.sidebar.selectbox(
    label = 'Select standard deviation.',
    options = [0.1, 0.5, 1]
)

numb_cols = st.sidebar.selectbox(
    label = 'Select how many columns you want in the dataframe.',
    options = [5, 6, 7, 10]
)

numb_rows = st.sidebar.selectbox(
    label = 'Select how many rows you want in the dataframe.',
    options = [5, 10, 20]
)


df = pd.DataFrame(
    np.random.normal(float(mu),float(sigma), size= (numb_rows, numb_cols) ),
    columns=('col %d' % i for i in range(1, numb_cols+1))
)

st.dataframe( df )




"""
---
"""