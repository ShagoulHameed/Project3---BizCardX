import streamlit as st
from streamlit_option_menu import option_menu
import easyocr
from PIL import Image
import pandas as pd
import numpy as np
import re
import io
import sqlite3
import base64

def image_to_text(path):
    input_img = Image.open(path)

    #convet image to array
    image_arr = np.array(input_img)
    reader = easyocr.Reader(['en'])
    text=reader.readtext(image_arr, detail=0)

    return text , input_img

def extracted_text(texts):
    extrd_dict = {"NAME": [],"DESIGNATION":[],"COMPANY_NAME":[],"CONTACT":[],"EMAIL":[],"WEBSITE":[],
                    "ADDRESS":[],"PINCODE":[]}
    
    extrd_dict["NAME"].append(texts[0])
    extrd_dict["DESIGNATION"].append(texts[1])

    for i in range(2,len(texts)):
        if texts[i].startswith("+") or (texts[i].replace("-","").isdigit() and '-' in texts[i]):
            extrd_dict["CONTACT"].append(texts[i])
        elif "@" in texts[i] and ".com" in texts[i]:
            extrd_dict["EMAIL"].append(texts[i])
        elif "WWW" in texts[i] or "www" in texts[i] or "Www" in texts[i] or "wWw" in texts[i] or "wwW" in texts[i]:
            mak_small = texts[i].lower()
            extrd_dict["WEBSITE"].append(mak_small)
        elif "Tamil Nadu" in texts[i] or "TamilNadu" in texts[i] or texts[i].isdigit():
            extrd_dict["PINCODE"].append(texts[i])   
        elif re.match(r'^[A-Za-z]',texts[i]):
            extrd_dict["COMPANY_NAME"].append(texts[i])
        else:
            remove_colon = re.sub(r'[,;]','',texts[i])
            extrd_dict["ADDRESS"].append(remove_colon) 
    for key,value in extrd_dict.items():
        if len(value)>0:
            concadenate = " ".join(value)
            extrd_dict[key] = [concadenate]
        else:
            value = "NA"
            extrd_dict[key] = [value]                   
    return extrd_dict

