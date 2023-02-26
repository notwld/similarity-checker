# PDF Similarity Checker
This Python script is designed to compare the text content of two PDF files and determine their similarity using the Jaccard index.

# Requirements
* Python 3.6 or higher
* PyPDF2
* NLTK

# Usage
1. Place the two PDF files that you want to compare in the same directory as the Python script.
2. Name the PDFs as `1.pdf` and `2.pds`
3. Open a terminal window and navigate to the directory containing the script and PDF files.
4. Run the script using the following command: `python pdf_similarity_checker.py`
5. The script will output the Jaccard similarity index as a percentage.

# Notes
* The script removes stop words and non-alphanumeric characters from the PDF text before performing the similarity check.
* The script assumes that the text content of the PDF files is in English.
* The script does not take into account formatting, layout, or images in the PDF files.
* This script is for educational and personal use only and should not be used to compare copyrighted material without permission.

# References
[PyPDF2 documentation](https://pythonhosted.org/PyPDF2/)

[NLTK documentation](https://www.nltk.org/)

[Jaccard similarity index](https://en.wikipedia.org/wiki/Jaccard_index)



