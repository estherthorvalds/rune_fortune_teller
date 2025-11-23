"""
Student: Esther Ýr Þorvaldsdóttir
Course: MLT701F Programming in Language Technoogy (Icel. Forritun í máltækni)


Rune Fortune Teller
A program that analyzes user text to determine their primary concern.
(LOVE, HEALTH, or FINANCE) and interprets a rune accordingly.

Project Structure:
------------------
rune_fortune_teller/
├── rune_fortune_teller.py      # Main program (THIS FILE)
├── preprocessing.py           # SpaCy text preprocessing (from teacher, may modify)
├── claude_files/                # Emotion detection modules (created by Claude)
│   ├── __init__.py             # An empty __init__.py file so Python understands this is a package with importable modules
│   ├── emotion_detector.py     # Main interface for category detection
│   ├── category_analyzer.py    # Counts keyword matches and determines winner
│   └── emotion_words.py        # Keyword lists (LOVE, HEALTH, FINANCE)
└── test_cases/                  # Test texts for validation
    ├── Meredith_Grey.txt
    ├── Jane_Villanueva.txt
    ├── Gordon_Gekko.txt
    ├── Jordan_Belfort.txt
    ├── Romeo.txt
    └── Pam_Beesley.txt

Usage:
1. Concept explained to user
2. Library needs explained to user
3. User provides text (direct input or file upload)
4. Text is preprocessed and lemmatized using SpaCy
5. Lemmas are analyzed to determine emotional category
6. A rune is drawn and interpreted based on the detected category

"""

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import time
    import string
    import pickle
    import random
    from spacy.lang.en.stop_words import STOP_WORDS
    from preprocessing import tags_and_lemmas 
    import claude_files.rune_meanings as rune
    from claude_files.emotion_detector import detect_emotion_from_lemmas
    from claude_files.emotion_words import LOVE, HEALTH, FINANCE
except ModuleNotFoundError as e:
    print("IMPORT ERROR")
    print(e)
    print("Urður: Alack! Thou must fetch down some modules for these programmes to employ.")
    print("\nThis might mean:")
    print("  - A required file is missing:")
    print("     - claude_files.rune_meanings.py")
    print("     - claude_files.emotion_detector.py")
    print("     - claude_files.emotion_words.py")
    print("     - preprocessing.py")
    print("  - A library hasn't been pip installed:")
    print("     - pandas")
    print("     - matplotlib")
    print("     - spacy (the library)")
    print("  - SpaCy model has not been downloaded")
    print("\nPlease ensure all project files are present and modules are installed.")
    exit()

"""
NORN CLASS
Explain this class.
"""

