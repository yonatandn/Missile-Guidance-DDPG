from gymnasium.envs.registration import register

register(
    id='GymBomber-v0',
    entry_point='gym_bomber.envs:GymBomber',
    max_episode_steps=10000
)
