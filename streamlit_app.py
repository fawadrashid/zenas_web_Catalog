
# Import python packages
import streamlit as st
import requests, pandas as pd
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

cnx = st.connection("snowflake")
session = cnx.session()
my_catalog = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website")
pd_catalog= my_catalog.to_pandas()
color_list = pd_catalog[0].values.tolist()
sweatshirts_selected_option = st.selectbox(
    'Pick a sweatsuit color or style:',
    color_list)
)
#st.write ('You have selected', sweatshirts_selected_option )

if sweatshirts_selected_option:
    st.write(my_dataframe.select(col('PRICE')));   
    st.stop()
    for color_style_chooen in sweatshirts_selected_option:
        ingredients_string += fruit_chosen + ' '

        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        # st.write('The search value for ', fruit_chosen,' is ', search_on, '.')

        st.subheader(fruit_chosen + ' Nutrition Information')
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + search_on)
        fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width=True)
    
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
        values ('""" + ingredients_string +  """','""" + name_on_order+ """')"""
    #st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert = st.button('Submit Order')
    
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")
