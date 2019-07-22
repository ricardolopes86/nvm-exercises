provider "aws" {
    profile = "default"
    region = "${var.aws_region}"
}

resource "aws_vpc" "default_vpc" {
  cidr_block = "10.0.1.0/24"
}

resource "aws_internet_gateway" "default" {
  vpc_id = "${aws_vpc.default_vpc.id}"
}

resource "aws_route" "access_internet" {
  route_table_id = "${aws_vpc.default_vpc.main_route_table_id}"
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = "${aws_internet_gateway.default.id}"
}

resource "aws_subnet" "default_subnet" {
  vpc_id = "${aws_vpc.default_vpc.id}"
  cidr_block = "10.0.1.0/28"
  map_public_ip_on_launch = true

}

resource "aws_security_group" "default_sg" {
  name = "nvm_db_security_group"
  description = "Our default Security Group"
  vpc_id = "${aws_vpc.default_vpc.id}"

  ingress {
      from_port = 22
      to_port = 22
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
      from_port = 3306
      to_port = 3306
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "ssh_key" {
  key_name = "${var.key_name}"
  public_key = "${file(var.public_key_path)}"
}


resource "aws_instance" "master-db" {

  connection {
    # The default username for our AMI
    user = "ubuntu"
    host = "${self.public_ip}"
  }

  ami = "${var.aws_instance_ami}"
  instance_type = "t2.medium"

  key_name = "${aws_key_pair.ssh_key.id}"
  vpc_security_group_ids = ["${aws_security_group.default_sg.id}"]
  subnet_id = "${aws_subnet.default_subnet.id}"
  provisioner "local-exec" {
    command = "echo [master] > inventory && echo ${aws_instance.master-db.public_ip} ansible_connection=ssh ansible_user=ubuntu >> inventory"
  }
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get -y update",
      "sudo apt-get install python-pip -y"
    ]
  }

}

resource "aws_instance" "replica-db" {

  connection {
    # The default username for our AMI
    user = "ubuntu"
    host = "${self.public_ip}"
  }

  ami = "${var.aws_instance_ami}"
  instance_type = "t2.medium"

  key_name = "${aws_key_pair.ssh_key.id}"
  vpc_security_group_ids = ["${aws_security_group.default_sg.id}"]
  subnet_id = "${aws_subnet.default_subnet.id}"

  provisioner "local-exec" {
    command = "echo [replica] >> inventory && echo ${aws_instance.replica-db.public_ip} ansible_connection=ssh ansible_user=ubuntu >> inventory"
  }
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get -y update",
      "sudo apt-get install python-pip -y"
    ]
  }
}
