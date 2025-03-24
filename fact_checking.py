from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, pipeline
import torch

# Load the optimized spam detection model
model_name = "AventIQ-AI/distilbert-spam-detection"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def detect_spam(text: str) -> dict:
    """
    Detects whether a given text is spam or not.
    """
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

# Load Hugging Face's pre-trained fact-checking model
fact_checker = pipeline("text-classification", model="fractalego/fact-checking")

label_mapping = {
    "LABEL_0": "REFUTES",
    "LABEL_1": "SUPPORTS"
}

def verify_fact(claim, evidence):
    input_text = f"Claim: {claim} Evidence: {evidence}"
    result = fact_checker(input_text)[0]
    label = label_mapping.get(result["label"], "UNKNOWN")  # Map labels correctly
    return {
        "label": label,
        "confidence": round(result["score"] * 100, 2)
    }



if __name__ == "__main__":
    print("\n1️⃣ Spam Detection")
    text_input = input("Enter a message to check for spam: ")
    spam_result = detect_spam(text_input)
    print(f"Spam Prediction: {spam_result['label']} (Confidence: {spam_result['confidence']})")

    print("\n2️⃣ Fact Checking")
    claim = input("Enter a claim to verify: ")
    evidence = input("Enter evidence for verification: ")
    fact_result = verify_fact(claim, evidence)
    print(f"Fact-Check Result: {fact_result['label']} (Confidence: {fact_result['confidence']}%)")
