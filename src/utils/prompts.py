def get_task_prompts():
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
    ]
