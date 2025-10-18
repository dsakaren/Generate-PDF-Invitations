import csv
import os

os.environ['WEASYPRINT_DLL_DIRECTORIES'] = r'C:\msys64\ucrt64\bin'

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('invitation_template.html')

os.makedirs('output_pdfs', exist_ok=True)

with open('invitations.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        html = template.render(name=row['name'])
        filename = f"output_pdfs/invitation_{row['name'].lower()}.pdf"
        HTML(string=html, base_url='.').write_pdf(filename)
        print(f"Created: {filename}")

