Name:		python-python-multipart
Version:	0.0.12
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/python-multipart/python_multipart-%{version}.tar.gz
Summary:	A streaming multipart parser for Python
URL:		https://pypi.org/project/python-multipart/
License:	None
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A streaming multipart parser for Python

%prep
%autosetup -p1 -n python_multipart-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/multipart
%{py_sitedir}/python_multipart-*.*-info
