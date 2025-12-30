from gpt4all import GPT4All
import time

modelA = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", n_threads=2, device="gpu",)
#modelB = GPT4All("Llama-3.2-1B-Instruct-Q4_0", n_threads=2, device="cpu",)

conv = "USER: you are ORCA, an AI assistant, do as the USER prompts,"

with modelA.chat_session():
    while True:
        conv = conv + "USER: " + input() + "\n"
        output = modelA.generate(conv, max_tokens=150)

        conv += "ORCA: " + output + "\n"

        print(output)
        print("-"*15)
        print("\n")

