import random
from collections import deque, namedtuple

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

BUFFER_SIZE = int(1e6)       # replay buffer size
BATCH_SIZE = 64              # minibatch size
GAMMA = 0.99                  # discount factor
GAE_LAMBDA = 0.95            # Generalized Advantage Estimation lambda
PPO_EPSILON = 0.2            # PPO clipping parameter
PPO_EPOCHS = 10              # Number of optimization epochs per update
LR_ACTOR = 1e-4              # learning rate of the actor
LR_CRITIC = 1e-3             # learning rate of the critic
VALUE_COEF = 0.5             # coefficient for the value loss
ENTROPY_COEF = 0.01          # coefficient for the entropy regularization
CLIP_GRADIENTS = 0.5         # clip gradients to prevent large updates
UPDATE_EVERY = 20            # how often to update the network

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class Agent():
    """Interacts with and learns from the environment using PPO."""

    def __init__(self, state_size, action_size, random_seed):
        """Initialize an Agent object.

        Params:
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            random_seed (int): Random seed
        """
        self.state_size = state_size
        self.action_size = action_size
        self.seed = random.seed(random_seed)

        # Actor and Critic Networks
        self.policy_network = PolicyNetwork(state_size, action_size, random_seed).to(device)
        self.value_network = ValueNetwork(state_size, random_seed).to(device)
        self.policy_optimizer = optim.Adam(self.policy_network.parameters(), lr=LR_ACTOR)
        self.value_optimizer = optim.Adam(self.value_network.parameters(), lr=LR_CRITIC)

        # Memory for storing experiences
        self.memory = PPOReplayBuffer(action_size, BUFFER_SIZE, BATCH_SIZE, random_seed)

        # Initialize time step (for updating every UPDATE_EVERY steps)
        self.t_step = 0

    def step(self, state, action, log_prob, value, reward, next_state, done):
        """Save experience in replay memory and use it to learn.

        Params:
        state (Tensor): Current state
        action (Tensor): Taken action
        log_prob (Tensor): Log probability of taking the action
        value (Tensor): Estimated value of the state
        reward (float): Received reward
        next_state (Tensor): Next state
        done (bool): Whether the episode is done
        """
        self.memory.add(state, action, log_prob, value, reward, next_state, done)

        # Learn every UPDATE_EVERY time steps
        # self.t_step = (self.t_step + 1) % UPDATE_EVERY
        # if self.t_step == 0:
        if len(self.memory) > BATCH_SIZE:
            # for _ in range(PPO_EPOCHS):
            experiences = self.memory.sample()
            self.learn(experiences)

    def act(self, state):
        """Select an action using the current policy.

        Params:
        state (Tensor): Current state

        Returns:
        action (Tensor): Selected action
        log_prob (Tensor): Log probability of selecting the action
        """
        state = torch.FloatTensor(state).to(device)

        print("state: ", state)

        with torch.no_grad():
            action, log_prob, entropy = self.policy_network(state)

        print("action: ", action)
        print("type(action): ", type(action))
        print("log_prob: ", log_prob)
        print("type(log_prob): ", type(log_prob))
        print("entropy", entropy)
        print("type(entropy): ", type(entropy))

        return action.cpu().numpy(), log_prob

        # Policy network computes action distribution
        # state = torch.from_numpy(state).float().to(device)
        # action_distribution, _, _ = self.policy_network(state)

        # # Sample action from the distribution
        # action = action_distribution.sample()
        # log_prob = action_distribution.log_prob(action)
        # return action.cpu().data.numpy(), log_prob

    def learn(self, experiences):
        """Update the policy and value networks using PPO.

        Params:
        experiences (tuple of Tensors): Tuple containing states, actions, log probs, values, returns, advantages.
        """
        # states, actions, old_log_probs, old_values, returns, advantages = experiences

        # # Policy loss
        # _, log_probs, entropy = self.policy_network(states, actions)
        # ratio = torch.exp(log_probs - old_log_probs)
        # clipped_ratio = torch.clamp(ratio, 1.0 - PPO_EPSILON, 1.0 + PPO_EPSILON)
        # policy_loss = -torch.min(ratio * advantages, clipped_ratio * advantages).mean()

        # # Value loss
        # values = self.value_network(states).squeeze(1)
        # value_loss = F.mse_loss(values, returns)

        # # Entropy regularization
        # entropy_loss = -entropy.mean()

        # # Total loss
        # loss = policy_loss + VALUE_COEF * value_loss + ENTROPY_COEF * entropy_loss

        # # Update policy network
        # self.policy_optimizer.zero_grad()
        # loss.backward()
        # if CLIP_GRADIENTS > 0:
        #     torch.nn.utils.clip_grad_norm_(self.policy_network.parameters(), CLIP_GRADIENTS)
        # self.policy_optimizer.step()

        # # Update value network
        # self.value_optimizer.zero_grad()
        # value_loss.backward()
        # self.value_optimizer.step()

        states, actions, old_log_probs, old_values, returns, advantages = experiences

        # Calculate the ratio of new and old policy probabilities
        action_distribution, value = self.policy_network(states)
        new_log_probs = action_distribution.log_prob(actions)
        ratio = torch.exp(new_log_probs - old_log_probs)

        # Calculate surrogate loss and clip it
        # actor_loss = -torch.min(ratio * advantages, torch.clamp(ratio, 1 - EPSILON, 1 + EPSILON) * advantages).mean()
        actor_loss = -torch.min(ratio * advantages, torch.clamp(ratio, 1 - PPO_EPSILON, 1 + PPO_EPSILON) * advantages).mean()

        # Calculate value loss
        # clipped_values = old_values + torch.clamp(value - old_values, -EPSILON, EPSILON)
        clipped_values = old_values + torch.clamp(value - old_values, -PPO_EPSILON, PPO_EPSILON)
        value_loss1 = (returns - clipped_values).pow(2)
        value_loss2 = (returns - value).pow(2)
        value_loss = 0.5 * torch.max(value_loss1, value_loss2).mean()

        # Calculate the entropy regularization term
        entropy = action_distribution.entropy().mean()

        # Total loss
        # total_loss = actor_loss + value_loss - ENTROPY_WEIGHT * entropy
        total_loss = actor_loss + value_loss - ENTROPY_COEF * entropy

        # Perform optimization step
        self.policy_optimizer.zero_grad()
        total_loss.backward()
        self.policy_optimizer.step()

