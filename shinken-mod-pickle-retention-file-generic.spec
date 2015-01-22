Name:		shinken-mod-pickle-retention-file-generic
Version:	1.4.1
Release:	2kaji0.2
Summary:	Shinken Module Pickle Retention for all daemons

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/shinken-mod-pickle-retention-file-generic
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

Requires:	shinken-common >= 2.0

%description
Shinken Pickle Retention module for all daemons

%prep
%setup -q


%build


%install
rm -rf %{buildroot}/*

install -d %{buildroot}/usr/share/pyshared/shinken/modules/pickle-retention-file-generic
install -pm07555 module/* %{buildroot}/usr/share/pyshared/shinken/modules/pickle-retention-file-generic

install -d %{buildroot}/usr/share/doc/%{name}
install -pm0755 README.md %{buildroot}/%{_docdir}/%{name}

install -d %{buildroot}/etc/shinken/modules
install -pm0755 etc/modules/* %{buildroot}/etc/shinken/modules


%files
/usr/share/pyshared/shinken/modules/pickle-retention-file-generic
%config(noreplace) %{_sysconfdir}/shinken/modules/

%docdir
%{_docdir}/%{name}


%changelog
* Wed Jan 21 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 1.4.1-2kaji0.2
- Initial Package
