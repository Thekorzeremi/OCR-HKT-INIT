from faker import Faker
from fpdf import FPDF
import os

fake = Faker()


def wipe_generated_docs():
    folder_path = "./generated_docs/"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Suppression: {file_path}")
        except Exception as e:
            print(f"Erreur lors de la suppression de {file_path}: {e}")

def generate_documents():
    for _ in range(10):
        count = _ + 1
        name = fake.name()
        today = fake.date()  

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('helvetica', size=12)
        pdf.cell(text=name)
        pdf.ln()
        pdf.cell(text=today)
        pdf.output("./generated_docs/" + str(count) + "doc_.pdf")

        print(f"Document {count} généré : {name}, {today}")

if __name__ == "__main__":
    wipe_generated_docs()
    generate_documents()