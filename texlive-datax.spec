Name:		texlive-datax
Version:	61772
Release:	1
Summary:	Import individual data from script files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datax
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datax.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datax.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datax.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package uses pgfkeys to retrieve individual data
points generated in some script. Analogous to how one might
generate graphics in a script and import those graphics into a
LaTeX document.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/datax
%{_texmfdistdir}/tex/latex/datax
%doc %{_texmfdistdir}/doc/latex/datax

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
