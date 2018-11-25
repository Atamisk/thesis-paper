\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{odu_thesis}[ODU Style Guide interpretation]

\LoadClass{report}
\RequirePackage{geometry}
\RequirePackage[explicit]{titlesec}

\geometry{letterpaper,
          lmargin=1in,
          rmargin=1in,
          tmargin=1in,
          bmargin=1in}
\linespread{1.3}
\titleformat{\chapter}[display]
  {\LARGE\bfseries\centering}{CHAPTER \thechapter \\ \vspace{0.5em} \uppercase{#1}}{-2.3em}{}

