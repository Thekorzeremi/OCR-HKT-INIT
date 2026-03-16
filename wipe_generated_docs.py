import os

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

if __name__ == "__main__":
    wipe_generated_docs()