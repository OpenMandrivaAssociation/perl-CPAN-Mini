%define upstream_name    CPAN-Mini
%define upstream_version 1.111

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Create a minimal mirror of CPAN
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(URI)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
CPAN::Mini provides a simple mechanism to build and update a minimal mirror of
the CPAN on your local disk. It comes with a small utility, minicpan(1), to
create and update such mirrors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/CPAN
%{_mandir}/*/*
%{_bindir}/minicpan
