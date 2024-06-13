from llama_cpp import Llama


class LLM:
    def __init__(self) -> None:
        print("INFO: Loading model...")
        self.llm = Llama.from_pretrained(
            repo_id="MaziyarPanahi/Qwen2-1.5B-Instruct-GGUF",
            filename="Qwen2-1.5B-Instruct.Q4_K_M.gguf",
            local_dir="./models",
            n_ctx=4096,
            n_gpu_layers=-1,
            flash_attn=True,
            cont_batching=True,
            verbose=False,
        )
        print("INFO: Model loaded successfully.")
        self.system_prompt = "You are responsible for rephrasing, summarizing, or editing various text snippets to make them more concise, coherent, and engaging. You are also responsible for writing emails, messages, and other forms of communication."

    def generate(
        self, text: str, max_tokens: int = 4096, temperature: float = 0.3
    ) -> str:
        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {"role": "user", "content": text},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response["choices"][0]["message"]["content"]
