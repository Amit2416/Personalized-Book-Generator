import os

def save_chapter(chapter_number, chapter_title, content, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = f"chapter_{chapter_number:02d}_{chapter_title.lower().replace(' ', '_')}.md"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved chapter {chapter_number}: {chapter_title}")

def combine_chapters(directory, output_file):
    md_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    md_files.sort()

    combined_content = ""
    for md_file in md_files:
        file_path = os.path.join(directory, md_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            combined_content += file.read() + "\n\n"

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(combined_content)

    print(f"All .md files combined into {output_file}")