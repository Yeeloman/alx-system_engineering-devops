# Web Stack Debugging #2

This project is part of a series focused on debugging broken web stacks within isolated containers. The main objective is to restore each web stack to a functional state by identifying and resolving issues. For each task, a script is provided to automate the necessary commands for fixing the web stack.

## Tasks :page_with_curl:

### 0. Run Software as Another User

* [0-iamsomeonelese](./0-iamsomeonelese):
  * Bash script that executes the `whoami` command under the user passed as an argument.
  * Usage: `./0-iamsomeonelese <user>`

### 1. Run Nginx as Nginx

* [1-run_nginx_as_nginx](./1-run_nginx_as_nginx):
  * Bash script that resolves a web server issue, ensuring that Nginx runs and listens on port `8080` as the `nginx` user.

### 2. 7 Lines or Less

* [100-fix_in_7_lines_or_less](./100-fix_in_7_lines_or_less):
  * Bash script designed to fix a web server by configuring Nginx to run and listen on port `8080` as the `nginx` user.
  * Constrained to 7 lines.
