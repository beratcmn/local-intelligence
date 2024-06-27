from llama_cpp import Llama


class LLM:
    """
    LLM class encapsulates the logic to load a pre-trained language model and generate text based on input prompts.
    """

    def __init__(self) -> None:
        print("INFO: Loading model...")
        self.system_prompt = (
            "You are responsible for rephrasing, summarizing, or editing various text snippets to make them more "
            "concise, coherent, and engaging. You are also responsible for writing emails, messages, and other forms "
            "of communication."
        )
        self.llm = Llama.from_pretrained(
            repo_id="MaziyarPanahi/Qwen2-1.5B-Instruct-GGUF",
            filename="Qwen2-1.5B-Instruct.Q4_K_M.gguf",
            local_dir="./models",
            n_ctx=2048,
            n_batch=1024,
            n_gpu_layers=-1,
            flash_attn=True,
            cont_batching=True,
            verbose=False,
        )
        print("INFO: Model loaded successfully.")

    def generate(
        self, text: str, max_tokens: int = 2048, temperature: float = 0.3
    ) -> str:
        """
        Generate a response from the language model based on the provided text.

        :param text: Input text prompt for the model.
        :param max_tokens: Maximum number of tokens to generate.
        :param temperature: Sampling temperature for generation.
        :return: Generated text response.
        """
        response = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": text},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response["choices"][0]["message"]["content"]
