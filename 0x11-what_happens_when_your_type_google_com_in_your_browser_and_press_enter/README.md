# 0x11. What happens when you type google.com in your browser and press Enter

## Task Responses :

* **0. What happens when...**
  * [0-blog_post](./0-blog_post)

* **1. Everything's better with a pretty diagram**
  * [1-what_happen_when_diagram](./1-what_happen_when_diagram)

## Project Questions and Requirements :☑️

### Task 0

#### What happens when you type https://www.google.com in your browser and press Enter:

- **DNS Request:**
  - Browser initiates a Domain Name System (DNS) request to resolve www.google.com to an IP address.

- **TCP/IP:**
  - Transmission Control Protocol/Internet Protocol (TCP/IP) establishes a connection to the identified IP address.

- **Firewall:**
  - The request passes through a firewall, which monitors and controls incoming and outgoing network traffic.

- **HTTPS/SSL:**
  - Secure Sockets Layer (SSL) handshake occurs to establish a secure encrypted connection (HTTPS).

- **Load-Balancer:**
  - If applicable, the request is distributed through a load balancer to optimize server resource utilization.

- **Web Server:**
  - The web server receives the request and processes it to serve static content like HTML files.

- **Application Server:**
  - The application server, if necessary, generates dynamic content and interacts with databases.

- **Database:**
  - Data may be retrieved or updated in the database based on the application server's request.

### Task 1

#### Request Flow Diagram:

- **DNS Resolution:**
  - Illustrates the process of translating www.google.com into an IP address.

- **Server IP and Port:**
  - Shows the request reaching the server's IP address on the appropriate port.

- **Traffic Encryption:**
  - Indicates that the traffic is encrypted using HTTPS/SSL.

- **Firewall:**
  - Depicts the request passing through a firewall for security checks.

- **Load Balancer:**
  - Visualizes the load balancer distributing the request among multiple servers.

- **Web Server Response:**
  - Demonstrates the web server responding by serving the requested web page.

- **Application Server Interaction:**
  - Shows the application server generating dynamic content and interacting with the database.
