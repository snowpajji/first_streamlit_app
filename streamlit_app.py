import streamlit
streamlit.title("My mom's new healthy dinner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 & blueberry oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("pick some fruits:',list(my_fruit_list.index))



streamlit.dataframe(my_fruit_list)
