import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

st.title("*Bengalies*") 
from PIL import Image
img = Image.open("sindur.jpg")
st.image(img)

st.subheader("*All about the bengali culture*")
st.write("**The sanctity of Hooghly, the beauty of Eastern Himalayas, the diversity of Sunderbans and the freshness of the Tea Gardens, all blend together to constitute what we call the unique culture of West Bengal. Bengali culture also has its root in Bengali music, Bengali cinema and Bengali literature.Bengalies are very simple people or rather should I say simple living, high thinking.Most of them are brilliant students growing up to become famous scholars.Bengali language has been voted as the sweetest language in the world by UNESCO.**")

ben = st.radio(
    "Do you like the bengali culture?",
    ('Yeah', 'No'))

if ben == 'Yeah':
    st.write('Wow cool')
else:
    st.write('Okey')

st.sidebar.text("Some glimpses of bengal")
from PIL import Image
img = Image.open("pic2.jpg")
st.sidebar.image(img)
from PIL import Image
img = Image.open("pic1.jpg")
st.sidebar.image(img)
from PIL import Image
img = Image.open("pic3.jpg")
st.sidebar.image(img)

st.subheader("*All about the bengali festivals*")
st.write("**The most popular festival celebrated in West Bengal is Durga Puja where all the people come out in the streets and celebrate this four day festival. Other festivals celebrated in West Bengal are Kaali Puja,Bijaya Dashami, Bhai Phonta, Holi, Rathyatra and Christmas.**")


tab1, tab2, tab3,tab4,tab5 = st.tabs(["Durga Puja", "Kaali Puja","Bhai Phonta", "Holi","Christmas"])
with tab1:
 st.subheader("The most popular festival celebrated in West Bengal is Durga Puja where all the people come out in the streets and celebrate this four day festival.")
 st.image("durga.jpg",width =500 )


with tab2:
 st.subheader("Kali Puja, a festival dedicated to goddess Kali, is celebrated on the new moon day (Dipannita Amavasya) of the Hindu month Kartik. It usually coincides with the Lakshmi Puja day of Diwali.")
 st.image("kali.jpg",width =500 )

with tab3:
  st.subheader("Brothers in return bless their sisters and pray for their well-being. West Bengal- The occasion is known as Bhai Phonta and falls on the first or second day of the Kali Puja festival.")
  st.image("vaifota.jpg",width =500 )

with tab4:
 st.subheader("West Bengal celebrates Holi as the Dol Jatra Here the people celebrate this day by placing the idols of Krishna and Radha on a Palki (Palinquin) and they carry them around and play with Abir (Gulal). It is a ritual on this day for young people to seek blessings from elders by touching their feet with colours.")
 st.image("holi.jpg",width =500 )

with tab5:
 st.subheader("Kolkata Christmas Festival is held annually during the month of December in Kolkata on Park Street, Kolkata, which is one of the largest dedicated Christmas carnivals in India. In this festival various Bands and choir groups perform on the stage at Allen Park on Park Street.")
 st.image("christmas.jpg",width =500 )   

be = st.radio(
    "So do you wanna visit kolkata once in your life?",
    ('Yeah really I want to visit', 'No not that much interested'))

if be == 'Yeah really I want to visit':
    st.write('wow great!!')
else:
    st.write('Okey')

st.subheader("*All about the bengali food*")
st.write("**Bengal's food is the pride of the state as it has huge variety to offer. When it comes to festivities and events food is the main focal point for the people, for the culture. This is because the practice of multi-cropping is quite common in Bengal which has earned fame for producing varied and good quality rice.**")

st.write("**West Bengal is famous for an array of things, and one of the most important of them is food. The mouth-watering Rosogullas, Chomchom, and Rasamalai, the super tasty Sorshe Ilish and Chingri Macher Malai Curry,kolkata style biriyani,Alu posto,luchi,Alur dom,Basanti Pulao,Kasha Mangsho,Fish fry and but a few of the mouthwatering and tempting food of the highly illustrated and exquisite Bengali cuisine.**")
st.image("food.jpg",width=600)

op = st.selectbox(
    'So do you wanna have this kind of mouthwatering and delicious food ?',
    ('Yeah really!!', 'No not that much...', 'Big no!'))


st.subheader("*Why West Bengal famous in world?*")
st.write("**The cultural capital of India has been the home to several stalwarts belonging from various fields. Not to forget the fact that most of the Nobel laureates have been produced from this state- Rabindranath Tagore, Amartya Sen , St.**")
if st.button("See it!"):
    st.image("wb.png",width=200)

st.subheader("*How old is Bengali culture?*")
st.write("**Bengal has a recorded history of 1,400 years. The Bengali people are its dominant ethnolinguistic group. The region has been a historical melting point, blending indigenous traditions with cosmopolitan influences from pan-Indian subcontinental empires.**")
if st.button("See it!!"):
 st.image("cul.jpg",width=500)

text_input = st.text_input(
        "Say something about bengalies")

if st.button("Thank you!!"):
    st.snow()