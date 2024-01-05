# -*- coding: utf-8 -*-
"""Douglass_Thane_Lab 11: Natural Language Processing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qhlk9HCrQruPKEJOzeddykwZWwLwft01

<br>
<br>
<br>
<br>

#**Make sure to run this cell first:**

# Welcome to the Final Lab Assignment!

**Please make a copy of this file before attempting any question. To do so, click on File -> Save a copy in Drive. After that, you will have your own copy of the file and can modify it.**


In this lab, you'll be introduced to the transformers library from Hugging Face (yes, that’s a real company name 🙂). Please take quick look at this page before starting the assignment: https://huggingface.co/learn/nlp-course/chapter1/3


This lab is not graded for accuracy and the contents won't appear on your final exam. The answers to the challenges aren't predetermined and depend on the inputs you provide. You'll receive a full score as long as you make a sincere effort to answer the questions. If you're interested in building chatbots or engaging in other exciting projects that leverage Natural Language Processing, this lab is an excellent starting point. After completion, please download this notebook and submit it directly to Canvas.


## Using Google Colab

For this assignment, we will use Google Colab since EdStem doesn't allow the installation of the transformers library we'll be using. Google Colab is a free cloud-based coding environment, similar to the interface on EdStem, with some key differences.

### Running Code Cells

Here's how to run a code cell in Google Colab:

1. Click the "Run" button next to the code cell you want to run.
2. Alternatively, use the keyboard shortcut Shift + Enter.

Once the cell has run, the code results will be displayed below the cell. You can then proceed to run the next cell in your program. For each code cell provided below, please read the comment above the code to find the instructions.

### Working with Multiple Code Cells

Google Colab notebooks are divided into code cells, each containing a separate piece of code. You can run each cell individually to step through your code and observe the results.

Additional tips for working with code cells in Google Colab:

- You can edit the code in any cell before running it.
- Add new code cells by clicking the "+ Code" button at the top left.
- Delete code cells by clicking the "delete" button next to the cell you want to remove.

## Troubleshooting

If you encounter issues running a code cell, consider the following:

- Ensure you're using the correct syntax.
- Confirm you're not attempting to run code dependent on undefined variables. You may need to rerun cells above.
- Run the first cell that installs the transformer library before using any imports from this library.

If the problems persist, please post on EdStem, and I will provide assistance. Alternatively, check out this 10 min tutorial on Colab: https://www.youtube.com/watch?v=RLYoEyIHL6A

Happy coding!
"""

# Run this cell and make sure it completes without any errors.
# Please do not modify this cell.
!pip install transformers
!pip install sentencepiece
!pip install sacremoses

"""<br>
<br>
<br>
<br>
<br>
<br>





## **Question 1**

You have been provided with a list named `sentences`. The list consists of 20 sentences, and each sentence discusses one of three topics: education, music, or sleep. It's important to note that the sentences may not explicitly contain the words "education," "music," or "sleep." For example, the sentence "Howard University is a leading research institution." should be categorized as a sentence related to education.


Using the example below as a starting point, create a Python program that categorizes each sentence and outputs a result indicating how many lines are associated with each of the three topics.
"""

# Your solution should be in the next cell. This one is an example.
# Run it to see the output.
# In this example, we will use a text classifier to determine what
# a given text is about. The name of the library we'll use is called
# zero-shot-classification, and for a given string and a list of candidate options
# it returns a dictionary with the three keys: "sequence", "labels", "scores"
# you need to find the highest number in scores (the first one!), and find the corresponding
# candidate label (also the first one).
# Please ignore any texts produced by running this code unless it's an error message.

from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
output = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "music", "sleep"],
)
print()
print("The returned dictionary looks like this: ")
print(output)

# YOUR CODE FOR Question 1 GOES HERE:

