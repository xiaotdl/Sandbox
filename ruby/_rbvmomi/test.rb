require 'rbvmomi'
require 'pry'

HOST = '10.192.72.20'
USER = 'root'
PASS = '123qweasd'
DATACENTER = 'DOS-LAB'
COMPUTE = 'DOS-Cluster'
CLUSTER_HOST = '10.192.12.51'

DHCP_PORT_GROUP = 'DHCP-AutoTest-Vlan-2130'

VIM = RbVmomi::VIM

vim = VIM.connect(host: HOST, user: USER, password: PASS, insecure: true)
dc = vim.serviceInstance.find_datacenter(DATACENTER) || fail("datacenter not found: #{DATACENTER}")
compute = dc.find_compute_resource(COMPUTE)
host = compute.host.select {|h| h.name.eql?(CLUSTER_HOST)}[0]
puts host
puts host.name
# #=>
# HostSystem("host-6085")
# 10.192.12.51

# vm = dc.find_vm('my_vm') || fail('VM not found')
# vm.PowerOnVM_Task.wait_for_completion


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
    :obj => host,
    :skip => true,
    :selectSet => [
      VIM.TraversalSpec(
        :type => 'HostSystem',
        :path => 'network',
        :skip => false,
      )
    ]
  }],
  :propSet => [{
    :type => 'Network',
    :pathSet => %w(name),
  }]
)

result = vim.propertyCollector.RetrievePropertiesEx(
  :specSet => [filterSpec],
  :options => { }
)

result.objects.each do |o|
    if (o.obj.name.eql?(DHCP_PORT_GROUP))
      puts o.obj
      puts o.obj.name
    end
end
# #=>
# DistributedVirtualPortgroup("dvportgroup-6163")
# DHCP-AutoTest-Vlan-2130

