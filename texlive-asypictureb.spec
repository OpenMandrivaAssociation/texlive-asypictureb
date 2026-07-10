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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is an unofficial alternative to the package provided with
the Asymptote distribution, for including pictures within a LaTeX source
file. While it does not duplicate all the features of the official
package, this package is more user-friendly in several ways. Most
notably, Asymptote errors are repackaged as LaTeX errors, making
debugging less of a pain. It also has a more robust mechanism for
identifying unchanged pictures that need not be recompiled.

