# MySQL

In this project, I focused on configuring database servers in a primary-replica model. The task involved setting up two servers provided by ALX as a MySQL primary-replica configuration. Additionally, I created a Bash script to automate the generation of database backups.

## Tasks :

### 4-mysql_configuration_primary

- The MySQL `my.conf` configuration file used to set up the first server as a primary database server on the database `tyrell_corp`.
- [4-mysql_configuration_primary](./4-mysql_configuration_primary)

### 4-mysql_configuration_replica

- The MySQL `my.conf` configuration file used to set up the second server as the replica database server on the database `tyrell_corp`.
- [4-mysql_configuration_replica](./4-mysql_configuration_replica)

### 5-mysql_backup

- Bash script for generating a compressed `tar.gz` archive from a MySQL dump.
  - **Usage:** `./5-mysql_backup <MySQL root password>`
  - Generates a dump containing all MySQL databases on the root server.
  - Names the resulting tar archive in the format `day-month-year.tar.gz`.
- [5-mysql_backup](./5-mysql_backup)
