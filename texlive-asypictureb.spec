%global tl_name asypictureb
%global tl_revision 73611

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	User-friendly integration of Asymptote into LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/asypictureb
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asypictureb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asypictureb.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asypictureb.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is an unofficial alternative to the package provided with
the Asymptote distribution, for including pictures within a LaTeX source
file. While it does not duplicate all the features of the official
package, this package is more user-friendly in several ways. Most
notably, Asymptote errors are repackaged as LaTeX errors, making
debugging less of a pain. It also has a more robust mechanism for
identifying unchanged pictures that need not be recompiled.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/asypictureb
%dir %{_datadir}/texmf-dist/source/latex/asypictureb
%dir %{_datadir}/texmf-dist/tex/latex/asypictureb
%doc %{_datadir}/texmf-dist/doc/latex/asypictureb/README
%doc %{_datadir}/texmf-dist/doc/latex/asypictureb/asypictureB.pdf
%doc %{_datadir}/texmf-dist/source/latex/asypictureb/asypictureB.dtx
%doc %{_datadir}/texmf-dist/source/latex/asypictureb/asypictureB.ins
%{_datadir}/texmf-dist/tex/latex/asypictureb/asypictureB.sty
