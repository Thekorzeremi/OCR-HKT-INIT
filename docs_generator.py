from faker import Faker
from fpdf import FPDF
from datetime import datetime

fake = Faker()

for _ in range(10):
    count = _ + 1
    name = fake.name()
    today = fake.date()  
    datetime_object = datetime.strptime(today, '%Y-%m-%d')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    pdf.cell(text=name)
    pdf.ln()
    pdf.cell(text=today)
    pdf.output("./generated_docs/" + datetime_object.strftime('%Y-%m-%d') + "_doc_.pdf")