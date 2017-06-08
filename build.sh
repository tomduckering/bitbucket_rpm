#!/bin/sh -xe

if test "${TRAVIS}" = "true"
then
	BUILD_NUMBER=${TRAVIS_BUILD_NUMBER}
else
	BUILD_NUMBER="localbuild"
fi

export BUILD_NUMBER

 # Run build in Container
docker run --env BUILD_NUMBER --volume `pwd`:/spec_src tomduckering/el7_chef_rpm_builder bitbucket.spec
