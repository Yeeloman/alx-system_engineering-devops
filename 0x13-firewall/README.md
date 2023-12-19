# Firewall Configuration Project

In this project, I employed the Uncomplicated Firewall (`ufw`) to set up and configure firewalls on the designated web servers.

## Tasks :

### Task 0: Block All Incoming Traffic Except for Specific Ports
- **Script:** [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but)
- **Description:** This Bash script installs a `ufw` firewall on a web server, blocking all incoming traffic except for essential ports such as `22` (SSH), `443` (HTTPS), and `80` (HTTP).

### Task 1: Port Forwarding
- **Configuration File:** [100-port_forwarding](./100-port_forwarding)
- **Description:** This `ufw` configuration file facilitates port forwarding by redirecting incoming traffic on port `8080/TCP` to port `80/TCP`.
