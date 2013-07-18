Name:           qemu.x86_64
Version:        1.2
Release:        0
License:        GPLv2
Summary:        Qemu Binaries
Group:          System
Source:         %{name}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}



%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%post

%postun

%files
%defattr(-,root,root)
/usr/bin/*
/usr/sbin/*

%changelog

