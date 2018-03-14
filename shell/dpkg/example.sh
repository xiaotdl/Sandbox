$ apt-cache search <pkg_pattern>

$ apt list --installed
...


$ dpkg -l virtualbox-5.2
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                                   Version                  Architecture             Description
+++-======================================-========================-========================-=================================================================================
ii  virtualbox-5.2                         5.2.0-118431~Ubuntu~trus amd64                    Oracle VM VirtualBox


$ dpkg -L virtualbox-5.2 | grep '/usr/bin' | head -n 5
/usr/bin
/usr/bin/VBoxDTrace
/usr/bin/VBoxTunctl
/usr/bin/VBox
/usr/bin/rdesktop-vrdp
