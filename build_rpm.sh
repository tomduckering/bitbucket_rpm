#!/bin/bash -e

SPEC_FILE_NAME=$1

cd /root/rpmbuild

#Copy spec file into generic location
cp /spec_src/${SPEC_FILE_NAME} /root/rpmbuild/SPECS/build.spec

#Lint the spec file
rpmlint --verbose SPECS/build.spec

#Fetch sources
spectool -g -R SPECS/build.spec

#Install build dependencies
yum-builddep -y SPECS/build.spec

#Install build the binary package
rpmbuild -bb SPECS/build.spec

cp -aR RPMS /spec_src
