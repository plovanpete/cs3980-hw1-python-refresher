def echo(text: str, repetitions: int = 3) -> str:
    '''Imitates a reach-world echo.'''
    
    # Initializes an empty list
    echoed_lines = []

    # Loops through the range of values in reverse order, using the number of repetitions.
    for i in range(min(len(text), repetitions, len(text)), 0, -1):
        line = text[-i:]
        echoed_lines.append(line)
    
    # If the repetitions are greater than one, we decrease it by one and extend the list.
    if repetitions > 1:
        repetitions -= 1
        echoed_lines.extend([text[:i-1] + "."] * (repetitions - 1))

    return '\n'.join(echoed_lines)

# Main function that runs for the echo.
if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
