# CaseFile AI – Mystery Evidence Analyzer

## Project Overview

CaseFile AI is a beginner-friendly AI application that analyzes mystery evidence images.

The application takes an evidence image as input and processes it through:

**Image → OCR → Embedding → Attention → Clue Detection → Investigation Result**

It extracts text from the uploaded image, converts the extracted words into numerical representations, calculates attention scores, and identifies important clue words.

---

# Demo Link :

https://mysteryevidenceanalyzer-9xxxthfpz4b8pyfqr4fxen.streamlit.app/

---

## Objectives

- To extract text from mystery evidence images using OCR.
- To convert extracted words into numerical embeddings.
- To apply an attention mechanism to identify important words.
- To detect possible mystery-related clues.
- To display the investigation result using a simple web interface.

---

## Technologies Used

- Python
- Streamlit
- Tesseract OCR
- Pytesseract
- NumPy
- Pillow
- Regular Expressions

---

## AI Concepts Used

### 1. OCR

OCR stands for **Optical Character Recognition**.

It is used to read text from an uploaded evidence image.

### 2. Embedding

The extracted words are converted into numerical representations.

These numerical values are used for further mathematical processing.

### 3. Attention Mechanism

The attention mechanism calculates the importance of words.

Important words can receive higher attention and can be considered possible clues.

---

## Project Workflow

```text
Upload Evidence Image
        ↓
      OCR
        ↓
 Extract Text
        ↓
 Clean Words
        ↓
    Embedding
        ↓
 Numerical Representation
        ↓
 Attention Mechanism
        ↓
 Calculate Word Importance
        ↓
 Detect Mystery Clues
        ↓
 Investigation Result
```

---

## Project Structure

```text
Mystery Investigation/
│
├── app.py
├── ocr.py
├── embedding.py
├── attention.py
├── requirements.txt
├── packages.txt
└── README.md
```

---

# Work Pictures :

<img width="1471" height="885" alt="image" src="https://github.com/user-attachments/assets/a80027c5-50d8-43ae-a1b9-ae24098924df" />

<img width="1447" height="777" alt="image" src="https://github.com/user-attachments/assets/0dc6f7e9-d5fa-49cc-a91a-0061cd3db4eb" />

<img width="1396" height="737" alt="image" src="https://github.com/user-attachments/assets/63da4fb7-0a69-4ec4-9ab4-8d29b88d11bf" />

<img width="1371" height="857" alt="image" src="https://github.com/user-attachments/assets/b4c77c23-6319-4082-9b53-b067b231e44e" />

<img width="1496" height="862" alt="image" src="https://github.com/user-attachments/assets/a2b85aa6-a58c-4cc6-bd25-287cb69efba3" />

---

## File Description

### app.py

The main Streamlit application.

It handles:

- Evidence image upload
- Image display
- OCR processing
- Word cleaning
- Embedding creation
- Attention calculation
- Clue detection
- Investigation result

### ocr.py

This file performs **Optical Character Recognition** and extracts text from the evidence image using Pytesseract and Tesseract OCR.

### embedding.py

This file converts extracted words into simple numerical representations using NumPy.

### attention.py

This file implements the attention mechanism and calculates word importance.

### requirements.txt

Contains the Python packages required to run the application.

### packages.txt

Contains the Linux system package required by Streamlit Cloud for Tesseract OCR.

---

## Installation

Install the required Python packages:

```bash
py -m pip install streamlit pillow numpy pytesseract
```

Tesseract OCR must also be installed on the local system.

For Streamlit Cloud deployment, the `packages.txt` file contains:

```text
tesseract-ocr
```

---

## How to Run

Open the project folder in VS Code.

Open the PowerShell terminal and run:

```bash
py -m streamlit run app.py
```

The application will open in the browser.

---

## How to Use

1. Open the CaseFile AI application.
2. Click **Upload Evidence**.
3. Upload a JPG, JPEG, or PNG evidence image.
4. OCR extracts the text from the image.
5. The extracted words are converted into embeddings.
6. The attention mechanism identifies important words.
7. Possible mystery clues are displayed.
8. The strongest clue is shown in the Investigation Result section.

---

## User Interface

The application contains three main sections.

### Evidence

Shows the text extracted from the uploaded evidence image.

It also checks for dates and times in the evidence.

### Clue Board

The system searches for mystery-related clue words such as:

```text
missing
suspect
secret
footprint
phone
message
letter
key
door
witness
evidence
unknown
building
```

### AI Insight

Shows the words identified as important by the attention mechanism.

---

## Example

### Input Evidence

```text
A footprint was found near the door.
The witness reported a missing phone.
```

### Processing

```text
Evidence Image
      ↓
      OCR
      ↓
Extracted Words
      ↓
   Embedding
      ↓
   Attention
      ↓
Important Clues
      ↓
Investigation Result
```

### Possible Clues

```text
Footprint
Door
Witness
Missing
Phone
```

---

## Features

- Evidence image upload
- OCR-based text extraction
- Text cleaning
- Word embeddings
- Attention mechanism
- Mystery clue detection
- Date and time extraction
- Simple Streamlit interface
- Beginner-friendly implementation
- Streamlit Cloud deployment support

---

## Advantages

- Easy to use
- Simple interface
- Combines OCR, Embedding, and Attention
- Works with image-based evidence
- Helps identify possible important clues
- Suitable for learning basic AI concepts
- Demonstrates an AI-based investigation workflow

---

## Limitations

- OCR accuracy depends on image quality.
- Clue detection uses a predefined list of clue words.
- The attention mechanism is a simplified implementation.
- The application does not solve a complete real-world crime case.
- Results should be treated as possible clues, not as actual forensic conclusions.

---

## Future Enhancements

- Improve OCR preprocessing.
- Add advanced language embeddings.
- Detect names and locations automatically.
- Generate an investigation timeline.
- Generate a complete investigation report.
- Add a mystery case database.
- Improve AI-based reasoning.
- Add multiple evidence image analysis.
- Add relationship detection between clues.
- Generate an AI-generated case summary.

---

## Conclusion

CaseFile AI combines OCR, embeddings, and an attention mechanism to analyze mystery evidence images.

The application extracts text from an image, converts words into numerical representations, identifies important words, and displays possible clues through a simple Streamlit interface.

This project provides a beginner-friendly example of applying AI concepts to a mystery investigation scenario.

---


## Project Keywords

```text
Artificial Intelligence
OCR
Optical Character Recognition
Embeddings
Attention Mechanism
Natural Language Processing
Python
Streamlit
Tesseract OCR
Mystery Investigation
Clue Detection
AI Project
```
