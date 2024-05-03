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
   - **Home**: Overview and introduction to the application.
   - **Upload and Modify**: Upload business card images, preview extracted data, and make modifications.
   - **Delete**: Delete unwanted entries from the database.

## Directory Structure

project_directory/
│
├── app.py
├── bizcardx.db
├── README.md
├── requirements.txt
└── images/
└── BIZ.jpg


## Screenshots

[Insert screenshots or GIFs of the application here]


