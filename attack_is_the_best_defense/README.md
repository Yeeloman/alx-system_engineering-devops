# Network Security Exploration

## Tools

* Wireshark
* Telnet
* Tcpdump
* Docker
* Hydra

## 0-0-sniffing

### What is this?

Security encompasses various domains, with network security being a critical aspect. Networks transmit sensitive information, making them susceptible to interception by malicious entities. A malicious machine can pretend to be a network device, intercepting and analyzing traffic for potentially sensitive data. It's crucial to forward the intercepted traffic to its intended destination after analysis.

Unencrypted information, especially over legacy systems like telnet, can be easily intercepted. In this project, we explore sniffing unencrypted traffic to extract information.

SendGrid, an email service, supports both secure and unsecured methods, including telnet. The task involves executing the script `user_authenticating_into_server` locally, sniffing the network using tcpdump, and finding the password used in the authentication.

### Solution

* The code in ASCII = `bXlwYXNzd29yZDk4OTgh7`

* User name: `mylogin`

### Packet

```packet
  0000   d8 b6 b7 a1 1f 63 cc b0 da 2a bf b6 08 00 45 10   .....c...*....E.
0010   00 4a 40 f2 40 00 40 06 62 67 c0 a8 01 07 12 c5   .J@.@.@.bg......
0020   c2 d0 b5 12 02 4b 67 8b 60 d1 67 35 59 20 80 18   .....Kg.`.g5Y ..
0030   01 f5 a3 88 00 00 01 01 08 0a 21 35 2c 39 b2 84   ..........!5,9..
0040   5c 4c 62 58 6c 77 59 58 4e 7a 64 32 39 79 5a 44   \LbXlwYXNzd29yZD
0050   6b 34 46 6d 47 68 0d 0a                           k4FmGh..
```

## 1-dictionary_attack

Password-based authentication systems are vulnerable to dictionary attacks. Let's apply this technique to an SSH account.

* Install Docker on your Ubuntu Vagrant machine.
* Pull and run the Docker image `sylvainkalache/264-1` using the command `docker run -p 2222:22 -d -ti sylvainkalache/264-1`.
* Obtain a password dictionary (create your own if necessary).
* Install and use Hydra to perform a brute force attack on the SSH account `sylvain` on the Docker container.
* As the Docker container is running locally, Hydra should access the SSH account via IP `127.0.0.1` and port `2222`.
* Hint: The password is 11 characters long.

**Source:**
[Project Repository](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/264/user_authenticating_into_server)
