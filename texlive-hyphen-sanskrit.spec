# revision 28522
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-sanskrit
Version:	20131011
Release:	5
Summary:	Sanskrit hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-sanskrit.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Sanskrit and Prakrit in
transliteration, and in Devanagari, Bengali, Kannada, Malayalam
and Telugu scripts for Unicode engines.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-sanskrit
%_texmf_language_def_d/hyphen-sanskrit
%_texmf_language_lua_d/hyphen-sanskrit

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-sanskrit <<EOF
\%% from hyphen-sanskrit:
sanskrit loadhyph-sa.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-sanskrit
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-sanskrit <<EOF
\%% from hyphen-sanskrit:
\addlanguage{sanskrit}{loadhyph-sa.tex}{}{1}{3}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-sanskrit
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-sanskrit <<EOF
-- from hyphen-sanskrit:
	['sanskrit'] = {
		loader = 'loadhyph-sa.tex',
		lefthyphenmin = 1,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-sa.pat.txt',
		hyphenation = '',
	},
EOF
