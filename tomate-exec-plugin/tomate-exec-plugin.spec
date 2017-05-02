#
# spec file for package tomate-exec-plugin
#
# Copyright (c) 2014 Elio Esteves Duarte <elio.esteves.duarte@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define real_name tomate
%define module_name %{real_name}_exec_plugin

Name: %{real_name}-exec-plugin
Version: 0.0.0
Release: 0
License: GPL-3.0+
Summary: Tomate exec commands plugin
Source: %{name}-%{version}.tar.gz
Url: https://github.com/eliostvs/tomate-exec-plugin

BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: tomate-gtk >= 0.6.0

%if 0%{?suse_version}
BuildArchitectures: noarch
%endif

%if 0%{?fedora}
BuildArch: noarch
%endif

%description
Run commands when the timer starts, stops or finishes

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_datadir}/%{real_name}/
%{_datadir}/%{real_name}/plugins/
%{python_sitelib}/%{module_name}-%{version}-*.egg-info/

%doc AUTHORS COPYING README.md

%changelog
