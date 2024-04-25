
# Import python packages
import streamlit as st
import requests, pandas as pd
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

cnx = st.connection("snowflake")
session = cnx.session()
my_catalog = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website")
pd_catalog = my_catalog.to_pandas()

color_list = pd_catalog["COLOR_OR_STYLE"]

sweatshirts_selected_option = st.selectbox(
    'Pick a sweatsuit color or style:',
    color_list)

selected_sweatshirt_product = pd_catalog.loc[pd_catalog["COLOR_OR_STYLE"] == sweatshirts_selected_option]
#st.write(type(st.dataframe(selected_sweatshirt_product)))
#st.write(type(selected_sweatshirt_product))
#st.write(selected_sweatshirt_product["DIRECT_URL"])
#st.stop()
#st.write ('You have selected', selected_sweatshirt_product ["DIRECT_URL"])


#st.write(selected_sweatshirt_product["DIRECT_URL"].to_string(index=False))
sweatshirt_image_url = selected_sweatshirt_product["DIRECT_URL"]
#st.write(type(sweatshirt_image_url))
#st.write(sweatshirt_image_url.index[0])
st.write(selected_sweatshirt_product["COLOR_OR_STYLE"].values[0])
st.image(sweatshirt_image_url[sweatshirt_image_url.index[0]],width=400, caption="Our warn comfortable, " + selected_sweatshirt_product["COLOR_OR_STYLE"].index[0] + " sweatshirt!" )


