#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mapproj
Version  : 1.2.4
Release  : 10
URL      : https://cran.r-project.org/src/contrib/mapproj_1.2-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mapproj_1.2-4.tar.gz
Summary  : Map Projections
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mapproj-lib
Requires: R-maps
BuildRequires : R-maps
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-mapproj package.
Group: Libraries

%description lib
lib components for the R-mapproj package.


%prep
%setup -q -c -n mapproj

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492805887

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492805887
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mapproj
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mapproj


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mapproj/DESCRIPTION
/usr/lib64/R/library/mapproj/INDEX
/usr/lib64/R/library/mapproj/Meta/Rd.rds
/usr/lib64/R/library/mapproj/Meta/features.rds
/usr/lib64/R/library/mapproj/Meta/hsearch.rds
/usr/lib64/R/library/mapproj/Meta/links.rds
/usr/lib64/R/library/mapproj/Meta/nsInfo.rds
/usr/lib64/R/library/mapproj/Meta/package.rds
/usr/lib64/R/library/mapproj/NAMESPACE
/usr/lib64/R/library/mapproj/R/mapproj
/usr/lib64/R/library/mapproj/R/mapproj.rdb
/usr/lib64/R/library/mapproj/R/mapproj.rdx
/usr/lib64/R/library/mapproj/help/AnIndex
/usr/lib64/R/library/mapproj/help/aliases.rds
/usr/lib64/R/library/mapproj/help/mapproj.rdb
/usr/lib64/R/library/mapproj/help/mapproj.rdx
/usr/lib64/R/library/mapproj/help/paths.rds
/usr/lib64/R/library/mapproj/html/00Index.html
/usr/lib64/R/library/mapproj/html/R.css
/usr/lib64/R/library/mapproj/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mapproj/libs/mapproj.so
