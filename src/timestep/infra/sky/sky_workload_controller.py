import os

import sky
import yaml


class SkyWorkloadController:
    """Manages workloads using SkyPilot."""

    def __init__(self, project_config):
        """
        Initialize SkyPilot workload controller.

        Args:
            project_config (dict): Project-specific workload configuration
        """
        self.project_config = project_config

    def launch_task(self, task_spec, env_overrides={}, down=False):
        """
        Launch a specific workload task.

        Args:
            task_spec (dict): Task specification details

        Returns:
            Task execution result
        """
        print(f"Launching task: {task_spec}")
        print(f"Project config: {self.project_config}")
        # env_overrides = self.project_config.items()
        env_overrides = env_overrides.items()
        print("Env overrides:", env_overrides)

        yaml_path = task_spec

        with open(os.path.expanduser(yaml_path), "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        task = sky.Task.from_yaml_config(config, env_overrides=env_overrides)

        print("Task:", task)

        job_id, handle = sky.launch(task, detach_run=True, down=down)

        print(f"Task launched with job ID: {job_id}")
        return job_id, handle

    def monitor_tasks(self):
        """
        Monitor currently running tasks.

        Returns:
            List of active task statuses
        """
        raise NotImplementedError()
