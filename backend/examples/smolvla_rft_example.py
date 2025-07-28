#!/usr/bin/env python3
"""
Complete SmolVLA RFT Example
Demonstrates the full RFT workflow from expert demonstrations to environment feedback
"""

import torch
import numpy as np
import logging
from pathlib import Path
import sys

# Add src to path for imports
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
    SimulatedEnvironmentGrader,
    create_environment_grader
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def demonstrate_expert_grader():
    """Demonstrate expert demonstration grader (Stage 1 RFT)"""
    logger.info("🎯 Stage 1: Expert Demonstration Grader")
    
    # Create expert demonstration grader
    config = RFTConfig(
        rft_iterations=10,  # Small number for demo
        training_examples=5,
        grader_type='expert_demonstration',
        task_type='manipulation'
    )
    
    grader = ExpertDemonstrationGrader(config)
    
    # Simulate expert demonstrations
    observations = torch.randn(5, 512)
    expert_actions = torch.randn(5, 64)
    
    # Test different prediction qualities
    test_cases = [
        ("Perfect Match", expert_actions.clone()),
        ("Good Match", expert_actions + 0.1 * torch.randn_like(expert_actions)),
        ("Poor Match", expert_actions + 2.0 * torch.randn_like(expert_actions))
    ]
    
    for name, predicted_actions in test_cases:
        scores = grader.grade_trajectory(observations, predicted_actions, expert_actions)
        logger.info(f"  {name}: {scores['overall']:.4f}")
    
    return grader


def demonstrate_environment_grader():
    """Demonstrate environment feedback grader (Stage 2 RFT)"""
    logger.info("🌍 Stage 2: Environment Feedback Grader")
    
    # Create environment grader
    env_config = EnvironmentConfig(
        max_joint_velocity=2.0,
        max_trajectory_time=30.0,
        collision_threshold=0.05
    )
    
    grader = create_environment_grader("simulated", "manipulation", env_config)
    
    # Test different action qualities
    observations = torch.randn(5, 512)
    
    test_cases = [
        ("High Quality Actions", torch.randn(5, 64) * 0.5),  # Small magnitude
        ("Medium Quality Actions", torch.randn(5, 64) * 1.0),  # Medium magnitude
        ("Low Quality Actions", torch.randn(5, 64) * 2.0),   # Large magnitude
    ]
    
    for name, actions in test_cases:
        # Simulate environment data
        if isinstance(grader, SimulatedEnvironmentGrader):
            env_data = grader.simulate_environment_data(observations, actions)
        else:
            env_data = grader.collect_environment_data(observations, actions)
        
        # Grade trajectory
        scores = grader.grade_trajectory(observations, actions, env_data)
        
        logger.info(f"  {name}:")
        logger.info(f"    Overall: {scores['overall']:.4f}")
        logger.info(f"    Task Completion: {scores['task_completion']:.4f}")
        logger.info(f"    Safety: {scores['safety']:.4f}")
        logger.info(f"    Efficiency: {scores['efficiency']:.4f}")
        logger.info(f"    Smoothness: {scores['smoothness']:.4f}")
    
    return grader


def demonstrate_multi_objective_grading():
    """Demonstrate multi-objective grading for different task types"""
    logger.info("🎯 Stage 3: Multi-Objective Grading")
    
    # Test manipulation task
    logger.info("  Manipulation Task Grading:")
    manip_config = RFTConfig(task_type="manipulation")
    manip_grader = SmolVLARFTGrader(manip_config)
    
    observations = torch.randn(5, 512)
    actions = torch.randn(5, 64)
    outcomes = {'success': True}
    
    manip_scores = manip_grader.grade_trajectory(observations, actions, outcomes)
    logger.info(f"    Overall: {manip_scores['overall']:.4f}")
    logger.info(f"    Weights: {manip_grader.grader_weights}")
    
    # Test navigation task
    logger.info("  Navigation Task Grading:")
    nav_config = RFTConfig(task_type="navigation")
    nav_grader = SmolVLARFTGrader(nav_config)
    
    nav_scores = nav_grader.grade_trajectory(observations, actions, outcomes)
    logger.info(f"    Overall: {nav_scores['overall']:.4f}")
    logger.info(f"    Weights: {nav_grader.grader_weights}")
    
    return manip_grader, nav_grader


def demonstrate_rft_training_workflow():
    """Demonstrate the complete RFT training workflow"""
    logger.info("🚀 Stage 4: Complete RFT Training Workflow")
    
    # Configuration for demonstration
    config = RFTConfig(
        rft_iterations=5,  # Very small for demo
        training_examples=3,
        grader_type='expert_demonstration',
        task_type='manipulation',
        log_freq=1,
        save_freq=2
    )
    
    # Create trainer
    trainer = OpenAIRFTTrainer(config)
    
    logger.info(f"  Configuration:")
    logger.info(f"    RFT Iterations: {config.rft_iterations}")
    logger.info(f"    Training Examples: {config.training_examples}")
    logger.info(f"    Grader Type: {config.grader_type}")
    logger.info(f"    Task Type: {config.task_type}")
    
    # Simulate training loop
    logger.info("  Simulating RFT training loop:")
    
    for iteration in range(config.rft_iterations):
        # Collect trajectories (simulated)
        trajectories = trainer.collect_trajectories()
        
        # Grade trajectories
        graded_data = trainer.grade_trajectories(trajectories)
        
        # Update policy (simulated)
        metrics = trainer.update_policy(graded_data)
        
        # Log progress
        if iteration % config.log_freq == 0:
            logger.info(f"    Iteration {iteration}:")
            logger.info(f"      Mean Grade: {metrics['mean_grade']:.4f}")
            logger.info(f"      Grade Variance: {metrics['grade_variance']:.4f}")
            logger.info(f"      Loss: {metrics['loss']:.4f}")
    
    logger.info("  ✅ RFT training workflow completed!")
    
    return trainer


