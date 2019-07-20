variable "aws_region" {
  description = "Region where resource will be provisioned."
  default = "eu-west-2"
}

variable "aws_instance_ami" {
  description = "The default AMI used to deploy our instances."
  default = "ami-0cbe2951c7cd54704"
}
