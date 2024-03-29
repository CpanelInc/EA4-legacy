Name: ea4-legacy
Version: 0.1
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4602 for more details
%define release_prefix 6
Release: %{release_prefix}%{?dist}.cpanel
Summary: Access the EA4 legacy repository

Group: Development/Tools
License: BSD 2-Clause
Vendor: cPanel, Inc.
Requires: yum

%description
This package puts in please the EA4-legacy.repo file needed to use the software related to EA4 from cPanel that is no longer actively supported.

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -m 644 %_sourcedir/EA4-legacy.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/EA4-legacy.repo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/EA4-legacy.repo

%changelog
* Thu Apr 13 2023 Dan Muey <dan@cpanel.net> - 0.1-6
- ZC-10895: make `From repo` have OS info akin to `APT-Sources`

* Wed Sep 14 2016 Dan Muey <dan@cpanel.net> - 0.1-5
- EA-5221: Change package name to match github for clarity

* Mon Jun 20 2016 Dan Muey <dan@cpanel.net> - 0.1-4
- EA-4383: Update Release value to OBS-proof versioning

* Thu Oct 22 2015 Darren Mobley <darren@cpanel.net> - 0.1-2
- Finalized path for mirrorlist in .repo file

* Fri Oct 16 2015 Darren Mobley <darren@cpanel.net> - 0.1-1
- Renaming release packages due to conflicts in ea- namespace

* Tue Oct 13 2015 Darren Mobley <darren@cpanel.net> - 0.1-0
- Inital spec file and package creation