class Norn:

    """The Norn class does not need to store anything in this program. But if it develops, for example if the norns get their own object, this would be where they are stored."""
    def __init__(self):
        self.questions_asked = 0  # (instance variable)
        self.user_name = ""
        self.user_pronoun = ""

    def print_slowly(self, text, delay=0.01):
        """Print Norn text for dramatic effect."""
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

    def greet_user(self):
        self.print_slowly("Urður: Welcome, mortal. Welcome to Urðarbrunnur.")
        self.print_slowly("Verðandi: You are here to seek the truth about your fortune.")
        self.print_slowly("THE THREE NORNS: We are the norns of fortune.")
        self.print_slowly("Skuld: And you...")
        self.print_slowly("Verðandi: We already know your name... we know what was, what is and what will be.")
        self.print_slowly("Urður: We know all that was.")
        self.print_slowly("Verðandi: All that is.")
        self.print_slowly("Skuld: And all that will be.")
        self.print_slowly("Verðandi: But that is not the way of today. We are polite.")
        self.print_slowly("Skuld: We shall ask for a name and pronoun.")
        self.print_slowly("Urður: What should we call you, dear seeker?")
        time.sleep(0.3)
        while True:
            self.user_name = input("My name is: ")
            if self.user_name != "":
                return
            else:
                self.print_slowly("Urður: A name is required. Try again...")
    
    def explain_concept(self):
        self.print_slowly(f"\nUrður: We welcome you, dear {self.user_name}, to Urðarbrunnur.")
        self.print_slowly("Verðandi: Digital Urðarbrunnur!")
        self.print_slowly("Skuld: We've gone digital. All the cool kids are doing it.")
        self.print_slowly(f"Urður: {self.user_name} is here to seek the truth about the fortune.")
        self.print_slowly("Verðandi: Yup, we're ready to weave your tapestry!")
        self.print_slowly("Urður: You will provide us with words. Your words. That way, we will know what is on your mind.")
        self.print_slowly("Verðandi: Once we know what is on your mind, we will analyse your thoughts and emotions.")
        self.print_slowly("Skuld: We will weave your tapestry for you to download on your computer.")
        self.print_slowly("Urður: You must follow all our instructions for this to work.")
        time.sleep(0.3)
        print()
        while True:
            choice = input("Urður: Are you ready to move on? Press ENTER.")
            return
        

    def explain_imports(self):
        """Explain required installations to the user."""
        
        self.print_slowly("\nUrður: Before we begin, you must prepare your system with the tools...")
        time.sleep(0.3)
        
        # Skip option for Steinunn
        skip = input("\nPress Enter to see installation instructions, or type 'steinunn' to skip: ").lower()
        if skip == 'steinunn':
            self.print_slowly("\nSkuld: Ah, Steinunn! The all-seeing teacher who tests our creator's work!")
            self.print_slowly("Verðandi: We bow before your power. The installations are surely complete.")
            self.print_slowly("Urður: Let us proceed...\n")
            time.sleep(0.5)
            return
        
        self.print_slowly("\nVerðandi: We require several Python libraries. And extra files. And one model.")
        self.print_slowly("Skuld: We assume you're using Linux. If not, then too bad!")
        self.print_slowly("Urður: Our creator didn't tell us how to do install these tools in other environments, the program got too big.")
        self.print_slowly("Verðandi: Oh, yes. It was getting way too large for a beginner's programming assignment.")
        self.print_slowly("Urður: But she did give it a thought and decided against it.\n")
        
        time.sleep(0.3)

        print("REQUIRED FILES")
        self.print_slowly("\nSkuld: Make sure these are in your directory:")
        time.sleep(0.5)

        print("     - claude_files.rune_meanings.py")
        print("     - claude_files.emotion_detector.py")
        print("     - claude_files.emotion_words.py")
        print("     - preprocessing.py")
        print()
        time.sleep(0.5)
        
        print("REQUIRED INSTALLATIONS")
        
        self.print_slowly("\nSkuld: Open your terminal and type these commands:")
        time.sleep(0.5)
        
        print("\n1. SpaCy (for natural language processing):")
        print("   pip install spacy --break-system-packages")
        print("   python3 -m spacy download en_core_web_sm")
        time.sleep(0.3)
        
        print("\n2. Matplotlib (for creating mystical visualizations):")
        print("   pip install matplotlib --break-system-packages")
        time.sleep(0.3)
        
        print("\n3. Pandas (for data manipulation):")
        print("   pip install pandas --break-system-packages")
        time.sleep(0.3)
        
        self.print_slowly("\nUrður: The --break-system-packages flag is necessary on some Linux systems.")
        self.print_slowly("Verðandi: It allows pip to install packages outside a virtual environment.")
        time.sleep(0.5)
        
        print("\n-------------------\n")
        
        self.print_slowly("\nSkuld: If installations succeed, you're ready to consult the Norns!")
        self.print_slowly("Urður: If you encounter errors, seek guidance from your terminal's wisdom...")
        print()
        self.print_slowly("Skuld: Oh and once you have run this program once, so change the 'delay=' to 0.01 in the print_slowly method.")
        self.print_slowly("Verðandi: Right. This will take forever to loop through again and again.")
        time.sleep(0.5)

        while True:
            choice = input("Urður: Are you ready to move on? Press ENTER.")
            return
    
    def collect_first_choice(self):
        while True:
            choice = input("Urður: You wish to upload file or type? (f/t): ")
            try:
                if choice.lower() in ['f', 't']:
                    return choice
            except:
                print(f"Verðandi: Nahh, {choice} is not an option.")
                print(f"Skuld: Give it another go.")

    def collect_text(self, new_text):
        while not self.check_word_count(new_text):  
            self.print_slowly("Urður: This is not enough. You have only given us " + str(len(new_text.split())) + " words so far.")
            new_text = self.ask_questions()
            collected_text += " " + new_text
        if self.check_word_count(new_text): 
            return new_text
                     
    def check_word_count(self, text):
        word_count = len(text.split())
        if word_count < 400:
            return False
        else:
            return True

    def read_file(self):
        while True:
            self.print_slowly("Urður: The full path to your .txt file will lead us, the norns, on the path of your truths... Paste it here:")
            path = input()
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                    return text
            except FileNotFoundError:
                self.print_slowly("Urður: This file is nowhere to be found. Try again!")
            except Exception as e:
                self.print_slowly(f"Urður: Something went terribly wrong: {e}")

    def ask_questions(self):

            questions = [
        "Urður: What brings you to seek the Norns today?",
        "Verðandi: Tell us about your current situation in life.",
        "Skuld: What are your hopes for the future?",
        "Urður: Describe your relationships with those close to you.",
        "Verðandi: What challenges are you facing right now?",
        "Skuld: What makes you feel most alive?",
        "Urður: Tell us about your former dreams and aspirations. Did you achieve them?",
        "Verðandi: What do you fear most?",
        "Verðandi: Describe a recent moment that brought you joy.",
        "Verðandi: What occupies your thoughts most these days?",
        "Skuld: Tell us about your deepest desires.",
        "Skuld: What would you change about your life if you could?",
        "Urður: Tell us about your childhood.",
        "Urður: Tell us about your teenage years.",
        "Urður: What is the biggest challange you have faced in your past?",
        "Verðandi: How do you like your life, right now?",
        "Verðandi: What do you feel your life purpose is?",
        "Urður: What made you happy as a child?",
        "Verðandi: What makes you happy today?",
        "Skuld: What needs to happen for you to be happy in the future?",
        "Verðand: What does happiness mean to you?",
        "Skuld: How would you define success?",
        "Urður: If you could go back and change one thing about your past, what would it be?",
        "Verðandi: What do you owe to yourself?",
        "Urður: What fear have you outgrown?",
        "Urður: What's the most important life lesson you've learned the hard way?",
        "Urður: What accomplishment are you most proud of?",
        "Verðandi: What core values guide your actions and decisions?",
        "Verðandi: What do you value most in your personal relationships?",
        "Verðandi: Who in your life really sees you, and how do you know?",
        "Skuld: How do you approach building trust with someone?",
        "Verðandi: What makes you feel most loved?",
        "Verðandi: When do you feel most like yourself?",
        "Urður: If you could talk to your past self, what would you say?",
        "Verðandi: What is something about yourself that you have trouble acknowledging?",
        "Verðandi: What's a misconception people often have about you?",
        "Verðandi: What is your biggest fear?"
    ]
    
            selected_questions = random.sample(questions, 3)
            collected_answers = ""
    
            for question in selected_questions:
                self.print_slowly(question)
                answer = input("Answer: ")
                collected_answers += " " + answer
            
            return collected_answers


    def interpret(self, text_object):
        self.print_slowly(f"Urður: Ah. That's enough words. We are satisfied. Let us begin weaving.")
        
        wordc = Text.count_words(text_object)
        self.print_slowly(f"Verðandi: You wrote {wordc} words in total.")
        if wordc <= 440:
            self.print_slowly("Urður: You have never been a person of many words.")
            self.print_slowly("Verðandi: Thank you for making an effort tonight.")
        elif wordc <= 500:
            self.print_slowly("Urður: We see your words. We see you.")
            self.print_slowly("Verðandi: Words are powerful. We will use them to see your fotune.")
        else:
            self.print_slowly("Urður: Your words are many, we have much to weave with.")
        
        avsent = Text.average_sent(text_object)
        self.print_slowly(f"Verðandi: Your average sentence was {avsent:.2f} words long.")
        if avsent <= 12:
            self.print_slowly("Urður: You see no need in overcomplicating things.")
            self.print_slowly("Verðandi: You like it this way. Short thoughts, long lists. No need for long monologues.")
            self.print_slowly("Skuld: Remember, there is room to breathe.")
            self.print_slowly("Verðandi: Take a moment and give it some thought.")
            self.print_slowly("Verðandi: You see width and length.")
            self.print_slowly("Skuld: Don't forget about the depth. Depth isn't bad.")
        elif avsent <= 19:
            self.print_slowly("Urður: There's a murmur in your sentences. Patterns.")
            self.print_slowly("Skuld: Organised chaos. The sentences are not small, per se.")
            self.print_slowly("Verðandi: Nor are they big.")
            self.print_slowly("Skuld: For you, they are just right.")
        else:
            self.print_slowly("Urður: Your tapestry is full of patterns.")
            self.print_slowly("Verðandi: You must take a breather.")
            self.print_slowly("Skuld: Stop overthinking. Nothing good can come of it.")

        questm = Text.questionm(text_object)
        self.print_slowly(f"Verðandi: You used {questm} '?'.")
        if questm == 0:
            self.print_slowly("Urður: You did not come here looking for answers.")
            self.print_slowly("Verðandi: You are here on your own accord.")
            self.print_slowly("Skuld: We welcome you anyway.")
            self.print_slowly("Verðandi: Watch us weave your tapestry.")

        elif questm <= 3:
            self.print_slowly("Skuld: You don't need us to tell you the answers.")
            self.print_slowly("Urður: You already have them.")
        else:
            self.print_slowly("Urður: The crossstiching suggests crossroads.")
            self.print_slowly("Verðandi: Your tapestry has many unanswered questions.")
            self.print_slowly("Skuld: You must be the one to choose where to go.")
            self.print_slowly("Verðandi: We are mere observers.")
            self.print_slowly("Skuld: Though you seek our wisdom, you will not see your tapestry.")

        exclam = Text.exclamationm(text_object)
        self.print_slowly(f"Verðandi: You used {exclam} '!'.")
        if exclam == 0:
            self.print_slowly("Urður: Your stoicism is admirable.")
            self.print_slowly("Skuld: Your precence is especially calming tonight.")
        elif exclam <= 1:
            self.print_slowly("Urður: You have always been down to earth.")
            self.print_slowly("Skuld: Even when the future is a place of uncertainty.")
        else:
            self.print_slowly("Skuld: You must try and find more calmness in your life.")
            self.print_slowly("Urður: Much emotion in this one.")
            self.print_slowly("Verðandi: Be mindful not to overwhelm the people around you.")

        firstw, lastw = Text.first_last(text_object)
        translator = str.maketrans('', '', string.punctuation)
        self.print_slowly(f"Verðandi: Your first word was {firstw} and your last word was {lastw}")
        self.print_slowly(f"Skuld: Think about what '{firstw}' means to you. It's the direction you took when you started writing.")
        self.print_slowly(f"Urður: And your last word. The last thing you thought about when writing. What does it mean: \n- {lastw.translate(translator)} -")

        try:
            avgvow_list = Text.vowel_percentage(text_object)
            avrgv = sum(avgvow_list) / len(avgvow_list)
            self.print_slowly(f"Verðandi: Your average vowels count was {(avrgv):.1f}%.")
            self.print_slowly("Skuld: Did we count the Y's?")
            self.print_slowly("Verðandi: No, it is unclear whether this is a vowel or a constonant in the English language.")
            self.print_slowly("Urður: We skipped those entirely.")
            self.print_slowly("Verðandi: Our creator thought it was irrelevant for the assignment.")
            self.print_slowly("Skuld: That's fine. The future is not about the y's, it is about the hows.")
            if avrgv <= 30:
                self.print_slowly("Urður: It is difficult to peak through your rough exterior.")
                self.print_slowly("Skuld: You're tough. The future may soften you up a bit.")
            elif avrgv <= 43:
                self.print_slowly("Urður: You are sometimes soft, sometimes hard.")
                self.print_slowly("Skuld: We will continue to weave.")
            else:
                self.print_slowly("Urður: Your soft words have always entertained.")
                self.print_slowly("Skuld: The words melt in your mouth.")

        except ZeroDivisionError:
            self.print_slowly("Verðandi: Your speech is odd. We cannot understand you.")
            self.print_slowly("Urður: This one has always been trying to break the rules.")
            self.print_slowly("Skuld: Maybe one day you will break the fundamentals of math and divide by ZERO.")
            self.print_slowly("Verðandi: But that day is not gonna be today.")

        lemmaset, uniqper = Text.lemma_analysis(text_object)
        self.print_slowly(f"Verðandi: {(uniqper * 100):.1f} of your lemmas were unique.")
        if uniqper <= 0.30:
            self.print_slowly("Urður: You have always been set in your way. You feel no need to expand.")
            self.print_slowly("Skuld: But Maybe you should expand?")
            self.print_slowly("Verðandi: You will find your expansion in a book.")
            self.print_slowly("Skuld: Choose a book that you'll be sure to enjoy.")
        elif uniqper <= 0.40:
            self.print_slowly("Urður: You will find your answers in the nearest library.")
            self.print_slowly("Verðandi: A librarian will guide you towards your next adventure.")
        elif uniqper <= 50:
            self.print_slowly("Urður: You take good care of your intellectual needs.")
            self.print_slowly("Skuld: Continue to do so at your own pace.")
        else:
            self.print_slowly("Urður: Your thirst for knowledge has always been insetiable.")
            self.print_slowly("Skuld: The thirst brings you joy. But you will never be satisfied.")

        postag = Text.pos_tags_adj(text_object)
        self.print_slowly(f"Verðandi: {(postag * 100):.1f}% of your words were descriptive.")
        if postag <= 0.07:
            self.print_slowly("Urður: You always get straight to the point.")
            self.print_slowly("Skuld: Straight to the point, this one.")
            self.print_slowly("Verðandi: Have you thought about meditating?")
            self.print_slowly("Skuld: Stop and smell the roses.")
        elif postag <= 0.1:
            self.print_slowly("Urður: There is balance in your heart.")
            self.print_slowly("Verðandi: We will weave in the color palatte of the Earth.")
            self.print_slowly("Urður: You have never felt any need to overcomplicate things.")
            self.print_slowly("Skuld: It wouldn't hurt to add more spices in your life.")
            self.print_slowly("Verðandi: Adding more color wouldn't hurt.")
            self.print_slowly("Skuld: It's up to you.")
        elif postag <= 0.15:
            self.print_slowly("Urður: You have always been full of emtions.")
            self.print_slowly("Verðandi: You have painted quite the picture. Your future has color.")
            self.print_slowly("Skuld: The tapestry is visual.")
        else:
            self.print_slowly("Urður: You like painting pictures.")
            self.print_slowly("Verðandi: Your tapestry is vivid. It's like poetry.")
            self.print_slowly("Skuld: The choice is yours, continue on your colorful path...")
            self.print_slowly("Verðandi: ...or slow down.")
            self.print_slowly("Urður: You tend to follow your heart. Don't forget about your brain.")
            self.print_slowly("Verðandi: Yes, for once, ask yourself what your brain wants.")
            self.print_slowly("Skuld: Choosing the most logical approach is also an option.")

        stopw = Text.stop_words(text_object)
        self.print_slowly(f"Verðandi: {(stopw * 100):.1f}% of words were stop words.")
        if stopw <= 0.45:
            self.print_slowly("Urður: You have always chosen your words wisely.")
            self.print_slowly("Verðandi: You can relax.")
            self.print_slowly("Skuld: Try to set yourself free.")
        elif stopw <= 0.50:
            self.print_slowly("Skuld: Be careful.")
            self.print_slowly("Urður: This one always has been careful.")
            self.print_slowly("Verðandi: The patterns in the tapestry are large.")
            self.print_slowly("Urður: Why have details when you can get straight to the point?")
            self.print_slowly("Skuld: The details of your future are unclear.")
        elif stopw <= 0.60: 
            self.print_slowly("Urður: You are balanced. You can see the big picture.")
            self.print_slowly("Skuld: Continue on your path.")
            self.print_slowly("Verðandi: The details are not lost to you either.")
            self.print_slowly("Skuld: Your future is clear like your vision.")
        else:
            self.print_slowly("Urður: It is difficult to navigate through your thoughts.")
            self.print_slowly("Verðandi: There is clutter in the tapestry.")
            self.print_slowly("Skuld: You have trouble getting to the point.")
            self.print_slowly("Verðandi: Could it be that you already know what you want.")
            self.print_slowly("Urður: You just don't want to admit it to your old self.")
            self.print_slowly("Skuld: Let your new self take control. Don't be ashamed of who you are.")
    
    def select_rune(self, emotion):
        rune_symbol = rune.draw_a_random_rune()
        self.print_slowly(f"Urður: You have drawn {rune_symbol}.")
        rune_name = rune.get_rune_name(rune_symbol)
        self.print_slowly(f"Verðandi: This is {rune_name}.")
        rune_meaning = rune.get_rune_interpretation(rune_symbol, emotion)
        self.print_slowly(f"Skuld: What this means for you: {rune_meaning}")
        time.sleep(1)

    # Save the ENTIRE Text object after analysis
    def save_analysis(self, text_obj):
        with open('last_analysis.pkl', 'wb') as f:
            pickle.dump(text_obj, f)
        print("Skuld: Your analysis has now been saved on your computer.")

    # Load it later
    def load_previous_analysis(self):
        pass
        try:
            with open('last_analysis.pkl', 'rb') as f:
                text_obj = pickle.load(f)
            print("Urður: I remember your last visit...")
            return text_obj
        except FileNotFoundError:
            return None
        
    def goodbye(self):
        self.print_slowly("Skuld: That's it.")
        self.print_slowly("Verðandi: Your visit has been pleasant.")
        self.print_slowly("Urður: Your tapestry will stay with us.")
        self.print_slowly("Skuld: Mortals don't get to see it.")
        self.print_slowly("Verðand: Nor do gods.")
        self.print_slowly("Skuld: You'll will make due with our analysis and rune reading.")
        self.print_slowly("Urður: Welcome back any time.")

