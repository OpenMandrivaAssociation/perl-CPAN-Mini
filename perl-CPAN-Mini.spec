%define upstream_name    CPAN-Mini
%define upstream_version 1.111013

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Create a minimal mirror of CPAN
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/CPAN-Mini-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More) >= 0.960.0
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
CPAN::Mini provides a simple mechanism to build and update a minimal mirror of
the CPAN on your local disk. It comes with a small utility, minicpan(1), to
create and update such mirrors.

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
%doc Changes README
%{perl_vendorlib}/CPAN
%{_mandir}/*/*
%{_bindir}/minicpan


%changelog
* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.7-1mdv2011.0
+ Revision: 674647
- update to new version 1.111007

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.6-1
+ Revision: 662788
- update to new version 1.111006

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.3-1
+ Revision: 659891
- update to new version 1.111003

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.2-1
+ Revision: 654003
- update to new version 1.111002

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.111.1-2
+ Revision: 640764
- rebuild to obsolete old packages

* Sat Feb 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.1-1
+ Revision: 637365
- update to new version 1.111001

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.0-1
+ Revision: 636579
- update to new version 1.111

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.0-1
+ Revision: 634217
- update to new version 1.110

* Fri Mar 05 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.630-1mdv2011.0
+ Revision: 514396
- update to 1.100630

* Tue Mar 02 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.593-1mdv2010.1
+ Revision: 513470
- update to 1.100593

* Sat Feb 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.576.0-3mdv2010.1
+ Revision: 505417
- rebuild using %%perl_convert_version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.576-2mdv2010.0
+ Revision: 440543
- rebuild

* Sat Jan 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.576-1mdv2009.1
+ Revision: 330404
- update to new version 0.576

* Wed Jan 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.575-1mdv2009.1
+ Revision: 329394
- update to new version 0.575

* Fri Nov 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.574-1mdv2009.1
+ Revision: 307434
- update to new version 0.574

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.573-1mdv2009.1
+ Revision: 307108
- update to new version 0.573

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.572-1mdv2009.1
+ Revision: 300684
- update to new version 0.572

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.571-2mdv2009.0
+ Revision: 268373
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.571-1mdv2009.0
+ Revision: 210845
- update to new version 0.571

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.570-1mdv2009.0
+ Revision: 201847
- update to new version 0.570

* Mon Mar 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.568-1mdv2008.1
+ Revision: 183287
- update to new version 0.568

* Thu Feb 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.567-1mdv2008.1
+ Revision: 173531
- update to new version 0.567

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.566-1mdv2008.1
+ Revision: 156853
- update to new version 0.566

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.565-1mdv2008.1
+ Revision: 110894
- new version

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.564-1mdv2008.1
+ Revision: 105302
- update to new version 0.564

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 0.563-1mdv2008.1
+ Revision: 101003
- update to new version 0.563

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.562-1mdv2008.0
+ Revision: 55686
- update to new version 0.562


* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 0.55.2-1mdv2007.0
+ Revision: 93907
- 0.552

* Sat Nov 18 2006 Olivier Thauvin <nanardon@mandriva.org> 0.55.1-1mdv2007.1
+ Revision: 85442
- 0.551
- 0.55
- Import perl-CPAN-Mini

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1mdv2007.0
- New version (upstream version 0.500)

* Thu Nov 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.40-1mdk
- 0.40

* Fri Oct 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.38-1mdk
- 0.38

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.36-3mdk
- Fix BuildRequires
- %%mkrel

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.36-2mdk
- buildrequires fix

* Fri Jan 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.36-1mdk
- 0.36

* Tue Dec 07 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.24-1mdk
- Initial MDK release.


