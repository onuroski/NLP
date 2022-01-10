# task 9:Frequently Asked Questions chatbot based on one of BERT or ELMo or GPT-x models.

import tensorflow as tf
from transformers import BertTokenizer, TFBertForQuestionAnswering
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/answer",methods = ["GET","POST"])
def answer():
    if request.method == "POST":
        modelName = 'bert-large-uncased-whole-word-masking-finetuned-squad'
        tokenizer = BertTokenizer.from_pretrained(modelName)
        model = TFBertForQuestionAnswering.from_pretrained(modelName)
        f = open(r'C:\Users\ONUR\PycharmProjects\task9\task9.txt', 'r', encoding='utf-8')
        text = f.read()
        question = request.form.get("question")
        input_text = question + "[SEP]" + text
        input_ids = tokenizer.encode(input_text)
        input = tf.constant(input_ids)[None, :]
        token_type_ids = [0 if i <= input_ids.index(102) else 1 for i in range(len(input_ids))]
        answer = model(input, token_type_ids=tf.convert_to_tensor([token_type_ids]))

        startScores = answer.start_logits
        endScores = answer.end_logits

        input_tokens = tokenizer.convert_ids_to_tokens(input_ids)

        startIdx = tf.math.argmax(startScores[0], 0).numpy()
        endIdx = tf.math.argmax(endScores[0], 0).numpy() + 1
        x = (" ".join(input_tokens[startIdx:endIdx]))
        return render_template("answer.html", data=x)
    else:
        return render_template("index.html")
if __name__ =="__main__":
    app.run(debug = True)
