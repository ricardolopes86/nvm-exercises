#!/bin/bash
echo "Cleaning provisioned infrastructure and Ansible inventory..."
$(which terraform) destroy -auto-approve && > inventory
