# 1. Replace a string across multiple files:
`grep -Rl --exclude "*.swp" "search" . | xargs -I '{}' bash -c "echo sed -i \"s/old/new/g\" {} && echo p4 edit {}"`




`xargs -a 123 -n 1 echo p4 edit`
# >>>
# p4 edit tests/adf.py
# p4 edit tests/afbzvz.py
# p4 edit tests/bvfddd.py


# grep -Rl --exclude "*.swp" "search" . > 123
# vim 123
# gf     // go to file
# ctrl+6 // go back

➜  ~  cat file
95:            self.bigip_selfip[device] = RCMD.asm.get_self_ip(dev.icontrol_rest)
177:        virtual = RCMD.asm.create_virtual_server(rstifc, self.VS_NAME,
178:                                                 "%s:%s" % (self.all_bps[device].selfip, self.bpcfg.vs_port))
185:        policy = RCMD.asm.import_asm_policy(rstifc, self.POLICY_NAME, file_path)

➜  ~  sed "s/RCMD.asm.\(.*\)(dev.icontrol_rest)/RCMD.asm.\1(device=device)/g" file
95:            self.bigip_selfip[device] = RCMD.asm.get_self_ip(device=device)

➜  ~  sed "/RCMD.asm.create_virtual_server(rstifc/{n;s/self.bpcfg.vs_port))/self.bpcfg.vs_port), device=device)/g}" file
178:                                                 "%s:%s" % (self.all_bps[device].selfip, self.bpcfg.vs_port), device=device)
➜  ~  sed "s/RCMD.asm.create_virtual_server(rstifc, \(.*\)/RCMD.asm.create_virtual_server(\1/g" file
177:        virtual = RCMD.asm.create_virtual_server(self.VS_NAME,


➜  ~  sed "s/RCMD.asm.\(.*\)(rstifc, \(.*\))/RCMD.asm.\1(\2, device=device)/g" file
185:        policy = RCMD.asm.import_asm_policy(self.POLICY_NAME, file_path, device=device)



sed "s/RCMD.asm.\(.*\)(rstifc)/RCMD.asm.\1(device=device)/g" file | sed "/RCMD.asm.create_virtual_server(rstifc/{n;s/self.bpcfg.vs_port))/self.bpcfg.vs_port), device=device)/g}" | sed "s/RCMD.asm.create_virtual_server(rstifc, \(.*\)/RCMD.asm.create_virtual_server(\1/g" | sed "s/RCMD.asm.\(.*\)(rstifc, \(.*\))/RCMD.asm.\1(\2, device=device)/g"

xili@xili-ubuntu-vm:~/.virtualenvs/testenv$ grep -nRIl "RCMD.asm.*(" tests/firestone4_5_1/functional/standalone/asm/ --exclude=*.{swo
,swp} | xargs -I '{}' bash -c "p4 edit -c 1523594 {} && sed -i \"s/RCMD.asm.\(.*\)(dev.icontrol_rest)/RCMD.asm.\1(device=device)/g\"
{} && sed -i \"/RCMD.asm.create_virtual_server(rstifc/{n;s/self.bpcfg.vs_port))/self.bpcfg.vs_port), device=device)/g}\" {} && sed -i
 \"s/RCMD.asm.create_virtual_server(rstifc, \(.*\)/RCMD.asm.create_virtual_server(\1/g\" {} && sed -i \"s/RCMD.asm.\(.*\)(rstifc, \(.
*\))/RCMD.asm.\1(\2, device=device)/g\" {}"