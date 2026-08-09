from stable_baselines3 import PPO
from grid_env import GridEnv

env = GridEnv(size=5)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

obs, _ = env.reset()
for _ in range(50):
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()
    if terminated or truncated:
        obs, _ = env.reset()