class PPOReplayBuffer:
    """Fixed-size buffer to store experiences for PPO."""

    def __init__(self, action_size, buffer_size, batch_size, seed):
        """Initialize a PPOReplayBuffer object.

        Params:
            action_size (int): Dimension of each action
            buffer_size (int): Maximum size of buffer
            batch_size (int): Size of each training batch
            seed (int): Random seed
        """
        self.action_size = action_size
        self.memory = deque(maxlen=buffer_size)
        self.batch_size = batch_size
        self.experience = namedtuple("Experience", field_names=["state", "action", "log_prob", "value", "reward", "next_state", "done"])
        self.seed = random.seed(seed)

    def add(self, state, action, log_prob, value, reward, next_state, done):
        """Add a new experience to memory."""
        e = self.experience(state, action, log_prob, value, reward, next_state, done)
        self.memory.append(e)

    def sample(self):
        """Randomly sample a batch of experiences from memory."""
        experiences = random.sample(self.memory, k=self.batch_size)

        states = torch.stack([e.state for e in experiences if e is not None]).float().to(device)
        actions = torch.stack([e.action for e in experiences if e is not None]).float().to(device)
        log_probs = torch.stack([e.log_prob for e in experiences if e is not None]).float().to(device)
        old_values = torch.stack([e.value for e in experiences if e is not None]).float().to(device)
        rewards = torch.FloatTensor([e.reward for e in experiences if e is not None]).to(device)
        next_states = torch.stack([e.next_state for e in experiences if e is not None]).float().to(device)
        dones = torch.FloatTensor([e.done for e in experiences if e is not None]).to(device)

        return states, actions, log_probs, old_values, rewards, next_states, dones

    def __len__(self):
        """Return the current size of internal memory."""
        return len(self.memory)


class PolicyNetwork(nn.Module):
    """Policy Network (Actor) Model for PPO."""

    def __init__(self, state_size, action_size, seed, fc_units=64):
        """Initialize parameters and build model.

        Params:
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc_units (int): Number of nodes in the fully connected layers
        """
        super(PolicyNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc_units)
        self.fc2 = nn.Linear(fc_units, fc_units)
        self.fc3_mean = nn.Linear(fc_units, action_size)
        self.fc3_std = nn.Linear(fc_units, action_size)

    def forward(self, state):
        """Build a policy network that maps states to actions and action log probabilities.

        Params:
            state (Tensor): Input state tensor

        Returns:
            action (Tensor): Predicted action
            log_prob (Tensor): Log probability of the action
            entropy (Tensor): Entropy of the action distribution
        """
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        mean = torch.tanh(self.fc3_mean(x))  # Ensure action values are in [-1, 1]
        std = F.softplus(self.fc3_std(x))    # Softplus to ensure positive standard deviation

        # Create a normal distribution for action sampling
        dist = torch.distributions.Normal(mean, std)

        # Sample an action and calculate its log probability
        action = dist.sample()
        log_prob = dist.log_prob(action)

        # Calculate the entropy of the action distribution
        entropy = dist.entropy()

        return action, log_prob, entropy


class ValueNetwork(nn.Module):
    """Value Network (Critic) Model for PPO."""

    def __init__(self, state_size, seed, fc_units=64):
        """Initialize parameters and build model.

        Params:
            state_size (int): Dimension of each state
            seed (int): Random seed
            fc_units (int): Number of nodes in the fully connected layers
        """
        super(ValueNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc_units)
        self.fc2 = nn.Linear(fc_units, fc_units)
        self.fc3 = nn.Linear(fc_units, 1)

    def forward(self, state):
        """Build a value network that estimates the state value.

        Params:
            state (Tensor): Input state tensor

        Returns:
            value (Tensor): Estimated state value
        """
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        value = self.fc3(x)
        return value
