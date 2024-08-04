# Personalized Book Generator

This project is a modular book generator that creates educational textbooks using AI-powered content generation, review, and revision.

## Features

- Generate book structure based on a specific topic
- Create detailed chapter content
- Review and revise content for accuracy and engagement
- Save individual chapters and combine them into a single file - mark down format

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/book-generator.git
   cd book-generator
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in your API keys:
   ```
   cp .env.example .env
   ```

## Usage

Run the main script to generate a textbook:

```
python -m src.main
```

The generated chapters will be saved in the specified output directory (default is "HTML"), and a combined file will be created as `combined_textbook.md` in the same directory.

## Customization

You can modify the `topic` and `learning_prompt` variables in `src/main.py` to generate different types of textbooks.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.# Personalized-Book-Generator
