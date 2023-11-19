.PHONY: prov nginx black

prov:
	@vagrant up

nginx:
	@ansible-playbook -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory playbooks/nginx-playbook.yaml 

black:
	@black -l 79 monitoramento/*
