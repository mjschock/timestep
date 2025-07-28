#!/usr/bin/env python3
"""
Comprehensive tests for SmolVLA RFT implementation
"""

import pytest
import torch
import numpy as np
from unittest.mock import Mock, patch
from pathlib import Path

# Add src to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from backend.rft.smolvla_rft_trainer import (
    RFTConfig, 
    SmolVLARFTGrader, 
    ExpertDemonstrationGrader,
    SmolVLARFTPolicy,
    OpenAIRFTTrainer,
    train_smolvla_rft
)

from backend.rft.environment_grader import (
    EnvironmentConfig,
    EnvironmentFeedbackGrader,
    SimulatedEnvironmentGrader,
    RealEnvironmentGrader,
    create_environment_grader
)


class TestRFTConfig:
    """Test RFT configuration"""
    
    def test_default_config(self):
        """Test default RFT configuration"""
        config = RFTConfig()
        
        assert config.training_examples == 50
        assert config.rft_iterations == 1000
        assert config.responses_per_state == 4
        assert config.grader_type == "multi_objective"
        assert config.task_type == "manipulation"
        assert config.learning_rate == 1e-5
    
    def test_custom_config(self):
        """Test custom RFT configuration"""
        config = RFTConfig(
            training_examples=30,
            rft_iterations=500,
            grader_type="expert_demonstration",
            task_type="navigation"
        )
        
        assert config.training_examples == 30
        assert config.rft_iterations == 500
        assert config.grader_type == "expert_demonstration"
        assert config.task_type == "navigation"


class TestSmolVLARFTGrader:
    """Test SmolVLA RFT grader"""
    
    @pytest.fixture
    def grader(self):
        """Create a test grader"""
        config = RFTConfig(task_type="manipulation")
        return SmolVLARFTGrader(config)
    
    def test_grader_initialization(self, grader):
        """Test grader initialization"""
        assert grader.config.task_type == "manipulation"
        assert "task_completion" in grader.grader_weights
        assert "safety" in grader.grader_weights
    
    def test_manipulation_weights(self):
        """Test manipulation task weights"""
        config = RFTConfig(task_type="manipulation")
        grader = SmolVLARFTGrader(config)
        
        expected_weights = {
            'task_completion': 0.5,
            'safety': 0.3,
            'efficiency': 0.1,
            'smoothness': 0.1
        }
        
        assert grader.grader_weights == expected_weights
    
    def test_navigation_weights(self):
        """Test navigation task weights"""
        config = RFTConfig(task_type="navigation")
        grader = SmolVLARFTGrader(config)
        
        expected_weights = {
            'task_completion': 0.4,
            'safety': 0.4,
            'efficiency': 0.15,
            'comfort': 0.05
        }
        
        assert grader.grader_weights == expected_weights
    
    def test_grade_trajectory(self, grader):
        """Test trajectory grading"""
        observations = torch.randn(5, 512)
        actions = torch.randn(5, 64)
        outcomes = {'success': True}
        
        scores = grader.grade_trajectory(observations, actions, outcomes)
        
        # Check that all expected scores are present
        expected_metrics = ['task_completion', 'safety', 'efficiency', 'smoothness', 'overall']
        for metric in expected_metrics:
            assert metric in scores
            assert 0.0 <= scores[metric] <= 1.0
    
    def test_compute_overall_score(self, grader):
        """Test overall score computation"""
        scores = {
            'task_completion': 0.8,
            'safety': 0.9,
            'efficiency': 0.7,
            'smoothness': 0.8
        }
        
        overall_score = grader._compute_overall_score(scores)
        
        # Overall score should be weighted average
        expected_score = (0.5 * 0.8 + 0.3 * 0.9 + 0.1 * 0.7 + 0.1 * 0.8)
        assert abs(overall_score - expected_score) < 1e-6


class TestExpertDemonstrationGrader:
    """Test expert demonstration grader"""
    
    @pytest.fixture
    def grader(self):
        """Create expert demonstration grader"""
        config = RFTConfig()
        return ExpertDemonstrationGrader(config)
    
    def test_expert_grader_initialization(self, grader):
        """Test expert grader initialization"""
        assert isinstance(grader, ExpertDemonstrationGrader)
        assert grader.config is not None
    
    def test_grade_against_expert(self, grader):
        """Test grading against expert demonstrations"""
        observations = torch.randn(5, 512)
        predicted_actions = torch.randn(5, 64)
        expert_actions = torch.randn(5, 64)
        
        scores = grader.grade_trajectory(observations, predicted_actions, expert_actions)
        
        # All scores should be the same (based on distance to expert)
        first_score = scores['task_completion']
        for score in scores.values():
            assert abs(score - first_score) < 1e-6
    
    def test_perfect_expert_match(self, grader):
        """Test perfect match with expert actions"""
        observations = torch.randn(5, 512)
        expert_actions = torch.randn(5, 64)
        predicted_actions = expert_actions.clone()  # Perfect match
        
        scores = grader.grade_trajectory(observations, predicted_actions, expert_actions)
        
        # Perfect match should give high score
        assert scores['overall'] > 0.9
    
    def test_poor_expert_match(self, grader):
        """Test poor match with expert actions"""
        observations = torch.randn(5, 512)
        expert_actions = torch.randn(5, 64)
        predicted_actions = expert_actions + 10.0  # Large difference
        
        scores = grader.grade_trajectory(observations, predicted_actions, expert_actions)
        
        # Poor match should give low score
        assert scores['overall'] < 0.1


