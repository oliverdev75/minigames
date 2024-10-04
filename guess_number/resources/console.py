from .colors import reset, blue, red, yellow, green

def info(message: str) -> None:
    blue()
    print(" INFO ", end="")
    reset()
    print(" " + message + "\n")

def error(message: str) -> None:
    red()
    print(" ERROR ", end="")
    reset()
    print(" " + message + "\n")

def warning(message: str) -> None:
    yellow()
    print(" WARNING ", end="")
    reset()
    print(" " + message + "\n")

def success(message: str) -> None:
    green()
    print(" SUCCESSFULLY ", end="")
    reset()
    print(" " + message + "\n")

def prompt(question: str, allowed_answers: list) -> str:
    allowed = False
    answer = ""
    while not allowed:
        answer = input(question)
        if answer.strip() in allowed_answers:
            allowed = True
        else:
            answers = ", ".join(allowed_answers)
            error(f"The answer must be between: {answers}")
    return answer

def prompt_int(question: str, allowed_answers: list) -> int:
    allowed = False
    int_answer = 0
    while not allowed:
        try:
            answer = input(question)
            int_answer = int(answer)
            if int_answer in allowed_answers:
                allowed = True
        except Exception:
            printable_answers = []
            for allowed_answer in allowed_answers:
                printable_answers.append(str(allowed_answer))
            error(f"The answer must be a number between: {printable_answers}")
    return int_answer