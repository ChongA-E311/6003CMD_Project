# Dissertation Project
# High-level goal:
#   Make bomb

# -------------------------
# Inputs:
#   - What goes into the system?
#   (environment? data? user input?)

# Outputs:
#   - What comes out?
#   (movement path? score? visualization?)

# Core components:
#   1. Environment / world
#   2. Agent / logic
#   3. Evaluation / metrics

# Plan:
#   - Build environment
#   - Add simple agent
#   - Add learning/adaptation
#   - Measure performance

# Goal: Create an agent that learns to move items to a target efficiently

# Inputs:
#   - Grid size
#   - Item positions
#   - Target location

# Outputs:
#   - Path taken
#   - Total steps

# Components:
#   - GridWorld
#   - Agent
#   - Reward function

def create_environment():
    import gymnasium as gym

    env = gym.make("CartPole-v1")
    obs, info = env.reset()

    print("Observation:", obs)
    print("Action space:", env.action_space)

    env.close()

def create_agent():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    from transformers import pipeline

    llm = pipeline("text-generation", model="distilgpt2")
    print(llm("")[0]["generated_text"])
        
    return

def run_episode():
    pass

def evaluate():
    pass

def main():
    create_agent()
    
if __name__ == "__main__":
    main()