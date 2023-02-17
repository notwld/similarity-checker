import re
from os import system as s
try:
    from PyPDF2 import PdfReader
    import nltk

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

except ImportError as e:
    print("Modules are not installed!\nInstalling modules...")
    s("pip install nltk")
    s("pip install PyPDF2")

s("cls")

def remove_redundant_words(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower()
                      not in stopwords.words('english')]

    return ' '.join(filtered_words)


def extract_pdf_text(pdf_file):
    
    with open(pdf_file, 'rb') as file:
        pdf = PdfReader(file)
        number_of_pages = len(pdf.pages)
        text = ''
        for page in range(number_of_pages):
            text += pdf.pages[page].extract_text()

    return text


def jaccard_similarity(text1, text2):
    text1,text2  = set(remove_redundant_words(re.sub(r'[^\w\s]', '', text1.lower())).split()),set(remove_redundant_words(re.sub(r'[^\w\s]', '', text2.lower())).split())
    intersection = text1.intersection(text2)
    union = text1.union(text2)
    jaccard_index = len(intersection) / len(union)

    return round(jaccard_index, 2)*100

pdf1,pdf2 = extract_pdf_text("1.pdf"),extract_pdf_text("2.pdf")
print(jaccard_similarity(pdf1,pdf2))