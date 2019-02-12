# -*- mode: ruby -*-
# vi: set ft=ruby :

# global vars
api_version = "2"
vm_name = "coinscraper"
sync_dir = "/tmp/coinscraper/"
ansible_dir = "/tmp/coinscraper/ansible/"
is_proxy = true

Vagrant.configure(api_version) do |config|
  
  config.vm.box = "ubuntu/xenial64" # server v16.04.05
  config.vm.define vm_name
  config.vm.hostname = vm_name
  config.vm.box_check_update = false

  # avaliacao da existencia do proxy
  if Vagrant.has_plugin?("vagrant-proxyconf") && is_proxy
    config.proxy.http     = "http://prxdf.prevnet:3128/"
    config.proxy.https    = "http://prxdf.prevnet:3128/"
  end

  # Mapeamento das portas guest e host
  config.vm.network "forwarded_port", guest: 3001, host: 3001

  # Mapeamento de sincronismo host e guest  
  config.vm.synced_folder ".", sync_dir
  
  # configuracoes gerais da maquina
  config.vm.provider "virtualbox" do |vb|
    # vb.gui = true
    vb.memory = "3072"
    vb.cpus = 2
    vb.name = vm_name
  end
 
  # configuracao para o provisionamento do conteudo da maquina
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.provisioning_path = ansible_dir
  end
end