sentences = [
    'Listening to calming music before bed can aid in relaxation.',
    'Creating a bedtime routine promotes better sleep hygiene.',
    'Deep sleep is crucial for physical and mental restoration.',
    'Music therapy is used to support various forms of rehabilitation.',
    'Music has the ability to transcend language and connect people.',
    'STEM education fosters innovation and technological advancements.',
    'Different genres of music have unique cultural influences.',
    'Establishing a consistent sleep schedule is beneficial for health.',
    'Access to quality education is a basic human right.',
    'Teachers play a crucial role in shaping the future of students.',
    'Lack of sleep can negatively impact mood and productivity.',
    'Learning is a lifelong journey that enriches the mind.',
    'Online learning has become increasingly popular in recent years.',
    'Critical thinking is a fundamental skill honed through education.',
    'Concerts provide a communal experience for music enthusiasts.',
    'Education is the key to unlocking endless opportunities.',
    'Quality sleep improves memory consolidation and cognitive function.',
    'Playing a musical instrument enhances cognitive abilities.',
    'Music has the power to evoke emotions and memories.',
    "A good night's sleep is essential for overall well-being."
]

# YOUR CODE GOES HERE:
from transformers import pipeline

categories = ["education", "music", "sleep"]
topic_counts = {i: 0 for i in categories}
for sentence in sentences:
    output = classifier(sentence, candidate_labels=categories)
    predicted_category = output['labels'][0]
    topic_counts[predicted_category] += 1
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
output = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "music", "sleep"],
)
print()
print("Here are how many lines are associated with each of the three topics: ")
print()
for i, count in topic_counts.items():
  print(f"{i}: {count}")

"""<br>
<br>
<br>
<br>

# **Question 2**
## Task:

You are given a list `beyonce_songs` containing some titles of Beyoncé's songs. Your objective is write a python program to identify five positive and five negative titles. Use the `sentiment-analysis` model to determine the positivity or negativity of each title.

Start with the example structure provided to understand how to use the model and the data types it returns.

*If you found that easy, can you write a program to identify the five most positive and the five most negative ones?*


"""

# Your solution should be in the next cell. This one is an example.
# Run it to see the output.
# In this example, we will use a sentiment analyzer to determine if a given piece
# of text is POSITIVE or NEGATIVE. The name of the model we'll use is called
# sentiment-analysis, and for a given string it returns a list with a dictionary.
# The dictionary comes with the following keys: "label" and "score"
# "label" will be associated with a string, either "POSITIVE" or "NEGATIVE"

# you need to do these two lines just once per cell
from transformers import pipeline
classifier = pipeline("sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english")

# now that we have created a classifier, we can give it different strings and test it.
response1 = classifier("I am happy")
print(response1)

response2 = classifier("I am sad")
print(response2)

# YOUR CODE FOR Question 2 GOES IN THIS CELL AFTER THIS LIST

beyonce_songs = [
    "Crazy in Love",
    "Single Ladies (Put a Ring on It)",
    "Irreplaceable",
    "Halo",
    "Drunk in Love",
    "Formation",
    "If I Were a Boy",
    "Love on Top",
    "Run the World (Girls)",
    "Sweet Dreams",
    "Sorry",
    "Partition",
    "Best Thing I Never Had",
    "Beautiful Liar (with Shakira)",
    "Check On It",
    "Diva",
    "Countdown",
    "Listen",
    "Upgrade U",
    "Deja Vu (featuring Jay-Z)",
    "End of Time",
    "Pretty Hurts",
    "XO",
    "Flawless",
    "Me, Myself and I",
    "Green Light",
    "Ring the Alarm",
    "Why Don't You Love Me",
    "Blow",
    "Party (featuring André 3000)",
    "Freedom (featuring Kendrick Lamar)",
    "Ego",
    "Get Me Bodied",
    "Hold Up",
    "All Night",
    "Start Over",
    "I Was Here",
    "Rocket",
    "Forward (featuring James Blake)",
    "Love Drought",
    "Pray You Catch Me",
    "Heaven",
    "Blue (featuring Blue Ivy)",
    "Daddy Lessons",
    "Sandcastles",
    "Hold Up",
    "Don't Hurt Yourself (featuring Jack White)",
    "6 Inch (featuring The Weeknd)",
    "Ave Maria",
    "Dance for You",
    "Haunted",
    "I Care",
    "Disappear",
    "Yes",
    "Satellites",
    "No Angel",
    "Scared of Lonely",
    "Smash Into You",
    "World Wide Woman",
    "Suga Mama"
]

