from .config import anthropic_client

def generate_book_structure(topic):
    prompt = f'''
    As an expert educator and author, create a detailed structure for an educational book on {topic}.
    The book is aimed at beginners.

    Please provide:
    1. A compelling book title
    2. 5-7 chapter titles
    3. For each chapter, list main topics or key points to be covered

    Structure the output as a JSON object using the following format:

    Do not add any sentence to explain the output.
    
    class BookStructure:
        def __init__(self, title, genre, length):
            self.title = "<Book Title>"
            self.topic = "{topic}"
            self.chapters = [
                
                    "chapter_number": "<Chapter Number>",
                    "chapter_title": "<Chapter Title>",
                    "chapter_outline": List of Main Topics in normal progression of learning from easy to hard
                
                ...
            ]
    '''
    response = anthropic_client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.content[0].text