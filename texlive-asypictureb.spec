# revision 33490
# category Package
# catalog-ctan /graphics/asypictureb
# catalog-date 2014-04-15 22:25:36 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-asypictureb
Version:	0.3
Release:	4
Summary:	User-friendly integration of Asymptote into LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/asypictureb
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asypictureb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asypictureb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asypictureb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The asypictureB package is an unofficial alternative to the
asymptote package for creating Asymptote pictures within a
latex source file. While it does not duplicate all the features
of the official package, it is more user-friendly in several
ways. Most notably, Asymptote errors are repackaged as LaTeX
errors, making debugging less of a pain. It also has a more
robust mechanism for identifying unchanged pictures that need
not be recompiled.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/asypictureb/asypictureB.sty
%doc %{_texmfdistdir}/doc/latex/asypictureb/README
%doc %{_texmfdistdir}/doc/latex/asypictureb/asypictureB.pdf
#- source
%doc %{_texmfdistdir}/source/latex/asypictureb/asypictureB.dtx
%doc %{_texmfdistdir}/source/latex/asypictureb/asypictureB.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
