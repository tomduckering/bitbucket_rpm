#This stops the build from trying to repackage all the jar files
#that are part of wildlfy.
%global __os_install_post %{nil}

Name: bitbucket
Summary: The bitbucket development collaboration server
Version: 5.1.0
Release: 1
License: Proprietary
Group: TODO
Source: https://downloads.atlassian.com/software/stash/downloads/atlassian-bitbucket-5.1.0.tar.gz
Source1: https://github.com/tomduckering/bitbucket_rpm_extras/archive/master.tar.gz
URL: http://bitbucket.org
Distribution: RHEL6
Vendor: Red Hat
Packager: Tom Duckering <tom.duckering@gmail.com>
Requires: java => 1.8.0

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
cp -aR $RPM_BUILD_DIR/atlassian-%{name}-%{version} $RPM_BUILD_ROOT/opt/
mv $RPM_BUILD_ROOT/opt/atlassian-%{name}-%{version} $RPM_BUILD_ROOT/opt/%{name}
cp $RPM_BUILD_DIR/%{name}_rpm_extras-master/bitbucket.init $RPM_BUILD_ROOT/etc/init.d/bitbucket

%files
%defattr(-, root, root,-)
/opt/%{name}
%attr(755, root, root) /etc/init.d/bitbucket
