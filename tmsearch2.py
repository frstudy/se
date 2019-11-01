#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2 as PDF #import pdf module 
import re

p = PDF.PdfFileReader("C:\\Users\\frank\\Downloads\\result.pdf")

# get number of pages
NumPages = p.getNumPages()

#define keyterms; David, Final, End, Score, Birthday, Hello Ben

kTerm = "SWELINEX|BSC|Entor|MOBACH|FEVICOL"

#extract text and do the search
for i in range(0, NumPages):
    PageObj = p.getPage(i)
    print("Looking through page " + str(i))
    Text = PageObj.extractText()
    Result = re.search(kTerm,Text)

    if Result:
         print(f"{kTerm} found")
    else:
         print("0")


# In[ ]:




