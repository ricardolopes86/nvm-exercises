# NVM Exercises

## Exercise 1:
Using AWS: 
1. Automate the creation of two Linux instances with MySQL;
2. Configure MySQL with one master and one slave with replication enabled between these two databases;
3. Create a data structure of your choice capturing name, address, phone number;
4. Create a script to insert 1000 entries of data into the DB;
5. Create a script which performs monitoring. Insert a record into the master and monitor on the slave. Alert if there is a replication deplay of more than 1s.

## Exercise 2:
Write a program in Python (or any other language) based on the following requirements:  

First, program must accept 6 consecutive numbers from command line arguments (each number is one argument).  
Second, program must present to the user the simple choice menu in standard output and operate accordingly in the background with the numbers the user entered previously:
* Perform subtraction and show output on screen comma separated;
* Perform multiplication and store result in a JSON file (i.e.  
```json
    {
      "InputNumber1": "x",
      "InputNumber2": "y",
      "InputNumber3": "a",
      "InputNumber4": "b",
      "InputNumber5": "c",
      "InputNumber6": "d",
      "Multiplication": "X"
    }
```
where: `x`, `y`, `a`, `b`, `c` and `d` are user line arguments and `X` is the multiplication result.)

* Pick randomly a numbers and show it on the screen;
* Print sorted (highest to lowest) array/list of numbers;
* Print sorted (lowest to highest) array/list of numbers.

Keep in mind that the program must respond appropriately upon possible human-errors. Also, the above choice menu must run forever on a loop until the user kills the program through SIGINIT or CTRL+C.

# How to Use

## Pre-requisites
This project was created to run in *nix based O.S (i.e Linux, Unix or MacOS).  
In order to have it running properly in your computer, you should have the following list of software installed and configured in your system:
* `python 3.*`
* `pip`
* `ansible`
* `terraform`
* `aws cli`

### Setup tools
#### Install `python`
In order to have `python3` installed in your system:

In Debian based distro (like Ubuntu):

    $ sudo apt-get install python3

In Slackware based distro (like Fedora or CentOS):

    $ sudo yum install centos-release-scl
    $ sudo yum install rh-python36
    $ scl enable rh-python36 bash

#### Install `pip`
Issue the following command to install `pip`:  

In Debian based distro (like Ubuntu):

    $ sudo apt-get install python3-pip

In Slackware based distro (like Fedora or CentOS):

    $ sudo yum install python36-setuptools
    $ sudo easy_install-3.4 pip

#### Install `ansible`
You can install `ansible` without access to root or sudo, by issuing the following command:

    $ pip3 install ansible --user

#### Install `terraform`
For *nix, just run the following steps to have your installation of `terraform`:

    $ wget https://releases.hashicorp.com/terraform/0.12.5/terraform_0.12.5_linux_amd64.zip
    $ unzip terraform_0.12.5_linux_amd64.zip
    $ sudo mv terraform /usr/bin/terraform

#### Install `aws cli`
AWS command line interface can me installed using `pip3`:

    $ pip3 install awscli --upgrade --user

Your `aws` credentials should have rights to create resources in AWS.  

After installing it, don't forget to configure and create the `default` profile with your `aws_access_key_id` and `aws_secret_access_key`. For further instructions on achieving this, please, follow the official AWS instructions at [AWS website](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html)

## Step-by-step

Once you have everything configured, type (or copy and paste) the following commands to have this project running and provisioning your infrastructure:

    $ git clone https://github.com/ricardolopes86/nvm-exercises.git
    $ cd nvm-exercises/exercise1/

Use your favorite text editor to edit the following files:
* `roles/{common|mysql-master|mysql-replicas}/files/root.txt` - your disired root password goes here, just plain text is fine. If the directory doesn't existe, please, create it. This pipe `|`, means that for each item pipe-separated, you should change/create;
* `roles/{common|mysql-master|mysql-replicas}/files/replica.txt` - your disired replication user password goes here, just plain text is fine. If the directory doesn't existe, please, create it. This pipe `|`, means that for each item pipe-separated, you should change/create;
* `roles/{common|mysql-master|mysql-replicas}/vars/main.yml` - at line 5, change the content between quotes (I know, that's not secure, but the purpose of this exercise is to show different ways of working with ansible variables. For prod environment, we should use `ansible vault` for each and every secret in our repository). In this directory, you can define many other variables values.

`Ansible` will connect to the hosts via `ssh` protocol, as it's new connection, it will ask you to confirm if you'd like to add the keys to the `authorized_keys` in your personal computer. Because we wan't to work in a fully automated fashion, we're going to disable this prompt by:  

a. Setting and environment variable that `ansible` will read before executing the playbook:

    $ export ANSIBLE_HOST_KEY_CHECKING=False

b. Setting the configuration file for `ansible`. Add the following lines to `~/.ansible.cfg` or to `/etc/ansible/ansible.cfg`:

    [defaults]
    host_key_checking = False

If it's the first time you're using this project, the you should run:

    $ ./deploy.sh

Once you're done, run the `clean` script to shutdown and destroy the infrastructure provisioned:

    $ ./clean.sh

# How does it works

## TL;DR

The whole infrastructure will be provisioned with `Terraform` files `maint.tf`, `outputs.tf` and `variables.tf`. Where `main` defines the infrastructure itself, like AWS as the provider, EC2 Instances, VPC, Security Group, Subnet, Internet Gateway, Routes, and the AWS Keys. In `outputs` we will just, at the end of the provisioning, print the public IP for each instance. In `variables`, we just use as space for customizing some options in our `main`.  

Once our infrastructure is provisioned, we then use the `Terraform` `provisioner` to run some commands, both locally and remotely. Locally we're dumping the `inventory` file with configuration (list of hosts and their role in our infra, i.e. master or replica) which `Ansible` will use to run the playbooks against.  

We're now in the `Ansible` phase. It will run a playbook with `roles`: `common`, `mysql-master` and `mysql-replicas`. `common` will perform actions that are common to both hosts: install MySQL Server and MySQL Client, `pip` for `python` modules, set root user password, create users and so on. `mysql-master` will perform tasks related to master only, like: change `mysqld.cnf` file to master become a master indeed, create table, dump data which will be imported in our replica. Finally, `mysql-replicas` will keep actions related to replicas only, including configure `mysqld.cnf`, import data exported from master, change to master and so on.  

Last, but not least, we have our cluster set up, we now run a `python` program to inset 1K roles into our `users` table. The program will read `user_data.csv` and `INSERT INTO` our table. It was done on purpose line by line to give a chance to the monitoring script catch any lag between `master` and `replica` - the proper way should be in batches, not line-by-line.