class TestEnvironmentConfig:
    """Test environment configuration"""
    
    def test_default_config(self):
        """Test default environment configuration"""
        config = EnvironmentConfig()
        
        assert config.max_joint_velocity == 2.0
        assert config.max_joint_acceleration == 5.0
        assert config.collision_threshold == 0.05
        assert config.position_tolerance == 0.01
        assert config.max_trajectory_time == 30.0
    
    def test_custom_config(self):
        """Test custom environment configuration"""
        config = EnvironmentConfig(
            max_joint_velocity=3.0,
            max_acceleration=3.0,
            max_trajectory_time=60.0
        )
        
        assert config.max_joint_velocity == 3.0
        assert config.max_acceleration == 3.0
        assert config.max_trajectory_time == 60.0


class TestEnvironmentFeedbackGrader:
    """Test environment feedback grader"""
    
    @pytest.fixture
    def grader(self):
        """Create environment feedback grader"""
        config = EnvironmentConfig()
        return EnvironmentFeedbackGrader(config, "manipulation")
    
    def test_grader_initialization(self, grader):
        """Test environment grader initialization"""
        assert grader.task_type == "manipulation"
        assert len(grader.metrics) == 4  # task_completion, safety, efficiency, smoothness
    
    def test_manipulation_metrics(self):
        """Test manipulation task metrics"""
        config = EnvironmentConfig()
        grader = EnvironmentFeedbackGrader(config, "manipulation")
        
        expected_metrics = ['task_completion', 'safety', 'efficiency', 'smoothness']
        for metric in expected_metrics:
            assert metric in grader.metrics
    
    def test_navigation_metrics(self):
        """Test navigation task metrics"""
        config = EnvironmentConfig()
        grader = EnvironmentFeedbackGrader(config, "navigation")
        
        expected_metrics = ['task_completion', 'safety', 'efficiency', 'comfort']
        for metric in expected_metrics:
            assert metric in grader.metrics
    
    def test_grade_manipulation_completion(self, grader):
        """Test manipulation completion grading"""
        observations = torch.randn(5, 512)
        actions = torch.randn(5, 64)
        
        # Test successful completion
        env_data = {
            'target_reached': True,
            'object_grasped': True,
            'object_placed': True
        }
        
        score = grader._grade_manipulation_completion(observations, actions, env_data)
        assert score == 1.0
        
        # Test partial completion
        env_data = {
            'target_reached': True,
            'object_grasped': True,
            'object_placed': False
        }
        
        score = grader._grade_manipulation_completion(observations, actions, env_data)
        assert score == 0.7
    
    def test_grade_manipulation_safety(self, grader):
        """Test manipulation safety grading"""
        observations = torch.randn(5, 512)
        actions = torch.randn(5, 64)
        
        # Test safe trajectory
        env_data = {
            'collisions': 0,
            'unsafe_joint_configs': 0
        }
        
        score = grader._grade_manipulation_safety(observations, actions, env_data)
        assert score == 1.0
        
        # Test unsafe trajectory
        env_data = {
            'collisions': 2,
            'unsafe_joint_configs': 1
        }
        
        score = grader._grade_manipulation_safety(observations, actions, env_data)
        assert score < 1.0
        assert score >= 0.0


class TestSimulatedEnvironmentGrader:
    """Test simulated environment grader"""
    
    @pytest.fixture
    def grader(self):
        """Create simulated environment grader"""
        config = EnvironmentConfig()
        return SimulatedEnvironmentGrader(config, "manipulation")
    
    def test_simulated_grader_initialization(self, grader):
        """Test simulated grader initialization"""
        assert isinstance(grader, SimulatedEnvironmentGrader)
        assert grader.simulation_step == 0
    
    def test_simulate_environment_data(self, grader):
        """Test environment data simulation"""
        observations = torch.randn(5, 512)
        actions = torch.randn(5, 64)
        
        env_data = grader.simulate_environment_data(observations, actions)
        
        # Check that all expected fields are present
        expected_fields = [
            'target_reached', 'object_grasped', 'object_placed',
            'distance_to_target', 'collisions', 'unsafe_joint_configs',
            'trajectory_length', 'execution_time', 'simulation_step'
        ]
        
        for field in expected_fields:
            assert field in env_data
    
    def test_simulation_step_increment(self, grader):
        """Test that simulation step increments"""
        observations = torch.randn(5, 512)
        actions = torch.randn(5, 64)
        
        initial_step = grader.simulation_step
        grader.simulate_environment_data(observations, actions)
        
        assert grader.simulation_step == initial_step + 1


