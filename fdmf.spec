%include	/usr/lib/rpm/macros.perl
Summary:	FDMF - find duplicate music files
Summary(pl.UTF-8):	FDMF - szukanie duplikatów plików muzycznych
Name:		fdmf
Version:	0.0.9r
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://www.w140.com/audio/%{name}-%{version}.tar.gz
# Source0-md5:	1d79911c83605a68573d0a2ea8a01d18
URL:		http://www.w140.com/audio/
BuildRequires:	fftw3-devel
BuildRequires:	gdbm-devel
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	plotutils
Requires:	mplayer
Suggests:	mpg123
Suggests:	vorbis-tools
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
%attr(755,root,root) %{_bindir}/cleanup_dups
%attr(755,root,root) %{_bindir}/fdmf
%attr(755,root,root) %{_bindir}/fdmf_bench
%attr(755,root,root) %{_bindir}/optparam
%attr(755,root,root) %{_bindir}/sonic_reducer
%attr(755,root,root) %{_bindir}/vector_pairs
