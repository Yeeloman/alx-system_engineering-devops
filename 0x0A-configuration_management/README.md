# Configuration Management with Puppet

In this project, I delved into the realm of configuration management using Puppet. This powerful tool allows me to define and enforce the desired state of a system by writing Puppet manifest files. Throughout this project, I honed my skills in creating files, installing packages, and executing commands using Puppet.

## Tasks :page_with_curl:

### **Task 0: Create a File**
- **Manifest File:** [0-create_a_file.pp](./0-create_a_file.pp)
  - Creates a file named `school` in the `/tmp` directory.
  - **File Permissions:** `0744`
  - **File Group:** `www-data`
  - **File Owner:** `www-data`
  - **File Content:** `I love Puppet`

  [Source Code - 0-create_a_file.pp](./0-create_a_file.pp)

### **Task 1: Install a Package**
- **Manifest File:** [1-install_a_package.pp](./1-install_a_package.pp)
  - Installs the `flask` package from pip3.

  [Source Code - 1-install_a_package.pp](./1-install_a_package.pp)

### **Task 2: Execute a Command**
- **Manifest File:** [2-execute_a_command.pp](./2-execute_a_command.pp)
  - Kills the process named `killmenow`.

  [Source Code - 2-execute_a_command.pp](./2-execute_a_command.pp)

These Puppet manifest files showcase practical configurations, providing a hands-on experience in orchestrating system states with Puppet.

*Explore the source code for each task to understand the Puppet syntax and implementation details.*

**Source:**
- [Puppet Documentation](https://puppet.com/docs/puppet/latest/)
