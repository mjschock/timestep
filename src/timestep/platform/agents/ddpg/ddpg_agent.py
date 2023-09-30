import copy
import random
from collections import deque, namedtuple

import ivy
# import numpy as np
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim

BUFFER_SIZE = int(1e6)  # replay buffer size
BATCH_SIZE = 128        # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR_ACTOR = 1e-4         # learning rate of the actor
LR_CRITIC = 1e-4        # learning rate of the critic
WEIGHT_DECAY = 0.0001   # L2 weight decay

# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
device = "cuda:0" if ivy.gpu_is_available() else "cpu"

def mse_loss(y, target):
    return ivy.mean((y - target)**2)

class Agent():
    """Interacts with and learns from the environment."""

    def __init__(self, state_size, action_size, random_seed):
        """Initialize an Agent object.

        Params
        ======
            state_size (int): dimension of each state
            action_size (int): dimension of each action
            random_seed (int): random seed
        """
        self.state_size = state_size
        self.action_size = action_size
        self.seed = random.seed(random_seed)

        # Actor Network (w/ Target Network)
        # self.actor_local = Actor(state_size, action_size, random_seed).to(device)
        self.actor_local = Actor(state_size, action_size, random_seed)
        # self.actor_target = Actor(state_size, action_size, random_seed).to(device)
        self.actor_target = Actor(state_size, action_size, random_seed)
        # self.actor_optimizer = optim.Adam(self.actor_local.parameters(), lr=LR_ACTOR)
        self.actor_optimizer = ivy.Adam(lr=LR_ACTOR)

        # Critic Network (w/ Target Network)
        # self.critic_local = Critic(state_size, action_size, random_seed).to(device)
        self.critic_local = Critic(state_size, action_size, random_seed)
        # self.critic_target = Critic(state_size, action_size, random_seed).to(device)
        self.critic_target = Critic(state_size, action_size, random_seed)
        # self.critic_optimizer = optim.Adam(self.critic_local.parameters(), lr=LR_CRITIC, weight_decay=WEIGHT_DECAY)
        self.critic_optimizer = ivy.Adam(lr=LR_CRITIC)

        # Noise process
        self.noise = OUNoise(action_size, random_seed)

        # Replay memory
        self.memory = ReplayBuffer(action_size, BUFFER_SIZE, BATCH_SIZE, random_seed)

    def step(self, state, action, reward, next_state, done):
        """Save experience in replay memory, and use random sample from buffer to learn."""

        # print('type(state): ', type(state))
        # print('type(action): ', type(action))
        # print('type(reward): ', type(reward))
        # print('type(next_state): ', type(next_state))
        # print('type(done): ', type(done))

        # Save experience / reward
        self.memory.add(state, action, reward, next_state, done)

        # Learn, if enough samples are available in memory
        if len(self.memory) > BATCH_SIZE:
            experiences = self.memory.sample()
            self.learn(experiences, GAMMA)

    def act(self, state, add_noise=True):
        """Returns actions for given state as per current policy."""

        # @ivy.unify(source="numpy")
        # def observe(x):
            # return x

        # print('type(state): ', type(state))

        # obs = observe(state)
        # print('type(obs): ', type(obs))

        # state = torch.from_numpy(state).float().to(device)

        # self.actor_local.eval()

        # with torch.no_grad():
            # action = self.actor_local(state).cpu().data.numpy()

        action = self.actor_local(state)

        # self.actor_local.train()

        if add_noise:
            action += self.noise.sample()

        # import jax

        # Simple JAX function to transpile
        # def clip(x):
            # return jax.numpy.clip(x, -1, 1)

        # return np.clip(action, -1, 1)
        # return ivy.native_array(np.clip(action, -1, 1))
        return ivy.clip(action, -1, 1)

        # eager_graph = ivy.transpile(clip, source="jax", to="numpy", args=(action,))

        # return ivy.transpile(np.clip(action, -1, 1), source="jax", to="numpy")

        # return eager_graph(action)

    def reset(self):
        self.noise.reset()

    def learn(self, experiences, gamma):
        """Update policy and value parameters using given batch of experience tuples.
        Q_targets = r + γ * critic_target(next_state, actor_target(next_state))
        where:
            actor_target(state) -> action
            critic_target(state, action) -> Q-value

        Params
        ======
            experiences (Tuple[torch.Tensor]): tuple of (s, a, r, s', done) tuples
            gamma (float): discount factor
        """
        states, actions, rewards, next_states, dones = experiences

        # ---------------------------- update critic ---------------------------- #
        # Get predicted next-state actions and Q values from target models
        actions_next = self.actor_target(next_states)
        Q_targets_next = self.critic_target(next_states, actions_next)
        # Compute Q targets for current states (y_i)
        Q_targets = rewards + (gamma * Q_targets_next * (1 - dones))
        # Compute critic loss
        Q_expected = self.critic_local(states, actions)

        # critic_loss = F.mse_loss(Q_expected, Q_targets)
        # critic_loss = mse_loss(Q_expected, Q_targets)
        # # Minimize the loss
        # self.critic_optimizer.zero_grad()
        # critic_loss.backward()
        # self.critic_optimizer.step()

        # compute critic loss and gradients
        critic_loss, critic_grads = ivy.execute_with_gradients(lambda v: mse_loss(Q_expected, Q_targets), self.critic_local.v)
        # update parameters
        self.critic_local.v = self.critic_optimizer.step(self.critic_local.v, critic_grads)
        # print current loss
        # print(f'Epoch: {epoch + 1:2d} --- Loss: {ivy.to_numpy(loss).item():.5f}')

        # ---------------------------- update actor ---------------------------- #
        # Compute actor loss
        actions_pred = self.actor_local(states)
        # actor_loss = -self.critic_local(states, actions_pred).mean()
        # Minimize the loss
        # self.actor_optimizer.zero_grad()
        # actor_loss.backward()
        # self.actor_optimizer.step()

        # compute actor loss and gradients
        actor_loss, actor_grads = ivy.execute_with_gradients(lambda v: -self.critic_local(states, actions_pred).mean(), self.actor_local.v)
        # update parameters
        self.actor_local.v = self.actor_optimizer.step(self.actor_local.v, actor_grads)

        # ----------------------- update target networks ----------------------- #
        self.soft_update(self.critic_local, self.critic_target, TAU)
        self.soft_update(self.actor_local, self.actor_target, TAU)

    def soft_update(self, local_model, target_model, tau):
        """Soft update model parameters.
        θ_target = τ*θ_local + (1 - τ)*θ_target

        Params
        ======
            local_model: PyTorch model (weights will be copied from)
            target_model: PyTorch model (weights will be copied to)
            tau (float): interpolation parameter
        """
        # for target_param, local_param in zip(target_model.parameters(), local_model.parameters()):
            # target_param.data.copy_(tau*local_param.data + (1.0-tau)*target_param.data)

        target_model.v = ivy.add(ivy.multiply(local_model.v, tau), ivy.multiply(target_model.v, 1.0-tau))

