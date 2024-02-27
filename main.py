import streamlit as st
import requests

KEY = "4UQKbsQUeRvtVHwspDC0MhC7QEPikUWZ9McbeE7M"
url = f"https://api.nasa.gov/planetary/apod?api_key={KEY}&thumbs=True"
response = requests.get(url)

cont = response.json()
if cont["media_type"] == "image":
    img_link = cont["hdurl"]
else:
    img_link = cont['thumbnail_url']
with open("image.jpg", "wb") as file:
    r2 = requests.get(img_link)
    file.write(r2.content)

st.title(cont["title"])
st.image("image.jpg")
content = cont["explanation"]
st.write(content)

