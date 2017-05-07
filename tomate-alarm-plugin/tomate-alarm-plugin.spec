#
# spec file for package tomate-alarm-plugin
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
%define module_name %{modname}_alarm_plugin

Name: %{modname}-alarm-plugin
Version: 0.0.0
Release: 0
License: GPL-3.0+
Summary: Tomate alarm plugin
Source: %{name}-%{version}.tar.gz
Url: https://github.com/eliostvs/tomate-alarm-plugin

BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: tomate-gtk >= 0.7.0

%if 0%{?suse_version}
BuildArchitectures: noarch
Requires: gstreamer-plugins-base
Requires: gstreamer-plugins-good
Requires: typelib-1_0-Gst-1_0
%endif

%if 0%{?fedora}
BuildArch: noarch
Requires: gstreamer1-plugins-base
Requires: gstreamer1-plugins-good
Requires: python3-gstreamer1
%endif

%description
Tomate plugin that plays a alarm at session end.

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
%{_datadir}/%{modname}/media/
%doc AUTHORS COPYING README.md

%changelog
