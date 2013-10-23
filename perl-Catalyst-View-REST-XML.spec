%define upstream_name    Catalyst-View-REST-XML
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	XML View Class
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/Catalyst-View-REST-XML-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(XML::Simple)
BuildArch:	noarch

%description
This is the XML::Simple view class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/Catalyst/View/*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 680770
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 402994
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.01-4mdv2009.0
+ Revision: 255592
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.01-2mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-2mdv2008.0
+ Revision: 86062
- rebuild


* Thu Mar 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.01-1mdk
- Initial mdv rpm



