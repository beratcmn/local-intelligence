from utils.llm import LLM

llm = LLM()

while True:
    text = input("Enter text: ")
    if text == "exit":
        break
    print(llm.generate(text, max_tokens=256))
