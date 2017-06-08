#This stops the build from trying to repackage all the jar files
#that are part of wildlfy.
%global __os_install_post %{nil}

Name: bitbucket
Summary: The bitbucket development collaboration server
Version: 4.14.5
Release: 1
License: Proprietary
Group: TODO
Source: https://www.atlassian.com/software/stash/downloads/binary/atlassian-bitbucket-4.14.5.tar.gz
Source1: https://github.com/tomduckering/bitbucket_rpm_extras/archive/master.tar.gz
URL: http://bitbucket.org
Distribution: RHEL6
Vendor: Red Hat
Packager: Tom Duckering <tom.duckering@gmail.com>
Requires: java => 1.8.0
Requires(pre): shadow-utils

%description
TODO: Bitbucket description

%prep
%setup -b0 -q -n atlassian-%{name}-%{version}
%setup -b1 -q -n %{name}_rpm_extras-master

%build
#No compilation step

%install
install -d $RPM_BUILD_ROOT/opt/
install -d $RPM_BUILD_ROOT/etc/init.d
install -d $RPM_BUILD_ROOT/etc/sysconfig
cp -aR $RPM_BUILD_DIR/atlassian-%{name}-%{version} $RPM_BUILD_ROOT/opt/
mv $RPM_BUILD_ROOT/opt/atlassian-%{name}-%{version} $RPM_BUILD_ROOT/opt/%{name}
#Install extra bits to make it behave well
cp $RPM_BUILD_DIR/%{name}_rpm_extras-master/bitbucket.init $RPM_BUILD_ROOT/etc/init.d/bitbucket
cp $RPM_BUILD_DIR/%{name}_rpm_extras-master/bitbucket.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/bitbucket

%files
%defattr(-, bitbucket, bitbucket,-)
/opt/%{name}
/etc/sysconfig/%{name}
%attr(755, root, root) /etc/init.d/bitbucket

%pre
USERNAME="bitbucket"
GROUPNAME="bitbucket"
HOMEDIR="/opt/bitbucket"

getent group ${GROUPNAME} >/dev/null || groupadd -f -r ${GROUPNAME}
getent passwd ${USERNAME} >/dev/null || useradd -r -g ${GROUPNAME} -d ${HOMEDIR} -s /sbin/nologin -c "The service account for bitbucket" ${USERNAME}
fi
exit 0
