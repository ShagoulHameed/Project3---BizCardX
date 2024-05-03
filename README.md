# BizCardX: Extracting Business Card Data with OCR

BizCardX is a Streamlit application for extracting business card data using Optical Character Recognition (OCR). It allows users to upload an image of a business card, extract relevant information, and manage the extracted data easily.

## Technologies Used

- Streamlit
- EasyOCR
- Python
- SQLite
- Pandas
- NumPy
- PIL (Python Imaging Library)

## Features

- **OCR Extraction:** Extract text data from uploaded business card images.
- **Preview and Modify:** Preview extracted data and make modifications before saving it to the database.
- **Save Data:** Save extracted data to a SQLite database for easy management.
- **User-Friendly Interface:** Easy-to-use interface with sidebar navigation.

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/your_username/your_repository.git


2. Install the required dependencies:

pip install -r requirements.txt


## Usage

1. Run the Streamlit application:

streamlit run app.py


2. Use the sidebar menu to select the desired operation:
   # Home

Upon launching the application, users are greeted with a welcome message and an overview of the features. They can select an option from the sidebar menu to proceed.

![image](https://github.com/ShagoulHameed/Project3---BizCardX/assets/154894802/1390b0ce-15dd-4292-8267-5fd7fe655779)


# Upload and Modify

Users can upload business card images, extract data using OCR, and modify the extracted information before saving it to the database.

![image](https://github.com/ShagoulHameed/Project3---BizCardX/assets/154894802/9bd34517-585a-405a-a1c7-def395709ce1)


# Preview

Users can preview the existing entries in the database, providing an overview of all saved business card data.

![image](https://github.com/ShagoulHameed/Project3---BizCardX/assets/154894802/4324e055-6f26-48b6-9ce6-0bdb0e6e263b)


# Modify

Users can select a specific entry from the database, modify its details, and save the changes.

![image](https://github.com/ShagoulHameed/Project3---BizCardX/assets/154894802/bcc0456d-bce0-4298-a7b2-a133a901bbcb)

![image](https://github.com/ShagoulHameed/Project3---BizCardX/assets/154894802/cda050fc-639a-431c-946b-19bf9b9a6450)


# Delete

Users can delete unwanted entries from the database by selecting the name and designation of the entry to be deleted.

![image](https://github.com/ShagoulHameed/Project3---BizCardX/assets/154894802/dad274d1-dbcc-4563-a2f7-d78cdccb2526)



## Directory Structure

project_directory/
│
├── app.py
├── bizcardx.db
├── README.md
├── requirements.txt
└── images/
└── BIZ.jpg


## Project Demo Video
https://www.linkedin.com/posts/shagoul-hameed_python-ocr-sqllite-activity-7192251011258802179-8QDE?utm_source=share&utm_medium=member_desktop
![1spage](https://github.com/ShagoulHameed/Project3---BizCardX/assets/154894802/640d2d18-de28-40bd-bc70-374f5e1d26e7)




