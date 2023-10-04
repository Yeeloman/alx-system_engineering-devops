# Networking Basics #0

This project marks the beginning of our journey into the world of networking. Throughout this project, we explore fundamental networking concepts, including the OSI model, LAN and WAN networks, and the TCP/UDP data transfer protocols.

## Tasks :page_with_curl:

* **0. OSI Model**
  * [0-OSI_model](./0-OSI_model): This text file answers crucial questions about the OSI model, providing insights into its structure and functionality.
  * What is the OSI model?
    1. A set of specifications that network hardware manufacturers must adhere to.
    2. The OSI model is a conceptual framework that characterizes communication functions within a telecommunication system, independent of underlying technology.
    3. The OSI model is a framework that characterizes the communication functions within a telecommunication system, with a strong focus on the underlying technology.
  * How is the OSI model organized?
    1. Alphabetically.
    2. From the lowest to the highest level.
    3. Randomly.

* **1. Types of Networks**
  * [1-types_of_network](./1-types_of_network): This text file provides insights into different types of networks and their usage scenarios.
  * What type of network is a computer in a local environment connected to?
    1. Internet.
    2. WAN.
    3. LAN.
  * What type of network could connect an office in one building to another office in a building a few streets away?
    1. Internet.
    2. WAN.
    3. LAN.
  * What network do you use when you browse www.google.com from your smartphone (not connected to Wi-Fi)?
    1. Internet.
    2. WAN.
    3. LAN.

* **2. MAC and IP Addresses**
  * [2-MAC_and_IP_address](./2-MAC_and_IP_address): This text file delves into the concepts of MAC and IP addresses, elucidating their significance.
  * What is a MAC address?
    1. The name of a network interface.
    2. The unique identifier of a network interface.
    3. A network interface.
  * What is an IP address?
    1. Is to devices connected to a network what a postal address is to houses.
    2. The unique identifier of a network interface.
    3. Is a number that network devices use to connect to networks.

* **3. UDP and TCP**
  * [3-UDP_and_TCP](./3-UDP_and_TCP): This text file clarifies the differences between UDP and TCP data transfer protocols.
  * Which statement is correct for the TCP box?
    1. It is a protocol that transfers data slowly but reliably.
    2. It is a protocol that transfers data quickly and may lose data in the process.
  * Which statement is correct for the UDP box?
    1. It is a protocol that transfers data slowly but reliably.
    2. It is a protocol that transfers data quickly and may lose data in the process.
  * Which statement is correct for the TCP worker?
    1. Have you received boxes x, y, z?
    2. May I increase the rate at which I am sending you boxes?

* **4. TCP and UDP Ports**
  * [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports): This Bash script displays listening ports, showcasing only listening sockets. It additionally reveals the PID and name of the program associated with each socket.

* **5. Is the Host on the Network**
  * [5-is_the_host_on_the_network](./5-is_the_host_on_the_network): This Bash script pings an IP address provided as an argument five times, checking for network connectivity.
  * Usage: `5-is_the_host_on_the_network {IP_ADDRESS}`.
