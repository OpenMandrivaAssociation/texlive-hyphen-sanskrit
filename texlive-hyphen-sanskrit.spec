%global tl_name hyphen-sanskrit
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Sanskrit hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-sanskrit
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-sanskrit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-sanskrit.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Sanskrit and Prakrit in transliteration, and in
Devanagari, Bengali, Kannada, Malayalam and Telugu scripts for Unicode
engines.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-sanskrit:
sanskrit loadhyph-sa.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-sanskrit:
\addlanguage{sanskrit}{loadhyph-sa.tex}{}{1}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-sanskrit:
['sanskrit'] = {
	loader = 'loadhyph-sa.tex',
	lefthyphenmin = 1,
	righthyphenmin = 3,
	synonyms = {  },
	patterns = 'hyph-sa.pat.txt',
},
TL_HYPHEN_EOF
