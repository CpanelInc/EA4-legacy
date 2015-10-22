Name: cpanel-ea4-legacy-release
Version: 0.1
Release: 2%{?dist}
Summary: Access the EA4-legacy repository

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
* Thu Oct 22 2015 Darren Mobley <darren@cpanel.net> - 0.1-2
- Finalized path for mirrorlist in .repo file

* Fri Oct 16 2015 Darren Mobley <darren@cpanel.net> - 0.1-1
- Renaming release packages due to conflicts in ea- namespace

* Tue Oct 13 2015 Darren Mobley <darren@cpanel.net> - 0.1-0
- Inital spec file and package creation
