'''
My OpenAI Gym game environment for Bomber game

'''

import gymnasium as gym
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class GymBomber(gym.Env):

    def __init__(self):

        gym.Env.__init__(self)
        self.action_space = gym.spaces.Box(low=-10, high=10, shape=(1,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(5,), dtype=np.float32)
        self.gravity = 9.81
        self.timestep = 0.1
        self.epoch = 0
        self.plane_y = 100
        self.plane_x = 0
        self.fig, self.ax = plt.subplots()
        self.reset()

    def step(self, action):
        force_x = action[0]
        self.dx += force_x * self.timestep
        self.dy -= self.gravity * self.timestep
        self.plane_y = 100
        self.plane_x += 3
        old_missile_x = self.missile_x
        old_missile_y = self.missile_y

        self.missile_x += self.dx * self.timestep + 0.5 * force_x * self.timestep ** 2
        self.missile_y += self.dy * self.timestep - 0.5 * self.gravity * self.timestep ** 2

        if self.missile_y <= 0:
            terminated = True
            truncated = True
            # done = True
            self.missile_y = 0
            # reward = -abs(self.target_x - self.missile_x)
            reward = -abs(self.target_x - self.missile_x)
            if abs(self.target_x - self.missile_x) < 3:
                reward += 1000
            elif abs(self.target_x - self.missile_x) < 15:
                reward += 500
            elif abs(self.target_x - self.missile_x) < 25:
                reward += 100

        else:
            terminated = False
            truncated = False
            distance_to_target_before_x = abs(old_missile_x - self.target_x)
            distance_to_target_before_y = abs(old_missile_y - 0)
            distan = np.sqrt(distance_to_target_before_x**2 + distance_to_target_before_y**2)
            reward = -distan

        state = np.array([self.missile_x, self.missile_y, self.target_x, self.target_y, self.target_x - self.missile_x])

        info = {}

        return state, reward, terminated, truncated, info

    def render(self, mode='human'):
        self.ax.clear()
        self.ax.set_xlim(0, 110)
        self.ax.set_ylim(0, 110)
        # Draw missile
        # self.ax.scatter(self.missile_x, self.missile_y, c='b', label='Missile')

        # Load the icon image
        Missile_icon = mpimg.imread('gym_bomber/Visualization/Missile.png')
        Corona_icon = mpimg.imread('gym_bomber/Visualization/Corona.png')
        Explosion_icon = mpimg.imread('gym_bomber/Visualization/explosion.png')
        Plane_icon = mpimg.imread('gym_bomber/Visualization/Plane.png')
        Desert = mpimg.imread('gym_bomber/Visualization/Desert.png')
        self.ax.imshow(Desert, extent=[0, 110, 0, 110])

        if self.plane_x <= 50:
                self.ax.imshow(Plane_icon, extent=[self.plane_x - 10, self.plane_x + 10, self.plane_y - 10, self.plane_y + 10])
                self.ax.imshow(Corona_icon, extent=[self.target_x - 5, self.target_x + 5, self.target_y, self.target_y + 10])
                self.ax.set_xticks([])
                self.ax.set_yticks([])

        if self.plane_x >= 50:
            self.ax.imshow(Plane_icon, extent=[self.plane_x - 10, self.plane_x + 10, self.plane_y - 10, self.plane_y + 10])

            if self.missile_y <= 2:
                self.ax.imshow(Explosion_icon, extent=[self.target_x - 20, self.target_x + 20, self.target_y - 3 , (self.target_y + 10) + 30])
                self.ax.set_xticks([])
                self.ax.set_yticks([])
                plt.title('Corona-Virus War')
                plt.pause(2)
            else:
                self.ax.imshow(Corona_icon, extent=[self.target_x - 5, self.target_x + 5, self.target_y, self.target_y + 10])
                self.ax.imshow(Missile_icon, extent=[self.missile_x - 6, self.missile_x + 6, self.missile_y - 6, self.missile_y + 6])

        self.ax.set_xticks([])
        self.ax.set_yticks([])
        # plt.legend()
        plt.title('Corona-Virus War')
        plt.pause(0.01)
        pass

    def reset(self, seed=None, options={}):
        self.missile_x = 50 #np.random.uniform(0, 100)
        self.missile_y = 100 #np.random.uniform(50, 100)
        self.target_x = np.random.uniform(40, 60)
        self.plane_x = 0
        self.target_y = 0
        self.dx = 0
        self.dy = 0
        self.epoch +=1
        obs = np.array([self.missile_x, self.missile_y, self.target_x, self.target_y, self.target_x - self.missile_x])

        if seed is not None:

            pass  # XXX Seed the random-number generator

        # obs = np.zeros(1, dtype=np.float32)

        info = {}

        return obs, info

    def close(self):

        gym.Env.close(self)

        
