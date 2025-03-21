

import fitz  # PyMuPDF for PDF text extraction
import os
from elevenlabs import ElevenLabs

# 🔹 Replace with your actual ElevenLabs API Key
API_KEY = "sk_04b7085ee1fb59ce5303f8a10a4abed17fad516ef42e8cbb"

# 🔹 Initialize ElevenLabs Client
client = ElevenLabs(api_key=API_KEY)

# 🔹 Directory paths
PDF_FOLDER = "pdfs"
OUTPUT_FOLDER = "output"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 🔹 Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text") + "\n"
    return text.strip()

# 🔹 Function to convert text to speech using ElevenLabs
def text_to_speech(text, output_file="output/audiobook.mp3"):
    try:
        # Convert text to speech using ElevenLabs API
        audio_stream = client.text_to_speech.convert(
            text=text,
            voice_id="pNInz6obpgDQGcFmaJgB",  # Replace with your chosen voice ID
            model_id="eleven_multilingual_v2"
        )

        # ✅ Correct way to write the audio stream to a file
        with open(output_file, "wb") as f:
            for chunk in audio_stream:  # Iterate over the generator
                f.write(chunk)

        print(f"✅ Audio saved as {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")



# 🔹 Main Function
def main():
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in the 'pdfs/' folder!")
        return

    print("📖 Available PDFs:")
    for idx, pdf in enumerate(pdf_files, 1):
        print(f"{idx}. {pdf}")

    while True:  # Keep asking until valid input is given
        choice = input("Enter the number of the PDF to convert: ").strip()

        if not choice.isdigit():
            print("⚠️ Please enter a valid number!")
            continue

        choice = int(choice) - 1

        if 0 <= choice < len(pdf_files):
            break
        else:
            print("⚠️ Invalid choice! Please enter a number from the list.")

    pdf_path = os.path.join(PDF_FOLDER, pdf_files[choice])
    print(f"📂 Processing: {pdf_path}")

    text = extract_text_from_pdf(pdf_path)

    if text:
        print("✅ Text extracted successfully!")
        output_audio_path = os.path.join(OUTPUT_FOLDER, f"{pdf_files[choice].replace('.pdf', '.mp3')}")
        text_to_speech(text, output_audio_path)
    else:
        print("⚠️ No text found in the PDF!")


# 🔹 Run the script
if __name__ == "__main__":
    main()
