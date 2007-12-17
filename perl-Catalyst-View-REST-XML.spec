%define realname Catalyst-View-REST-XML
%define name	 perl-%{realname}
%define version	 0.01
%define release	 %mkrel 2

Summary:	XML View Class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:	perl-Catalyst >= 5
BuildRequires:	perl(XML::Simple)
BuildArch:	noarch

%description
This is the XML::Simple view class.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Catalyst/View/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

