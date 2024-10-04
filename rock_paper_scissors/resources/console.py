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

def prompt(question: str, allowedAnswers: list) -> str:
    allowed = False
    answer = ""
    while not allowed:
        answer = input(question)
        if answer.strip() in allowedAnswers:
            allowed = True
        else:
            answers = ", ".join(allowedAnswers)
            error(f"The answer must be between: {answers}")
    return answer

def prompt_int(question: str, allowedAnswers: list) -> int:
    allowed = False
    answer = 0
    while not allowed:
        try:
            answer = input(question)
            intAnswer = int(answer)
            if intAnswer in allowedAnswers:
                allowed = True
            else:
                error(f"The answer must be a number between: {printableAnswers}")
        except Exception:
            printableAnswers = []
            for allowedAnswer in allowedAnswers:
                printableAnswers.append(str(allowedAnswer))
            error(f"The answer must be a number between: {printableAnswers}")
    return intAnswer