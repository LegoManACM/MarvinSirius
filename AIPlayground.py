from gpt4all import GPT4All
import time

modelA = GPT4All("Llama-3.2-1B-Instruct-Q4_0", n_threads=2, device="cpu",)
modelB = GPT4All("Llama-3.2-1B-Instruct-Q4_0", n_threads=2, device="cpu",)

with modelA.chat_session():
    with modelB.chat_session():
        MessageB = modelB.generate("You are currently speaking with another LLM", max_tokens=150)

        while True:
            MessageA = modelA.generate(MessageB, max_tokens=150)
            print("\n--- A " + "-"*15)
            print(MessageA)
            MessageB = modelB.generate(MessageA, max_tokens=150)
            print("\n--- B " + "-"*15)
            print(MessageB)
