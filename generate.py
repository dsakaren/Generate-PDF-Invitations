import os
os.environ['WEASYPRINT_DLL_DIRECTORIES'] = r'C:\msys64\ucrt64\bin'

from weasyprint import HTML

HTML('index.html').write_pdf('output.pdf')
print("PDF created successfully.")