require 'rbvmomi'
require 'pry'
require 'uri'

def to_short_s(s, limit=100)
    if (s.to_s.size() > limit)
        s.to_s[0..limit] + "..."
    else
        s.to_s
    end
end

HOST = '10.192.50.223'
USER = 'root'
PASS = '123qweasd'
DATACENTER = 'PDLab'
COMPUTE = 'ASM_LAB'
CLUSTER_HOST = '10.192.197.23'

VIM = RbVmomi::VIM

vim = VIM.connect(host: HOST, user: USER, password: PASS, insecure: true)

dc = vim.serviceInstance.find_datacenter(DATACENTER) || fail("datacenter not found: #{DATACENTER}")
compute = dc.find_compute_resource(COMPUTE)

host = compute.host.select {|h| h.name.eql?(CLUSTER_HOST)}[0]
puts host
cm = host.configManager
ns = cm.networkSystem


propertyCollector = vim.propertyCollector
## TODO Retreive distrubuted port groups, to allow distributed
## port group to be selected when cloning.  See
## Action::Clone.prepare_network_card_backing_info.
#
# #== retrieve host network info ==
# filterSpec = VIM.PropertyFilterSpec(
#   :objectSet => [{
#	 :obj => host,
#	 :skip => true,
#	 :selectSet => [
#	   VIM.TraversalSpec(
#		 :type => 'HostSystem',
#		 :path => 'configManager.networkSystem',
#		 :skip => false,
#	   )
#	 ]
#   }],
#   :propSet => [{
#	 :type => 'HostNetworkSystem',
#	 :pathSet => %w(networkInfo.vswitch networkInfo.portgroup),
#   }]
# )
#r = propertyCollector.RetrieveProperties(:specSet => [filterSpec])

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

   filterSpec = VIM.PropertyFilterSpec(
	 :objectSet=>dc.network.map{|network| {:obj => network}},
	 :propSet=>[{:type=>"DistributedVirtualPortgroup", :all=>true}]
   )
   
   r = propertyCollector.RetrieveProperties(:specSet => [filterSpec])
   #puts r
   #puts r.class
   #puts r.size
   #puts r[0].propSet.map{|dynamicProp| "  #{dynamicProp.name} => "+to_short_s(dynamicProp.val)}
   dvpg = []
   r.each do |objectContent|
	 dvpg << objectContent.obj
	 puts "== #{objectContent.class}, #{objectContent.obj}, #{objectContent.obj.name} =="
	 puts "== #{objectContent.class}, #{objectContent.obj}, #{objectContent.obj.name} =="
	 #if objectContent.obj.name.eql?("DHCP-AutoTest-Vlan-2130")
	 #end
	 #objectContent.propSet.each do |p|
	 #  puts "  #{p.name} => "+to_short_s(p.val)
	 #  #network_info[:portgroup].concat(p.val)
	 #end
   end
#   puts dvpg

puts 'eof';
