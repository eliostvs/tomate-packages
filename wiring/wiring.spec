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

Name: python3-wiring
Version: 0.0.0
Release: 0
License: GPL-3.0+
Summary: Architectural foundation for Python applications.
Source: %{name}-%{version}.tar.gz
Url: https://github.com/eliostvs/wiring

BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3-venusian

%description
Architectural foundation for Python applications.

%prep
%setup -q -n %{name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{modname}

%doc LICENSE README.rs

%changelog
