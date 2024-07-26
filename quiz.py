
quiz = [
    {
        "question": "What is 1+1?",
        "choices": ["1", "2", "3", "4"],
        "answer": "2"
    },
    {
        "question": "What is the spelling of the word below?",
        "choices": ["recieve","reiceve","receive", "recievie"],
        "answer": "receive"
    },
    {
        "question": "How many points is a free throw?",
        "choices": ["1", "2", "3", "4"],
        "answer": "1"
    },
    {
        "question": "What colour is a UK bus?",
        "choices": ["Green", "Blue", "Green", "Red"],
        "answer": "Red"
    },
    {
        "question": "How many states are there in the USA?",
        "choices": ["48", "49", "50", "51"],
        "answer": "50"
    }
]


def start_quiz(quiz): 
    score = 0
    for item in quiz:
        print(f"\n{item['question']}")
        for i, choice in enumerate(item['choices']):
            print(f"{i + 1}. {choice}")
        
        while True:  
            user_answer = input("Enter the number of your answer: ")
            try:
                if item['choices'][int(user_answer) - 1] == item['answer']:
                    score += 1
                    print("Correct answer.")
                    break   
                else: 
                    print(f"Incorrect answer. The correct answer is:\n{item['answer']}")
                    break  
            except (ValueError, IndexError):
                print("Invalid Input. Please enter a number between 1-4.")    

    print(f"\nYou have finished the quiz. Your score is {score}/{len(quiz)}.")


start_quiz(quiz)
