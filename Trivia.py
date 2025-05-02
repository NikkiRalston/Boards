import random

#making a class called Question
#this holds the questions, choices, and answers
class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
    
    def ask(self):
        # displays the question and choices
        print(f"\n{self.question}")
        for choice in self.choices:
            print(choice)
            #tells you how to put your answer 
        user_input = input("Your answer (A/B/C): ").strip().upper()
        return user_input == self.answer.upper()


#making the hash table and naming it "trivia_bank"
#making 3 subjects Science, History, and Math
trivia_bank = {
    "Science": [
        Question("What planet is known as the Red Planet?", ["A) Venus", "B) Mars", "C) Jupiter"], "B"),
        Question("What gas do plants absorb?", ["A) Oxygen", "B) Hydrogen ", "C)  Carbon Dioxide"], "C"),
        Question("What does the Earth revolve around?", ["A) The Sun", "B) The Moon", "C) Mars"], "A"),
    ],
    "History": [
        Question("Who was the first president of the United States?", ["A) Abraham Lincoln", "B) George Washington", "C) Thomas Jefferson"], "B"),
        Question("In which year did World War II end?", ["A) 1945", "B) 1939", "C) 1950"], "A"),
        Question("What country built the Great Wall?", ["A) Japan", "B) China", "C) Korea"], "B"),
    ],
    "Math": [
        Question("What is 2 + 2?", ["A) 3", "B) 4", "C) 5"], "B"),
        Question("What is 10 ÷ 2?", ["A) 5", "B) 4", "C) 6"], "A"),
        Question("What is 3 × 3?", ["A) 6", "B) 10", "C) 9"], "C"),
    ],
}

#the main area
def play_trivia():
    score = 0
    total = 0
    #welcome message/categories
    print("welcome to the trivia!\n")
    print("categories:")
    for category in trivia_bank:
        print(f"- {category}")
    #tells you to pick a category
    selected = input("\npick a category: ").strip().title()
    #if selected category isnt found, you will get a try again message 
    if selected not in trivia_bank:
        print("category not found. Try again.")
        return

    questions = trivia_bank[selected]
    #the questions get shuffled randomly each game
    random.shuffle(questions)
    
    for q in questions:
        total += 1
        if q.ask():
            #tells you if its right plus 1 point
            print("That's correct!")
            score += 1
        else:
            #tells you the right answer
            print(f"Sorry, That's incorrect. The correct answer was: {q.answer}")
    #your score at the end of the game
    print(f"\nYour final score: {score}/{total}")


if __name__ == "__main__":
    play_trivia()