import random

# Function to generate the sentence determiner
def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]

    random_determiner= random.choice(determiners) ;
    cap_selected_determiner = random_determiner.capitalize()
    return cap_selected_determiner

# Function to generate noun for a sentence
def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    random_noun = random.choice(nouns);
    cap_selected_noun = random_noun.capitalize()
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


    random_verb= random.choice(verbs);
    cap_selected_verb = random_verb.capitalize()
    return cap_selected_verb

# Function to get random preposition from a list
def get_preposition(quantity):
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    random_preposition = random.choice(preposition)
    cap_preposition = random_preposition.capitalize()
    return cap_preposition

# Function to generate prepositional phrase
def get_prepositional_phrase(quantity): 
    preposition = get_preposition(quantity)
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    preposition_phrase = f"{preposition} {determiner} {noun}"
    cap_preposition_phrase = preposition_phrase.capitalize()
    return cap_preposition_phrase

# Function to generate adjective random from a list
def get_adjective():
    adjectives = ["happy", "sad", "fast", "slow", "loud", "quiet", "bright", "dark", "tall", "short"]
    random_adjective =random.choice(adjectives)
    cap_adjective = random_adjective.capitalize()
    return cap_adjective

# Function to generate adverb random from a list
def get_adverb():
    adverbs = ["quickly", "quietly", "happily", "slowly", "loudly", "gently", "eagerly", "calmly", "briskly", "cheerfully"]
    random_adverb = random.choice(adverbs)
    cap_adverb = random_adverb.capitalize()
    return cap_adverb

# Function to generate and append sentence to sentences list
def make_sentence():
    # defining a list to hold all sentences to be generatd
    sentences = []

    # singular present tense
    adjective = get_adjective()
    adverb = get_adverb()
    determiner = get_determiner(1);
    noun = get_noun(1);
    verb = get_verb(1,"present"); 
    preposition_phrase = get_prepositional_phrase(1)
    second_noun = get_noun(2);
    second_adjective = get_adjective()
    second_determiner = get_determiner(2);
    second_preposition_phrase = get_prepositional_phrase(1)
    sentence = f"{determiner} {adjective} {noun} {preposition_phrase} {adverb} {verb} {second_determiner} {second_adjective} {second_noun} {second_preposition_phrase}"
    sentences.append(sentence)

    # singular past tense
    adjective = get_adjective()
    adverb = get_adverb()
    determiner = get_determiner(1);
    noun = get_noun(1);
    verb = get_verb(1,"past"); 
    preposition_phrase = get_prepositional_phrase(1)
    second_noun = get_noun(2);
    second_adjective = get_adjective()
    second_determiner = get_determiner(2);
    second_preposition_phrase = get_prepositional_phrase(1)
    sentence = f"{determiner} {adjective} {noun} {preposition_phrase} {adverb} {verb} {second_determiner} {second_adjective} {second_noun} {second_preposition_phrase}"
    sentences.append(sentence)

    # singular future tense
    adjective = get_adjective()
    adverb = get_adverb()
    determiner = get_determiner(1);
    noun = get_noun(1);
    verb = get_verb(1,"future");
    preposition_phrase = get_prepositional_phrase(1)
    second_noun = get_noun(2);
    second_adjective = get_adjective()
    second_determiner = get_determiner(2);
    second_preposition_phrase = get_prepositional_phrase(1)
    sentence = f"{determiner} {adjective} {noun} {preposition_phrase} {adverb} {verb} {second_determiner} {second_adjective} {second_noun} {second_preposition_phrase}"
    sentences.append(sentence)

    # plural present tense
    adjective = get_adjective()
    adverb = get_adverb()
    determiner = get_determiner(2);
    noun = get_noun(2);
    verb = get_verb(2,"present"); 
    preposition_phrase = get_prepositional_phrase(2)
    second_noun = get_noun(2);
    second_adjective = get_adjective()
    second_determiner = get_determiner(2);
    second_preposition_phrase = get_prepositional_phrase(2)
    sentence = f"{determiner} {adjective} {noun} {preposition_phrase} {adverb} {verb} {second_determiner} {second_adjective} {second_noun} {second_preposition_phrase}"
    sentences.append(sentence)

    # plural past tense
    adjective = get_adjective()
    adverb = get_adverb()
    determiner = get_determiner(2);
    noun = get_noun(2);
    verb = get_verb(2,"past"); 
    preposition_phrase = get_prepositional_phrase(2)
    second_noun = get_noun(2);
    second_adjective = get_adjective()
    second_determiner = get_determiner(2);
    second_preposition_phrase = get_prepositional_phrase(2)
    sentence = f"{determiner} {adjective} {noun} {preposition_phrase} {adverb} {verb} {second_determiner} {second_adjective} {second_noun} {second_preposition_phrase}"
    sentences.append(sentence)

    # plural future tense
    adjective = get_adjective()
    adverb = get_adverb()
    determiner = get_determiner(2);
    noun = get_noun(2);
    verb = get_verb(2,"future"); 
    preposition_phrase = get_prepositional_phrase(2)
    second_noun = get_noun(2);
    second_adjective = get_adjective()
    second_determiner = get_determiner(2);
    second_preposition_phrase = get_prepositional_phrase(2)

    sentence = f"{determiner} {adjective} {noun} {preposition_phrase} {adverb} {verb} {second_determiner} {second_adjective} {second_noun} {second_preposition_phrase}"
    sentences.append(sentence)  

    return sentences

# Main function 
def main():
    generated_sentences = make_sentence();
    print(f"\n||+++++++++++++++++++++++ RANDOM SENTENCE GENERATOR PROGRAM +++++++++++++++++++++++|| \n")
    for sentence in generated_sentences:
        print(f"{sentence}") 
    print("\n||+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++||")

    # Sentence generated in order:\n{Determiner} {adjective} {noun} {prepositional_phrase} {adverb} {verb} {determiner} {adjective} {noun} {prepositional_phrase}

if __name__ == "__main__":
    main()
