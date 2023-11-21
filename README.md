# Estudos de infraestrutura.


# Instruções para rodar


### Instalação do ansible e httpx
```bash
pip install -r requirements.txt 
```

#### Antes de provisionar o Vagrant deve estar instalado juntamente com o Virtualbox.

### Provisionamento das VMs
```bash
make 
```

### Executar playbook para instalação do NGINX
```bash
make nginx 
```

### Executar o playbook para instalaçãodo freeSWITCH
```bash
make freeswitch
```
