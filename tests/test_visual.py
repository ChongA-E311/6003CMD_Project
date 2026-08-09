from grid_env import GridEnv
import time

env = GridEnv(size=10, render_mode="human")
obs, info = env.reset()

for _ in range(50):
    env.render()
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)

    if terminated:
        print("Reached goal!")
        break

    time.sleep(0.2)

env.close()