import PyPDF2
import os
import pandas as pd

def getResumeDetails(output_directory):
    text = ""
    with open(output_directory, 'rb') as resume_file:
        pdf_reader = PyPDF2.PdfReader(resume_file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  
    return text
def getFolder(output_directory):
    texts=[]
    filenames=[]
    for filename in os.listdir(output_directory):
        if filename.endswith(".pdf"):
            path=os.path.join(output_directory,filename)
            text=getResumeDetails(path)
            texts.append(text)
            filenames.append(filename)
    return pd.DataFrame({
        'filename': filenames,
        'text': texts
    })

if __name__=="__main__":
    Folder='C:\\Users\\LENOVO\\Desktop\\resumes\\resume_files'
    data=getFolder(Folder)
    print(data)