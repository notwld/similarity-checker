import re
from os import system as s
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Uncomment the following two lines on the first run
# nltk.download('punkt')
# nltk.download('stopwords')

try:
    stopwords.words('english')
except LookupError:
    print("Downloading NLTK stopwords...")
    nltk.download('stopwords')

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
    text1, text2 = set(remove_redundant_words(re.sub(r'[^\w\s]', '', text1.lower())).split()), set(remove_redundant_words(re.sub(r'[^\w\s]', '', text2.lower())).split())
    intersection = text1.intersection(text2)
    union = text1.union(text2)
    jaccard_index = len(intersection) / len(union)

    return round(jaccard_index, 2) * 100


pdf1 = extract_pdf_text("1.pdf")
pdf2 = extract_pdf_text("2.pdf")
print(jaccard_similarity(pdf1, pdf2), "percent similar")
