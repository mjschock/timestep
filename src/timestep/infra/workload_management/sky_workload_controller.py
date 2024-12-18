class SkyWorkloadController:
    """Manages workloads using SkyPilot."""

    def __init__(self, project_config):
        """
        Initialize SkyPilot workload controller.

        Args:
            project_config (dict): Project-specific workload configuration
        """
        raise NotImplementedError()

    def launch_task(self, task_spec):
        """
        Launch a specific workload task.

        Args:
            task_spec (dict): Task specification details

        Returns:
            Task execution result
        """
        raise NotImplementedError()

    def monitor_tasks(self):
        """
        Monitor currently running tasks.

        Returns:
            List of active task statuses
        """
        raise NotImplementedError()
