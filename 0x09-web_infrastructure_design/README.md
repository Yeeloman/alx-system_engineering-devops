# 0x09. Web Infrastructure Design

This project is part of the Full Stack Software Engineering curriculum at ALX. It focuses on understanding the principles of designing a web infrastructure.

## Key Concepts
- Network basics
- Server
- Web server
- Application server
- DNS & DNS record types
- Load Balancer
- Monitoring
- Database
- Single point of failure
- HTTP & HTTPS
- Firewall

## File Descriptions

The project consists of multiple files, each of which represents a stage in designing a web infrastructure:

### [0-simple_web_stack](0-simple_web_stack)

In this stage, you design a basic web infrastructure on a whiteboard. The infrastructure hosts a website accessible via `www.foobar.com`. It starts with a user wanting to access your website. You must include the following components:

- 1 physical server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name `foobar.com` configured with a `www` record that points to your server's IP address `8.8.8.8`.

### [1-distributed_web_infrastructure](1-distributed_web_infrastructure)

In this stage, you expand the web infrastructure to include three servers that host the website `www.foobar.com`. You build upon the components in [0-simple_web_stack] and add:

- 2 physical servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

### [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)

In this stage, you enhance the web infrastructure to make it secure, enable encrypted traffic, and implement monitoring. Building on [1-distributed_web_infrastructure], you include:

- 3 firewalls
- 1 SSL certificate to serve `www.foobar.com` over HTTPS
- 3 monitoring clients (data collectors for Sumologic or other monitoring services)

### [3-scale_up](3-scale_up)

This final stage further expands the infrastructure designed in [2-secured_and_monitored_web_infrastructure]. You incorporate:

- 1 physical server
- 1 load-balancer (HAproxy) configured as a cluster with the existing one
- Split components (web server, application server, database) with their own servers.

## File Overview

| Filename                                     | Description                                              |
| -------------------------------------------- | -------------------------------------------------------- |
| [0-simple_web_stack](./0-simple_web_stack)   | Design a basic LAMP stack web infrastructure.            |
| [1-distributed_web_infrastructure](./1-distributed_web_infrastructure) | Expand the infrastructure with additional components. |
| [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure) | Enhance security and monitoring. |
| [3-scale_up](./3-scale_up)                   | Further scale up the infrastructure.                    |