class OUNoise:
    """Ornstein-Uhlenbeck process."""

    def __init__(self, size, seed, mu=0., theta=0.15, sigma=0.2):
        """Initialize parameters and noise process."""
        # self.mu = mu * np.ones(size)
        self.mu = mu * ivy.ones(size)
        self.theta = theta
        self.sigma = sigma
        self.seed = random.seed(seed)
        self.reset()

    def reset(self):
        """Reset the internal state (= noise) to mean (mu)."""
        self.state = copy.copy(self.mu)

    def sample(self):
        """Update internal state and return it as a noise sample."""
        x = self.state
        # dx = self.theta * (self.mu - x) + self.sigma * np.array([random.random() for i in range(len(x))])
        dx = self.theta * (self.mu - x) + self.sigma * ivy.array([random.random() for i in range(len(x))])
        self.state = x + dx
        return self.state

class ReplayBuffer:
    """Fixed-size buffer to store experience tuples."""

    def __init__(self, action_size, buffer_size, batch_size, seed):
        """Initialize a ReplayBuffer object.
        Params
        ======
            buffer_size (int): maximum size of buffer
            batch_size (int): size of each training batch
        """
        self.action_size = action_size
        self.memory = deque(maxlen=buffer_size)  # internal memory (deque)
        self.batch_size = batch_size
        self.experience = namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])
        self.seed = random.seed(seed)

    def add(self, state, action, reward, next_state, done):
        """Add a new experience to memory."""
        e = self.experience(state, action, reward, next_state, done)
        self.memory.append(e)

    def sample(self):
        """Randomly sample a batch of experiences from memory."""
        experiences = random.sample(self.memory, k=self.batch_size)

        # states = torch.from_numpy(np.vstack([e.state for e in experiences if e is not None])).float().to(device)
        states = ivy.stack([e.state for e in experiences if e is not None], axis=0)
        # actions = torch.from_numpy(np.vstack([e.action for e in experiences if e is not None])).float().to(device)
        actions = ivy.stack([e.action for e in experiences if e is not None], axis=0)
        # rewards = torch.from_numpy(np.vstack([e.reward for e in experiences if e is not None])).float().to(device)
        rewards = ivy.stack([e.reward for e in experiences if e is not None], axis=0)
        # next_states = torch.from_numpy(np.vstack([e.next_state for e in experiences if e is not None])).float().to(device)
        next_states = ivy.stack([e.next_state for e in experiences if e is not None], axis=0)
        # dones = torch.from_numpy(np.vstack([e.done for e in experiences if e is not None]).astype(np.uint8)).float().to(device)
        dones = ivy.stack([e.done for e in experiences if e is not None], axis=0)

        return (states, actions, rewards, next_states, dones)

    def __len__(self):
        """Return the current size of internal memory."""
        return len(self.memory)

