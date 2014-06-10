# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	config.vm.box = "Trusty64"
	config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/20140418/trusty-server-cloudimg-amd64-vagrant-disk1.box"
	config.vm.network :forwarded_port, guest: 80, host:8080
end
