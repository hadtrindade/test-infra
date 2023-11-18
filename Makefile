send-key:
	ssh-copy-id -i /home/hadd/.ssh/id_rsa user@192.168.1.14

black:
	black -l 79 monitoramento/*

nginx:
	@ansible-playbook -i ansible/hosts ansible/playbook.yaml -K 