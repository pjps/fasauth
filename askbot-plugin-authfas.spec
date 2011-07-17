%global srcname fasauth

Name:		askbot-plugin-authfas
Version:	0.1
Release:	2%{?dist}
Summary:	Askbot plugin to facilitate FAS authentication

Group:		Development/Libraries
License:	GPLv2+
URL:		http://pjp.fedorapeople.org/
Source0:	http://pjp.fedorapeople.org/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-setuptools

Requires:	askbot
Requires:	python-fedora

%description
Askbot plugin to facilitate FAS authentication. It uses python-fedora
package to send the authentication requests.

It exports a single API which is used by the Askbot server to perform
authentication. It returns True or False based on the authentication result.

 - Boolean check_password(username, password)

%prep
%setup -q -n %{srcname}-%{version}


%build
CFLAGS=$RPM_OPT_FLAGS %{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT


%files
%doc README fedora.png settings.py
%{python_sitelib}/*
%{python_sitelib}/*.egg-info/


%changelog
* Sat Jul 16 2011 P J P <pj.pandit@yahoo.co.in> - 0.1-2
- fixed setup.py to distribute files like README, COPYING etc.
- fixed errors pointed out in the review.

* Wed Jul 12 2011 P J P <pj.pandit@yahoo.co.in> - 0.1-1
- Initial RPM for askbot-plugin-authfas.
