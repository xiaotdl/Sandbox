#!/usr/bin/env ruby

# Copyright (c) 2011-2017 VMware, Inc.  All Rights Reserved.
# SPDX-License-Identifier: MIT

require 'pry'
require 'trollop'
require 'rbvmomi'
require 'rbvmomi/trollop'

VIM = RbVmomi::VIM

opts = Trollop.options do
  banner <<-EOS
List all vms.

VIM connection options:
    EOS

    rbvmomi_connection_opts

    text <<-EOS

VM location options:
    EOS

    rbvmomi_datacenter_opt

    text <<-EOS

Other options:
  EOS

end

Trollop.die("must specify host") unless opts[:host]

vim = VIM.connect opts
dc = vim.serviceInstance.find_datacenter(opts[:datacenter]) or abort "datacenter not found"

#def list_all_vms(folder, indent = "") # recursively go thru a folder, dumping vm info
#   folder.childEntity.each do |x|
#      name, junk = x.to_s.split('(')
#      case name
#      when "Folder"
#         puts indent + "#{x.to_s}: #{x.name}"
#         list_all_vms(x, " " * indent.length + "  |--")
#      when "VirtualMachine"
#         puts indent + x.name
#      else
#         puts "# Unrecognized Entity " + x.to_s
#      end
#   end
#end

#list_all_vms(dc.vmFolder)

def find_vm_by_name_recursively(folder, vm_name)
   folder.childEntity.each do |child|
      name, junk = child.to_s.split('(')
      case name
      when "Folder"
          #puts child.to_s
         vm = find_vm_by_name_recursively(child, vm_name)
         if vm
             return vm
         end
      when "VirtualMachine"
          #puts child.to_s + " ==> " + child.name
         if child.name.eql?(vm_name)
             return child
         end
      else
         raise "Error: # Unrecognized Entity " + child.to_s
      end
   end
   return nil
end


# ruby test.rb --insecure --host=10.192.72.20 --user=root --password=123qweasd --datacenter=DOS-LAB
vm = find_vm_by_name_recursively(dc.vmFolder, "fit.xili-cluster-fitdev1.2.tr")
puts vm
puts vm.name
