#
# spec file for package tomate-notify-plugin
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

%define modname tomate

Name: %{modname}-notify-plugin
Version: 0.0.0
Release: 0
License: GPL-3.0+
Summary: Tomate notify plugin
Source: %{name}-%{version}.tar.gz
Url: https://github.com/eliostvs/tomate-notify-plugin

BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%if 0%{?suse_version}
BuildArchitectures: noarch
Requires: typelib-1_0-Notify-0_7
%endif

%if 0%{?fedora}
BuildArch: noarch
Requires: libnotify
Requires: notification-daemon
%endif

%description
Tomate plugin that shows screen notifications.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*.egg-info
%dir %{_datadir}/%{modname}/
%{_datadir}/%{modname}/plugins/
%doc AUTHORS COPYING README.md CHANGELOG.md

%changelog
