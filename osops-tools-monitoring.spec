
%global service example

Name:		osops-tools-monitoring
Version:        XXX
Release:        XXX
Summary:	OpenStack Monitoring tools
License:	ASL 2.0
URL:		http://launchpad.net/osops-tools-monitoring/

Source0:	?

BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
BuildRequires:  git


%description
Monitoring for OpenStack Operators.

%package -n python-osops-tools-monitoring
Summary:	Example Python libraries

Requires:       python2-psutil
Requires:       python-six
Requires:       python3-six
Requires:       python2-psutil
Requires:       python-ceilometerclient
Requires:       python-cinderclient
Requires:       python-glanceclient
Requires:       python-keystoneclient
Requires:       python-neutronclient
Requires:       python-novaclient

%description -n python-osops-tools-monitoring
Python Monitoring tools for OpenStack Operators.


# Let's handle dependencies ourseleves
rm -f *requirements.txt

%changelog
