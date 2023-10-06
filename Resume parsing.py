#!/usr/bin/env python
# coding: utf-8

# In[11]:


import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
nlp=spacy.load("en_core_web_sm")
import PyPDF2
file=open("C://oyyyy//RESUMESSS//vinay's Resume.pdf","rb")
pdfReader=PyPDF2.PdfReader(file)
print(len(pdfReader.pages))
pageobj=pdfReader.pages[0]
data=pageobj.extract_text()
data
doc=nlp(data)
terms=["pyhton","java","Data Scientist","Machine learning","statistics","NLP","Deep learning","Tableau","Data preprocessing","sql","pytorch","tensorflow","Scikit_learn"]
pattern=[nlp(term) for term in terms]
matcher=PhraseMatcher(nlp.vocab)
matcher.add("programming",None,*pattern)
matches=matcher(doc)
for match_id,start,end in matches:
    matched_term=doc[start:end]
    print(matched_term)


# In[ ]:




