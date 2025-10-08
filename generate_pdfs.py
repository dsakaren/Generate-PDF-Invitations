import csv
import os

os.environ['WEASYPRINT_DLL_DIRECTORIES'] = r'C:\msys64\ucrt64\bin'

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML



# Set up Jinja2 template loader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('invitation_template.html')

# Ensure output directory exists
os.makedirs('output_pdfs', exist_ok=True)

# Read CSV and generate PDFs
with open('invitations.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        html = template.render(
            name=row['name'],
            email=row['email'],
            event_date=row['event_date']
        )
        filename = f"output_pdfs/invitation_{row['name'].lower()}.pdf"
        HTML(string=html).write_pdf(filename)
        print(f"Created: {filename}")
