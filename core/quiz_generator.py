def generate_quiz(content, num_questions=5):
    """
    Generates a quiz based on the provided content.

    Args:
        content (str): The content to generate quiz questions from.
        num_questions (int): The number of questions to generate. Default is 5.

    Returns:
        list: A list of quiz questions.
    """
    # Placeholder implementation
    # Replace this with actual quiz generation logic
    return [f"Question {i+1} based on: {content}" for i in range(num_questions)]


# Example usage
quiz = generate_quiz("Sample content", num_questions=5)
