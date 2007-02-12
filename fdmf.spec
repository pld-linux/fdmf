%include	/usr/lib/rpm/macros.perl
Summary:	FDMF - find duplicate music files
Summary(pl.UTF-8):	FDMF - szukanie duplikatów plików muzycznych
Name:		fdmf
Version:	0.0.9q
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.w140.com/audio/%{name}-%{version}.tar.gz
# Source0-md5:	10fa68d4b4c14f4b65ae526c17b02f6d
URL:		http://www.w140.com/audio/
BuildRequires:	fftw3-devel
BuildRequires:	gdbm-devel
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	fftw3
Requires:	gdbm
Requires:	mpg123
Requires:	ogg123
Requires:	openssl-tools
Requires:	plotutils
Requires:	perl-GDBM_File
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dmf is portable Perl/C software for finding pairs of music files in a
collection that are likely to contain the same music. It works on the
music itself, not on the filename, tags, or headers.

%description -l pl.UTF-8
dmf to przenośny program w Perlu/C do znajdowania w swojej kolekcji
par plików muzycznych, które najprawdopodobniej zawierają tę samą
muzykę. Porównuje samą muzykę, a nie nazwę pliku, znaczniki czy
nagłówki.

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
