Name:       ansible-role-dci-feeders
Version:    0.0.VERS
Release:    1%{?dist}
Summary:    dci-feeders Ansible role
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-feeders
Source0:    ansible-role-dci-feeders-%{version}.tar.gz

BuildArch:  noarch
Requires:   ansible
Requires:   createrepo
Requires:   dci-ansible
Requires:   python2-dciclient
Requires:   yum-utils

%description
An Ansible role that deploys the necessary playbook for a host to act as a DCI feeder

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/dci/roles/dci-feeders
chmod 755 %{buildroot}%{_datadir}/dci/roles/dci-feeders

cp -r meta %{buildroot}%{_datadir}/dci/roles/dci-feeders
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-feeders


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-feeders


%changelog
* Wed Apr 26 2017 Yanis Guenane <yguenane@redhat.com> - 0.0.1-1
- Initial release
