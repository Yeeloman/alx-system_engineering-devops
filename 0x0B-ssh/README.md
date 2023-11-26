# SSH Project Readme

## Project Overview

In this project, I gained experience in connecting to and working with servers using the SSH (Secure Shell) protocol. The project involved tasks aimed at understanding and implementing secure communication with a server provided by ALX.

## Tasks :

### 1. **Use a Private Key**
   - **Script**: [0-use_a_private_key](./0-use_a_private_key)
   - **Description**: Bash script utilizing the `ssh` command to establish a connection to the ALX-provided server using a private key.
   - **Implementation Details**: The script is designed to enhance security by using a private key for authentication.

   [Source for Secure Connection](https://www.ssh.com/ssh/)

### 2. **Create an SSH Key Pair**
   - **Script**: [1-create_ssh_key_pair](./1-create_ssh_key_pair)
   - **Description**: Bash script responsible for generating an RSA key pair.
   - **Implementation Details**: The script facilitates the creation of a secure key pair for cryptographic authentication.

   [Source for SSH Key Pair Generation](https://www.ssh.com/ssh/keygen/)

### 3. **Client Configuration File**
   - **Script**: [2-ssh_config](./2-ssh_config)
   - **Description**: SSH configuration file (`ssh_config`) setup to use the private key located at `~/.ssh/school` and configured to reject authentication via password.
   - **Implementation Details**: The configuration file optimizes security by specifying key-based authentication and denying password-based authentication.

   [Source for SSH Configuration](https://www.ssh.com/ssh/config/)

By completing these tasks, the project aims to provide a foundational understanding of secure communication protocols and server authentication using SSH.

For more information on SSH and its applications, refer to the provided sources above.
