#!/usr/bin/env bash
#
# Calls kernel-install on all kernels found in /usr/lib/modules
#
# Run kernel install for all the installed kernels
while read -r kernel; do
    kernelversion=$(basename "${kernel%/vmlinuz}")
    echo "Installing kernel ${kernelversion}"
    kernel-install add ${kernelversion} ${kernel}
done < <(find /usr/lib/modules -maxdepth 2 -type f -name vmlinuz)
