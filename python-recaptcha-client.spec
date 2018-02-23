%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           python-recaptcha-client
Version:        2.0.0
Release:        1%{?dist}
Summary:        Python module for reCAPTCHA and reCAPTCHA Mailhide

Group:          Development/Languages
License:        MIT
Source0:        https://github.com/redhat-infosec/python-recaptcha/releases/download/v%{version}/recaptcha-client-%{version}.tar.gz
URL:            https://github.com/redhat-infosec/python-recaptcha
       
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch:      noarch
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif



%global _description\
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not require\
any imaging libraries because the CAPTCHA is served directly from reCAPTCHA.\
Also allows you to securely obfuscate emails with Mailhide. This functionality\
requires python-crypto. This library requires two types of API keys. If you'd\
like to use the CAPTCHA, you'll need a key from\
http://recaptcha.net/api/getkey. For Mailhide, you'll need a key from\
http://mailhide.recaptcha.net/apikey.

%description %_description

%package -n python2-recaptcha-client
Group:      %{group}
Summary: %summary
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
Requires:       python-crypto
%else
Requires:       python2-crypto
%endif

Obsoletes: python-recaptcha-client

%{?python_provide:%python_provide python2-recaptcha-client}

%description -n python2-recaptcha-client %_description

%prep
%setup -q -n recaptcha-client-%{version}
#sed -i 's/^from ez_setup/#from ez_setup/' setup.py
#sed -i 's/^use_setuptools()/#use_setuptools()/' setup.py


%build
%{__python} setup.py build


%install

rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
 
%files -n python2-recaptcha-client
%defattr(-,root,root,-)
%doc PKG-INFO
%{python_sitelib}/recaptcha/
%{python_sitelib}/recaptcha_client*-nspkg.pth
%{python_sitelib}/recaptcha_client*.egg-info/

%changelog
* Thu Feb 22 2018 Richard Monk <rmonK@redhat.com> - 2.0.0-1
- Updated to support ReCAPTCHA v2

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.6-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.6-11
- Python 2 binary package renamed to python2-recaptcha-client
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Stephen Gallagher <sgallagh@redhat.com> 1.0.6-1
- New upstream release 1.0.6
- Enhancements to setup.py build-system
- Drop Fedora-specific build hacks

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-4
- Rebuild for python 2.7

* Fri Mar 12 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-3
- Bump revision to chain-build ReviewBoard

* Thu Mar 11 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-2
- Conditionally define python_sitelib
- Remove CFLAGS from the build step (unneeded)
- Remove useless comment from %%files
- Update summary

* Tue Mar 09 2010 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-1
- Specfile changes from package review

* Mon Dec 21 2009 Stephen Gallagher <sgallagh@redhat.com> 1.0.5-0
- First release

