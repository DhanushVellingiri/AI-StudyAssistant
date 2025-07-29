# 🧠 AI Study Assistant

A fully offline, AI-powered study tool that lets you upload PDF documents and ask questions about them. Powered by local LLMs (like LLaMA 3 via Ollama), semantic search (FAISS), and a clean Streamlit interface — all with no paid API keys or internet connection required.

> Built with 💡 education, 🔐 privacy, and 🏃‍♂️ speed in mind.

---

## ✨ Features

- 📄 Upload and process any PDF (lecture notes, articles, etc.)
- 🧠 Ask questions about your documents using a local AI model
- 🗂️ Embeds content using `sentence-transformers` (MiniLM)
- 🔍 Finds relevant sections via FAISS vector search
- 💬 Generates answers with LLaMA (via [Ollama](https://ollama.com))
- 🖥️ Streamlit-powered interface
- 🚫 100% offline — no OpenAI API or internet needed
- 🛠️ Modular code structure for easy upgrades

---

## 🔧 Tech Stack

| Layer         | Tools & Libraries                                      |
|---------------|--------------------------------------------------------|
| LLM Backend   | [Ollama](https://ollama.com) + LLaMA 3 / Mistral       |
| Embeddings    | `sentence-transformers` (`all-MiniLM-L6-v2`)           |
| Vector Search | FAISS                                                  |
| PDF Parsing   | PyMuPDF (`fitz`)                                       |
| UI            | Streamlit                                              |
| Language      | Python 3.10+                                           |

---

## 📁 Project Structure
```
AI-Assist/
├── app.py                  # Streamlit frontend
├── main.py                 # Core logic (PDF processing, Q&A)
├── requirements.txt        # Python dependencies
├── data/                   # Stores FAISS index (auto-created)
├── temp/                   # Uploaded PDFs (auto-created)
└── modules/
    ├── __init__.py
    ├── pdf_parser.py       # Extract text from PDFs
    ├── embedder.py         # Generate sentence embeddings
    ├── vector_store.py     # FAISS index handling
    ├── llm_interface.py    # Communicate with local LLaMA via Ollama
    └── utils.py            # Helpers (text chunking, etc.)
```

---

## 🚀 Getting Started

### 1. Clone the repo

git clone https://github.com/DhanushVellingiri/AI-StudyAssistant.git
cd AI-StudyAssistant
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Install & run Ollama
Download from: https://ollama.com

In a separate terminal:

bash
Copy
Edit
ollama run llama3
(You can also use mistral or other smaller models.)

4. Launch the app
bash
Copy
Edit
streamlit run app.py
Then open http://localhost:8501 in your browser.

📸 Screenshots
📤 Upload a PDF

💬 Ask questions

(Add your own screenshots in a docs/screenshots/ folder and update these)

💡 Future Enhancements
📚 Multi-document support

🧠 Quiz generation mode

🗣️ Voice-based Q&A using Whisper

📝 Save chat history

🌐 Deployable demo version

👨‍💻 Author
Dhanush Vellingiri
📫 LinkedIn
🌐 Portfolio (optional)

🪪 License
MIT License — feel free to fork, learn, and build on top.

⭐ If you like this project...
Give it a ⭐ on GitHub!

Share your feedback

Connect with me!
