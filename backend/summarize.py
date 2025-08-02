from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str) -> str:
    # HuggingFace recommends keeping inputs under 1024 tokens for this model
    if len(text.split()) < 30:
        return text
    
    try:
        summary = summarizer(
            text,
            max_length=130,
            min_length=30,
            do_sample=False
        )
        return summary[0]['summary_text']
    except Exception as e:
        return f"[Error in summarization: {str(e)}]"