def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    # lim = 1. / np.sqrt(fan_in)
    lim = 1. / ivy.sqrt(fan_in)
    return (-lim, lim)

# class Actor(nn.Module):
class Actor(ivy.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=400, fc2_units=300):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        # super(Actor, self).__init__()
        # self.seed = torch.manual_seed(seed)
        # self.fc1 = nn.Linear(state_size, fc1_units)
        # self.fc2 = nn.Linear(fc1_units, fc2_units)
        # self.fc3 = nn.Linear(fc2_units, action_size)
        # self.reset_parameters()

        self.state_size = state_size
        self.action_size = action_size
        self.fc1_units = fc1_units
        self.fc2_units = fc2_units

        super().__init__()


    def _build(self, *args, **kwargs):
        self.fc1 = ivy.Linear(self.state_size, self.fc1_units)
        self.fc2 = ivy.Linear(self.fc1_units, self.fc2_units)
        self.fc3 = ivy.Linear(self.fc2_units, self.action_size)

    def _forward(self, state):
        x = ivy.relu(self.fc1(state))
        x = ivy.relu(self.fc2(x))

        return ivy.tanh(self.fc3(x))

    # def reset_parameters(self):
    #     self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
    #     self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
    #     self.fc3.weight.data.uniform_(-3e-3, 3e-3)

    # def forward(self, state):
    #     """Build an actor (policy) network that maps states -> actions."""
    #     x = F.relu(self.fc1(state))
    #     x = F.relu(self.fc2(x))
    #     return F.tanh(self.fc3(x))


# class Critic(nn.Module):
class Critic(ivy.Module):
    """Critic (Value) Model."""

    def __init__(self, state_size, action_size, seed, fcs1_units=256, fc2_units=256, fc3_units=128):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fcs1_units (int): Number of nodes in the first hidden layer
            fc2_units (int): Number of nodes in the second hidden layer
        """
        # super(Critic, self).__init__()
        # self.seed = torch.manual_seed(seed)
        # self.fcs1 = nn.Linear(state_size, fcs1_units)
        # self.fc2 = nn.Linear(fcs1_units+action_size, fc2_units)
        # self.fc3 = nn.Linear(fc2_units, fc3_units)
        # self.fc4 = nn.Linear(fc3_units, 1)
        # self.reset_parameters()

        self.state_size = state_size
        self.action_size = action_size
        self.fcs1_units = fcs1_units
        self.fc2_units = fc2_units
        self.fc3_units = fc3_units

        super().__init__()


    def _build(self, *args, **kwargs):
        self.fcs1 = ivy.Linear(self.state_size, self.fcs1_units)
        self.fc2 = ivy.Linear(self.fcs1_units+self.action_size, self.fc2_units)
        self.fc3 = ivy.Linear(self.fc2_units, self.fc3_units)
        self.fc4 = ivy.Linear(self. fc3_units, 1)

    def _forward(self, state, action):
        xs = ivy.leaky_relu(self.fcs1(state))

        # print('xs.shape: ', xs.shape) # ivy.Shape(128, 1, 256)
        # print('action.shape: ', action.shape) # ivy.Shape(128, 1, 4)

        # x = ivy.concat((xs, action), axis=1) # ivy.utils.exceptions.IvyValueError: numpy: concat: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 2, the array at index 0 has size 256 and the array at index 1 has size 4
        # x = ivy.concat((xs, action), axis=0) # ivy.utils.exceptions.IvyValueError: numpy: concat: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 2, the array at index 0 has size 256 and the array at index 1 has size 4

        x = ivy.concat((xs, action), axis=-1)

        x = ivy.leaky_relu(self.fc2(x))
        x = ivy.leaky_relu(self.fc3(x))

        return self.fc4(x)

    # def reset_parameters(self):
    #     self.fcs1.weight.data.uniform_(*hidden_init(self.fcs1))
    #     self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
    #     self.fc3.weight.data.uniform_(*hidden_init(self.fc3))
    #     self.fc4.weight.data.uniform_(-3e-3, 3e-3)

    # def forward(self, state, action):
    #     """Build a critic (value) network that maps (state, action) pairs -> Q-values."""
    #     xs = F.leaky_relu(self.fcs1(state))
    #     x = torch.cat((xs, action), dim=1)
    #     x = F.leaky_relu(self.fc2(x))
    #     x = F.leaky_relu(self.fc3(x))
    #     return self.fc4(x)
