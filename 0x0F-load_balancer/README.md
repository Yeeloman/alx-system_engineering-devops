# Load Balancer Project Readme

## Project Overview

In this project, the objective is to enhance the web server configuration established in Project 0x0B. Two additional servers are introduced: one to replicate the Nginx configuration of the original server, and the other to implement an HAproxy load balancer. The load balancer is responsible for managing both web servers efficiently.

## Tasks :

### 0. Double the number of webservers
- **Script Description:** [0-custom_http_response_header](./0-custom_http_response-header) is a Bash script designed to install and configure Nginx on a server with a specific HTTP response header.
  - The HTTP header is named `X-Served-By`.
  - The value of the HTTP header is set to the hostname of the server.

[Source for Task 0](./0-custom_http_response-header)

### 1. Install your load balancer
- **Script Description:** [1-install_load_balancer](./1-install_load_balancer) is a Bash script tasked with installing and configuring HAproxy version 1.5 on a server.
  - Enables management via the init script.
  - Implements a round-robin algorithm for distributing requests.

[Source for Task 1](./1-install_load_balancer)

By completing these tasks, the project aims to enhance the web server configuration and introduce effective load balancing for improved performance and reliability.
