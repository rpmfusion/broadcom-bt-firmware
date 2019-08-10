%global commit0 c0bd928b8ae5754b6077c99afe6ef5c949a58f32
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           broadcom-bt-firmware
Version:        12.0.1.1012
Release:        6%{?dist}
Summary:        Firmware of Broadcom WIDCOMM Bluetooth devices

License:        Redistributable, no modification permitted
URL:            https://github.com/winterheart/broadcom-bt-firmware
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
BuildRequires:  hardlink
Requires:       usbutils
Requires:       bluez


%description
This package provides the firmware of Broadcom WIDCOMM Bluetooth
devices (including BCM20702, BCM20703, BCM43142 chipsets and other)
for Linux kernel.


%prep
%autosetup -n %{name}-%{commit0} -p1


%build
# Nothing to build


%install
mkdir -p %{buildroot}/lib/firmware/brcm/
cp -pr brcm/* %{buildroot}/lib/firmware/brcm/
hardlink %{buildroot}/lib/firmware/brcm/

touch %{buildroot}/lib/firmware/brcm/BCM.hcd


%files
%doc DEVICES.md README.md
%license LICENSE.broadcom_bcm20702
%dir /lib/firmware/brcm
/lib/firmware/brcm/*.hcd
%ghost /lib/firmware/brcm/BCM.hcd


%changelog
* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 12.0.1.1012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 12.0.1.1012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 12.0.1.1012-4
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 12.0.1.1012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 12.0.1.1012-2
- Owns bcrm
- Fix spaces and tabs

* Wed Sep 13 2017 Nicolas Chauvet <kwizart@gmail.com> - 12.0.1.1012-1
- Update to 12.0.1.1012

* Wed May 17 2017 Nicolas Chauvet <kwizart@gmail.com> - 12.0.1.1011-1
- Initial spec file
