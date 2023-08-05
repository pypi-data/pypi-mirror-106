\documentclass{article}
\usepackage{curvenote_paper}
\usepackage{framed}
\usepackage{url}
\usepackage{graphicx}
\usepackage{framed}
\usepackage{natbib}
\usepackage[hidelinks]{hyperref}
\usepackage{adjustbox}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{amsmath}
\usepackage[short, nodayofweek]{datetime}
\graphicspath{{assets/}}
\bibliographystyle{abbrvnat}
\setcitestyle{authoryear,open={(},close={)},comma,aysep={,}}
\usepackage[normalem]{ulem}
\usepackage{minted}
\usemintedstyle{friendly}
\title{\VAR{main_title}}
\author{\BLOCK{ for author in main_author_list }
\VAR{author}\BLOCK{ if not loop.last } \and \BLOCK{ endif }
\BLOCK{ endfor }}
\newdate{articleDate}{\VAR{main_day}}{\VAR{main_month}}{\VAR{main_year}}
\date{\displaydate{articleDate}}
\begin{document}
\maketitle
\BLOCK{ for article_path in article_paths }
\input{\VAR{article_path}}
\BLOCK{ endfor }
\bibliography{main}
\end{document}
