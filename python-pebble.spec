#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Threading and multiprocessing eye-candy
Summary(pl.UTF-8):	Miłe dla oka wątli i wieloprocesowość
Name:		python-pebble
Version:	4.4.0
Release:	5
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pebble/
Source0:	https://files.pythonhosted.org/packages/source/p/pebble/Pebble-%{version}.tar.gz
# Source0-md5:	c8c06548a13af018bfa247ae1ecdd844
URL:		https://pypi.org/project/Pebble/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-futures
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pebble provides a neat API to manage threads and processes within an
application.

%description -l pl.UTF-8
Pebble udostępnia schludne API do zarządzania wątkami i procesami
wewnątrz aplikacji.

%package -n python3-pebble
Summary:	Threading and multiprocessing eye-candy
Summary(pl.UTF-8):	Miłe dla oka wątli i wieloprocesowość
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pebble
Pebble provides a neat API to manage threads and processes within an
application.

%description -n python3-pebble -l pl.UTF-8
Pebble udostępnia schludne API do zarządzania wątkami i procesami
wewnątrz aplikacji.

%prep
%setup -q -n Pebble-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/pebble
%{py_sitescriptdir}/Pebble-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pebble
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/pebble
%{py3_sitescriptdir}/Pebble-%{version}-py*.egg-info
%endif
