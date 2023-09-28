# Loops, conditions and parsing

This repository contains a collection of Bash scripts that demonstrate various concepts related to loops, conditions, and parsing. These scripts are designed to help you understand and practice working with Bash, a popular shell scripting language.

## Table of Contents

1. [Helper File](#helper-file-raised_hands)
2. [Tasks](#tasks-page_with_curl)
    - [Task 0: Create a SSH RSA key pair](#task-0-create-a-ssh-rsa-key-pair)
    - [Task 1: For Best School loop](#task-1-for-best-school-loop)
    - [Task 2: While Best School loop](#task-2-while-best-school-loop)
    - [Task 3: Until Best School loop](#task-3-until-best-school-loop)
    - [Task 4: If 9, say Hi!](#task-4-if-9-say-hi)
    - [Task 5: 4 bad luck, 8 is your chance](#task-5-4-bad-luck-8-is-your-chance)
    - [Task 6: Superstitious numbers](#task-6-superstitious-numbers)
    - [Task 7: Clock](#task-7-clock)
    - [Task 8: For ls](#task-8-for-ls)
    - [Task 9: To file, or not to file](#task-9-to-file-or-not-to-file)
    - [Task 10: FizzBuzz](#task-10-fizzbuzz)
    - [Task 11: Read and cut](#task-11-read-and-cut)
    - [Task 12: Tell the story of passwd](#task-12-tell-the-story-of-passwd)
    - [Task 13: Let's parse Apache logs](#task-13-lets-parse-apache-logs)
    - [Task 14: Dig the data](#task-14-dig-the-data)

## Helper File :raised_hands:

- [apache-access.log](./apache-access.log): An Apache access log file parsed in tasks `102` and `103`.

## Tasks :page_with_curl:

### Task 0: Create a SSH RSA key pair

- [0-RSA_public_key.pub](./0-RSA_public_key.pub): A public SSH key uploaded for the purposes of ALX.

### Task 1: For Best School loop

- [1-for_best_school](./1-for_best_school): Bash script that displays `Best School` 10 times using a `for` loop.

### Task 2: While Best School loop

- [2-while_best_school](./2-while_best_school): Bash script that displays `Best School` 10 times using a `while` loop.

### Task 3: Until Best School loop

- [3-until_best_school](./3-until_best_school): Bash script that displays `Best School` 10 times using an `until` loop.

### Task 4: If 9, say Hi!

- [4-if_9_say_hi](./4-if_9_say_hi): Bash script that displays `Best School` 10 times using a `while` loop. For the 9th iteration, it displays `Best School` and then `Hi` on a new line, using an `if` statement.

### Task 5: 4 bad luck, 8 is your chance

- [5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance): Bash script that loops from 1 to 10 using a `while` loop and:
    - Displays `bad luck` on the 4th iteration.
    - Displays `good luck` on the 8th iteration.
    - Displays `Best School` for all other iterations.
    - Uses the `if`, `elif`, and `else` statements.

### Task 6: Superstitious numbers

- [6-superstitious_numbers](./6-superstitious_numbers): Bash script that displays numbers from `1` to `20` using a `while` loop and:
    - Displays `4` and then `bad luck from China` for the 4th iteration.
    - Displays `9` and then `bad luck from Japan` for the 9th iteration.
    - Displays `17` and then `bad luck from Italy` for the 17th iteration.
    - Uses a `case` statement.

### Task 7: Clock

- [7-clock](./7-clock): Bash script that displays the time for 12 hours and 59 minutes. It displays hours from `0` to `12` and minutes from `0` to `59`.

### Task 8: For ls

- [8-for_ls](./8-for_ls): Bash script that displays the contents of the current directory in list format. Only the part of the name after the first dash is displayed.

### Task 9: To file, or not to file

- [9-to_file_or_not_to_file](./9-to_file_or_not_to_file): Bash script that gives information about the `bestschool` file. Depending on its state, it displays messages such as:
    - `school file exists` if the file exists.
    - `school file does not exist` if the file does not exist.
    - `school file is empty` if the file exists and is empty.
    - `school file is not empty` if the file exists and is not empty.
    - `school file is a regular file` if the file exists and is a regular file.

### Task 10: FizzBuzz

- [10-fizzbuzz](./10-fizzbuzz): Bash script that displays numbers from `1` to `100` in list format. It displays `FizzBuzz` when the number is a multiple of 3 and 5, `Fizz` when the number is a multiple of 3, `Buzz` when the number is a multiple of 5, and the number itself for all other cases.

### Task 11: Read and cut

- [100-read_and_cut](./100-read_and_cut): Bash script that displays the contents of the `/etc/passwd` file, showing only the username, user id, and user home directory path for each line.

### Task 12: Tell the story of passwd

- [101-tell_the_story_of_passwd](./101-tell_the_story_of_passwd): Bash script that tells stories based on the contents of the `/etc/passwd` file. It displays information about users in the format: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY, and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`.

### Task 13: Let's parse Apache logs

- [102-lets_parse_apache_logs](./102-lets_parse_apache_logs): Bash script that extracts and displays the visitor IP along with the HTTP status code from logs read from an Apache access log file. It uses `awk` for parsing.

### Task 14: Dig the data

- [103-dig_the-data](./103-dig_the-data): Bash script that reads content from an Apache log access file and

 groups visitors by IP and HTTP status code, displaying the grouped number of visitors to an IP address. The logs are grouped in order of greatest to lowest number of visitors. This task also utilizes `awk` for data manipulation.

Feel free to explore these scripts to learn and practice your Bash scripting skills. Happy scripting! :computer:
