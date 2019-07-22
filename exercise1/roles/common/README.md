Common
=========

Role to perform tasks that are common to all servers (i.e. deploy MySQL, configure it and etc).

Role Variables
--------------

`mysql_root_pass`: needs to be used to set the `root` password in each database instance. To set it, just enter in plain text to the file `files/root.txt`. Ansible will lookup for text in this file and will configure MySQL database root user with this password.

Dependencies
------------

It uses `PyMySQL` to connect and issue SQL statements against the database instance. Make sure you have it installed before running this role.

Example Playbook
----------------

How to use this role in your playbook:

    - hosts: master
      become: yes
      gather_facts: yes
      roles:
        - mysql-master
