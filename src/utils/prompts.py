def get_task_prompts():
    """
    Return a list of task prompts for various text processing tasks. Each prompt is designed to guide the language model
    in performing a specific task such as summarizing, composing an email, fixing grammar, extracting keywords, or explaining text.

    :return: List of dictionaries, each containing a 'task' and its corresponding 'prompt'.
    """
    return [
        {
            "task": "Summarize",
            "prompt": """
Summarize the text below:

{text}

Summary:
""".strip(),
        },
        {
            "task": "Compose Mail",
            "prompt": """
Compose an email about the text below:

{text}

Email:
""".strip(),
        },
        {
            "task": "Fix Grammar",
            "prompt": """
Fix the grammar in the text below:

{text}

Corrected Text:
""".strip(),
        },
        {
            "task": "Extract Keywords",
            "prompt": """
List the keywords in the text below:

{text}

Keywords:
""".strip(),
        },
        {
            "task": "Explain",
            "prompt": """
Explain the text below:

{text}

Explanation:
""".strip(),
        },
    ]
