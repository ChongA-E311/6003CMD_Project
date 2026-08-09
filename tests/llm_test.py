from transformers import pipeline
from grid_env import GridEnv
import numpy as np

llm = pipeline("text-generation", model="distilgpt2")

def parse_action(text):
    text = text.lower()

    if "up" in text:
        return 0
    if "down" in text:
        return 1
    if "left" in text:
        return 2
    if "right" in text:
        return 3

    # handle numeric outputs
    if "0" in text: return 0
    if "1" in text: return 1
    if "2" in text: return 2
    if "3" in text: return 3

    # fallback (random move)
    return np.random.randint(0,4)

env = GridEnv(size=5)
obs, _ = env.reset()

for step in range(10):
    print ("Prompt:")
    prompt = f"Pos {obs}, goal {env.goal_pos}. Move:"

    out = llm(prompt, max_new_tokens=3,do_sample=False, return_full_text=False, pad_token_id=llm.tokenizer.eos_token_id)[0]["generated_text"]
    action = parse_action(out)

    print("LLM output:", out, "\n")
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()

    if terminated:
        print("Reached goal!")
        break