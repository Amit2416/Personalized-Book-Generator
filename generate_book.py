import json
import os
from src.config import anthropic_client, openai_client
from src.book_structure import generate_book_structure
from src.chapter_generation import generate_chapter_content
from src.content_review import review_content
from src.content_revision import revise_content
from src.file_operations import save_chapter, combine_chapters

def generate_textbook(topic, learning_prompt, output_dir):
    # Generate book structure
    book_structure = generate_book_structure(topic)
    print(book_structure)  # Print the generated structure
    book_data = json.loads(book_structure)
    
    for chapter in book_data['chapters']:
        print(f"Processing chapter {chapter['chapter_number']}: {chapter['chapter_title']}")
        
        # Generate initial content
        initial_content = generate_chapter_content(anthropic_client, chapter, learning_prompt)
        print("Initial content generated.")
        
        # Review content
        review = review_content(openai_client, initial_content, chapter['chapter_title'])
        print("Content reviewed.")
        
        # Revise content based on review
        revised_content = revise_content(initial_content, review, chapter['chapter_title'])
        print("Content revised.")
        
        # Save revised content
        save_chapter(int(chapter['chapter_number']), chapter['chapter_title'], revised_content, output_dir)
    
    # Combine all chapters into a single file
    combined_file = os.path.join(output_dir, "combined_textbook.md")
    combine_chapters(output_dir, combined_file)

if __name__ == "__main__":
    topic = "HTML"
    learning_prompt = """
    Create an outline for this chapter following this structure:

    a) Introduction
    b) Core Content (3-5 subsections)
    c) Application
    d) Review and Critical Thinking
    e) Closing Thought

    For each section, provide detailed content as follows:

    a) Introduction:
    - Develop a simple story with real-world analogies related to the chapter topic
    - Write a brief introduction to the topic, assuming no prior knowledge
    - State 3-5 clear learning objectives
    - Create an engaging hook (an intriguing question, surprising fact, or continuation of the opening story)

    b) Core Content:
    - Divide this section into 3-5 subsections following the What, Why, How, Where, When structure
    - For each subsection:
      1. What: Explain the concept clearly, using simple language before introducing technical terms
      2. Why: Explain the importance of the concept and how it relates to the bigger picture
      3. How: Provide a step-by-step breakdown of processes or mechanisms, using analogies and stories
      4. Where & When: Give examples of where and when this concept applies in nature, including case studies
      5. Interesting Facts: Include 2-3 fun facts or surprising information to make the content memorable

    c) Application:
    - Design a hands-on activity or experiment related to the topic, with clear instructions and safety guidelines
    - Explain how the concept applies to everyday life or current issues

    d) Review and Critical Thinking:
    - Summarize 5-7 key points from the chapter
    - Create 3-5 review questions with hints that guide students back to relevant content
    - Develop 2-3 critical thinking questions that encourage students to apply knowledge to new scenarios
    - Suggest 2-3 ideas for further exploration of the topic

    e) Closing Thought:
    - Reflect on the chapter's main ideas
    - Preview how this topic connects to upcoming chapters

    Throughout the outline:
    - Suggest diverse presentation methods (e.g., diagrams, analogies, stories)
    - Include examples from various plant species, especially common plants students might encounter daily
    - Indicate where to use a conversational tone and incorporate light humor or amusing anecdotes
    """
    output_directory = "HTML"

    generate_textbook(topic, learning_prompt, output_directory)