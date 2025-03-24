from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

# Load the optimized spam detection model [1]
model_name = "AventIQ-AI/distilbert-spam-detection"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def detect_spam(text: str) -> dict:
    inputs = tokenizer(text, 
                      return_tensors="pt", 
                      padding="max_length",
                      truncation=True, 
                      max_length=128).to(device)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    probs = torch.softmax(outputs.logits, dim=-1)
    confidence = torch.max(probs).item()
    label = "SPAM" if torch.argmax(probs).item() == 1 else "NOT SPAM"
    
    return {
        "label": label,
        "confidence": round(confidence, 4)
    }
