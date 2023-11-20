# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"
  config.vm.define "debian11"
  config.vm.network "public_network", bridge: "wlp4s0"
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end

  config.vm.provision "shell" do |s|
    key = Dir::home() + "/.ssh/id_rsa.pub"
    ssh_pub_key = File.readlines(key).first.strip
    s.inline = <<-SHELL
    echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
    echo #{ssh_pub_key} >> /root/.ssh/authorized_keys
    SHELL
    end

  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "1.8"
    ansible.playbook = "ansible/playbooks/prov-playbook.yaml"
    ansible.groups = {
      "webservers" => ["debian12"],
    }
  end
end
