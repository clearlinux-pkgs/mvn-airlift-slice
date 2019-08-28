#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-airlift-slice
Version  : 0.31
Release  : 1
URL      : https://github.com/airlift/slice/archive/0.31.tar.gz
Source0  : https://github.com/airlift/slice/archive/0.31.tar.gz
Source1  : https://repo1.maven.org/maven2/io/airlift/slice/0.31/slice-0.31.jar
Source2  : https://repo1.maven.org/maven2/io/airlift/slice/0.31/slice-0.31.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-airlift-slice-data = %{version}-%{release}
Requires: mvn-airlift-slice-license = %{version}-%{release}

%description
# Slice
[![Maven Central](https://img.shields.io/maven-central/v/io.airlift/slice.svg?label=Maven%20Central)](https://search.maven.org/#search%7Cga%7C1%7Cg%3A%22io.airlift%22%20AND%20a%3A%22slice%22)
[![Build Status](https://travis-ci.org/airlift/slice.svg?branch=master)](https://travis-ci.org/airlift/slice)

%package data
Summary: data components for the mvn-airlift-slice package.
Group: Data

%description data
data components for the mvn-airlift-slice package.


%package license
Summary: license components for the mvn-airlift-slice package.
Group: Default

%description license
license components for the mvn-airlift-slice package.


%prep
%setup -q -n slice-0.31

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-airlift-slice
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-airlift-slice/LICENSE
cp src/license/LICENSE-HEADER.txt %{buildroot}/usr/share/package-licenses/mvn-airlift-slice/src_license_LICENSE-HEADER.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/airlift/slice/0.31
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/io/airlift/slice/0.31/slice-0.31.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/airlift/slice/0.31
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/io/airlift/slice/0.31/slice-0.31.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/io/airlift/slice/0.31/slice-0.31.jar
/usr/share/java/.m2/repository/io/airlift/slice/0.31/slice-0.31.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-airlift-slice/LICENSE
/usr/share/package-licenses/mvn-airlift-slice/src_license_LICENSE-HEADER.txt
