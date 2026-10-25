# 🦥 SlothDesk: The "Slow and Steady" Offline File Organizer

> Channel your inner sloth. Let local open-source AI clean your chaotic Downloads folder so you don't have to.

[![Built with Ollama](https://img.shields.io/badge/Powered%20by-Ollama-blue.svg)](https://ollama.com)
[![Framework](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![Privacy](https://img.shields.io/badge/Data%20Privacy-100%25%20Local-green.svg)](#why-open-source-matters)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Overview

**SlothDesk** is an automated desktop tidy-up agent built for the **"Slow and Steady"** open-source AI hackathon. 

Instead of spending hours manually dragging invoices, receipts, code snippets, and installers into designated folders, SlothDesk inspects your chaotic directories, understands the contents, renames files cleanly, and proposes a tidy reorganization plan—all running completely on your local machine.

---

## 🌟 Why Open Source Matters (The Core Philosophy)

Closed-source cloud APIs make privacy impossible for desktop automation. A file organizer needs to touch bank statements, tax documents, ID copies, and proprietary code files. Sending those files across the wire to a remote cloud server is a major security and privacy compromise.

SlothDesk solves this through open innovation:

* **100% Local & Confidential:** Using **Ollama** and open-weight models (`llama3.2:3b`, `llama3.2:1b`, or `qwen2.5:0.5b`), zero bytes of personal data ever leave your machine.
* **$0 Operational Cost:** No recurring token bills or rate limits. Run it on thousands of files completely free.
* **Off-Grid Capable:** Operates with no internet connection on a flight, train, or remote workspace.
* **Model Flexibility:** Swap freely between ultra-fast edge models (`llama3.2:1b`) and complex reasoning models without touching the core application logic.

---

## ✨ Features

- **Hybrid Classification Engine:** Instant 0ms sorting for obvious system files (`.exe`, `.zip`, `.png`) combined with local LLM reasoning for ambiguous text and PDF documents.
- **Dry-Run Safety Mode:** Inspect the proposed file moves, clean new names, and AI explanations in an interactive table before executing any disk operations.
- **Pydantic Structured Outputs:** Leverages Ollama's native JSON schema enforcement to ensure predictable, error-free categorization.
- **Batch Throttle Control:** Process loose files in manageable batches (5–50 at a time) to prevent CPU/memory bottlenecks.

---

## 🛠️ Tech Stack

- **Model Engine:** [Ollama](https://ollama.com) (Running `llama3.2:1b` / `llama3.2:3b`)
- **Dashboard UI:** [Streamlit](https://streamlit.io)
- **Document Ingestion:** `pypdf` (local PDF text extraction)
- **Data Validation:** `pydantic`
- **Language:** Python 3.10+

---

## 🚀 Quickstart Guide

### 1. Prerequisites

1. Install [Ollama](https://ollama.com/download) for your operating system.
2. Pull a lightweight model via terminal:
   ```bash
   ollama run llama3.2:1b
### 2. Clone and Setup
   git clone (https://github.com/Richs03/SlothDesk)
cd SlothDesk

### 3. Install Dependencies
     pip install -r requirements.txt

### 4. Run the Application
     streamlit run app.py
