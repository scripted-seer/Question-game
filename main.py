import json

# Load json file :
def LoadQuestion(filename):
    with open('quizs.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# The game runs in this function :
def RunQuiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"question :\n{i} : {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"{idx + 1}. {option}")

        while True:
            try:
                user_answer = int(input("your answer : "))
                break  
            except ValueError:
                print("just number ❌❌")

        if user_answer == q['correct_answer']:
            print("True ✅")
            score += 1
        else:
            print("False ❌") 
    return score

# Display the result of the game
def ShowResult(total, score):
    percentage = (score / total) * 100
    print(f"\n--- final result ---\nYour score {score}/{total}\nSuccess rate: {percentage:.1f}%")

# just use this :>
def main():
    questions = LoadQuestion('quizs.json')
    total_questions = len(questions)
    final_score = RunQuiz(questions)
    ShowResult(total_questions, final_score)

if __name__ == "__main__":
    main()