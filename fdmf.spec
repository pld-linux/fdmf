%include	/usr/lib/rpm/macros.perl
Summary:	FDMF - find duplicate music files
Name:		fdmf
Version:	0.0.9j
Release:	0.1
License:	GPL
Group:		Applications/Sound
URL:		http://www.w140.com/audio/
Source0:	http://www.w140.com/audio/%{name}-%{version}.tar.gz
# Source0-md5:	5aca21e61ef3bb1cd876828af9c54d32
BuildRequires:	fftw3-devel
BuildRequires:	gdbm-devel
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	fftw3
Requires:	gdbm
Requires:	mpg321
Requires:	openssl-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dmf is portable perl/C software for finding pairs of music files in a
collection that are likely to contain the same music. It works on the
music itself, not on the filename, tags, or headers.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install cleanup_dups fdmf fdmf_bench optparam sonic_reducer vector_pairs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README
%attr(755,root,root) %{_bindir}/*
