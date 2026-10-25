# SlothDesk
🦥 SlothDesk Desktop Cleaner
Clean your messy folders with 100% offline, open-source AI.

SlothDesk is a local-first file organizer built with Python, Streamlit, and Ollama. It reads a short preview of each file, uses a local LLM to decide where it belongs, and suggests a clear filename. Nothing is uploaded anywhere, and nothing moves until you approve it.

Features
Offline and private: runs on your machine through Ollama. No cloud APIs.
Content-aware: reads the first 600 characters of .pdf, .txt, .md, .csv, .json, and .py files instead of guessing from the extension.
Reliable output: Pydantic schemas keep the model's answers clean and valid.
Dry run first: preview every proposed move, new filename, and the AI's reasoning before anything changes.
Categories
Files are sorted into one of seven folders:

Category	Examples
Invoices & Receipts	bills, receipts, payment confirmations
Work & Documents	reports, notes, letters
Code & Dev	scripts, source files, project data
Personal & Identity	IDs, certificates, resumes
Media & Assets	images, audio, video
Archives & Installers	zip files, installers
Miscellaneous	everything else
Tech Stack
UI: Streamlit
Local AI: Ollama (qwen2.5:3b or llama3.2:3b)
Validation: Pydantic
PDF parsing: pypdf
Getting Started
Requirements: Python 3.10+, Git, and Ollama.

1. Clone the repository

git clone https://github.com/DeependraGurjar/SlothDesk.git
cd SlothDesk
2. Install dependencies

pip install -r requirements.txt
3. Pull a model

Make sure Ollama is running, then:

ollama pull qwen2.5:3b
4. Run the app

streamlit run app.py
The app opens in your browser at http://localhost:8501.

Usage Tips
Always review the dry-run table before applying changes.
Test on a small folder first.
Small models can make mistakes, so skip any suggestion that looks wrong.
Scanned PDFs have no readable text and will usually land in Miscellaneous.
Contributing
Contributions are welcome, including for Hacktoberfest.

Fork the repo
Create a branch: git checkout -b feature/your-feature
Commit your changes: git commit -m "Add your feature"
Push: git push origin feature/your-feature
Open a Pull Request
Ideas to work on:

Support for .docx, .xlsx, and images
Undo option for applied moves
Custom user-defined categories
Model selector in the UI
Duplicate file detection
