import random

# Function to generate the sentence determiner
def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]

    selected_determiner= random.choice(determiners) ;
    cap_selected_determiner = selected_determiner.capitalize()
    return cap_selected_determiner

# Function to generate noun for a sentence
def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    selected_noun = random.choice(nouns);
    cap_selected_noun =selected_noun.capitalize()
    return cap_selected_noun

# Function to gnereate a verb for a sentence
def get_verb(quantity,tense):
    if (quantity==1 or quantity!=1 and tense == "past"):
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"] 
    elif (quantity==1 and tense =="present"):
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif (quantity != 1 and tense == "present"):
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"] 
    else:
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]


    selected_verb= random.choice(verbs);
    cap_selected_verb = selected_verb.capitalize()
    return cap_selected_verb

# Function to generate and append sentence to sentences list
def make_sentence():
    # defining a list to hold all sentences to be generatd
    sentences = []

    # singular present tense
    determiner = get_determiner(1);
    noun = get_noun(1);
    verb = get_verb(1,"present"); 
    sentence = f"{determiner} {noun} {verb}"
    sentences.append(sentence)

    # singular past tense
    determiner = get_determiner(1);
    noun = get_noun(1);
    verb = get_verb(1,"past"); 
    sentence = f"{determiner} {noun} {verb}"
    sentences.append(sentence)

    # singular future tense
    determiner = get_determiner(1);
    noun = get_noun(1);
    verb = get_verb(1,"future"); 
    sentence = f"{determiner} {noun} {verb}"
    sentences.append(sentence)

    # plural present tense
    determiner = get_determiner(2);
    noun = get_noun(2);
    verb = get_verb(2,"present"); 
    sentence = f"{determiner} {noun} {verb}"
    sentences.append(sentence)

    # plural past tense
    determiner = get_determiner(2);
    noun = get_noun(2);
    verb = get_verb(2,"past"); 
    sentence = f"{determiner} {noun} {verb}"
    sentences.append(sentence)

    # plural future tense
    determiner = get_determiner(2);
    noun = get_noun(2);
    verb = get_verb(2,"future"); 
    sentence = f"{determiner} {noun} {verb}"
    sentences.append(sentence)

     

    return sentences

# Main function 
def main():
    generated_sentences = make_sentence();
    print("************RANDOM SENTENCE GENERATOR PROGRAM*********")
    for sentence in generated_sentences:
        print(f"{sentence}")
    print("*******************************************************")

if __name__ == "__main__":
    main()
