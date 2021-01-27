import question1
import question2
import question3
import question4


def solve_quetion(choice):
    """
    This function receives user input for a displayed question set and then it
    look for a input in the dictionary and then triggers a method named
    'solution' for that particular question number in return call.
    """
    problem_set = {
        1: question1.solution,
        2: question2.solution,
        3: question3.solution,
        4: question4.solution,
    }
    return problem_set.get(
        choice, lambda: print("wrong number entered...!"))()


if __name__ == '__main__':
    with open('question_set.txt', 'r') as questions:
        parsed = questions.read()
        print(parsed)
    try:
        choice = int(input(
            "\nEnter the Question number that you want to obtain"
            "a Solution in a graph format: "
            ))
        solve_quetion(choice)
    except ValueError:
        print("Enter a number, not a string...!")
