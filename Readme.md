# Git Diff Commit Message Generator

## Overview
This Python script automates the generation of commit messages for Git repositories. It specializes in interpreting the output of `git diff` and crafting comprehensive commit messages that adhere to best practices. The script is designed for developers who need to produce clear, concise, and standardized commit messages in their version control workflow.

## Features
- **Git Diff Parsing**: Automatically reads and analyzes the output from `git diff`.
- **Commit Message Generation**: Creates commit messages that cover all changes, major and minor.
- **Best Practices Adherence**: Ensures commit messages follow capitalization, punctuation, mood, length, and content guidelines.
- **Direct Output**: Provides commit messages formatted for immediate use in Git.

## Requirements
- Python 3
- Access to a Git repository

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ohnotnow/diff_message_generator.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd diff_message_generator
   ```
3. Make sure required libraries are installed:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To use the script, follow these steps:
1. Ensure you are in the directory containing your Git repository.
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will output a commit message based on the latest `git diff`.

## Example
Running the script in a Git repository with recent changes:
```bash
python main.py
```
Output:
```
Refactor code for improved readability

- Optimized import statements
- Updated variable names for clarity
- Enhanced error handling in file processing
```

## Options
You can optionally add some extra freeform context to the LLM and also specifiy which model you want to use.
```bash
python main.py --model='gpt-3.5-turbo' --context='Feature: add new thing so users can do X'
```

## Customisation
There is a system prompt at the top of the script which tells the LLM the kind of commit messages you prefer.  Change that to make it more to your liking.

## Troubleshooting
If you encounter an error with `git diff`, the script will output the specific error message. Ensure you have the correct permissions and that your Git repository is properly initialized.
