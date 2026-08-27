import json

ch1_code = """
questions_ch1 = [
    {
        "q": "Exercise 1A",
        "subs": []
    },
    {
        "q": "1. Add each of the following pairs of rational numbers.",
        "subs": [
            {"q": "(i) $\\frac{-1}{3}$ and $\\frac{2}{3}$", "a": "$\\frac{-1 + 2}{3} = \\frac{1}{3}$"},
            {"q": "(ii) $\\frac{2}{5}$ and $\\frac{-3}{5}$", "a": "$\\frac{2 - 3}{5} = \\frac{-1}{5}$"},
            {"q": "(iii) $\\frac{-7}{11}$ and $\\frac{-4}{11}$", "a": "$\\frac{-7 - 4}{11} = \\frac{-11}{11} = -1$"},
            {"q": "(iv) $\\frac{-13}{17}$ and $\\frac{4}{17}$", "a": "$\\frac{-13 + 4}{17} = \\frac{-9}{17}$"},
            {"q": "(v) $\\frac{11}{25}$ and $\\frac{-7}{25}$", "a": "$\\frac{11 - 7}{25} = \\frac{4}{25}$"},
            {"q": "(vi) $\\frac{-8}{9}$ and $\\frac{-19}{9}$", "a": "$\\frac{-8 - 19}{9} = \\frac{-27}{9} = -3$"}
        ]
    },
    {
        "q": "2. Add.",
        "subs": [
            {"q": "(i) $\\frac{2}{3}$ and $\\frac{3}{5}$", "a": "$\\frac{10 + 9}{15} = \\frac{19}{15}$"},
            {"q": "(ii) $\\frac{-2}{5}$ and $\\frac{5}{7}$", "a": "$\\frac{-14 + 25}{35} = \\frac{11}{35}$"},
            {"q": "(iii) $\\frac{3}{-8}$ and $\\frac{-5}{12}$", "a": "$\\frac{-9}{24} + \\frac{-10}{24} = \\frac{-19}{24}$"},
            {"q": "(iv) $\\frac{-7}{26}$ and $\\frac{-5}{39}$", "a": "$\\frac{-21}{78} + \\frac{-10}{78} = \\frac{-31}{78}$"},
            {"q": "(v) $\\frac{5}{-24}$ and $\\frac{7}{36}$", "a": "$\\frac{-15}{72} + \\frac{14}{72} = \\frac{-1}{72}$"},
            {"q": "(vi) $\\frac{3}{16}$ and $\\frac{-7}{24}$", "a": "$\\frac{9}{48} + \\frac{-14}{48} = \\frac{-5}{48}$"},
            {"q": "(vii) $4 \\frac{11}{25}$ and $\\frac{13}{-15}$", "a": "$\\frac{111}{25} + \\frac{-13}{15} = \\frac{333 - 65}{75} = \\frac{268}{75}$"},
            {"q": "(viii) $-2$ and $1 \\frac{7}{11}$", "a": "$-2 + \\frac{18}{11} = \\frac{-22 + 18}{11} = \\frac{-4}{11}$"},
            {"q": "(ix) $-1$ and $2 \\frac{3}{5}$", "a": "$-1 + \\frac{13}{5} = \\frac{-5 + 13}{5} = \\frac{8}{5}$"},
            {"q": "(x) $\\frac{-7}{8}$ and $0$", "a": "$\\frac{-7}{8}$"}
        ]
    },
    {
        "q": "3. Verify the commutative law of addition for the following pairs of rational numbers.",
        "subs": [
            {"q": "(i) $\\frac{-5}{7}$ and $\\frac{3}{4}$", "a": "$\\frac{-5}{7} + \\frac{3}{4} = \\frac{-20 + 21}{28} = \\frac{1}{28}$<br>$\\frac{3}{4} + \\frac{-5}{7} = \\frac{21 - 20}{28} = \\frac{1}{28}$<br>(Verified)"},
            {"q": "(ii) $\\frac{-1}{3}$ and $\\frac{-2}{5}$", "a": "$\\frac{-1}{3} + \\frac{-2}{5} = \\frac{-5 - 6}{15} = \\frac{-11}{15}$<br>$\\frac{-2}{5} + \\frac{-1}{3} = \\frac{-6 - 5}{15} = \\frac{-11}{15}$<br>(Verified)"},
            {"q": "(iii) $\\frac{4}{-7}$ and $\\frac{-2}{21}$", "a": "$\\frac{-12 - 2}{21} = \\frac{-14}{21} = \\frac{-2}{3}$<br>$\\frac{-2}{21} + \\frac{-12}{21} = \\frac{-14}{21} = \\frac{-2}{3}$<br>(Verified)"},
            {"q": "(iv) $5$ and $\\frac{-3}{5}$", "a": "$5 + \\frac{-3}{5} = \\frac{25 - 3}{5} = \\frac{22}{5}$<br>$\\frac{-3}{5} + 5 = \\frac{-3 + 25}{5} = \\frac{22}{5}$<br>(Verified)"}
        ]
    },
    {
        "q": "4. Verify the associative law of addition for the following groups of rational numbers.",
        "subs": [
            {"q": "(i) $\\frac{1}{2}, \\frac{-2}{3}$ and $\\frac{1}{5}$", "a": "$\\left(\\frac{1}{2} + \\frac{-2}{3}\\right) + \\frac{1}{5} = \\left(\\frac{3 - 4}{6}\\right) + \\frac{1}{5} = \\frac{-1}{6} + \\frac{1}{5} = \\frac{-5 + 6}{30} = \\frac{1}{30}$<br>$\\frac{1}{2} + \\left(\\frac{-2}{3} + \\frac{1}{5}\\right) = \\frac{1}{2} + \\left(\\frac{-10 + 3}{15}\\right) = \\frac{1}{2} + \\frac{-7}{15} = \\frac{15 - 14}{30} = \\frac{1}{30}$<br>(Verified)"},
            {"q": "(ii) $\\frac{-3}{5}, \\frac{7}{10}$ and $\\frac{4}{15}$", "a": "$\\left(\\frac{-3}{5} + \\frac{7}{10}\\right) + \\frac{4}{15} = \\left(\\frac{-6 + 7}{10}\\right) + \\frac{4}{15} = \\frac{1}{10} + \\frac{4}{15} = \\frac{3 + 8}{30} = \\frac{11}{30}$<br>$\\frac{-3}{5} + \\left(\\frac{7}{10} + \\frac{4}{15}\\right) = \\frac{-3}{5} + \\left(\\frac{21 + 8}{30}\\right) = \\frac{-3}{5} + \\frac{29}{30} = \\frac{-18 + 29}{30} = \\frac{11}{30}$<br>(Verified)"},
            {"q": "(iii) $\\frac{3}{-7}, \\frac{2}{21}$ and $\\frac{-5}{14}$", "a": "$\\left(\\frac{-9 + 2}{21}\\right) + \\frac{-5}{14} = \\frac{-7}{21} + \\frac{-5}{14} = \\frac{-1}{3} + \\frac{-5}{14} = \\frac{-14 - 15}{42} = \\frac{-29}{42}$<br>$\\frac{-3}{7} + \\left(\\frac{4 - 15}{42}\\right) = \\frac{-3}{7} + \\frac{-11}{42} = \\frac{-18 - 11}{42} = \\frac{-29}{42}$<br>(Verified)"},
            {"q": "(iv) $1, \\frac{5}{-11}$ and $\\frac{7}{22}$", "a": "$\\left(1 + \\frac{-5}{11}\\right) + \\frac{7}{22} = \\left(\\frac{11 - 5}{11}\\right) + \\frac{7}{22} = \\frac{6}{11} + \\frac{7}{22} = \\frac{12 + 7}{22} = \\frac{19}{22}$<br>$1 + \\left(\\frac{-10 + 7}{22}\\right) = 1 + \\frac{-3}{22} = \\frac{22 - 3}{22} = \\frac{19}{22}$<br>(Verified)"}
        ]
    },
    {
        "q": "5. Find the additive inverse of each of the following rationals.",
        "subs": [
            {"q": "(i) $0$", "a": "$0$"},
            {"q": "(ii) $1$", "a": "$-1$"},
            {"q": "(iii) $-5$", "a": "$5$"},
            {"q": "(iv) $\\frac{-3}{4}$", "a": "$\\frac{3}{4}$"},
            {"q": "(v) $\\frac{2}{-9}$", "a": "$\\frac{2}{9}$"},
            {"q": "(vi) $\\frac{-7}{-15}$", "a": "$\\frac{-7}{15}$"},
            {"q": "(vii) $\\frac{-13}{2}$", "a": "$\\frac{13}{2}$"},
            {"q": "(viii) $\\frac{-25}{-133}$", "a": "$\\frac{-25}{133}$"},
            {"q": "(ix) $\\frac{13}{-27}$", "a": "$\\frac{13}{27}$"},
            {"q": "(x) $\\frac{17}{8}$", "a": "$\\frac{-17}{8}$"}
        ]
    },
    {
        "q": "6. Using the appropriate properties of addition, find the value of each of the following sums.",
        "subs": [
            {"q": "(i) $\\frac{5}{7} + \\frac{-7}{3} + \\frac{-3}{7} + \\frac{11}{3}$", "a": "Group by denominators:<br>$\\left(\\frac{5}{7} + \\frac{-3}{7}\\right) + \\left(\\frac{-7}{3} + \\frac{11}{3}\\right) = \\frac{2}{7} + \\frac{4}{3} = \\frac{6 + 28}{21} = \\frac{34}{21}$"},
            {"q": "(ii) $\\frac{4}{5} + \\frac{3}{10} + \\frac{11}{5} + \\frac{-13}{10}$", "a": "Group by denominators:<br>$\\left(\\frac{4}{5} + \\frac{11}{5}\\right) + \\left(\\frac{3}{10} + \\frac{-13}{10}\\right) = \\frac{15}{5} + \\frac{-10}{10} = 3 - 1 = 2$"},
            {"q": "(iii) $\\frac{2}{3} + \\frac{-11}{8} + \\frac{-17}{3} + \\frac{3}{8}$", "a": "Group by denominators:<br>$\\left(\\frac{2}{3} + \\frac{-17}{3}\\right) + \\left(\\frac{-11}{8} + \\frac{3}{8}\\right) = \\frac{-15}{3} + \\frac{-8}{8} = -5 - 1 = -6$"},
            {"q": "(iv) $\\frac{7}{8} + \\frac{3}{10} + \\frac{-5}{8} + \\frac{-7}{20}$", "a": "Group by denominators:<br>$\\left(\\frac{7}{8} + \\frac{-5}{8}\\right) + \\left(\\frac{3}{10} + \\frac{-7}{20}\\right) = \\frac{2}{8} + \\left(\\frac{6 - 7}{20}\\right) = \\frac{1}{4} + \\frac{-1}{20} = \\frac{5 - 1}{20} = \\frac{4}{20} = \\frac{1}{5}$"}
        ]
    },
    {
        "q": "7. Fill in the blanks.",
        "subs": [
            {"q": "(i) $\\frac{-2}{15} + \\frac{-3}{19} = \\frac{-3}{19} + ......$", "a": "<b>$\\frac{-2}{15}$</b>"},
            {"q": "(ii) $\\frac{23}{12} + \\frac{7}{5} = \\frac{7}{5} + ......$", "a": "<b>$\\frac{23}{12}$</b>"},
            {"q": "(iii) $\\frac{1}{2} + \\left(\\frac{3}{5} + \\frac{-7}{9}\\right) = \\left(\\frac{1}{2} + ......\\right) + \\frac{-7}{9}$", "a": "<b>$\\frac{3}{5}$</b>"},
            {"q": "(iv) \\left(\\frac{-5}{11} + \\frac{-7}{13}\\right) + \\frac{25}{29} = ...... + \\left(\\frac{-7}{13} + \\frac{25}{29}\\right)", "a": "<b>$\\frac{-5}{11}$</b>"},
            {"q": "(v) $-3 + \\left(\\frac{-5}{23} + \\frac{7}{31}\\right) = \\left(...... + \\frac{-5}{23}\\right) + \\frac{7}{31}$", "a": "<b>$-3$</b>"}
        ]
    },
    {
        "q": "8. Subtract.",
        "subs": [
            {"q": "(i) $\\frac{1}{3}$ from $\\frac{2}{5}$", "a": "$\\frac{2}{5} - \\frac{1}{3} = \\frac{6 - 5}{15} = \\frac{1}{15}$"},
            {"q": "(ii) $\\frac{-7}{8}$ from $\\frac{1}{2}$", "a": "$\\frac{1}{2} - \\left(\\frac{-7}{8}\\right) = \\frac{4}{8} + \\frac{7}{8} = \\frac{11}{8}$"},
            {"q": "(iii) $\\frac{-11}{13}$ from $\\frac{-2}{3}$", "a": "$\\frac{-2}{3} - \\left(\\frac{-11}{13}\\right) = \\frac{-26}{39} + \\frac{33}{39} = \\frac{7}{39}$"},
            {"q": "(iv) $\\frac{-13}{11}$ from $-1$", "a": "$-1 - \\left(\\frac{-13}{11}\\right) = \\frac{-11}{11} + \\frac{13}{11} = \\frac{2}{11}$"},
            {"q": "(v) $\\frac{-15}{17}$ from $1$", "a": "$1 - \\left(\\frac{-15}{17}\\right) = \\frac{17}{17} + \\frac{15}{17} = \\frac{32}{17}$"},
            {"q": "(vi) $\\frac{12}{19}$ from $-2$", "a": "$-2 - \\frac{12}{19} = \\frac{-38 - 12}{19} = \\frac{-50}{19}$"},
            {"q": "(vii) $\\frac{-19}{31}$ from $0$", "a": "$0 - \\left(\\frac{-19}{31}\\right) = \\frac{19}{31}$"},
            {"q": "(viii) $-5$ from $\\frac{-2}{3}$", "a": "$\\frac{-2}{3} - (-5) = \\frac{-2}{3} + \\frac{15}{3} = \\frac{13}{3}$"},
            {"q": "(ix) $7$ from $\\frac{-7}{17}$", "a": "$\\frac{-7}{17} - 7 = \\frac{-7 - 119}{17} = \\frac{-126}{17}$"},
            {"q": "(x) $\\frac{-9}{8}$ from $\\frac{-13}{7}$", "a": "$\\frac{-13}{7} - \\left(\\frac{-9}{8}\\right) = \\frac{-104}{56} + \\frac{63}{56} = \\frac{-41}{56}$"}
        ]
    },
    {
        "q": "9. Verify.",
        "subs": [
            {"q": "(i) $\\frac{1}{3} - \\frac{1}{4} \\neq \\frac{1}{4} - \\frac{1}{3}$", "a": "LHS: $\\frac{4 - 3}{12} = \\frac{1}{12}$<br>RHS: $\\frac{3 - 4}{12} = \\frac{-1}{12}$<br>(Verified)"},
            {"q": "(ii) $\\frac{-2}{7} - \\frac{3}{5} \\neq \\frac{3}{5} - \\frac{-2}{7}$", "a": "LHS: $\\frac{-10 - 21}{35} = \\frac{-31}{35}$<br>RHS: $\\frac{21 - (-10)}{35} = \\frac{31}{35}$<br>(Verified)"},
            {"q": "(iii) $\\frac{1}{2} - \\left(\\frac{1}{3} - \\frac{1}{5}\\right) \\neq \\left(\\frac{1}{2} - \\frac{1}{3}\\right) - \\frac{1}{5}$", "a": "LHS: $\\frac{1}{2} - \\left(\\frac{5 - 3}{15}\\right) = \\frac{1}{2} - \\frac{2}{15} = \\frac{15 - 4}{30} = \\frac{11}{30}$<br>RHS: \\left(\\frac{3 - 2}{6}\\right) - \\frac{1}{5} = \\frac{1}{6} - \\frac{1}{5} = \\frac{5 - 6}{30} = \\frac{-1}{30}$<br>(Verified)"},
            {"q": "(iv) $\\frac{5}{11} - \\left(\\frac{-2}{3} - \\frac{5}{7}\\right) \\neq \\left\\{\\frac{5}{11} - \\left(\\frac{-2}{3}\\right)\\right\\} - \\frac{5}{7}$", "a": "LHS: $\\frac{5}{11} - \\left(\\frac{-14 - 15}{21}\\right) = \\frac{5}{11} - \\left(\\frac{-29}{21}\\right) = \\frac{105 + 319}{231} = \\frac{424}{231}$<br>RHS: $\\left(\\frac{15 + 22}{33}\\right) - \\frac{5}{7} = \\frac{37}{33} - \\frac{5}{7} = \\frac{259 - 165}{231} = \\frac{94}{231}$<br>(Verified)"}
        ]
    },
    {
        "q": "10. Word Problems.",
        "subs": [
            {"q": "(a) The sum of two rational numbers is $\\frac{-3}{4}$. If one of the numbers is $\\frac{-28}{3}$, find the other.", "a": "Other number = Sum - given number<br>$\\frac{-3}{4} - \\left(\\frac{-28}{3}\\right) = \\frac{-9}{12} + \\frac{112}{12} = \\frac{103}{12}$"},
            {"q": "(b) The sum of two rational numbers is $-3$. If one of the numbers is $\\frac{7}{8}$, find the other.", "a": "Other number = Sum - given number<br>$-3 - \\frac{7}{8} = \\frac{-24 - 7}{8} = \\frac{-31}{8}$"}
        ]
    },
    {
        "q": "11. Word Problems.",
        "subs": [
            {"q": "(a) What number should be added to $\\frac{-11}{4}$ to get $\\frac{-25}{14}$?", "a": "$\\frac{-25}{14} - \\left(\\frac{-11}{4}\\right) = \\frac{-50}{28} + \\frac{77}{28} = \\frac{27}{28}$"},
            {"q": "(b) What number should be added to $-2$ to get $\\frac{-5}{8}$?", "a": "$\\frac{-5}{8} - (-2) = \\frac{-5}{8} + \\frac{16}{8} = \\frac{11}{8}$"}
        ]
    },
    {
        "q": "12. Word Problems.",
        "subs": [
            {"q": "(a) What number should be subtracted from $\\frac{-7}{8}$ to get $\\frac{-5}{12}$?", "a": "$\\frac{-7}{8} - \\left(\\frac{-5}{12}\\right) = \\frac{-21}{24} + \\frac{10}{24} = \\frac{-11}{24}$"},
            {"q": "(b) What number should be subtracted from $1$ to get $\\frac{-7}{17}$?", "a": "$1 - \\left(\\frac{-7}{17}\\right) = \\frac{17 + 7}{17} = \\frac{24}{17}$"}
        ]
    },
    {
        "q": "13. Identify the true statements only.",
        "subs": [
            {"q": "(i) The sum of two rational numbers is a rational number.", "a": "True"},
            {"q": "(ii) The difference of two rational numbers is not always a rational number.", "a": "False (It is always rational)"},
            {"q": "(iii) Zero is not a rational number.", "a": "False (0 = 0/1, so it is rational)"},
            {"q": "(iv) Addition is commutative on rational numbers.", "a": "True"},
            {"q": "(v) Subtraction is commutative on rational numbers.", "a": "False"},
            {"q": "(vi) Addition is associative on rational numbers.", "a": "True"},
            {"q": "(vii) Subtraction is associative on rational numbers.", "a": "False"},
            {"q": "(viii) Zero is the additive inverse of itself.", "a": "True"},
            {"q": "(ix) Zero is the additive identity for rational numbers.", "a": "True"},
            {"q": "(x) 1 is the additive inverse of -1.", "a": "True"}
        ]
    },
    {
        "q": "Exercise 1B",
        "subs": []
    },
    {
        "q": "1. Find the value of each of the following products.",
        "subs": [
            {"q": "(i) $\\frac{3}{7} \\times \\frac{4}{5}$", "a": "$\\frac{12}{35}$"},
            {"q": "(ii) $\\frac{-4}{9} \\times \\frac{10}{7}$", "a": "$\\frac{-40}{63}$"},
            {"q": "(iii) $\\frac{-1}{2} \\times \\frac{-9}{8}$", "a": "$\\frac{9}{16}$"},
            {"q": "(iv) $\\frac{-3}{4} \\times \\frac{8}{-15}$", "a": "$\\frac{-24}{-60} = \\frac{2}{5}$"},
            {"q": "(v) $\\frac{21}{-2} \\times \\frac{-4}{7}$", "a": "$\\frac{-84}{-14} = 6$"},
            {"q": "(vi) $\\frac{-7}{10} \\times \\frac{6}{-35}$", "a": "$\\frac{-42}{-350} = \\frac{3}{25}$"},
            {"q": "(vii) $\\frac{-14}{15} \\times \\frac{-25}{42}$", "a": "$\\frac{-14}{42} \\times \\frac{-25}{15} = \\frac{-1}{3} \\times \\frac{-5}{3} = \\frac{5}{9}$"},
            {"q": "(viii) $\\frac{-35}{-18} \\times \\frac{8}{-15}$", "a": "$\\frac{35}{18} \\times \\frac{-8}{15} = \\frac{7 \\times -4}{9 \\times 3} = \\frac{-28}{27}$"},
            {"q": "(ix) $\\frac{-7}{11} \\times 22$", "a": "$-7 \\times 2 = -14$"},
            {"q": "(x) $\\frac{14}{25} \\times (-100)$", "a": "$14 \\times -4 = -56$"},
            {"q": "(xi) $\\frac{-13}{-12} \\times (-3)$", "a": "$\\frac{13}{12} \\times -3 = \\frac{-13}{4}$"},
            {"q": "(xii) $\\frac{-12}{85} \\times (-17)$", "a": "$\\frac{-12 \\times -17}{85} = \\frac{12}{5}$"}
        ]
    },
    {
        "q": "2. Verify the commutative law of multiplication for the following pairs of rational numbers.",
        "subs": [
            {"q": "(i) $\\frac{2}{3}$ and $\\frac{-7}{5}$", "a": "$\\frac{2}{3} \\times \\frac{-7}{5} = \\frac{-14}{15}$<br>$\\frac{-7}{5} \\times \\frac{2}{3} = \\frac{-14}{15}$<br>(Verified)"},
            {"q": "(ii) $\\frac{-1}{7}$ and $\\frac{14}{3}$", "a": "$\\frac{-1}{7} \\times \\frac{14}{3} = \\frac{-2}{3}$<br>$\\frac{14}{3} \\times \\frac{-1}{7} = \\frac{-2}{3}$<br>(Verified)"},
            {"q": "(iii) $\\frac{3}{-8}$ and $\\frac{-16}{15}$", "a": "$\\frac{-3}{8} \\times \\frac{-16}{15} = \\frac{2}{5}$<br>$\\frac{-16}{15} \\times \\frac{-3}{8} = \\frac{2}{5}$<br>(Verified)"},
            {"q": "(iv) $\\frac{11}{13}$ and $\\frac{-26}{-55}$", "a": "$\\frac{11}{13} \\times \\frac{26}{55} = \\frac{2}{5}$<br>$\\frac{26}{55} \\times \\frac{11}{13} = \\frac{2}{5}$<br>(Verified)"}
        ]
    },
    {
        "q": "3. Verify the associative law of multiplication for the following groups of rational numbers.",
        "subs": [
            {"q": "(i) $\\frac{2}{3}, \\frac{-1}{5}$ and $\\frac{7}{12}$", "a": "$\\left(\\frac{2}{3} \\times \\frac{-1}{5}\\right) \\times \\frac{7}{12} = \\frac{-2}{15} \\times \\frac{7}{12} = \\frac{-7}{90}$<br>$\\frac{2}{3} \\times \\left(\\frac{-1}{5} \\times \\frac{7}{12}\\right) = \\frac{2}{3} \\times \\frac{-7}{60} = \\frac{-7}{90}$<br>(Verified)"},
            {"q": "(ii) $\\frac{-5}{7}, \\frac{1}{2}$ and $\\frac{-21}{20}$", "a": "$\\left(\\frac{-5}{7} \\times \\frac{1}{2}\\right) \\times \\frac{-21}{20} = \\frac{-5}{14} \\times \\frac{-21}{20} = \\frac{105}{280} = \\frac{3}{8}$<br>$\\frac{-5}{7} \\times \\left(\\frac{1}{2} \\times \\frac{-21}{20}\\right) = \\frac{-5}{7} \\times \\frac{-21}{40} = \\frac{105}{280} = \\frac{3}{8}$<br>(Verified)"},
            {"q": "(iii) $\\frac{-8}{9}, \\frac{-3}{4}$ and $\\frac{15}{16}$", "a": "$\\left(\\frac{-8}{9} \\times \\frac{-3}{4}\\right) \\times \\frac{15}{16} = \\frac{24}{36} \\times \\frac{15}{16} = \\frac{2}{3} \\times \\frac{15}{16} = \\frac{30}{48} = \\frac{5}{8}$<br>$\\frac{-8}{9} \\times \\left(\\frac{-3}{4} \\times \\frac{15}{16}\\right) = \\frac{-8}{9} \\times \\frac{-45}{64} = \\frac{5}{8}$<br>(Verified)"},
            {"q": "(iv) $\\frac{-3}{11}, \\frac{-7}{4}$ and $\\frac{-1}{2}$", "a": "$\\left(\\frac{-3}{11} \\times \\frac{-7}{4}\\right) \\times \\frac{-1}{2} = \\frac{21}{44} \\times \\frac{-1}{2} = \\frac{-21}{88}$<br>$\\frac{-3}{11} \\times \\left(\\frac{-7}{4} \\times \\frac{-1}{2}\\right) = \\frac{-3}{11} \\times \\frac{7}{8} = \\frac{-21}{88}$<br>(Verified)"}
        ]
    },
    {
        "q": "4. Find the multiplicative inverse of each of the following.",
        "subs": [
            {"q": "(i) $1$", "a": "$1$"},
            {"q": "(ii) $-1$", "a": "$-1$"},
            {"q": "(iii) $\\frac{3}{4}$", "a": "$\\frac{4}{3}$"},
            {"q": "(iv) $\\frac{5}{-7}$", "a": "$\\frac{-7}{5}$"},
            {"q": "(v) $\\frac{-11}{-13}$", "a": "$\\frac{13}{11}$"},
            {"q": "(vi) $\\frac{-7}{17}$", "a": "$\\frac{-17}{7}$"},
            {"q": "(vii) $3 \\frac{1}{4}$", "a": "$3 \\frac{1}{4} = \\frac{13}{4} \\rightarrow \\frac{4}{13}$"},
            {"q": "(viii) \\frac{-26}{5}", "a": "$\\frac{-5}{26}$"},
            {"q": "(ix) $\\frac{3}{4} \\times \\frac{-8}{9}$", "a": "$\\frac{-2}{3} \\rightarrow \\frac{-3}{2}$"},
            {"q": "(x) $\\frac{5}{13} \\times \\frac{-26}{-35}$", "a": "$\\frac{2}{7} \\rightarrow \\frac{7}{2}$"},
            {"q": "(xi) $\\frac{-13}{-14} \\times \\frac{70}{-39}$", "a": "$\\frac{13}{14} \\times \\frac{-70}{39} = \\frac{-5}{3} \\rightarrow \\frac{-3}{5}$"},
            {"q": "(xii) $3 \\frac{1}{3} \\times 1 \\frac{1}{2}$", "a": "$\\frac{10}{3} \\times \\frac{3}{2} = 5 \\rightarrow \\frac{1}{5}$"}
        ]
    },
    {
        "q": "5. Verify each of the following.",
        "subs": [
            {"q": "(i) $\\frac{3}{5} \\times \\left(\\frac{7}{12} + \\frac{1}{2}\\right) = \\frac{3}{5} \\times \\frac{7}{12} + \\frac{3}{5} \\times \\frac{1}{2}$", "a": "LHS: $\\frac{3}{5} \\times \\left(\\frac{7 + 6}{12}\\right) = \\frac{3}{5} \\times \\frac{13}{12} = \\frac{13}{20}$<br>RHS: $\\frac{7}{20} + \\frac{3}{10} = \\frac{7 + 6}{20} = \\frac{13}{20}$<br>(Verified)"},
            {"q": "(ii) $\\frac{-2}{3} \\times \\left(\\frac{-5}{4} + \\frac{4}{7}\\right) = \\frac{-2}{3} \\times \\frac{-5}{4} + \\frac{-2}{3} \\times \\frac{4}{7}$", "a": "LHS: $\\frac{-2}{3} \\times \\left(\\frac{-35 + 16}{28}\\right) = \\frac{-2}{3} \\times \\frac{-19}{28} = \\frac{19}{42}$<br>RHS: $\\frac{5}{6} + \\frac{-8}{21} = \\frac{35 - 16}{42} = \\frac{19}{42}$<br>(Verified)"},
            {"q": "(iii) $\\frac{8}{11} \\times \\left(\\frac{-3}{2} + \\frac{-5}{11}\\right) = \\frac{8}{11} \\times \\frac{-3}{2} + \\frac{8}{11} \\times \\frac{-5}{11}$", "a": "LHS: $\\frac{8}{11} \\times \\left(\\frac{-33 - 10}{22}\\right) = \\frac{8}{11} \\times \\frac{-43}{22} = \\frac{-172}{121}$<br>RHS: $\\frac{-12}{11} + \\frac{-40}{121} = \\frac{-132 - 40}{121} = \\frac{-172}{121}$<br>(Verified)"},
            {"q": "(iv) $\\frac{-3}{2} \\times \\left(\\frac{-5}{7} + \\frac{-5}{2}\\right) = \\frac{-3}{2} \\times \\frac{-5}{7} + \\frac{-3}{2} \\times \\frac{-5}{2}$", "a": "LHS: $\\frac{-3}{2} \\times \\left(\\frac{-10 - 35}{14}\\right) = \\frac{-3}{2} \\times \\frac{-45}{14} = \\frac{135}{28}$<br>RHS: $\\frac{15}{14} + \\frac{15}{4} = \\frac{30 + 105}{28} = \\frac{135}{28}$<br>(Verified)"},
            {"q": "(v) \\left(\\frac{7}{11} + \\frac{3}{5}\\right) \\times \\frac{2}{3} = \\frac{7}{11} \\times \\frac{2}{3} + \\frac{3}{5} \\times \\frac{2}{3}", "a": "LHS: $\\left(\\frac{35 + 33}{55}\\right) \\times \\frac{2}{3} = \\frac{68}{55} \\times \\frac{2}{3} = \\frac{136}{165}$<br>RHS: $\\frac{14}{33} + \\frac{6}{15} = \\frac{70 + 66}{165} = \\frac{136}{165}$<br>(Verified)"}
        ]
    },
    {
        "q": "6. Using the distributive property, find the value of each of the following.",
        "subs": [
            {"q": "(i) $\\frac{3}{5} \\times \\frac{-20}{9} + \\frac{3}{5} \\times \\frac{-1}{3}$", "a": "$\\frac{3}{5} \\times \\left(\\frac{-20}{9} + \\frac{-1}{3}\\right) = \\frac{3}{5} \\times \\left(\\frac{-20 - 3}{9}\\right) = \\frac{3}{5} \\times \\frac{-23}{9} = \\frac{-23}{15}$"},
            {"q": "(ii) $\\frac{7}{15} \\times \\frac{-50}{49} + \\frac{7}{15} \\times \\frac{1}{49}$", "a": "$\\frac{7}{15} \\times \\left(\\frac{-50}{49} + \\frac{1}{49}\\right) = \\frac{7}{15} \\times \\frac{-49}{49} = \\frac{7}{15} \\times (-1) = \\frac{-7}{15}$"},
            {"q": "(iii) $\\frac{-13}{5} \\times \\frac{16}{7} - \\frac{13}{5} \\times \\frac{19}{7}$", "a": "$\\frac{-13}{5} \\times \\left(\\frac{16}{7} + \\frac{19}{7}\\right) = \\frac{-13}{5} \\times \\frac{35}{7} = \\frac{-13}{5} \\times 5 = -13$"},
            {"q": "(iv) $\\frac{-1}{3} \\times \\frac{-3}{5} + \\frac{-1}{3} \\times \\frac{7}{11}$", "a": "$\\frac{-1}{3} \\times \\left(\\frac{-3}{5} + \\frac{7}{11}\\right) = \\frac{-1}{3} \\times \\left(\\frac{-33 + 35}{55}\\right) = \\frac{-1}{3} \\times \\frac{2}{55} = \\frac{-2}{165}$"},
            {"q": "(v) $\\frac{2}{3} \\times \\frac{9}{10} + \\frac{2}{3} \\times \\frac{-4}{10}$", "a": "$\\frac{2}{3} \\times \\left(\\frac{9}{10} + \\frac{-4}{10}\\right) = \\frac{2}{3} \\times \\frac{5}{10} = \\frac{2}{3} \\times \\frac{1}{2} = \\frac{1}{3}$"}
        ]
    },
    {
        "q": "7. Fill in the blanks.",
        "subs": [
            {"q": "(i) $\\frac{-7}{17} \\times \\frac{27}{35} = \\frac{27}{35} \\times ......$", "a": "<b>$\\frac{-7}{17}$</b>"}
        ]
    }
]
"""

with open("generator.py", "r", encoding="utf-8") as f:
    content = f.read()

# Insert questions_ch1 before questions_ch3
content = content.replace("questions_ch3 = [", ch1_code + "\nquestions_ch3 = [")

# Update chapters array
content = content.replace(
    """chapters = [
    {"id": "ch3", "title": "Chapter 3: Squares and Square Roots", "data": questions_ch3},
    {"id": "ch4", "title": "Chapter 4: Cubes and Cube Roots", "data": questions_ch4}
]""",
    """chapters = [
    {"id": "ch1", "title": "Chapter 1: Rational Numbers", "data": questions_ch1},
    {"id": "ch3", "title": "Chapter 3: Squares and Square Roots", "data": questions_ch3},
    {"id": "ch4", "title": "Chapter 4: Cubes and Cube Roots", "data": questions_ch4}
]"""
)

# Also let's update home view buttons to include Chapter 1.
# Actually the loop already builds buttons!
# for ch in chapters:
#    html_template += f'        <button class="home-btn" onclick="openChapter(\'{ch["id"]}\')">{ch["title"]}</button>\n'
# So adding it to the chapters array is enough!

with open("generator.py", "w", encoding="utf-8") as f:
    f.write(content)
