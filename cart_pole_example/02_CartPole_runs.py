import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human")

for episode in range(10):
    state, _ = env.reset()
    for step in range(100):
        print(f"Episode: {episode}, Step: {step}")
        action = env.action_space.sample()  # Take a random action
        state, reward, terminated, truncated, _ = env.step(action)
        time.sleep(0.05)
        if terminated or truncated:
            time.sleep(2)
            break
env.close()