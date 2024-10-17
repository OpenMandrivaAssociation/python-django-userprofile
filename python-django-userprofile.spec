%define realname    django-userprofile
%define name	    python-%{realname}
%define version 0.7
%define release 2

Name: %{name}
Version: %{version}
Release: %{release}
Summary:        A user private zone/profile management application
Group:          Development/Python
License:        BSD
URL:            https://transifex.org
Source:         userprofile-%{version}-r422-correct-validation.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
This is a user private zone/profile management application, allowing
the user to take control of his account and insert information about
him in his profile.

Inside this package you will find a demo application which will show
you what can be accomplished with the rest of the utilities included
in the package.

%prep
%setup -q -n userprofile-%{version}-r422-correct-validation
find . -name \*._* -exec rm {} +
find . -name \*.buildinfo* -exec rm {} +

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*



%changelog
* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7-1mdv2011.0
+ Revision: 591976
- import python-django-userprofile

