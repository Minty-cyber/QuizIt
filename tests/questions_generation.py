def test_quiz_generation():
    content = "AI helps generate questions."
    quiz = generate_quiz(content, num_questions=5)
    assert len(quiz) == 5
