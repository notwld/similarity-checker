import re
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_redundant_words(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower()
                      not in stopwords.words('english')]

    return ' '.join(filtered_words)


def extract_pdf_text(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(pdf.getNumPages()):
            text += pdf.getPage(page).extractText()
    return text


def jaccard_similarity(text1, text2):
    text1 = remove_redundant_words(re.sub(r'[^\w\s]', '', text1.lower()))
    text2 = remove_redundant_words(re.sub(r'[^\w\s]', '', text2.lower()))

    text1 = set(text1.split())
    text2 = set(text2.split())

    intersection = text1.intersection(text2)
    union = text1.union(text2)
    jaccard_index = len(intersection) / len(union)

    return jaccard_index

