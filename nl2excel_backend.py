from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import uvicorn

MODEL_PATH = r"D:\vscode_codes\Workingone\testmodel\nl2excel_t5_small_new"
BASE = "google/flan-t5-small"

print("Loading tokenizer (base)...")
tokenizer = T5Tokenizer.from_pretrained(BASE)

print("Loading fine-tuned model (custom weights)...")
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
model.eval()

app = FastAPI()

class Query(BaseModel):
    query: str


def predict_formula(text: str) -> str:
    prefix = "excel formula: "
    inputs = tokenizer(prefix + text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=64,
            num_beams=4,
            early_stopping=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


@app.post("/generateFormula")
def generate_formula(data: Query):
    formula = predict_formula(data.query)
    return {"formula": formula}


@app.get("/")
def root():
    return {"status": "T5 Excel server running!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
