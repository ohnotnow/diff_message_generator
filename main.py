import subprocess
import argparse
from gepetto import groq, claude, gpt

system_message = """
You are an AI assistant who specialises in reading the output of `git diff` and providing a well written commit message to go with it.

Your commit message should cover *all* of the changes, not just the major ones.  Where clear, think about the purpose of the change and include those thoughts.

Don't be lazy!

The commit should follow best practices :

* Capitalization and Punctuation: Capitalize the first word and do not end in punctuation. If using Conventional Commits, remember to use all lowercase.
* Mood: Use imperative mood in the subject line. Example - Add fix for dark mode toggle state. Imperative mood gives the tone you are giving an order or request.
* Type of Commit: *Only if the user provides this information*, then specify the type of commit. It is recommended and can be even more beneficial to have a consistent set of words to describe your changes. Example: Bugfix, Update, Refactor, Bump, and so on.
* Length: The first line should ideally be no longer than 50 characters, and the body lines should be restricted to 72 characters.
* Content: Be direct, try to eliminate filler words and phrases in these sentences (examples: though, maybe, I think, kind of). Think like a journalist.
* Use markdown bullet points for the body of the commit message to detail different changes.

Do NOT add extra text, markdown formatting or quotes around the title or body.  The user will be taking the output to directly use in their commit message.

If there is no diff output provided, you should just reply with "No changes to commit".
"""

def main(context="", model="gpt-4-1106-preview"):
    completed_process = subprocess.run(['git', '--no-pager', 'diff', '--color-moved=no'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exit_code = completed_process.returncode
    diff_stdout = completed_process.stdout.decode('utf-8')
    diff_stderr = completed_process.stderr.decode('utf-8')

    if exit_code != 0:
        print("Error running `git diff`")
        print(diff_stderr)
        exit(1)

    bot = gpt.GPTModelSync()
    prompt = f"I have the following output from running `git diff`.  Could you give me a commit message for it?  <diff>{diff_stdout}</diff>"
    if context:
        prompt = f"{context}\n\n{prompt}\n\n"
    response = bot.chat([
        {
            'role': 'system',
            'content': system_message
        },
        {
            'role': 'user',
            'content': prompt
        }
    ], model=model)
    commit_message = response.message.strip('"').strip('```').strip()
    print(commit_message)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--model", type=str, default="gpt-4-1106-preview")
    args.add_argument("--context", type=str, default="")
    args = args.parse_args()
    main(args.context, args.model)
