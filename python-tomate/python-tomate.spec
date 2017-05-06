#
# spec file for package python-tomate
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

Name: python-%{real_name}
Version: 0.0.0
Release: 0
License: GPL-3.0+
Source: %{real_name}-%{version}.tar.gz
Url: https://github.com/eliostvs/tomate
Summary: A pomodoro timer

BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3-blinker
Requires: python3-six
Requires: python3-wiring
Requires: python3-wrapt
Requires: python3-pyxdg
Requires: python3-gobject

%if 0%{?fedora}
BuildArch: noarch
Requires: python3-dbus
Requires: python3-yapsy
%endif

%if 0%{?suse_version}
BuildArchitectures: noarch
Requires: dbus-1-python3
Requires: python-Yapsy
%endif

%description
A pomodoro timer. Core classes.

%prep
%autosetup -n %{real_name}-%{version}

%build
%py3_build
%{__python} setup.py build

%install
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{real_name}
%doc AUTHORS COPYING README.md

%changelog