def demonstrate_advanced_configuration():
    """Demonstrate advanced configuration options"""
    logger.info("⚙️ Stage 5: Advanced Configuration")
    
    # Custom RFT configuration
    custom_config = RFTConfig(
        rft_iterations=1000,
        training_examples=50,
        responses_per_state=6,  # More action candidates
        grader_type='multi_objective',
        task_type='navigation',
        learning_rate=5e-6,     # Lower learning rate
        log_freq=10,
        save_freq=50
    )
    
    # Custom environment configuration
    env_config = EnvironmentConfig(
        max_joint_velocity=3.0,      # Higher velocity
        max_acceleration=2.5,         # Comfortable acceleration
        max_trajectory_time=45.0,     # Longer trajectories
        position_tolerance=0.02,      # More lenient positioning
        collision_threshold=0.1        # Larger safety margin
    )
    
    logger.info("  Custom RFT Configuration:")
    logger.info(f"    RFT Iterations: {custom_config.rft_iterations}")
    logger.info(f"    Training Examples: {custom_config.training_examples}")
    logger.info(f"    Responses per State: {custom_config.responses_per_state}")
    logger.info(f"    Learning Rate: {custom_config.learning_rate}")
    
    logger.info("  Custom Environment Configuration:")
    logger.info(f"    Max Joint Velocity: {env_config.max_joint_velocity} rad/s")
    logger.info(f"    Max Acceleration: {env_config.max_acceleration} m/s²")
    logger.info(f"    Max Trajectory Time: {env_config.max_trajectory_time} s")
    logger.info(f"    Position Tolerance: {env_config.position_tolerance} m")
    logger.info(f"    Collision Threshold: {env_config.collision_threshold} m")
    
    return custom_config, env_config


def demonstrate_integration_with_existing_pipeline():
    """Demonstrate integration with existing LeRobot pipeline"""
    logger.info("🔗 Stage 6: Integration with Existing Pipeline")
    
    # Simulate the two-stage approach
    logger.info("  Stage 1: Standard Imitation Learning (existing train.py)")
    logger.info("    - Use existing LeRobot train.py")
    logger.info("    - Train base policy from expert demonstrations")
    logger.info("    - Save checkpoint for RFT fine-tuning")
    
    logger.info("  Stage 2: RFT Fine-Tuning (new train_rft.py)")
    logger.info("    - Load base checkpoint")
    logger.info("    - Apply RFT with custom graders")
    logger.info("    - Save improved policy")
    
    # Example command-line usage
    logger.info("  Example Commands:")
    logger.info("    # Stage 1: Standard training")
    logger.info("    python lerobot/scripts/train.py \\")
    logger.info("      --policy.path=lerobot/smolvla_base \\")
    logger.info("      --dataset.repo_id=${HF_USER}/robot_demonstrations \\")
    logger.info("      --batch_size=64 --steps=20000 \\")
    logger.info("      --output_dir=outputs/train/smolvla_base")
    
    logger.info("    # Stage 2: RFT fine-tuning")
    logger.info("    python backend/src/backend/rft/train_rft.py \\")
    logger.info("      --checkpoint_path=outputs/train/smolvla_base/checkpoints/last \\")
    logger.info("      --grader_type=environment_feedback \\")
    logger.info("      --task_type=manipulation \\")
    logger.info("      --rft_iterations=1000 \\")
    logger.info("      --training_examples=50 \\")
    logger.info("      --output_dir=outputs/rft/smolvla_rft")


def main():
    """Main demonstration function"""
    logger.info("🎯 SmolVLA RFT Implementation Demo")
    logger.info("=" * 50)
    
    try:
        # Stage 1: Expert demonstration grader
        expert_grader = demonstrate_expert_grader()
        logger.info("")
        
        # Stage 2: Environment feedback grader
        env_grader = demonstrate_environment_grader()
        logger.info("")
        
        # Stage 3: Multi-objective grading
        manip_grader, nav_grader = demonstrate_multi_objective_grading()
        logger.info("")
        
        # Stage 4: RFT training workflow
        trainer = demonstrate_rft_training_workflow()
        logger.info("")
        
        # Stage 5: Advanced configuration
        custom_config, env_config = demonstrate_advanced_configuration()
        logger.info("")
        
        # Stage 6: Integration with existing pipeline
        demonstrate_integration_with_existing_pipeline()
        logger.info("")
        
        logger.info("✅ All demonstrations completed successfully!")
        logger.info("")
        logger.info("📚 Next Steps:")
        logger.info("  1. Implement real robot interface for environment feedback")
        logger.info("  2. Integrate with actual LeRobot training pipeline")
        logger.info("  3. Benchmark performance improvements")
        logger.info("  4. Deploy in real robotics applications")
        
    except Exception as e:
        logger.error(f"❌ Demo failed: {e}")
        raise


if __name__ == "__main__":
    main()