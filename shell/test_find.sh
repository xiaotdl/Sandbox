`find ../lib/F5/Fixture/ -name 'Generate*'`
# >>>
# ../lib/F5/Fixture/GenerateDpiRfcProtocolTests.pm
# ../lib/F5/Fixture/GenerateJSONTests.pm
# ../lib/F5/Fixture/GenerateDosTests.pm

`find ~/.ssh -printf "%m:%f\n"`
# >>>
# 755:.ssh
# 777:identity.pub
# 777:known_hosts
# 777:authorized_keys
# 644:README
# 777:identity

`cd .ssh; for f in $(ls -a); do stat -c "%a:%n" $f; done;`
# >>>
# 755:.
# 500:..
# 777:authorized_keys
# 777:identity
# 777:identity.pub
# 777:known_hosts
# 644:README


# execute file one by one
`find tmp/ -type f -exec echo -f {} \;`
# >>>
# -f tmp//main.py
# -f tmp//test.py
# -f tmp//utils/__init__.py
# -f tmp//utils/a.py

# rm all '.pyc' files
`find . -iname '*.pyc' -exec rm {} \;`
