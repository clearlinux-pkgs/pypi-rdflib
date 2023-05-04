#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-rdflib
Version  : 6.3.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/c8/28/4d1f27c5d73f58e567ca1a14a4eab7d7978a09c4e117687f9f6c216d3366/rdflib-6.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/28/4d1f27c5d73f58e567ca1a14a4eab7d7978a09c4e117687f9f6c216d3366/rdflib-6.3.2.tar.gz
Summary  : RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information.
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-rdflib-bin = %{version}-%{release}
Requires: pypi-rdflib-license = %{version}-%{release}
Requires: pypi-rdflib-python = %{version}-%{release}
Requires: pypi-rdflib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is the Armstrong Sphinx theme from https://github.com/armstrong/armstrong_sphinx

%package bin
Summary: bin components for the pypi-rdflib package.
Group: Binaries
Requires: pypi-rdflib-license = %{version}-%{release}

%description bin
bin components for the pypi-rdflib package.


%package license
Summary: license components for the pypi-rdflib package.
Group: Default

%description license
license components for the pypi-rdflib package.


%package python
Summary: python components for the pypi-rdflib package.
Group: Default
Requires: pypi-rdflib-python3 = %{version}-%{release}

%description python
python components for the pypi-rdflib package.


%package python3
Summary: python3 components for the pypi-rdflib package.
Group: Default
Requires: python3-core
Provides: pypi(rdflib)
Requires: pypi(isodate)
Requires: pypi(pyparsing)

%description python3
python3 components for the pypi-rdflib package.


%prep
%setup -q -n rdflib-6.3.2
cd %{_builddir}/rdflib-6.3.2
pushd ..
cp -a rdflib-6.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683223631
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-rdflib
cp %{_builddir}/rdflib-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rdflib/a63dafa907becdddd2a68a75839372992bb16db6 || :
cp %{_builddir}/rdflib-%{version}/docs/_themes/armstrong/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rdflib/d64f881dddfe314d1ed5a3fdd1ea82dea901adae || :
cp %{_builddir}/rdflib-%{version}/test/data/suites/w3c/n3/TurtleTests/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rdflib/a88f037134ac8b4cb7cc897173f19368a6822c4a || :
cp %{_builddir}/rdflib-%{version}/test/data/suites/w3c/turtle/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rdflib/a88f037134ac8b4cb7cc897173f19368a6822c4a || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/csv2rdf
/usr/bin/rdf2dot
/usr/bin/rdfgraphisomorphism
/usr/bin/rdfpipe
/usr/bin/rdfs2dot

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-rdflib/a63dafa907becdddd2a68a75839372992bb16db6
/usr/share/package-licenses/pypi-rdflib/a88f037134ac8b4cb7cc897173f19368a6822c4a
/usr/share/package-licenses/pypi-rdflib/d64f881dddfe314d1ed5a3fdd1ea82dea901adae

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*