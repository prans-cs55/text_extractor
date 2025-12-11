from PIL import Image
import pytesseract
import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_and_summarize(image):
    if image is None:
        return "Please upload an image.", "No summary yet."

    extracted_text = pytesseract.image_to_string(image).strip()
    if not extracted_text:
        return "No text detected in the image.", ""

    if len(extracted_text.split()) > 30:
        summary = summarizer(
            extracted_text,
            max_length=100,
            min_length=30,
            do_sample=False
        )[0]['summary_text']
    else:
        summary = "Text too short for summarization."

    return extracted_text, summary


interface = gr.Interface(
    fn=extract_and_summarize,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=[
        gr.Textbox(label="Extracted Text",scale=5),
        gr.Textbox(label="Summary",scale=5),
    ],
    title="🧠 OCR Text Extractor + Summarizer",
    description="Upload an image with text — it extracts the text using Tesseract OCR and summarizes it using a transformer model."
)

interface.launch()
