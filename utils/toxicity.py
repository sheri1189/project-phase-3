from model.model import load_model
from model.tokenizer import load_tokenizer

model = load_model()
tokenizer = load_tokenizer()

toxic_words = {
    'toxic': ['nasty', 'harsh'],
    'severe toxic': ['extremely harsh'],
    'obscene': ['vulgar', 'rude'],
    'threat': ['warning', 'intimidation'],
    'insult': ['offense', 'disrespect'],
    'identity hate': ['discrimination', 'prejudice']
}

def classify_toxicity(text):
    return predict_toxicity(model, tokenizer, text)

def replace_toxic_words(text):
    toxic_word_detected = None
    for word, synonyms in toxic_words.items():
        if word in text:
            text = text.replace(word, synonyms[0])
            toxic_word_detected = word
    return text, toxic_word_detected
