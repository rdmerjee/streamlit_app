import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

st.title('Rik Mukherjee Application')
st.markdown('This is **the special application for Stats 21**')
st.markdown('An application that gives you what you need for the project in Stats 21')

st.sidebar.title('More')
st.sidebar.markdown('This project was done in Spring 2023 for Stats 21')

web_apps = st.sidebar.selectbox("Select Web Apps",
                                ("Exploratory Data Analysis", "Spiderman Movie"))


if web_apps == "Exploratory Data Analysis":

  uploaded_file = st.sidebar.file_uploader("Choose a file")

  if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    show_df = st.checkbox("Show Data Frame", key="disabled")

    if show_df:
      st.write(df)

    column_type = st.sidebar.selectbox('Select Data Type',
                                       ("Numerical", "Categorical", "Bool", "Date"))

    if column_type == "Numerical":
      numerical_column = st.sidebar.selectbox(
          'Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

      # histogram
      choose_color = st.color_picker('Pick a Color', "#69b3a2")
      choose_opacity = st.slider(
          'Color Opacity', min_value=0.0, max_value=1.0, step=0.05)

      hist_bins = st.slider('Number of bins', min_value=5,
                            max_value=150, value=30)
      hist_title = st.text_input('Set Title', 'Histogram')
      hist_xtitle = st.text_input('Set x-axis Title', numerical_column)
      hist_ytitle = st.text_input('Set y-axis Title', numerical_column)

      fig, ax = plt.subplots()
      ax.hist(df[numerical_column], bins=hist_bins,
              edgecolor="black", color=choose_color, alpha=choose_opacity)
      ax.set_title(hist_title)
      ax.set_xlabel(hist_xtitle)
      ax.set_ylabel(hist_ytitle)
      ax.set_ylabel('Count')

      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)

      # Display the download button
      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )
if web_apps == "Spiderman Movie":
  st.markdown('I recently watched Spider-Man: Across the Spiderverse, and I was deeply moved by the film. The animation was beautiful, the characters were great, the main character was very vulnerable and easy to root for, and the villain was menacing but you could understand why he did what he did.')
    st.markdown('Do you agree that this movie is good?')

    agree = st.checkbox('I agree')

    if agree:
        st.write('Great, I agree with you')

    st.markdown('Was the villain cool?')

    yes = st.checkbox('Yes')
    no = st.checkbox ('No')

    if yes:
        st.markdown('**Great, I agree with you!**')

    if no:
        st.write('**I do not agree with you. What is the reason for this?**')
        st.text_input('Input your reasoning here.')
