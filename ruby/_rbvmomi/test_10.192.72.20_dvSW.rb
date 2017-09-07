require 'rbvmomi'
require 'pry'

HOST = '10.192.72.20'
USER = 'root'
PASS = '123qweasd'
DATACENTER = 'DOS-LAB'
COMPUTE = 'DOS-Cluster'
CLUSTER_HOST = '10.192.12.51'

VIM = RbVmomi::VIM

vim = VIM.connect(host: HOST, user: USER, password: PASS, insecure: true)
dc = vim.serviceInstance.find_datacenter(DATACENTER) || fail("datacenter not found: #{DATACENTER}")
compute = dc.find_compute_resource(COMPUTE)
puts compute

host = compute.host.select {|h| h.name.eql?(CLUSTER_HOST)}[0]
puts host
cm = host.configManager
ns = cm.networkSystem

propertyCollector = vim.propertyCollector

# TODO Retreive distrubuted port groups, to allow distributed
# port group to be selected when cloning.  See
# Action::Clone.prepare_network_card_backing_info.

#filterSpec = VIM.PropertyFilterSpec(
#  :objectSet => [{
#    :obj => host,
#    :skip => true,
#    :selectSet => [
#      VIM.TraversalSpec(
#        :type => 'HostSystem',
#        :path => 'configManager.networkSystem',
#        :skip => false,
#      )
#    ]
#  }],
#  :propSet => [{
#    :type => 'HostNetworkSystem',
#    :pathSet => %w(networkInfo.vswitch networkInfo.portgroup),
#  }]
#)

filterSpec = VIM.PropertyFilterSpec(
  :objectSet => [{
    :obj => vim.serviceInstance.content.rootFolder,
    #:skip => true,
    :selectSet => [
      VIM.TraversalSpec(
        :type => 'Folder',
        :path => 'childEntity',
        :skip => false,
      )
    ]
  }],
  :propSet => [{
    :type => 'Folder',
    :pathSet => %w(name parent childEntity),
  }]
)

result = propertyCollector.RetrievePropertiesEx(
  :specSet => [filterSpec],
  :options => { }
)
binding.pry; # RUBY BREAKPOINT
puts result;

#rootFolder.inventory_flat();

puts 'eof';
