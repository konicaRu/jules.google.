# F1 Daily Info

This script fetches and displays the countdown to the next Formula 1 race, along with the current driver and constructor standings.

## How to Run

1.  **Install Python:** If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

2.  **Install the `requests` library:** Open a command prompt or PowerShell and run the following command:
    ```
    pip install requests
    ```

3.  **Run the script:** Open a command prompt or PowerShell, navigate to the directory where you saved `f1_info.py`, and run the following command:
    ```
    python f1_info.py
    ```

## How to Schedule Daily Execution on Windows

You can use the Windows Task Scheduler to run this script automatically every day.

1.  **Open Task Scheduler:** Press the Windows key, type "Task Scheduler", and press Enter.

2.  **Create a new task:** In the right-hand pane, click "Create Basic Task...".

3.  **Name the task:** Give the task a name (e.g., "F1 Daily Info") and a description, then click "Next".

4.  **Set the trigger:** Choose "Daily" and click "Next". Set the time you want the script to run each day and click "Next".

5.  **Set the action:** Choose "Start a program" and click "Next".

6.  **Configure the action:**
    *   In the "Program/script" field, type `python.exe`.
    *   In the "Add arguments (optional)" field, type the full path to your `f1_info.py` script (e.g., `C:\Users\YourUser\Documents\f1_info.py`).
    *   Click "Next".

7.  **Finish:** Review the settings and click "Finish".

Now, the script will run automatically at the time you specified each day, and you will see the output in a command prompt window that appears briefly.
