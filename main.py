import subprocess
from gepetto import groq

system_message = """
You are an AI assistant who specialises in reading the output of `git diff` and providing a well written commit message to go with it.  The commit should follow best practices :

* Capitalization and Punctuation: Capitalize the first word and do not end in punctuation. If using Conventional Commits, remember to use all lowercase.
* Mood: Use imperative mood in the subject line. Example - Add fix for dark mode toggle state. Imperative mood gives the tone you are giving an order or request.
* Type of Commit: *Only if the user provides this information*, then specify the type of commit. It is recommended and can be even more beneficial to have a consistent set of words to describe your changes. Example: Bugfix, Update, Refactor, Bump, and so on.
* Length: The first line should ideally be no longer than 50 characters, and the body lines should be restricted to 72 characters.
* Content: Be direct, try to eliminate filler words and phrases in these sentences (examples: though, maybe, I think, kind of). Think like a journalist.
"""

# run `git diff` and capture it's output
diff = subprocess.check_output(['git', 'diff', 'HEAD^', 'HEAD'])

# run the diff through our model and get a commit message
bot = groq.GroqModelSync()
response = bot.chat([
    {
        'role': 'system',
        'content': system_message
    },
    {
        'role': 'user',
        'content': f"I have the following output from running `git diff`.  Could you give me a commit message for it?  <diff>{diff}</diff>"
    }
])
print(response.message)
