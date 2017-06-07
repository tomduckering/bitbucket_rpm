FROM centos:7
RUN yum -y install epel-release
RUN yum -y install rpm-build rpmdevtools redhat-rpm-config yum-utils rpmlint
RUN rpmdev-setuptree
ADD ./build_rpm_in_mock.sh /build_rpm_in_mock.sh
RUN chmod u+x ./build_rpm_in_mock.sh
ADD ./build_rpm.sh /build_rpm.sh
RUN chmod u+x ./build_rpm.sh
VOLUME /spec_src
ENTRYPOINT ["/build_rpm.sh"]

