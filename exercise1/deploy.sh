#!/bin/bash
echo "Provisioning Cloud infrastructure and deploying clustered MySQL with Ansible..."
$(which terraform) apply -auto-approve && $(which ansible-playbook) -i inventory provisioning.yml
