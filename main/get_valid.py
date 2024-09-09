def get_valid_input(prompt: str, validate_func, error_msg: str) -> str:
    while True:
        user_input = input(prompt)
        if validate_func(user_input):
            return user_input
        print(error_msg)