#Streamlit code here
st.set_page_config(layout = "wide")
#st.title("Extracting Business Card Data with OCR")
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-image: url('C:\\Users\\HameedS\\Desktop\\New folder\\VIdeos\\phonepe.jpg');
        background-size: cover;
    }
    .tabs .stTab {
        background-color: #0066ff;
        color: white;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-size: 18px;
        margin-right: 5px;
        cursor: pointer;
    }
    .tabs .stTab:hover {
        background-color: #0052cc;
    }
    .tabs .stTab.stTabSelected {
        background-color: #004080;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)



with st.sidebar:
    select = option_menu("Main Menu",["Home","Upload and Modify","Delete"])

st.sidebar.image("C:\\Users\\HameedS\\Desktop\\New folder\\BizCard\\images\\BIZ.jpg", use_column_width=True) 

#set_background('C:/Users/HameedS/Desktop/New folder/BizCard/images/BIZ.png')
if select == "Home":
    st.title("Welcome to BizCardX!")
    st.markdown("<h2 style='color:#f63366'>Extracting Business Card Data with OCR</h2>", unsafe_allow_html=True)
    st.markdown("""
    BizCardX is your ultimate solution for managing business card data with ease! 
    Upload business card images, extract data with OCR, and seamlessly organize your contacts.
    """)

    st.markdown("<h3 style='color:#f63366'>Key Features:</h3>", unsafe_allow_html=True)
    st.markdown("""
    - **OCR Extraction:** Extract text data from uploaded business card images.
    - **Easy Modification:** Modify extracted data before saving it to the database.
    - **Effortless Deletion:** Delete unwanted entries from the database.
    - **Seamless Management:** View and manage all saved business card data.

    BizCardX makes managing your contacts a breeze!

    """)

    st.markdown("<h3 style='color:#f63366'>Key Features:</h3>", unsafe_allow_html=True)
    st.markdown("""
    - **Streamlit:** Provides the user interface for easy interaction with the application.
    - **OCR (Optical Character Recognition):** Extracts text data from uploaded business card images.
    - **SQLite:** Database management system for storing and managing extracted business card data.
    - **Python:** Programming language used for application development.

    """)

    st.write("Ready to organize your business contacts? Please select an option from the sidebar to get started.")
elif select == "Upload and Modify":
    img = st.file_uploader("Upload the Image", type= ["png","jpg","jpeg"])
    if img is not None:
        st.image(img,width=300)

        text_img, input_img = image_to_text(img)

        text_dict =  extracted_text(text_img)

        if text_dict:
            st.success("Text data retrieved efficiently...")

        df= pd.DataFrame(text_dict)
        
        image_bytes = io.BytesIO()
        input_img.save(image_bytes, format = "PNG")

        image_data = image_bytes.getvalue()


        data = {"image":[image_data]}
        df_1  = pd.DataFrame(data)

        concat_df = pd.concat([df,df_1],axis=1)
        st.dataframe(concat_df)

        button_new = st.button("Save", use_container_width=True)

        if button_new:
            mybd = sqlite3.connect("bizcardx.db")
            cursor = mybd.cursor()

            #Table 

            create_table_query = '''Create table if not exists bizcard_details(name varchar(225),
                                                                                designation varchar(225),
                                                                                company_name varchar(225),
                                                                                contact varchar(225),
                                                                                email varchar(225),
                                                                                website text,
                                                                                address text,
                                                                                pincode varchar(225),
                                                                                image text) '''

            cursor.execute(create_table_query)
            mybd.commit()

            #insert query
            insert_query = '''insert into bizcard_details(name,designation,company_name,contact,email,website,address,pincode,image)
            values(?,?,?,?,?,?,?,?,?)'''

            datas = concat_df.values.tolist()
            cursor.executemany(insert_query, datas)
            mybd.commit()
            st.success("Data has been successfully saved to the SQL database.")
    method = st.radio("Select the appropriate method",["Please select below options (Preview OR Modify)","Preview","Modify"]) 

    if method == "Please select below options (Preview OR Modify)":
        st.write("")
    if method == "Preview":
        mybd = sqlite3.connect("bizcardx.db")
        cursor = mybd.cursor()
        select_quesry = "select * from bizcard_details" 

        cursor.execute(select_quesry)
        table  = cursor.fetchall()
        mybd.commit()

        table_df = pd.DataFrame(table,columns=("name","designation","company_name","contact","email","website","address","pincode","image"))
        st.dataframe(table_df)
    elif method == "Modify":
        mybd = sqlite3.connect("bizcardx.db")
        cursor = mybd.cursor()
        select_quesry = "select * from bizcard_details" 

        cursor.execute(select_quesry)
        table  = cursor.fetchall()
        mybd.commit()

        table_df = pd.DataFrame(table,columns=("name","designation","company_name","contact","email","website","address","pincode","image"))
        col1,col2 = st.columns(2)
        with col1:
            slected_name = st.selectbox("Please select name",table_df["name"])
        
        df_3 = table_df[table_df["name"] == slected_name]
        #st.markdown("### Original DataFrame:")
        #st.dataframe(df_3)

        df_4 = df_3.copy()
        
        col1,col2  = st.columns(2)
        with col1:
            default_name = df_3["name"].unique()[0]
            mo_name   = st.text_input("Name", df_3["name"].unique()[0])
            mo_designation   = st.text_input("Designation", df_3["designation"].unique()[0])
            mo_company_name   = st.text_input("Company Name", df_3["company_name"].unique()[0])
            mo_contact   = st.text_input("Contact", df_3["contact"].unique()[0])
            mo_email   = st.text_input("Email", df_3["email"].unique()[0])

            df_4["name"] = mo_name
            df_4["designation"] = mo_designation
            df_4["company_name"] = mo_company_name
            df_4["contact"] = mo_contact
            df_4["email"] = mo_email

        with col2:
            mo_website   = st.text_input("Website", df_3["website"].unique()[0])
            mo_address   = st.text_input("Address", df_3["address"].unique()[0])
            mo_pincode   = st.text_input("Pincode", df_3["pincode"].unique()[0])
            mo_image   = st.text_input("Image", df_3["image"].unique()[0])

            df_4["website"] = mo_website
            df_4["address"] = mo_address
            df_4["pincode"] = mo_pincode
            df_4["image"] = mo_image
        st.markdown("### After Modify DataFrame:")
        st.dataframe(df_4)

        col1,col2  = st.columns(2)
        with col1:
            button_3  = st.button("Modify", use_container_width=True)

        if button_3:
            mybd = sqlite3.connect("bizcardx.db")
            cursor = mybd.cursor()

            cursor.execute(f"delete from bizcard_details where name ='{slected_name}'")
            mybd.commit()

                        #insert query
            insert_query = '''insert into bizcard_details(name, designation, company_name, contact, email, website, address, pincode, image)
            values (?, ?, ?, ?, ?, ?, ?, ?, ?)'''

            datas = df_4.values.tolist()
            cursor.executemany(insert_query, datas)
            mybd.commit()
            st.success("Modified Data has been successfully saved to the SQL database.")

elif select ==  "Delete":
    mybd = sqlite3.connect("bizcardx.db")
    cursor = mybd.cursor()

    col1,col2  = st.columns(2)
    with col1:
        select_quesry = "select name from bizcard_details" 

        cursor.execute(select_quesry)
        table1  = cursor.fetchall()
        mybd.commit()

        names = []

        for i in table1:
            names.append(i[0])

        names_slected = st.selectbox("Select the Name",names)

    with col2:
        select_quesry = f"select designation from bizcard_details where name  = '{names_slected}' " 

        cursor.execute(select_quesry)
        table2  = cursor.fetchall()
        mybd.commit()

        designation = []

        for j in table2:
            designation.append(j[0])

        designation_slected = st.selectbox("Select the Designation",designation)

    if names_slected and designation_slected:
        col1,col2,col3 = st.columns(3)
        with col1:
            st.write(f"Selected the Name : {names_slected}")
            st.write("")
            st.write("")
            st.write("")
            st.write(f"Selected the Designation : {designation_slected}")
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            remove = st.button("Delete", use_container_width=True)

            if remove:
                cursor.execute(f"DELETE FROM bizcard_details WHERE name = '{names_slected}' AND designation = '{designation_slected}'")
                mybd.commit()

                st.warning("Deleted!!")





