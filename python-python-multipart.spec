%define module python_multipart
%define oname multipart
%bcond tests 1

Name:		python-python-multipart
Summary:	A streaming multipart parser for Python
Version:	0.0.22
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/python-multipart/
Source0:	https://files.pythonhosted.org/packages/source/p/python-multipart/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pyyaml)
%endif

%description
A streaming multipart parser for Python.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
