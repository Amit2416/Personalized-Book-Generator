from .config import anthropic_client

def revise_content(original_content, review, chapter_title):
    revision_prompt = f"""
    You are an expert textbook author specializing in {chapter_title}. Revise the following content based on the provided review. 
    Maintain the original structure and format, but improve the content according to the suggestions.

    Original Content:
    {original_content}

    Review:
    {review}

    Provide the revised content in markdown format, maintaining the original headings and subheadings structure. Rewrite the whole thing again. Don't say that this is the same as before. You must not be lazy.
    """

    response = anthropic_client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": revision_prompt}
        ]
    )
    return response.content[0].text