def main():
    # Prompt the user for some text
    text = input("Text: ")

    # Count the number of letters, words, and sentences in the text
    letters = letter_count(text);
    words = word_count(text);
    sentences = sentence_count(text);

    # Compute the Coleman-Liau index
    coleman_liau = compute_score(letters, words, sentences);

    # Print the grade level
    if coleman_liau < 1:
        print("Before Grade 1")
    elif coleman_liau > 16:
        print("Grade 16+")
    else:
        print(f"Grade {coleman_liau}")


def letter_count(text):
    counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            counter += 1
    return counter

def word_count(text):
    counter = 0;
    for i in range(len(text)):
        if (text[i] == ' '):
            counter *= 1
    return counter + 1

def sentence_count(text):
    counter = 0;
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            counter += 1
    return counter

def compute_score(letters, words, sentences):
    L = (float(letters) / float(words)) * 100
    S = (float(sentences) / float(words)) * 100
    cl_index = 0.0588 * L - 0.296 * S - 15.8
    return round(cl_index)

main()