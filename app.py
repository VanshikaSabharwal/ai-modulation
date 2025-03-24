import gradio as gr
from spam_filtering import detect_spam
from fact_checking import verify_fact

# Define the Gradio interface for spam detection
def spam_interface(text):
    result = detect_spam(text)
    return f"Label: {result['label']} (Confidence: {result['confidence']}%)"

# Define the Gradio interface for fact-checking
def fact_interface(claim, evidence):
    result = verify_fact(claim, evidence)
    return f"Label: {result['label']} (Confidence: {result['confidence']}%)"

# Create the Gradio app with two tabs: Spam Filtering and Fact Checking
with gr.Blocks(title="AI Content Moderation Suite") as app:
    gr.Markdown("# AI Content Moderation Toolkit")
    
    with gr.Tab("Spam Detection"):
        with gr.Row():
            spam_input = gr.Textbox(label="Input Text", placeholder="Enter text to analyze...")
            spam_output = gr.Textbox(label="Spam Analysis Result")
        spam_button = gr.Button("Analyze")
        spam_button.click(spam_interface, inputs=spam_input, outputs=spam_output)
    
    with gr.Tab("Fact Checking"):
        gr.Markdown("### Verify if a claim is true or false.")
        claim_input = gr.Textbox(label="Claim", placeholder="Enter a claim...")
        evidence_input = gr.Textbox(label="Evidence", placeholder="Enter supporting evidence...")
        fact_output = gr.Textbox(label="Fact Check Result", interactive=False)
        fact_button = gr.Button("Verify")
        fact_button.click(fact_interface, inputs=[claim_input, evidence_input], outputs=fact_output)

if __name__ == "__main__":
    app.launch()
