import json
from .config import anthropic_client

def generate_chapter_content(client, chapter_info, learning_prompt):
    prompt = f"""
    You are an expert in {chapter_info['chapter_title']} and the best teacher in the universe. 
    Create detailed content for the following chapter outline:
    
    {json.dumps(chapter_info, indent=2)}
    
    Use the following guidelines to structure and enhance the content:
    
    {learning_prompt}
    
    You must provide the content in markdown format, using appropriate headings, subheadings, and formatting.
    """
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.content[0].text