#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mFilter
Version  : 0.1.5
Release  : 27
URL      : https://cran.r-project.org/src/contrib/mFilter_0.1-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mFilter_0.1-5.tar.gz
Summary  : Miscellaneous Time Series Filters
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
for smoothing and extracting trend and cyclical components of a
        time series. The routines are commonly used in economics and
        finance, however they should also be interest to other areas.
        Currently, Christiano-Fitzgerald, Baxter-King,
        Hodrick-Prescott, Butterworth, and trigonometric regression
        filters are included in the package.

%prep
%setup -q -c -n mFilter
cd %{_builddir}/mFilter

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589535514

%install
export SOURCE_DATE_EPOCH=1589535514
rm -rf %{buildroot}
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mFilter
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mFilter
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mFilter
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mFilter || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mFilter/DESCRIPTION
/usr/lib64/R/library/mFilter/INDEX
/usr/lib64/R/library/mFilter/Meta/Rd.rds
/usr/lib64/R/library/mFilter/Meta/data.rds
/usr/lib64/R/library/mFilter/Meta/features.rds
/usr/lib64/R/library/mFilter/Meta/hsearch.rds
/usr/lib64/R/library/mFilter/Meta/links.rds
/usr/lib64/R/library/mFilter/Meta/nsInfo.rds
/usr/lib64/R/library/mFilter/Meta/package.rds
/usr/lib64/R/library/mFilter/NAMESPACE
/usr/lib64/R/library/mFilter/NEWS.md
/usr/lib64/R/library/mFilter/R/mFilter
/usr/lib64/R/library/mFilter/R/mFilter.rdb
/usr/lib64/R/library/mFilter/R/mFilter.rdx
/usr/lib64/R/library/mFilter/data/unemp.R
/usr/lib64/R/library/mFilter/help/AnIndex
/usr/lib64/R/library/mFilter/help/aliases.rds
/usr/lib64/R/library/mFilter/help/figures/README-ex1-1.png
/usr/lib64/R/library/mFilter/help/figures/README-ex2-1.png
/usr/lib64/R/library/mFilter/help/figures/README-ex3-1.png
/usr/lib64/R/library/mFilter/help/mFilter.rdb
/usr/lib64/R/library/mFilter/help/mFilter.rdx
/usr/lib64/R/library/mFilter/help/paths.rds
/usr/lib64/R/library/mFilter/html/00Index.html
/usr/lib64/R/library/mFilter/html/R.css
