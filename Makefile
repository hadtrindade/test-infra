.PHONY: prov nginx black

prov:
	@vagrant up

nginx:
	@ansible-playbook -i devops-test/hosts  devops-test/nginx/main.yml

freeswitch:
	@ansible-playbook -i devops-test/hosts devops-test/freeswitch/main.yml

black:
	@black -l 79 monitoramento/*
