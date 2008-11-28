%define module      CPAN-Mini
%define name        perl-%{module}
%define version     0.574
%define release     %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Create a minimal mirror of CPAN
License:    GPL or Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CPAN/%{module}-%{version}.tar.gz
BuildRequires:  perl(URI)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(File::HomeDir)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
CPAN::Mini provides a simple mechanism to build and update a minimal mirror of
the CPAN on your local disk. It comes with a small utility, minicpan(1), to
create and update such mirrors.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

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


