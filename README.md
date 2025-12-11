# text_extractor
🧠 OCR Text Extractor + Summarizer

An AI-powered tool that extracts text from images using Tesseract OCR and then summarizes it using a transformer model. Upload any image (screenshots, photos, scanned documents, notes) → Get clean extracted text + an AI summary.

🚀 Features

📤 Upload an image with text

🔎 Extracts text using Tesseract OCR

✨ Summarizes extracted text using HuggingFace transformers

⚡ Fast, simple Gradio UI

🛠️ Works on CPU — no GPU required

🧩 How it Works

Image is processed with Tesseract OCR

Extracted text is cleaned

Text is fed into a pretrained summarization model

Output summary is displayed instantly

🗂️ Project Structure ├── app.py ├── requirements.txt ├── packages.txt └── README.md

📦 Dependencies Python packages (requirements.txt) gradio pillow pytesseract transformers torch tesseract

System packages (packages.txt) tesseract-ocr tesseract-ocr-eng

These ensure Tesseract OCR runs correctly on HuggingFace Spaces.

▶️ Running Locally pip install -r requirements.txt python app.py

📸 Demo

Just upload an image → click Submit → done!
![Uploading image.png…]()

🙌 Acknowledgements

Tesseract OCR

HuggingFace Transformers

Gradio for UI

🔗 Try the live Space

👉https://huggingface.co/spaces/prans-cs55/text_extractor
