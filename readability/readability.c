#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int letter_count(string text);
int word_count(string text);
int sentence_count(string text);
int compute_score(int letters, int words, int sentences);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = letter_count(text);
    int words = word_count(text);
    int sentences = sentence_count(text);

    // Compute the Coleman-Liau index
    int coleman_liau = compute_score(letters, words, sentences);

    // Print the grade level
    if (coleman_liau < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (coleman_liau > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", coleman_liau);
    }
}

int letter_count(string text)
{
    int counter = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            counter++;
        }
    }
    return counter;
}

int word_count(string text)
{
    int counter = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            counter++;
        }
    }
    return counter + 1;
}

int sentence_count(string text)
{
    int counter = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            counter++;
        }
    }
    return counter;
}

int compute_score(int letters, int words, int sentences)
{
    float L = ((float) letters / (float) words) * 100;
    float S = ((float) sentences / (float) words) * 100;
    float cl_index = 0.0588 * L - 0.296 * S - 15.8;
    return round(cl_index);
}
