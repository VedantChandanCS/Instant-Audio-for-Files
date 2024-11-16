import pyttsx3
import PyPDF2
import docx
from tkinter import Tk, filedialog

def extract_text(file_path):
    """Extract text from PDF, TXT, or DOCX files."""
    if file_path.endswith(".pdf"):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return "".join([page.extract_text() for page in reader.pages])
    elif file_path.endswith(".txt"):
        with open(file_path, 'r') as file:
            return file.read()
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def file_to_audio():
    # Open a file dialog to choose a file
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt"), ("Word Documents", "*.docx")])
    
    if not file_path:
        print("No file selected.")
        return

    text = extract_text(file_path)
    if text:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
        
        audio_file = file_path.rsplit(".", 1)[0] + ".mp3"
        engine.save_to_file(text, audio_file)
        engine.runAndWait()
        print(f"Audio saved as {audio_file}")
    else:
        print("No text extracted from the file.")

# Call the function
file_to_audio()
