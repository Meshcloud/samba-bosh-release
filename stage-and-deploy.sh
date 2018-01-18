#!/bin/bash
set -e 

path=$(dirname $0)

cd $path
bosh create-release --force

bosh upload-release

bosh -d smb deploy -n manifests/smb-dev-local.yml