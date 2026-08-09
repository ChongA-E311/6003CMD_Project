from grid_env import GridEnv
import time

env = GridEnv(size=10)
obs, info = env.reset()

for _ in range(20):
    env.render()
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)

    if terminated:
        print("Reached goal!")
        break

    time.sleep(0.5)