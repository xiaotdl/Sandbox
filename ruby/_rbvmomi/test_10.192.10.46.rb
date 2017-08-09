require 'rbvmomi'
require 'pry'

HOST = '10.192.10.46'
USER = 'root'
PASS = 'vmware'
DATACENTER = 'tCloud'
COMPUTE = '10.192.89.56'

VIM = RbVmomi::VIM

vim = VIM.connect(host: HOST, user: USER, password: PASS, insecure: true)
dc = vim.serviceInstance.find_datacenter(DATACENTER) || fail("datacenter not found: #{DATACENTER}")
compute = dc.find_compute_resource(COMPUTE)
puts compute

host = compute.host[0]
cm = host.configManager
ns = cm.networkSystem
#fullId = 'fit.raja.asm.sjc-lab.f5ne.88'
fullId = '123456789012345678901234567'
         #fit.raja.asm.sjc-lab.f5net.com.8.pg1
puts fullId.length
hostNetworkConfig = VIM.HostNetworkConfig(
  portgroup: [VIM.HostPortGroupConfig(
     changeOperation: :add,
     spec: VIM.HostPortGroupSpec(
       name: "#{fullId}.pg1",
       policy: VIM.HostNetworkPolicy(  ),
       vlanId: 4095,
       vswitchName: "#{fullId}.sw1"
     )
   )],
  vswitch: [VIM.HostVirtualSwitchConfig(
     changeOperation: :add,
     name: "#{fullId}.sw1",
     spec: VIM.HostVirtualSwitchSpec( numPorts: 24 )
   )]
)
res = ns.UpdateNetworkConfig(
  :config => hostNetworkConfig,
  :changeMode => :modify
)
