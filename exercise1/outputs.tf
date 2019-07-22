output "master-address" {
  value = "${aws_instance.master-db.*.public_ip}"
}

output "replica-address" {
  value = "${aws_instance.replica-db.*.public_ip}"
}
