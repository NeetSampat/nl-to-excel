##NL2Excel – Natural Language to Excel Formula Generation

NL2Excel is a task-specific AI application that converts natural language instructions into valid Excel formulas using a fine-tuned FLAN-T5 transformer model.
The generated formulas are applied and evaluated in real time within an Excel-like web interface.

This project is developed as a Final Year Engineering Project and runs fully locally without external AI APIs.

##Features

Convert plain English instructions into Excel formulas

Supports common Excel operations:

SUM, COUNT, AVERAGE

SUMIF, COUNTIF, SUMIFS

Conditional logic (IF, logical expressions)

Real-time formula evaluation

Upload and download Excel files

Works offline (no dependency on ChatGPT or cloud APIs)

##Model Details

Base Model: FLAN-T5-small

Training Type: Supervised fine-tuning (sequence-to-sequence)

Dataset Size: 25,000+ Natural Language → Excel formula pairs

Training Epochs: 6

Output: Valid Excel-compatible formula strings

##System Architecture

Model Layer: Fine-tuned FLAN-T5 transformer for formula generation

Backend: FastAPI for model inference

Adapter Layer: Node.js bridge for frontend communication

##Workflow

1.User uploads an Excel file

2.Selects a target cell, column, or range

3.Enters a natural language instruction

4.Model generates the corresponding Excel formula

5.Formula is applied and evaluated instantly

6.User downloads the updated Excel file

##Tech Stack

AI / NLP: Python, HuggingFace, FLAN-T5

Backend: FastAPI

Frontend: HTML, JavaScript, Handsontable

Excel Processing: HyperFormula, SheetJS

Server Adapter: Node.js
Frontend: Excel-like interface using Handsontable and HyperFormula

Execution Engine: HyperFormula for real-time Excel evaluation
