# Processes and Signals

This project explores process management and signal handling in the Bash scripting environment, utilizing various commands such as `ps`, `pgrep`, `pkill`, `exit`, and `trap`.

## Tasks :page_with_curl:

### Task 0: What is my PID
- [0-what-is-my-pid](./0-what-is-my-pid): This Bash script displays its own Process ID (PID).

### Task 1: List your processes
- [1-list_your_processes](./1-list_your_processes): A Bash script that provides a list of currently running processes.
  - It includes all processes for all users, even those without a terminal (TTY).
  - The list of processes is organized in a user-oriented hierarchy.

### Task 2: Show your Bash PID
- [2-show_your_bash_pid](./2-show_your_bash_pid): This Bash script displays lines containing the keyword `bash` based on the output from `1-list_your_processes`.

### Task 3: Show your Bash PID made easy
- [3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy): A Bash script that displays the Process ID (PID) along with the process name for processes containing the word `bash`.

### Task 4: To infinity and beyond
- [4-to_infinity_and_beyond](./4-to_infinity_and_beyond): A Bash script that repeatedly displays `To infinity and beyond`, with a `sleep 2` delay between each iteration.

### Task 5: Don't stop me now!
- [5-dont_stop_me_now](./5-dont_stop_me_now): This Bash script terminates the [4-to_infinity_and_beyond](./4-to_infinity_and_beyond) process using the `kill` command.

### Task 6: Stop me if you can
- [6-stop_me_if_you_can](./6-stop_me_if_you_can): This Bash script terminates the [4-to_infinity_and_beyond](./4-to_infinity_and_beyond) process using the `pkill` command.

### Task 7: Highlander
- [7-highlander](./7-highlander): A Bash script that continuously displays `To infinity and beyond`, with a `sleep 2` delay between each iteration.
  - Upon receiving a `SIGTERM` signal, it displays `I am invincible!!!`.

### Task 8: Beheaded process
- [8-beheaded_process](./8-beheaded_process): This Bash script terminates the [7-highlander](./7-highlander) process.

### Task 9: Process and PID file
- [100-process_and_pid_file](./100-process_and-pid-file): A Bash script that creates the file `/var/run/holbertonscript.pid`, containing its own PID, and continuously displays `To infinity and beyond`.
  - Upon receiving a `SIGTERM` signal, it displays `I hate the kill command`.
  - Upon receiving a `SIGINT` signal, it displays `Y U no love me?!`.
  - The script also deletes the file `/var/run/holbertonscript.pid` and terminates itself upon receiving either the `SIGQUIT` or `SIGTERM` signal.

### Task 10: Manage my process
- [manage_my_process](./manage_my_process): A Bash script that writes `I am alive!` to the file `/tmp/my_process` indefinitely, with a two-second sleep between each write.
- [101-manage_my_process](./101-manage-my-process): A Bash script that manages the [manage_my_process](./manage_my_process) script.
  - When passed the argument `start`, it starts [manage_my_process](./manage_my_process), creates a file containing its PID in `/var/run/my_process.pid`, and displays `manage_my_process started`.
  - When passed the argument `stop`, it stops [manage_my_process](./manage_my_process), deletes the file `/var/run/my_process.pid`, and displays `manage_my_process stopped`.
  - When passed the argument `restart`, it stops [manage_my_process](./manage_my_process), deletes the file `/var/run/my_process.pid`, starts `manage_my_process`, creates a file containing its PID in `/var/run/my_process.pid`, and displays `manage_my_process started`.
  - Otherwise, it displays `Usage: manage_my_process {start|stop|restart}`.

### Task 11: Zombie
- [102-zombie.c](./102-zombie.c): A C program that generates five zombie processes and, for each one created, displays `Zombie process created, PID: <ZOMBIE_PID>`.

This project offers a comprehensive exploration of process management and signal handling within the Bash scripting environment. Each task tackles different aspects of these concepts, enhancing your understanding and proficiency in handling processes and signals.
