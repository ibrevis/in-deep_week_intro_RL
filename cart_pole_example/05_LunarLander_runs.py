import gymnasium as gym
import time

env = gym.make("LunarLander-v3", render_mode="human")

for episode in range(2):
    env.reset()
    episode_return = 0.
    for step in range(500):
        action = env.action_space.sample()  # Take a random action
        state, reward, terminated, truncated, _ = env.step(action)
        episode_return += reward
        time.sleep(0.05)
        if terminated or truncated:
            time.sleep(2)
            break
    print(f"Episode: {episode}, Total Return: {episode_return}")
env.close()