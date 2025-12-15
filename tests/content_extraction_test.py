from ..core.content_extractor import extract_content

def test_extract_content():
    text = "This is a sample article."
    result = extract_content(text)
    assert result == text
