# -- mode: ruby --
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "web" do |web|
    web.vm.box = "debian/bullseye64"
    web.vm.hostname = "web"
    web.vm.network "public_network", bridge: "wlp4s0"
    web.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  end

  config.vm.define "freeswitch" do |freeswitch|
    freeswitch.vm.box = "debian/bullseye64"
    freeswitch.vm.hostname = "freeswitch"
    freeswitch.vm.network "public_network", bridge: "wlp4s0"
    freeswitch.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  end

  config.vm.provision "shell" do |s|
     key = Dir::home() + "/.ssh/id_rsa.pub"
     ssh_pub_key = File.readlines(key).first.strip
     s.inline = <<-SHELL
     echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
     #echo #{ssh_pub_key} >> /root/.ssh/authorized_keys
     SHELL
  end
  
  # Ansible playbook provisioning
    config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "1.8"
    ansible.playbook = "devops-test/provisioning/main.yml"
  end
end