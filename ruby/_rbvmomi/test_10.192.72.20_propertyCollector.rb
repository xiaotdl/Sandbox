require 'rbvmomi'
require 'pry'
require 'awesome_print'

def to_short_s(s, limit=100)
    if (s.to_s.size() > limit)
        s.to_s[0..limit] + "..."
    else
        s.to_s
    end
end

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

# #== retrieve host network info ==
# filterSpec = VIM.PropertyFilterSpec(
#   :objectSet => [{
#     :obj => host,
#     :skip => true,
#     :selectSet => [
#       VIM.TraversalSpec(
#         :type => 'HostSystem',
#         :path => 'configManager.networkSystem',
#         :skip => false,
#       )
#     ]
#   }],
#   :propSet => [{
#     :type => 'HostNetworkSystem',
#     :pathSet => %w(networkInfo.vswitch networkInfo.portgroup),
#   }]
# )

# #== retrieve rootFolder's childEntity(datacenters) ==
#filterSpec = VIM.PropertyFilterSpec(
#  :objectSet => [{
#    :obj => vim.serviceInstance.content.rootFolder,
#    #:skip => true,
#    :selectSet => [
#      VIM.TraversalSpec(
#        :type => 'Folder',
#        :path => 'childEntity',
#        :skip => false,
#      )
#    ]
#  }],
#  :propSet => [{
#    :type => 'Folder',
#    :all => true,
#    #:pathSet => %w(name parent childEntity datastore),
#  }]
#)

#r = propertyCollector.RetrievePropertiesEx(
#  :specSet => [filterSpec],
#  :options => { }
##)

dvportgroup = dc.network.find {|network| network.name.eql?("DHCP-AutoTest-Vlan-2130")}
filterSpec = VIM.PropertyFilterSpec(
  :objectSet=>[{:obj=>dvportgroup}],
  :propSet=>[{:type=>"DistributedVirtualPortgroup", :all=>true}]
)

r = propertyCollector.RetrieveProperties(:specSet => [filterSpec])
puts dvportgroup
puts r[0].propSet.map{|dynamicProp| "  #{dynamicProp.name} => "+to_short_s(dynamicProp.val)}

puts 'eof';
