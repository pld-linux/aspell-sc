Summary:	Sardinian dictionary for aspell
Summary(pl.UTF-8):	Słownik sardyński dla aspella
Name:		aspell-sc
Version:	1.0
#%%define	subv	0
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/sc/aspell5-sc-%{version}.tar.bz2
# Source0-md5:	05284890c3445c5850a3c1410790a057
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sardinian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik sardyński (lista słów) dla aspella.

%prep
%setup -q -n aspell5-sc-%{version}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
