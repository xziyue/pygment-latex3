from pygments import highlight
from tex_lexer import Tex3Lexer
from pygments.formatters.html import HtmlFormatter

tex_src = r'''
\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage{datetime2}
\usepackage{expl3}

\begin{document}
\setlength{\parindent}{0cm}

\ExplSyntaxOn

\int_new:N \g_tmpc_int

\cs_set:Npn \longest_common_prefix:n #1 {
    \clist_gset:Nn \g_tmpa_clist {#1} % create a new list of tokens
    \par list~a:~\cs_meaning:N \g_tmpa_clist % debug line
    
    \clist_gclear:N \g_tmpb_clist % prepare a list of strings
    % construct a list of strings
    \clist_map_variable:NNn \g_tmpa_clist \g_tmpa_tl 
        {
        \exp_args:NNV \str_set:Nn \l_tmpa_str { \g_tmpa_tl }
        \clist_put_right:NV \g_tmpb_clist {\l_tmpa_str}
        }    
    \par list~b:~\cs_meaning:N \g_tmpb_clist % debug line
    
    \seq_gclear:N \g_tmpa_seq % clear length array
    \clist_map_variable:NNn \g_tmpb_clist \g_tmpa_tl
        {
        \seq_gput_right:Nx \g_tmpa_seq {\str_count:N \g_tmpa_tl}
        }
    \par seq~a:~\cs_meaning:N \g_tmpa_seq % debug line
    
    \int_gset:Nn \g_tmpa_int {\c_max_int} % initialize smallest length variable
    % find the smallest length
    \seq_map_variable:NNn \g_tmpa_seq \g_tmpa_tl
        {
        \exp_args:NNx \int_gset:Nn \g_tmpa_int {\int_min:nn {\g_tmpa_int} {\g_tmpa_tl}}
        }
    \par int~a:~\int_use:N \g_tmpa_int
    
    \exp_args:NNx \int_gset:Nn \g_tmpb_int {\clist_count:N \g_tmpb_clist} % get size of list
    \par int~b:~\int_use:N \g_tmpb_int
    
    \int_gset:Nn \g_tmpc_int {0} % loop variable
    \bool_gset:Nn \g_tmpa_bool {\c_true_bool} % loop control variable
    
    \bool_while_do:Nn {\g_tmpa_bool}
        {
        \str_set:NV \l_tmpa_str {\clist_item:Nn \g_tmpb_clist {\g_tmpc_int}}% extract the current string
        \par cur~str:
        \int_gincr:N \g_tmpc_int % increment loop variable
        % set exit condition if the loop ends
        \int_compare:nNnTF {\g_tmpc_int} {=} {\g_tmpb_int} 
            { \bool_gset:Nn \g_tmpa_bool {\c_false_bool} } {}
        }
} 

$\tex must$

\longest_common_prefix:n {abcde, bc, defg}

\ExplSyntaxOff

\DTMnow

\end{document}
'''

output = highlight(tex_src, Tex3Lexer(), HtmlFormatter(full=True))
with open('test.html', 'w') as outfile:
    outfile.write(output)