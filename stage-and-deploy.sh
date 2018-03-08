#!/bin/bash
set -e 

path=$(dirname $0)

cd $path
bosh create-release --force

bosh upload-release

bosh -d samba deploy -n manifests/smb-dev-local.yml