mysql-master
=========

Role that will configure and prepare the MySQL master node.

Role Variables
--------------

`master_ip_address`: this variable contains the private IP for the master host, which will be used lately to configure the replication.

Dependencies
------------

It uses `PyMySQL` to connect and issue SQL statements against the database instance. Make sure you have it installed before running this role.

Example Playbook
----------------

How to use this role:

    - hosts: master
      become: yes
      gather_facts: yes
      roles:
        - mysql-master
