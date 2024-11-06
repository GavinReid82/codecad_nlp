from flask import Flask, request, jsonify

app = Flask(__name__)

def letter_count(text):
    counter = 0
    for char in text:
        if char.isalpha():
            counter += 1
    return counter

def word_count(text):
    return len(text.split())

def sentence_count(text):
    counter = 0
    for char in text:
        if char in '.!?':
            counter += 1
    return counter

def compute_score(letters, words, sentences):
    L = (float(letters) / float(words)) * 100
    S = (float(sentences) / float(words)) * 100
    cl_index = 0.0588 * L - 0.296 * S - 15.8
    return round(cl_index)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    text = data.get('text', '')
    
    # Compute counts
    letters = letter_count(text)
    words = word_count(text)
    sentences = sentence_count(text)
    
    # Compute Coleman-Liau index
    coleman_liau = compute_score(letters, words, sentences)
    
    # Determine grade
    if coleman_liau < 1:
        grade = "Before Grade 1"
    elif coleman_liau > 16:
        grade = "Grade 16+"
    else:
        grade = f"Grade {coleman_liau}"
    
    return jsonify({"grade": grade})

if __name__ == '__main__':
    app.run(debug=True)