class TestSmolVLARFTPolicy:
    """Test SmolVLA RFT policy"""
    
    @pytest.fixture
    def config(self):
        """Create test configuration"""
        return RFTConfig(
            rft_iterations=10,
            training_examples=5,
            learning_rate=1e-4
        )
    
    @patch('backend.rft.smolvla_rft_trainer.AutoProcessor')
    @patch('backend.rft.smolvla_rft_trainer.AutoModelForImageTextToText')
    def test_policy_initialization(self, mock_model, mock_processor, config):
        """Test policy initialization with mocked components"""
        # Mock the model and processor
        mock_processor.from_pretrained.return_value = Mock()
        mock_model.from_pretrained.return_value = Mock()
        
        model_name = "HuggingFaceTB/SmolVLA-256M-Video-Instruct"
        policy = SmolVLARFTPolicy(model_name, config)
        
        assert policy.model_name == model_name
        assert policy.config == config
        assert policy.optimizer is not None
    
    @patch('backend.rft.smolvla_rft_trainer.AutoProcessor')
    @patch('backend.rft.smolvla_rft_trainer.AutoModelForImageTextToText')
    def test_generate_responses(self, mock_model, mock_processor, config):
        """Test response generation"""
        # Mock the model and processor
        mock_processor.from_pretrained.return_value = Mock()
        mock_model.from_pretrained.return_value = Mock()
        
        model_name = "HuggingFaceTB/SmolVLA-256M-Video-Instruct"
        policy = SmolVLARFTPolicy(model_name, config)
        
        states = torch.randn(3, 512)
        responses = policy.generate_responses(states, num_responses=2)
        
        assert len(responses) == 2
        assert all(isinstance(r, torch.Tensor) for r in responses)


class TestOpenAIRFTTrainer:
    """Test OpenAI RFT trainer"""
    
    @pytest.fixture
    def config(self):
        """Create test configuration"""
        return RFTConfig(
            rft_iterations=5,
            training_examples=3,
            log_freq=2,
            save_freq=3
        )
    
    @patch('backend.rft.smolvla_rft_trainer.SmolVLARFTPolicy')
    def test_trainer_initialization(self, mock_policy, config):
        """Test trainer initialization"""
        mock_policy.return_value = Mock()
        
        trainer = OpenAIRFTTrainer(config)
        
        assert trainer.config == config
        assert trainer.policy is not None
        assert trainer.grader is not None
    
    def test_create_grader(self, config):
        """Test grader creation"""
        trainer = OpenAIRFTTrainer(config)
        
        # Test expert demonstration grader
        config.grader_type = "expert_demonstration"
        grader = trainer.create_grader()
        assert isinstance(grader, ExpertDemonstrationGrader)
        
        # Test multi-objective grader
        config.grader_type = "multi_objective"
        grader = trainer.create_grader()
        assert isinstance(grader, SmolVLARFTGrader)
    
    def test_collect_trajectories(self, config):
        """Test trajectory collection"""
        trainer = OpenAIRFTTrainer(config)
        
        trajectories = trainer.collect_trajectories()
        
        assert len(trajectories) == config.training_examples
        for trajectory in trajectories:
            assert 'observations' in trajectory
            assert 'actions' in trajectory
            assert 'outcomes' in trajectory


class TestIntegration:
    """Integration tests"""
    
    def test_create_environment_grader(self):
        """Test environment grader creation"""
        config = EnvironmentConfig()
        
        # Test simulated grader
        grader = create_environment_grader("simulated", "manipulation", config)
        assert isinstance(grader, SimulatedEnvironmentGrader)
        
        # Test real grader
        grader = create_environment_grader("real", "navigation", config)
        assert isinstance(grader, RealEnvironmentGrader)
    
    def test_end_to_end_grading(self):
        """Test end-to-end grading workflow"""
        # Create grader
        config = EnvironmentConfig()
        grader = create_environment_grader("simulated", "manipulation", config)
        
        # Create test data
        observations = torch.randn(5, 512)
        actions = torch.randn(5, 64)
        
        # Simulate environment data
        if isinstance(grader, SimulatedEnvironmentGrader):
            env_data = grader.simulate_environment_data(observations, actions)
        else:
            env_data = grader.collect_environment_data(observations, actions)
        
        # Grade trajectory
        scores = grader.grade_trajectory(observations, actions, env_data)
        
        # Verify scores
        assert 'overall' in scores
        assert 0.0 <= scores['overall'] <= 1.0
        
        for metric, score in scores.items():
            assert 0.0 <= score <= 1.0


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])