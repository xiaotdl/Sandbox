find / -mount -size +100M -exec ls -lh {} \; | tee find.out
