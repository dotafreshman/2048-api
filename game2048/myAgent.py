import numpy as np
from game2048.agents import Agent

class myOwnAgent(Agent):

    def step(self):
        '''To define the agent's 1-step behavior given the `game`.
        You can find more instance in [`agents.py`](game2048/agents.py).
        
        :return direction: 0: left, 1: down, 2: right, 3: up
        '''
	 
        direction = np.random.randint(0, 10)
	if direction<3:
		direction=0
	elif direction<6:
		direction=1
	elif direction<8:
		direction=2
	else: direction=3
        return direction
        
