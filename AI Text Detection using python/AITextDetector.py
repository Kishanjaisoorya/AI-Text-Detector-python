import torch
from transformers import pipeline

def is_generated_by_ai(paragraph):
    # Load the text classification pipeline
    text_classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    # Classify the input paragraph
    result = text_classifier(paragraph)

    # You can adjust this threshold based on experimentation
    confidence_threshold = 0.7

    # Check if the label is consistent with AI-generated text
    label = result[0]['label']
    confidence = result[0]['score']
    if label == 'LABEL_1' and confidence >= confidence_threshold:
        return True
    else:
        return False

# Example usage
input_paragraph = "This is an example paragraph."
generated_by_ai = is_generated_by_ai(input_paragraph)

if generated_by_ai:
    print("The paragraph seems to be generated by AI.")
else:
    print("The paragraph seems to be written by a human.")
