#!/usr/bin/env python3
'''
Python distutils setup file for gym-bomber module.
'''

import gymnasium as gym

from stable_baselines3 import DDPG

env = gym.make('gym_bomber:GymBomber-v0')

model = "gym_bomber/Trained_Agents/DDPG_2000_Epoch.zip"

loaded_model = DDPG.load(model)

for i_episode in range(20):

    observation, _ = env.reset(seed=123)

    print(observation)
    for t in range(100):

        env.render()

        action, _ = loaded_model.predict(observation, deterministic=True)

        # action = env.action_space.sample()

        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:

            print("Episode finished after {} timesteps".format(t+1))
            break

env.close()
