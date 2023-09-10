'''
My OpenAI Gym game environment for Bomber game

'''

import gymnasium as gym

import numpy as np

class GymBomber(gym.Env):

    def __init__(self):

        gym.Env.__init__(self)

        # Use [-1,+1] for observation space an action space
        self.observation_space = gym.spaces.Box(-1, +1, shape=(1,), dtype=np.float32)
        self.action_space = gym.spaces.Box(-1, +1, (1,), dtype=np.float32)

        self.reset()

    def step(self, action):

        state = np.zeros(1, dtype=np.float32)
        reward = 0
        terminated = False
        truncated = False
        info = {}

        return state, reward, terminated, truncated, info

    def render(self, mode='human'):

        pass

    def reset(self, seed=None, options={}):

        if seed is not None:

            pass  # XXX Seed the random-number generator

        obs = np.zeros(1, dtype=np.float32)

        info = {}

        return obs, info

    def close(self):

        gym.Env.close(self)

        
