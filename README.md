**Instant Audio for Files 🎧📚**

Instant Audio for Files is a simple and powerful tool that converts text from PDF, TXT, and Word documents into high-quality, downloadable audio files. This project leverages Python's text-to-speech capabilities to read aloud any text-based document and convert it into an MP3 file, making it perfect for audiobooks, study materials, and accessibility purposes. 📖🔊

**Features ✨**

🔄 Convert PDF, TXT, and Word (DOCX) files into speech.

📥 Download the generated audio as an MP3 file.

🖱️ Easy-to-use file dialog for selecting documents.

🎤 Customizable speech rate and volume.

📄 Supports multiple document formats for a seamless experience.

**Installation 🛠️**

Clone the repository:git clone https://github.com/your-username/Instant-Audio-for-Files.git

Install the required libraries: pip install pyttsx3 PyPDF2 python-docx tkinter

**Usage 🚀**

Run the audio_converter.py script: python audio_converter.py

A file dialog will appear. Select a PDF, TXT, or Word (DOCX) file that you want to convert to audio.

Once the document is selected, the text will be extracted and converted into speech.

The generated audio file will be saved in the same directory as the document, with the .mp3 extension.

**How It Works 🧑‍💻**

PDF Files 📑: The text is extracted using the PyPDF2 library, which reads the content from each page of the PDF.

TXT Files 📝: The content is directly read from the text file.

Word Documents 📄: The python-docx library extracts the text from each paragraph in the Word document.

After extracting the text, the pyttsx3 library is used to convert the text to speech and save it as an MP3 file.


**Example 🎥**

Once the file is selected and converted, you will see an output like this:

engine.setProperty('rate', 150)  # Speed of speech (default: 200)

engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

**Customization ⚙️**

You can modify the speech rate and volume by adjusting the properties of the pyttsx3 engine in the code:

engine.setProperty('rate', 150)  # Speed of speech (default: 200)

engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

**Contributing 🤝**

If you'd like to contribute to the project, feel free to fork the repository, create a new branch, and submit a pull request. 

All contributions are welcome! 🚀


