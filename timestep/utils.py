import os
import signal
import subprocess
import urllib.request

from tqdm import tqdm


def download_with_progress_bar(url, filename):
    # Extract the basename of the file
    base_filename = os.path.basename(filename)

    # Define the reporthook function
    def reporthook(block_num, block_size, total_size):
        if pbar.total is None:
            pbar.total = total_size

        pbar.update(block_size)

    # Create a tqdm progress bar instance with a custom bar_format
    pbar = tqdm(
        unit="B",
        unit_scale=True,
        miniters=1,
        desc=base_filename,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.0f}%]",
    )

    # Use urlretrieve to download the file with the reporthook
    urllib.request.urlretrieve(url, filename, reporthook)

    # Close the progress bar
    pbar.close()


def start_shell_script(file_path, *args):
    try:
        # Construct the command with the script and the additional arguments
        command = ["sh", file_path] + list(args)

        # Open the script and redirect its stdout and stderr to log files for debugging
        with open("script_output.log", "w") as out, open(
            "script_error.log", "w"
        ) as err:
            process = subprocess.Popen(
                command,
                stdout=out,
                stderr=err,
                preexec_fn=os.setpgrp,  # Start the process in a new process group
            )

        print(f"Started the file: {file_path} with PID: {process.pid}")

        return process

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


def stop_shell_script(pid):
    try:
        # Kill the process group to ensure all child processes are terminated
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        print(f"Stopped the process with PID: {pid}")

    except Exception as e:
        print(f"An error occurred: {e}")
