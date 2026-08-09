import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pygame

class GridEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 10}

    def __init__(self, size=5, render_mode=None):
        super().__init__()
        self.size = size
        self.render_mode = render_mode
        self.window_size = 500

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(
            low=0, high=size-1, shape=(2,), dtype=np.float32
        )

        self.window = None
        self.clock = None
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.agent_pos = np.array([0, 0])
        self.goal_pos = np.array([self.size-1, self.size-1])
        return self.agent_pos, {}

    def step(self, action):
        if action == 0:   # up
            self.agent_pos[1] -= 1
        elif action == 1: # down
            self.agent_pos[1] += 1
        elif action == 2: # left
            self.agent_pos[0] -= 1
        elif action == 3: # right
            self.agent_pos[0] += 1

        self.agent_pos = np.clip(self.agent_pos, 0, self.size-1)

        terminated = np.array_equal(self.agent_pos, self.goal_pos)
        reward = 1 if terminated else 0

        return self.agent_pos, reward, terminated, False, {}

    def render(self):
        if self.window is None:
            pygame.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        pix_square = self.window_size / self.size

        # draw grid lines
        for x in range(self.size):
            for y in range(self.size):
                rect = pygame.Rect(
                    pix_square * x,
                    pix_square * y,
                    pix_square,
                    pix_square,
                )
                pygame.draw.rect(canvas, (200, 200, 200), rect, 1)

        # draw goal (green)
        gx, gy = self.goal_pos
        pygame.draw.rect(
            canvas,
            (0, 255, 0),
            pygame.Rect(gx * pix_square, gy * pix_square, pix_square, pix_square),
        )

        # draw agent (blue)
        ax, ay = self.agent_pos
        pygame.draw.circle(
            canvas,
            (0, 0, 255),
            (int((ax + 0.5) * pix_square), int((ay + 0.5) * pix_square)),
            int(pix_square / 3),
        )

        self.window.blit(canvas, canvas.get_rect())
        pygame.display.update()
        self.clock.tick(self.metadata["render_fps"])

    def close(self):
        if self.window is not None:
            pygame.quit()