"""

TEXT CLASS:
Explain this class.

"""

class Text:
    
    def __init__(self, text):
        try:
            self.text = text
            self.wordforms, self.tags, self.lemmas = tags_and_lemmas(text) # Three lists created using the teacher's preprocessing.py
        except Exception as e:
            print(f"Skuld: Something went wrong! We must shut this down: {e}")
            raise
    
    # 1 Count number of words
    def count_words(self):
        try:
            return len(self.text.split())	
        except Exception as e:
            print(f"Skuld: I wasn't able to count your words: {e}")

    # 2.A Count average length of sentences
    def average_sent(self):
        try:
            sentences = self.text.split(".")
            sentences = [s for s in sentences if s.strip()] # Removing empty sentences
            words = self.text.split()
            return len(words) / len(sentences) # float
        except ZeroDivisionError:
            print("Skuld: I couldn't find the average sentence length: Even Odinn the alfather cannot divide by ZERO!")
        except Exception as e:
            print(f"Skuld: I wasn't able to find the average length of your sentences: {e}")
    
    # 2.B Count average length of sentences for bar
    def sentence_lengths(self):
        try:
            length_list = []
            sentences = self.text.split(".")
            for sentence in sentences:
                word_count = len(sentence.split())
                if word_count > 0:
                    length_list.append(word_count)
            length_counter = {}
            for num in length_list:
                if num in length_counter:
                    length_counter[num] += 1
                else:
                    length_counter[num] = 1 
            return length_counter
        except Exception as e:
            print(f"Skuld: I wasn't able to count the length of your sentences: {e}")

    # 3 Count of question marks
    def questionm(self):
        try:
            return self.text.count("?") # int
        except Exception as e:
            print(f"Skuld: I wasn't able to count your question marks: {e}")
    
    # 4 Count of exclamation marks
    def exclamationm(self):
        try:
            return self.text.count("!") # int
        except Exception as e:
            print(f"Skuld: I wasn't able to count your exclamation marks: {e}") 
    
    # 5 First word, last word
    def first_last(self):
        try:
            words = self.text.split()
            first_word = words[0]
            last_word = words[-1]
            return first_word, last_word
        except Exception as e:
            print(f"Skuld: I wasn't able to find your first and last word: {e}")
    
    # 6.A The average number of vowels in a word 
    def average_vowels(self):
        try:
            vowels = "aeiouAEIOU"
            consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
            vowel_count = 0
            consonant_count = 0
            for wordform in self.wordforms:
                for letter in wordform:
                    if letter in vowels:
                        vowel_count += 1
                    if letter in consonants:
                        consonant_count += 1
                return vowel_count / (vowel_count + consonant_count)
        except ZeroDivisionError:
            print("Skuld: I couldn't find the average vowel percentage: We will divide by ZERO when Ragnarök comes!")
        except Exception as e:
            print(f"Skuld: I wasn't able to find the average percentage of your vowels in a word: {e}")
    
    # 6.B Vowels vs. consonants ratio
    def vowel_percentage(self):
        try:
            vowels = "aeiouAEIOU"
            consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
            vl_percentage_list = []
            for word in self.wordforms:
                vowel_count = 0
                consonant_count = 0
                for letter in word:
                    if letter in vowels:
                        vowel_count += 1
                    if letter in consonants:
                        consonant_count += 1
                if vowel_count + consonant_count > 0: # Preventing ZDE
                    percentage = (vowel_count/(vowel_count + consonant_count)) * 100
                    vl_percentage_list.append(percentage)
            
            # If list is empty or all zeros
            if not vl_percentage_list or all(v == 0 for v in vl_percentage_list):
                print("Skuld: You talk funny. Your text has no vowels!")
                return []  
            
            return vl_percentage_list
        except ZeroDivisionError:
            print("Skuld: I couldn't find the vowel percentage: You can't be the hero if you divide by ZERO!")
        except Exception as e:
            print(f"Skuld: I wasn't able to find out how many vowels you use per word: {e}")

    # 7.A Lemmas with percentage
    def lemma_analysis(self):
        try:
            set_of_lemmas = set(self.lemmas)
            percentage_unique = len(set_of_lemmas) / len(self.lemmas)
            return set_of_lemmas, percentage_unique # "You used X% unique words, you have thought about this thoroughly"
        except Exception as e:
            print(f"Skuld: I wasn't able to get the lemmas to your wordforms: {e}")
    
    # 7.B Lemma frequencies
    def lemma_frequencies(self):
        try:
            lemma_counter = {}
            for lemma in self.lemmas:
                if lemma in lemma_counter:
                    lemma_counter[lemma] += 1
                else:
                    lemma_counter[lemma] = 1 
            return lemma_counter
        except Exception as e:
            print(f"Skuld: I wasn't able to find the frequencies of your lemmas: {e}")
    
    # 8.A POS-tags
    def pos_tags_adj(self):
        try:
            descriptive_tags = ["RB", "RBR", "RBS", "JJ", "JJR", "JJS"]
            descriptive_words = 0
            for tag in self.tags:
                if tag in descriptive_tags:
                    descriptive_words += 1
            return descriptive_words / len(self.tags) # Percentage of the descriptive words "X% of your text is adverbs and adjectives, you can paint a picture"
        except ZeroDivisionError:
            print("Skuld: I couldn't find the descriptive word ratio: If you wish to know your might, by ZERO, you must not divide!")
        except Exception as e:
            print(f"Skuld: I wasn't able to find the percentage of your descriptive words: {e}")
    
    # 8.B
    def pos_tags(self):
        try:

            # POS Tags Dict
            penn_groups = {
                "NOUNS": ["NN", "NNS", "NNP", "NNPS"],
                "VERBS": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
                "ADJECTIVES": ["JJ", "JJR", "JJS"],
                "ADVERBS": ["RB", "RBR", "RBS", "WRB"],
                "PRONOUNS": ["PRP", "PRP$", "WP", "WP$"],
                "DETERMINERS": ["DT", "PDT", "WDT"],
                "CONJUNCTIONS": ["CC", "IN"],
                "NUMBERS": ["CD"],
                "MODALS": ["MD"],
                "POSSESSIVE_ENDING": ["POS"],
                "PARTICLES": ["RP"],
                "TO": ["TO"],
                "INTERJECTIONS": ["UH"],
                "EXISTENTIAL": ["EX"]
                }

            # Counting the tags
            tag_counter = {}
            for tag in self.tags:
                if tag in tag_counter:
                    tag_counter[tag] += 1
                else:
                    tag_counter[tag] = 1

            # Grouping the tags
            group_counter = {}
            for group_name, tag_list in penn_groups.items():
                total = 0 

                # Looking through each tag
                for tag in tag_list:
                    if tag in self.tags:
                        total += tag_counter[tag]

                group_counter[group_name] = total

            return group_counter
        
        except Exception as e:
            print(f"Skuld: I wasn't able to categorise your words into a POS-tags dictionary: {e}")

    # 9 Stop-Words percentage
    def stop_words(self):
        try:
            stop_count = 0
            for lemma in self.lemmas:
                if lemma in STOP_WORDS:
                    stop_count += 1
            return stop_count / len(self.lemmas) # Percentage "X% of your text was stoppwords, you have trouble getting to the point!"
        except ZeroDivisionError:
            print("Skuld: I couldn't see the stop word ratio: Every journey needs a hero, but non can divide by ZERO!")
        except Exception as e:
            print(f"Skuld: I wasn't able to count your stop words: {e}")
    
    # 10.A Finding emotion
    def analyze_emotion(self):
        try:
            return detect_emotion_from_lemmas(self.lemmas) # Finds the correct emotion so Skuld can read the rune text most in keeping with the tone of the text
        except Exception as e:
            print(f"Skuld: I wasn't able to find your main emotion: {e}")
    
    # 10.B Find emotions in chunks of 50
    def emotion_progression(self, segment_size=50):
        try:

            segments = []
            for i in range(0, len(self.lemmas), segment_size):
                segment = self.lemmas[i:i+segment_size]
                segments.append(segment)
            
            # Count emotion words in each segment
            love_counts = []
            health_counts = []
            finance_counts = []
            
            for segment in segments:
                # Convert to lowercase for matching
                segment_lower = [lemma.lower() for lemma in segment]
                
                love_count = sum(1 for lemma in segment_lower if lemma in LOVE)
                health_count = sum(1 for lemma in segment_lower if lemma in HEALTH)
                finance_count = sum(1 for lemma in segment_lower if lemma in FINANCE)
                
                love_counts.append(love_count)
                health_counts.append(health_count)
                finance_counts.append(finance_count)
            
            return {
                'segments': list(range(1, len(segments) + 1)),
                'love': love_counts,
                'health': health_counts,
                'finance': finance_counts
                }
        except Exception as e:
            print(f"Skuld: I wasn't able to see your emotion word progression: {e}")

    # Split lemmas into chunks of 50
    # For each chunk, count LOVE/HEALTH/FINANCE words
    # Return three lists: love_counts, health_counts, finance_counts


    # GRAPHICS

    # 1 Sentence Length Bar
    def graph_sentence_length(self):
        try:
            # Data
            sent_dict = self.sentence_lengths()
            if not sent_dict:
                print("Skuld: I'm not seeing any sentences in this dictionary, this will not turn out well!")
                return
            sents = list(sent_dict.keys())
            lengths = list(sent_dict.values())

            # Figure, Plot
            width = max(6, len(sent_dict) * 0.5)
            plt.figure(figsize=(width, 6), dpi=100)
            plt.bar(sents, lengths, color="#2F4F4F")

            # Ticks, Limits
            x_range = list(range(0, max(sents) + 2))
            plt.xticks(x_range[::2])
            max_length = max(lengths)
            plt.ylim(0, max_length * 1.1)
            
            # Grid, Labels
            plt.grid(True, alpha=0.3)
            plt.xlabel("Words per Sentence")
            plt.ylabel("Number of Sentences")
            plt.title("SENTENCE LENGTHS", size=14)

            # Save
            plt.savefig("sentence_length.png")
        except ValueError:
            print("Skuld: I couldn't draw you a bar chart with the sentence lengths: I need some data in the dictionary!")
        except TypeError:
            print(f"Skuld: I couldn't draw you a bar chart with the sentence lengths: I need a dictionary, specifically")
        except KeyError:
            print("Skuld: I couldn't draw you a bar chart with the sentence lengths: I couldn't access the dictionary!")
        except AttributeError:
            print("Skuld: I couldn't draw you a bar chart with the sentence lengths: I wasn't expecting the attribute!")
        except Exception as e:
            print(f"Skuld: Uh, oh! Something went wrong: {e}")
        finally:
            plt.close()

    # 2 Vowel Percentage Hist
    """
    This histogram is designed to divide the data into 10 bins exactly and therefore has no scalability on the x axis.
    """
    def graph_vowel_percentage_plot(self):
        try:
            # Data
            y = self.vowel_percentage()
            if not y:
                print("Skuld: I'm not seeing the percentage of your vowels, how odd!")
                return

            # Figure
            plt.figure(figsize=(10, 6), dpi=100)

            # Plot, Ticks, Limits
            counts, bins, patches = plt.hist(y, bins=10, color="#2F4F4F")
            plt.xticks(range(0, 101, 10))
            plt.ylim(0, max(counts) * 1.1) 
            x_min = min(min(y), 8)
            x_max = max(max(y), 6)
            plt.xlim(x_min, x_max)

            # Grid, Labels
            plt.grid(True, alpha=0.3)
            plt.xlabel("Vowel Percentage Groups (%)")
            plt.ylabel("Word Count")
            plt.title("VOWELS IN WORDS", size=14)
            plt.axhline(sum(y) / len(y), 
                        label="Average Vowel Percentage", 
                        color="#8B008B", 
                        linestyle="--"
                        )
            plt.legend()

            # Save
            plt.savefig("vowels.png")

        except ValueError:
            print("Skuld: I couldn't draw you a histograph showing your vowel usage: I need some data in the list!")
        except TypeError:
            print(f"Skuld: I couldn't draw you a histograph showing your vowel usage: I need a list, specifically!")
        except KeyError:
            print("Skuld: I couldn't draw you a histograph showing your vowel usage: I couldn't access the list!")
        except AttributeError:
            print("Skuld: I couldn't draw you a histograph showing your vowel usage: I wasn't expecting the attribute!")
        except ZeroDivisionError:
            print("Skuld: I couldn't find the average vowel percentage in your words for the histograph: Even Norns cannot divide by ZERO!")
        except Exception as e:
            print(f"Skuld: Uh, oh! Something went wrong with the histograph showing your vowel usage: {e}")   
        finally:
            plt.close()

    # 3 Emotion Plot
    def graph_emotion_lemmas(self):
        try: 
            # Data
            data = self.emotion_progression(segment_size=50)
            if not data:
                print("Skuld: I don't see any emotion words in your text! You must share your feelings if I am to draw you a plot showing your emotion flow.")
                return

            # Figure
            num_segments = len(data['segments'])
            width = max(10, num_segments * 0.5) 
            plt.figure(figsize=(width, 6), dpi=100)

            # Plot
            plt.plot(data['segments'], data['love'], label='LOVE', marker='o', color="#8B0000")
            plt.plot(data['segments'], data['health'], label='HEALTH', marker='s', color="#556B2F")
            plt.plot(data['segments'], data['finance'], label='FINANCE', marker='^', color="#191970")

            # Grid, Labels
            plt.grid(True, alpha=0.3)
            plt.xlabel('Text Segment (every 50 words)')
            plt.ylabel('Emotion Word Count')
            plt.title('EMOTIONAL PROGRESSION', size=14)
            plt.legend()

            # Save
            plt.savefig("emotions.png")

        except ValueError:
            print("Skuld: I couldn't draw the plot showing your emotion flow: I need some data in the dictionary!")
        except TypeError:
            print(f"Skuld: I couldn't draw the plot showing your emotion flow: I need a dictionary, specifically!")
        except Exception as e:
            print(f"Skuld: Uh, oh! Something went wrong with the plot showing your emotion words flow: {e}")   
        finally:
            plt.close()

    # 4 Lemma Barh
    def graph_top_lemmas(self):
        try: 
            # Data
            lemma_freq = self.lemma_frequencies()
            if not lemma_freq:
                print("Skuld: I can't find any lemmas to draw you top 10 lemma graph!")
                return
            sorted_items = sorted(lemma_freq.items(), key=lambda x: x[1], reverse=True) # lambda : sort by the second item in each pair
            top_lemmas = sorted_items[:10]
            x = [lemma[0] for lemma in top_lemmas]
            x = x[::-1]
            y = [count[1] for count in top_lemmas]
            y = y[::-1]

            # Figure, Plot
            plt.figure(figsize=(8, 6), dpi=100)
            plt.barh(x, y, color="#7A8F3A")
            
            # Grid, Labels
            plt.grid(True, alpha=0.3)
            plt.xlabel("Number of times in text")
            plt.ylabel("Lemmas")
            plt.title("TOP 10 LEMMAS", size=14)

            # Save
            plt.savefig("top_lemmas.png")
        
        except ValueError:
            print("Skuld: I couldn't draw the graph to show your top 10 lemmas: I need some data in the dictionary!")
        except TypeError:
            print(f"Skuld: I couldn't draw the graph to show your top 10 lemmas: I need a dictionary, specifically!")
        except Exception as e:
            print(f"Skuld: Gosh darn it! Something went wrong with the graph that shows your top 10 lemmas: {e}")   
        finally:
            plt.close()

    # POS-Usage Pie
    def graph_POS_pie(self):
        try:
            # Data
            tag_dict = self.pos_tags()
            if not tag_dict:
                print("Skuld: I can't find any POS-tags to sort into a pie graph!")
                return
            tag_names = []
            tag_count = []

            # Remove empty tag groups
            for tag, count in tag_dict.items():
                if count > 0:
                    tag_names.append(tag)
                    tag_count.append(count)

            total = sum(tag_count)
            new_names = []
            new_counts = []
            others_total = 0

            # Decide whether each slice is too small
            for name, count in zip(tag_names, tag_count):
                percent = (count / total) * 100
                if percent < 4:
                    others_total += count
                else:
                    new_names.append(name)
                    new_counts.append(count)

            # Add "OTHERS" if needed
            if others_total > 0:
                new_names.append("OTHERS")
                new_counts.append(others_total)

            # Design
            creepy_colors = [
                "#8B0000",  # Dark red (blood)
                "#2F4F4F",  # Dark slate gray
                "#4B0082",  # Indigo (deep purple)
                "#556B2F",  # Dark olive green
                "#8B4513",  # Saddle brown
                "#2C1810",  # Very dark brown
                "#483D8B",  # Dark slate blue
                "#8B008B",  # Dark magenta
                "#556B2F",  # Dark moss
                "#654321",  # Dark chocolate
                "#36454F",  # Charcoal
                "#301934",  # Dark purple
                "#704214",  # Sepia
                "#191970"   # Midnight blue
            ]

            # Figure
            plt.figure(figsize=(6, 6), dpi=100)
            plt.pie(new_counts, labels=new_names, autopct='%1.1f%%', startangle=90, colors=creepy_colors)
            plt.axis("equal")

            # Labels
            plt.title("POS USAGE", size=14)
            plt.legend()

            # Save
            plt.savefig("POS_tags.png")
        
        except ValueError:
            print("Skuld: I couldn't draw the pie with your POS tags: I need some data in the dictionary!")
        except TypeError:
            print(f"Skuld: I couldn't draw the pie with your POS tags: I need a dictionary, specifically!")
        except Exception as e:
            print(f"Skuld: Gosh darn it! Something went wrong with the pie that shows your POS tags: {e}")   
        finally:
            plt.close()

    # Save file: CSV
    def save_file(self, filename="fortune_results"):

        df.to_csv(f"{filename}.csv", index=False)
        try:
            with open(filename, "w") as f:
                data = {
                    "Category" : [
                        "Word Count",
                        "Average Sentence Length",
                        "Number of Question Marks",
                        "Number of Exclamation Marks",
                        "First Word",
                        "Last Word",
                        "Vowel Usage",
                        "Lemma Analysis",
                        "Descriptive Words Percentage",
                        "Stop Word Percentage",
                        "Primary Emotion"
                    ],
                    "Value" : [
                        self.count_words(),
                        f"{self.average_sent():.2f}",
                        self.questionm(),
                        self.exclamationm(),
                        self.first_last()[0],
                        self.first_last()[1],
                        f"{(self.average_vowels() * 100):.2f}%",
                        f"{self.lemma_analysis()[1]:.2f}",
                        f"{(self.pos_tags_adj() * 100):.2f}",
                        f"{(self.stop_words() * 100):.2f}",
                        self.analyze_emotion(),
                    ]
                }

                df = pd.DataFrame(data)

                df.to_csv("my_fortune.csv", index=False)
                print("\nSkuld: Your results have been saved to my_fortune.csv")
                
        except Exception as e:
            print(f"Skuld: Creating: comma ... separated ... values ... No, I cannot create this file for you: {e}")


