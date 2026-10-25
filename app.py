import os
import shutil
from pathlib import Path
import streamlit as st
import ollama
from pydantic import BaseModel
from pypdf import PdfReader

# 1. Define structured output schema for Ollama
class FileCategorization(BaseModel):
    category: str
    suggested_filename: str
    reason: str

# Helper: Fetch locally installed Ollama models
def get_installed_models() -> list[str]:
    try:
        models_info = ollama.list()
        models = [m.model for m in models_info.models]
        return models if models else ["qwen2.5:3b"]
    except Exception:
        return ["qwen2.5:3b"]

# 2. Extract sample text safely
def get_file_preview(file_path: Path, max_chars: int = 600) -> str:
    ext = file_path.suffix.lower()
    try:
        if ext in ['.txt', '.md', '.csv', '.json', '.py']:
            with open(file_path, 'r', errors='ignore') as f:
                return f.read(max_chars)
        elif ext == '.pdf':
            reader = PdfReader(str(file_path))
            if reader.pages:
                return reader.pages[0].extract_text()[:max_chars]
    except Exception:
        pass
    return "No text preview available."

# 3. Categorize using local Ollama model
def analyze_file_with_ollama(file_name: str, snippet: str, model: str = "qwen2.5:3b") -> FileCategorization:
    prompt = f"""
    Analyze this file from a messy folder and decide how to organize it.
    
    File Name: {file_name}
    Snippet / Content Sample: {snippet}

    Choose one standard category:
    - Invoices & Receipts
    - Work & Documents
    - Code & Dev
    - Personal & Identity
    - Media & Assets
    - Archives & Installers
    - Miscellaneous

    Also provide a clean, descriptive file name that keeps the original extension.
    """
    
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        format=FileCategorization.model_json_schema(),
        options={"temperature": 0.1}
    )
    return FileCategorization.model_validate_json(response.message.content)

# 4. Streamlit Dashboard
st.set_page_config(page_title="SlothDesk Cleaner", page_icon="🦥", layout="wide")
st.title("🦥 SlothDesk Desktop Cleaner")
st.caption("Channel your inner sloth: clean local files with 100% offline open AI.")

installed_models = get_installed_models()
default_idx = installed_models.index("qwen2.5:3b") if "qwen2.5:3b" in installed_models else 0

with st.sidebar:
    st.header("Settings")
    folder_path = st.text_input("Folder to clean", value=str(Path.home() / "Downloads"))
    model_name = st.selectbox("Ollama Model", options=installed_models, index=default_idx)
    max_files = st.slider("Max files to scan (for faster testing)", min_value=5, max_value=200, value=20)
    dry_run = st.checkbox("Dry Run (Preview only, don't move files)", value=True)

target_dir = Path(folder_path)

if st.button("Scan & Plan Clean-Up", type="primary"):
    if not target_dir.exists():
        st.error(f"Path does not exist: {target_dir}")
    else:
        all_files = [f for f in target_dir.iterdir() if f.is_file() and not f.name.startswith('.')]
        files = all_files[:max_files]
        
        if not files:
            st.info("No loose files found in this directory!")
        else:
            st.write(f"Scanning **{len(files)}** (out of {len(all_files)}) files. Analyzing with `{model_name}`...")
            progress_bar = st.progress(0)
            
            plan = []
            try:
                for idx, file in enumerate(files):
                    snippet = get_file_preview(file)
                    result = analyze_file_with_ollama(file.name, snippet, model=model_name)
                    
                    plan.append({
                        "original_path": file,
                        "original_name": file.name,
                        "category": result.category,
                        "new_name": result.suggested_filename,
                        "reason": result.reason
                    })
                    progress_bar.progress((idx + 1) / len(files))
                    
                st.session_state["cleanup_plan"] = plan
                st.success("Analysis complete!")
            except ollama.ResponseError as e:
                st.error(f"Ollama Error: {e.error}. Run `ollama pull {model_name}` in your terminal first.")

if "cleanup_plan" in st.session_state and st.session_state["cleanup_plan"]:
    plan = st.session_state["cleanup_plan"]
    
    st.subheader("Proposed Organization Plan")
    table_data = [
        {"File": item["original_name"], "Category": item["category"], "New Name": item["new_name"], "Reason": item["reason"]}
        for item in plan
    ]
    st.dataframe(table_data, use_container_width=True)
    
    if st.button("Execute Reorganization"):
        moved_count = 0
        for item in plan:
            orig = item["original_path"]
            dest_folder = target_dir / item["category"]
            dest_file = dest_folder / item["new_name"]
            
            if not dry_run:
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(orig), str(dest_file))
            moved_count += 1
            
        if dry_run:
            st.warning(f"Dry run enabled: simulated moving {moved_count} files.")
        else:
            st.success(f"Successfully organized {moved_count} files into clean subdirectories!")
            del st.session_state["cleanup_plan"]