# TODO: your code should go here:
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Dictionary to store sentiment scores for each song
sentiment_scores = {}

# Analyze sentiment for each song, index through each song
for song in beyonce_songs:
    sentiment = classifier(song)
    sentiment_scores[song] = sentiment[0]['score']

# Sort songs based on sentiment scores
sorted_songs = sorted(sentiment_scores.items(), key=lambda x: x[1], reverse=True)

# Get the five most positive and five most negative songs
top_positive_songs = sorted_songs[:5]
top_negative_songs = sorted_songs[-5:]

# Print the results
print("Top 5 Most Positive Beyoncé Songs:")
for song, score in top_positive_songs:
    print(f"{song}: {score}")

print("\nTop 5 Most Negative Beyoncé Songs:")
for song, score in top_negative_songs:
    print(f"{song}: {score}")

"""<br>
<br>
<br>
<br>
<br>

# **Question 3**

## Task:

You are provided with a list named `french_sentences` containing 10 French sentences. Your objective is to write a python program to translate each sentence into English.

Use the example structure below to understand how to use the model.

"""

# Your solution should be in the next cell. This is just an example.
# Run it to see the output.
# In this example, we will utilize a translation library to translate French into
# English. The model we'll use is called "translation," and it returns a list(!) with a dictionary.
# The dictionary includes the key "translation_text,"
# and the associated value is a string representing the translated English text.


# you need to do these two lines just once per cell
from transformers import pipeline
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")


# translate a couple of sentences and print out the response to see the dictionary
response1 = translator("L'Université Howard est incroyable.")
print(response1)

response2 = translator("La vie est belle.")
print(response2)

# Your response for Question 3 should go in this cell.

french_sentences = [
    "La mer est calme aujourd'hui.",
    "J'aime écouter de la musique classique le soir.",
    "Le soleil se couche derrière les montagnes.",
    "Les enfants jouent dans le parc.",
    "Mon plat préféré est la ratatouille.",
    "Elle a un chat noir et blanc très mignon.",
    "Nous avons visité le Louvre pendant nos vacances à Paris.",
    "Il fait froid, alors je porte un manteau épais.",
    "Les fleurs dans le jardin sont magnifiques ce printemps.",
    "Ils ont dégusté des croissants frais au petit-déjeuner."
]

# TODO: your code should go here:
from transformers import pipeline
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")


# translate all of the sentences and print out the response to see the dictionary
response1 = translator(french_sentences)
for i in response1:
    print(i['translation_text'])

"""<br>
<br>
<br>
<br>
<br>

# **Question 4**
This question is open-ended. Please pick another model that is listed here:

*   fill-mask
*   ner (named entity recognition)
*   question-answering
*   summarization
*   text-generation

and refer to https://huggingface.co/learn/nlp-course/chapter1/3?fw=pt to see how to use it.
Once you understand what the model does, write a python program that makes use of at least one of these models.

If you're up for a challenge, can you write one that uses two models?
"""

# MY CODE ATTEMPTS TO USE THE FOLLOWING TWO MODELS: SUMMARIZATION AND TRANSLATION.
from transformers import pipeline, AutoTokenizer
from datasets import load_dataset

model_checkpoint = "facebook/bart-large-cnn"  # Choose a summarization model
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
summarization_pipeline = pipeline(task="summarization", model=model_checkpoint)

# Load English and Spanish datasets
english_dataset = load_dataset("amazon_reviews_multi", "en")
spanish_dataset = load_dataset("amazon_reviews_multi", "es")

def generate_review_title(review_text):
    summary = summarization_pipeline(review_text, max_length=30, min_length=5, length_penalty=2.0, num_beams=4)
    return summary[0]['summary_text']

# Example usage
english_review = english_dataset['train'][0]['review_body']
spanish_review = spanish_dataset['train'][0]['review_body']

english_title = generate_review_title(english_review)
spanish_title = generate_review_title(spanish_review)

print("English Review:", english_review)
print("Generated English Title:", english_title)

print("\nSpanish Review:", spanish_review)
print("Generated Spanish Title:", spanish_title)