#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mapproj
Version  : 1.2.9
Release  : 70
URL      : https://cran.r-project.org/src/contrib/mapproj_1.2.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mapproj_1.2.9.tar.gz
Summary  : Map Projections
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mapproj-lib = %{version}-%{release}
Requires: R-mapproj-license = %{version}-%{release}
Requires: R-maps
BuildRequires : R-maps
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-mapproj package.
Group: Libraries
Requires: R-mapproj-license = %{version}-%{release}

%description lib
lib components for the R-mapproj package.


%package license
Summary: license components for the R-mapproj package.
Group: Default

%description license
license components for the R-mapproj package.


%prep
%setup -q -n mapproj
cd %{_builddir}/mapproj

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667238640

%install
export SOURCE_DATE_EPOCH=1667238640
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-mapproj
cp %{_builddir}/mapproj/LICENSE.note %{buildroot}/usr/share/package-licenses/R-mapproj/3e9ae7992b6aed5d01868d939dc38464ec2e2142 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mapproj/libs/mapproj.so
/usr/lib64/R/library/mapproj/libs/mapproj.so.avx2
/usr/lib64/R/library/mapproj/libs/mapproj.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-mapproj/3e9ae7992b6aed5d01868d939dc38464ec2e2142