def main():
    """The main function creates the norn object, then an empty text object and starts the interaction with the user. After collecting enough word tokens from the user the calculations will start."""
    try:
        norn = Norn() 

        norn.greet_user()
        norn.explain_concept()
        norn.explain_imports()

        collected_text = ""
        norn.print_slowly("\nVerðandi: We must collect your words now.")
        choice = norn.collect_first_choice()
        if choice == 'f':
            new_text = norn.read_file()  # Call read_file
        elif choice == 't':
            new_text = norn.ask_questions()  # Call ask_questions
        
        collected_text = norn.collect_text(new_text)
        text_obj = Text(collected_text)

        output_filename = input("Skuld: What shall we name your fortune file? (without extension): ")  
        text_obj.save_file(output_filename) 
        Text.save_file(text_obj)

        norn.interpret(text_obj)
        emotion = Text.analyze_emotion(text_obj)
        print(f"You're thinking about: {emotion.upper()}")
        norn.select_rune(emotion)
        norn.save_analysis(text_obj)

        # Generate visualizations
        text_obj.word_freq_visual()
        text_obj.pos_visual()
        text_obj.sentence_visual()
        text_obj.emotion_visual()
        text_obj.lemma_visual()

        norn.goodbye()
    except Exception as e:
        norn.print_slowly(f"Urður: We have encountered an error: {e}")



if __name__ == '__main__':
    main()