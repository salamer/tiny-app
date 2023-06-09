from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "ainize/bart-base-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)