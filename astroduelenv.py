import gymnasium as gym
from gymnasium import spaces
import numpy as np

class AstroDuelEnv(gym.Env):
    def __init__(self):
        super(AstroDuelEnv, self).__init__()
        # Define the action and observation spaces
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=500, shape=(2,), dtype=np.float32)
        self.is_player_alive = True
        self.state = None

    def reset(self):
        # Initialize the environment, return initial observation
        self.state = self.get_initial_state()
        return np.array(self.state)

    def step(self, action):
        # Execute one time step within the environment
        if self.state is None:
            raise Exception("You must reset the environment before calling step()")

        # Implement game dynamics based on the action
        if action == 0:
            self.state[0] -= 1
        elif action == 1:
            self.state[0] += 1
        elif action == 2:
            self.state[1] -= 1
        elif action == 3:
            self.state[1] += 1

        # Dummy reward and done condition for illustration
        reward = 0.0
        done = False

        return np.array(self.state), reward, done, {}

    def render(self, mode='human'):
        # Implement visualization of the environment
        pass

    def close(self):
        # Clean up resources if necessary
        pass

    def get_initial_state(self):
        # Define how the initial state looks like
        return [250, 250]  # Example initial state coordinates

# Example usage
if __name__ == "__main__":
    env = AstroDuelEnv()
    observation = env.reset()
    action = env.action_space.sample()
    next_observation, reward, done, _ = env.step(action)
    print(f"Observation: {next_observation}, Reward: {reward}, Done: {done}")
