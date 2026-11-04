import random

question_bank = [
    {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome"], "correct": "Paris"},
    {"question": "Which planet is the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "correct": "Mars"},
    {"question": "What is the chemical symbol for gold?", "options": ["Gd", "Go", "Ag", "Au"], "correct": "Au"},
    {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "correct": "Pacific"},
    {"question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Picasso", "Da Vinci", "Monet"], "correct": "Da Vinci"},
    {"question": "What is the square root of 144?", "options": ["10", "11", "12", "13"], "correct": "12"},
    {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Carbon Dioxide"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "correct": "7"},
    {"question": "What is the tallest mountain in the world?", "options": ["K2", "Kilimanjaro", "Everest", "Denali"], "correct": "Everest"},
    {"question": "Which metal is liquid at room temperature?", "options": ["Iron", "Mercury", "Copper", "Aluminum"], "correct": "Mercury"},
    {"question": "What is the primary currency of Japan?", "options": ["Yuan", "Won", "Yen", "Dollar"], "correct": "Yen"},
    {"question": "How many bones are in an adult human body?", "options": ["206", "208", "210", "212"], "correct": "206"}

    
]

def millionaire_game():
    print("Welcome to the Millionaire Game!")
    print("You will be asked a series of questions. Answer correctly to win 70,000,000!")
    prize_money = [1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 5000000, 10000000, 70000000]
    random.shuffle(question_bank)
    game_questions = question_bank[:10]

    score = 0
    Total_rounds_to_win = 10
    
    # Run through the 10 random questions
    for index, q_data in enumerate(game_questions):
        print(f"\nQuestion {index + 1} of {Total_rounds_to_win}:")
        print(q_data["question"])
        
        # Shuffle the options for each question
        display_options = q_data["options"].copy()
        random.shuffle(display_options)

        #Print the choices
        labels = ["A", "B", "C", "D"]
        option_mapping = {}
        for label, option in zip(labels, display_options):
            option_mapping[label] = option
            print(f"{label}: {option}")

        #Get player answer
        player_choice = input("Enter your choice (A, B, C, D): ").strip().upper()

        #Validate input
        while player_choice not in option_mapping:
            print("Invalid choice. Please select A, B, C, or D.")
            player_choice = input("Enter your choice (A, B, C, D): ").strip().upper()

        #Answer checking
        chosen_answer = option_mapping[player_choice]
        if chosen_answer == q_data["correct"]:
            score += 1
            print(f"Correct! You've won ${prize_money[index]:,}!")
        else:
            print(f"Wrong answer. The correct answer was: {q_data['correct']}.")
            # FIXED: Prevents index out of bounds error if they lose on question 1
            winnings = prize_money[score-1] if score > 0 else 0
            print(f"GAME OVER! You left with ${winnings:,}!")
            return

    #Win condition
    if score == Total_rounds_to_win:
        print("\n========================================")
        print("CONGRATULATIONS! You answered all 10 questions correctly!")
        print("🎉 YOU WIN THE 70,000,000 GRAND PRIZE! 🎉")
        print("========================================")

millionaire_game()
