import gymnasium as gym
from stable_baselines3 import SAC

env = gym.make("Pendulum-v1")  # continuous control

model = SAC("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=5000)

obs, _ = env.reset()
for _ in range(1000):
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, _ = env.reset()

env.close()
print("SAC test finished.")