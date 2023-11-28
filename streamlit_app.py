import streamlit
streamlit.title ('Hello,world!')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

# We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
#Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show). 
#Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page. 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
#display
streamlit.dataframe(fruits_to_show)

#LESSON 9 - API CODES IN Streamlit.
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

#another try.
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json()) #this just writes things on the screen.

# normalized table (not sure).
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# put it into the dataframe.
streamlit.dataframe(fruityvice_normalized)

#removed - next section so that it does not conflict with another 

#edit
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#normalized json response
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it the screen as a table
#streamlit.dataframe(fruityvice_normalized)

#add a text entry box and  send the Input to Fruityvice as Part of the API Call

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#does not show choice, still. need to add the table somehow
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) DID NOT WORK
streamlit.dataframe(fruityvice_normalized) #STILL OLD TABLE

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT* from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
