from .config import openai_client

def review_content(client, content, chapter_title):
    review_prompt = f"""
    You are an expert educator and subject matter expert in {chapter_title}. Review the following textbook content for accuracy, 
    clarity, and engagement. Suggest improvements or corrections where necessary. 
    Focus on major topics and overall structure rather than minor details.

    Content to review:
    {content}

    Provide your review in the following format:
    1. Overall Assessment
    2. Strengths
    3. Areas for Improvement
    4. Specific Suggestions
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert textbook reviewer and educator."},
            {"role": "user", "content": review_prompt}
        ]
    )
    return response.choices[0].message.content
