import json



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

questions_ch3 = [
    {
        "q": "1. Find the value of each of the following.",
        "subs": [
            {"q": "(i) $\\left(\\frac{11}{13}\\right)^2$", "a": "$\\left(\\frac{11}{13}\\right)^2 = \\frac{11^2}{13^2} = \\frac{121}{169}$"},
            {"q": "(ii) $\\left(-1 \\frac{7}{11}\\right)^3$", "a": "$\\left(-1 \\frac{7}{11}\\right)^3 = \\left(\\frac{-18}{11}\\right)^3 = \\frac{(-18)^3}{11^3} = \\frac{-5832}{1331}$"},
            {"q": "(iii) $(3.5)^2$", "a": "$(3.5)^2 = \\left(\\frac{35}{10}\\right)^2 = \\frac{1225}{100} = 12.25$"},
            {"q": "(iv) $(0.08)^3$", "a": "$(0.08)^3 = \\left(\\frac{8}{100}\\right)^3 = \\frac{512}{1000000} = 0.000512$"}
        ]
    },
    {
        "q": "2. Find the square root of each of the following by prime factorisation.",
        "subs": [
            {"q": "(i) 256", "a": "$256 = 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 \\times 2 = 2^8$<br>$\\sqrt{256} = \\sqrt{2^8} = 2^4 = 16$"},
            {"q": "(ii) 324", "a": "$324 = 2 \\times 2 \\times 3 \\times 3 \\times 3 \\times 3 = 2^2 \\times 3^4$<br>$\\sqrt{324} = 2 \\times 3^2 = 2 \\times 9 = 18$"},
            {"q": "(iii) 784", "a": "$784 = 2 \\times 2 \\times 2 \\times 2 \\times 7 \\times 7 = 2^4 \\times 7^2$<br>$\\sqrt{784} = 2^2 \\times 7 = 4 \\times 7 = 28$"},
            {"q": "(iv) 7056", "a": "$7056 = 2^4 \\times 3^2 \\times 7^2$<br>$\\sqrt{7056} = 2^2 \\times 3 \\times 7 = 4 \\times 21 = 84$"},
            {"q": "(v) 28224", "a": "$28224 = 2^6 \\times 3^2 \\times 7^2$<br>$\\sqrt{28224} = 2^3 \\times 3 \\times 7 = 8 \\times 21 = 168$"},
            {"q": "(vi) 60025", "a": "$60025 = 5^2 \\times 7^4$<br>$\\sqrt{60025} = 5 \\times 7^2 = 5 \\times 49 = 245$"}
        ]
    },
    {
        "q": "3. Find the square root of each of the following by division.",
        "subs": [
            {"q": "(i) 841", "a": "$$\\begin{array}{r|l} & 29 \\\\ \\hline 2 & \\overline{8}\\overline{41} \\\\ & -4 \\\\ \\hline 49 & 441 \\\\ & -441 \\\\ \\hline & 0 \\end{array}$$ <br>$\\sqrt{841} = 29$"},
            {"q": "(ii) 2304", "a": "$$\\begin{array}{r|l} & 48 \\\\ \\hline 4 & \\overline{23}\\overline{04} \\\\ & -16 \\\\ \\hline 88 & 704 \\\\ & -704 \\\\ \\hline & 0 \\end{array}$$ <br>$\\sqrt{2304} = 48$"},
            {"q": "(iii) 39204", "a": "$$\\begin{array}{r|l} & 198 \\\\ \\hline 1 & \\overline{3}\\overline{92}\\overline{04} \\\\ & -1 \\\\ \\hline 29 & 292 \\\\ & -261 \\\\ \\hline 388 & 3104 \\\\ & -3104 \\\\ \\hline & 0 \\end{array}$$ <br>$\\sqrt{39204} = 198$"},
            {"q": "(iv) 55225", "a": "$$\\begin{array}{r|l} & 235 \\\\ \\hline 2 & \\overline{5}\\overline{52}\\overline{25} \\\\ & -4 \\\\ \\hline 43 & 152 \\\\ & -129 \\\\ \\hline 465 & 2325 \\\\ & -2325 \\\\ \\hline & 0 \\end{array}$$ <br>$\\sqrt{55225} = 235$"},
            {"q": "(v) 177241", "a": "$$\\begin{array}{r|l} & 421 \\\\ \\hline 4 & \\overline{17}\\overline{72}\\overline{41} \\\\ & -16 \\\\ \\hline 82 & 172 \\\\ & -164 \\\\ \\hline 841 & 841 \\\\ & -841 \\\\ \\hline & 0 \\end{array}$$ <br>$\\sqrt{177241} = 421$"},
            {"q": "(vi) 425104", "a": "$$\\begin{array}{r|l} & 652 \\\\ \\hline 6 & \\overline{42}\\overline{51}\\overline{04} \\\\ & -36 \\\\ \\hline 125 & 651 \\\\ & -625 \\\\ \\hline 1302 & 2604 \\\\ & -2604 \\\\ \\hline & 0 \\end{array}$$ <br>$\\sqrt{425104} = 652$"}
        ]
    },
    {
        "q": "4. Find the square root of each of the following.",
        "subs": [
            {"q": "(i) 13.69", "a": "$\\sqrt{13.69} = \\sqrt{\\frac{1369}{100}} = \\frac{37}{10} = 3.7$"},
            {"q": "(ii) 0.002025", "a": "$\\sqrt{0.002025} = \\sqrt{\\frac{2025}{1000000}} = \\frac{45}{1000} = 0.045$"},
            {"q": "(iii) 1.5129", "a": "$\\sqrt{1.5129} = \\sqrt{\\frac{15129}{10000}} = \\frac{123}{100} = 1.23$"},
            {"q": "(iv) 20.7936", "a": "$\\sqrt{20.7936} = \\sqrt{\\frac{207936}{10000}} = \\frac{456}{100} = 4.56$"},
            {"q": "(v) 6146.56", "a": "$\\sqrt{6146.56} = \\sqrt{\\frac{614656}{100}} = \\frac{784}{10} = 78.4$"},
            {"q": "(vi) 1.024144", "a": "$\\sqrt{1.024144} = \\sqrt{\\frac{1024144}{1000000}} = \\frac{1012}{1000} = 1.012$"}
        ]
    },
    {
        "q": "5. Find the square root of each of the following.",
        "subs": [
            {"q": "(i) $\\frac{169}{484}$", "a": "$\\sqrt{\\frac{169}{484}} = \\frac{\\sqrt{169}}{\\sqrt{484}} = \\frac{13}{22}$"},
            {"q": "(ii) $5 \\frac{580}{729}$", "a": "$\\sqrt{\\frac{(5 \\times 729) + 580}{729}} = \\sqrt{\\frac{3645 + 580}{729}} = \\sqrt{\\frac{4225}{729}} = \\frac{65}{27}$"},
            {"q": "(iii) $12 \\frac{52}{81}$", "a": "$\\sqrt{\\frac{(12 \\times 81) + 52}{81}} = \\sqrt{\\frac{972 + 52}{81}} = \\sqrt{\\frac{1024}{81}} = \\frac{32}{9}$"},
            {"q": "(iv) 0.0009", "a": "$\\sqrt{0.0009} = \\sqrt{\\frac{9}{10000}} = \\frac{3}{100} = 0.03$"},
            {"q": "(v) 4.41", "a": "$\\sqrt{4.41} = \\sqrt{\\frac{441}{100}} = \\frac{21}{10} = 2.1$"}
        ]
    },
    {
        "q": "6. Find the square root of each of the following correct to two decimal places.",
        "subs": [
            {"q": "(i) 2", "a": "$\\sqrt{2} \\approx 1.41$"},
            {"q": "(ii) 3", "a": "$\\sqrt{3} \\approx 1.73$"},
            {"q": "(iii) 8", "a": "$\\sqrt{8} \\approx 2.83$"},
            {"q": "(iv) 11", "a": "$\\sqrt{11} \\approx 3.32$"},
            {"q": "(v) 35", "a": "$\\sqrt{35} \\approx 5.92$"},
            {"q": "(vi) 99", "a": "$\\sqrt{99} \\approx 9.95$"}
        ]
    },
    {
        "q": "7. Find the value of $\\sqrt{5}$ correct to two decimal places. Then, find the value of the square root of $\\frac{3-\\sqrt{5}}{3+\\sqrt{5}}$ correct to two decimal places.",
        "subs": [
            {"q": "", "a": "$\\sqrt{5} \\approx 2.24$<br>$\\sqrt{\\frac{3-\\sqrt{5}}{3+\\sqrt{5}}} = \\sqrt{\\frac{(3-\\sqrt{5})(3-\\sqrt{5})}{(3+\\sqrt{5})(3-\\sqrt{5})}}$<br>$= \\sqrt{\\frac{(3-\\sqrt{5})^2}{9-5}} = \\frac{3-\\sqrt{5}}{\\sqrt{4}} = \\frac{3-\\sqrt{5}}{2}$<br>Using $\\sqrt{5} = 2.236$ (taking 3 decimal places for calculation accuracy):<br>$\\frac{3 - 2.236}{2} = \\frac{0.764}{2} = 0.382$<br>Correct to two decimal places: $0.38$"}
        ]
    },
    {
        "q": "8. Find the square root of each of the following correct to three decimal places.",
        "subs": [
            {"q": "(i) 2.5", "a": "$\\sqrt{2.5} \\approx 1.581$"},
            {"q": "(ii) 0.036", "a": "$\\sqrt{0.036} \\approx 0.190$"},
            {"q": "(iii) 6.4", "a": "$\\sqrt{6.4} \\approx 2.530$"},
            {"q": "(iv) 0.100", "a": "$\\sqrt{0.100} \\approx 0.316$"}
        ]
    },
    {
        "q": "9. Find the least number by which 10368 should be (i) increased (ii) decreased (iii) multiplied (iv) divided to make it a perfect square.",
        "subs": [
            {"q": "", "a": "We find the square root of 10368. $101^2 = 10201$ and $102^2 = 10404$.<br>So, $101^2 < 10368 < 102^2$<br>(i) Increased: To get the next perfect square ($10404$), we add: $10404 - 10368 = 36$<br>(ii) Decreased: To get the previous perfect square ($10201$), we subtract: $10368 - 10201 = 167$<br>Now, prime factorization of $10368 = 2^7 \\times 3^4$<br>(iii) Multiplied: To make all powers even, we need to multiply by $2$. (Result will be $2^8 \\times 3^4$)<br>(iv) Divided: To make all powers even, we need to divide by $2$. (Result will be $2^6 \\times 3^4$)"}
        ]
    },
    {
        "q": "10. Find the following.",
        "subs": [
            {"q": "(i) $55^2$", "a": "$55^2 = 3025$"},
            {"q": "(ii) $98^2$", "a": "$98^2 = 9604$"},
            {"q": "(iii) $\\sqrt{38}$", "a": "$\\sqrt{38} \\approx 6.164$ (to 3 decimal places)"},
            {"q": "(iv) $\\sqrt{89}$", "a": "$\\sqrt{89} \\approx 9.43$ (to 2 decimal places)"},
            {"q": "(v) $\\sqrt{38.83}$", "a": "$\\sqrt{38.83} \\approx 6.23$ (to 2 decimal places)"},
            {"q": "(vi) $\\sqrt{64.25}$", "a": "$\\sqrt{64.25} \\approx 8.016$ (to 3 decimal places)"}
        ]
    },
    {
        "q": "11. Use algebraic methods to find the following.",
        "subs": [
            {"q": "(i) $52^2$", "a": "$(50 + 2)^2 = 50^2 + 2(50)(2) + 2^2 = 2500 + 200 + 4 = 2704$"},
            {"q": "(ii) $98^2$", "a": "$(100 - 2)^2 = 100^2 - 2(100)(2) + 2^2 = 10000 - 400 + 4 = 9604$"},
            {"q": "(iii) $309^2$", "a": "$(300 + 9)^2 = 300^2 + 2(300)(9) + 9^2 = 90000 + 5400 + 81 = 95481$"},
            {"q": "(iv) $495^2$", "a": "$(500 - 5)^2 = 500^2 - 2(500)(5) + 5^2 = 250000 - 5000 + 25 = 245025$"},
            {"q": "(v) $96^2$", "a": "$(100 - 4)^2 = 100^2 - 2(100)(4) + 4^2 = 10000 - 800 + 16 = 9216$"},
            {"q": "(vi) $305^2$", "a": "$(300 + 5)^2 = 300^2 + 2(300)(5) + 5^2 = 90000 + 3000 + 25 = 93025$"}
        ]
    },
    {
        "q": "12. Find in each case the smallest perfect square divisible by the given numbers.",
        "subs": [
            {"q": "(i) 2, 4 and 5", "a": "LCM of $2, 4, 5$ is $20$. <br>Prime factors of $20 = 2^2 \\times 5$.<br>To make it a perfect square, we need to multiply by $5$.<br>Smallest perfect square = $20 \\times 5 = 100$."},
            {"q": "(ii) 3, 4, 5 and 6", "a": "LCM of $3, 4, 5, 6$ is $60$. <br>Prime factors of $60 = 2^2 \\times 3 \\times 5$.<br>To make it a perfect square, we need to multiply by $3 \\times 5 = 15$.<br>Smallest perfect square = $60 \\times 15 = 900$."},
            {"q": "(iii) 6, 8, 10 and 12", "a": "LCM of $6, 8, 10, 12$ is $120$. <br>Prime factors of $120 = 2^3 \\times 3 \\times 5$.<br>To make it a perfect square, we need to multiply by $2 \\times 3 \\times 5 = 30$.<br>Smallest perfect square = $120 \\times 30 = 3600$."}
        ]
    },
    {
        "q": "13. In an auditorium, the number of rows is equal to the number of chairs in each row. If the capacity of the auditorium is 2304, find the number of chairs in a row.",
        "subs": [
            {"q": "", "a": "Let the number of rows be $x$. <br>Then, the number of chairs in each row is also $x$.<br>Total capacity = $x \\times x = x^2$<br>$x^2 = 2304$<br>$x = \\sqrt{2304} = 48$<br>Number of chairs in a row is 48."}
        ]
    },
    {
        "q": "14. In a garden, 1089 rose plants are arranged in such a way that there are as many rows as there are plants in each row. Find the number of rows in the garden.",
        "subs": [
            {"q": "", "a": "Let the number of rows be $x$. <br>Then, the number of plants per row is $x$.<br>Total plants = $x \\times x = x^2$<br>$x^2 = 1089$<br>$x = \\sqrt{1089} = 33$<br>Number of rows in the garden is 33."}
        ]
    },
    {
        "q": "15. An army officer wishes to arrange 4770 soldiers in the form of a square. After arranging he finds that nine soldiers are left out. Find the number of soldiers in each row.",
        "subs": [
            {"q": "", "a": "Soldiers placed in the square = $4770 - 9 = 4761$.<br>Let the number of soldiers in each row be $x$.<br>Total soldiers in square = $x^2 = 4761$<br>$x = \\sqrt{4761} = 69$<br>Number of soldiers in each row is 69."}
        ]
    },
    {
        "q": "16. Find the least number that must be subtracted from each of the following numbers to get a perfect square. Also, find the square root of this perfect square.",
        "subs": [
            {"q": "(i) 9845", "a": "$\\sqrt{9845} \\approx 99.22$<br>The perfect square just below it is $99^2 = 9801$.<br>Least number to subtract = $9845 - 9801 = 44$.<br>Square root of the perfect square is 99."},
            {"q": "(ii) 7585", "a": "$\\sqrt{7585} \\approx 87.09$<br>The perfect square just below it is $87^2 = 7569$.<br>Least number to subtract = $7585 - 7569 = 16$.<br>Square root of the perfect square is 87."},
            {"q": "(iii) 786", "a": "$\\sqrt{786} \\approx 28.03$<br>The perfect square just below it is $28^2 = 784$.<br>Least number to subtract = $786 - 784 = 2$.<br>Square root of the perfect square is 28."}
        ]
    },
    {
        "q": "17. Find the least number which must be added to each of the following numbers to make it a perfect square. Also, find the square root of this perfect square.",
        "subs": [
            {"q": "(i) 9389", "a": "$\\sqrt{9389} \\approx 96.89$<br>The perfect square just above it is $97^2 = 9409$.<br>Least number to add = $9409 - 9389 = 20$.<br>Square root of the perfect square is 97."},
            {"q": "(ii) 5601", "a": "$\\sqrt{5601} \\approx 74.83$<br>The perfect square just above it is $75^2 = 5625$.<br>Least number to add = $5625 - 5601 = 24$.<br>Square root of the perfect square is 75."},
            {"q": "(iii) 4725", "a": "$\\sqrt{4725} \\approx 68.73$<br>The perfect square just above it is $69^2 = 4761$.<br>Least number to add = $4761 - 4725 = 36$.<br>Square root of the perfect square is 69."}
        ]
    },
    {
        "q": "18. Find the greatest six-digit number which is a perfect square.",
        "subs": [
            {"q": "", "a": "The greatest 6-digit number is 999999.<br>$\\sqrt{999999} \\approx 999.999$<br>So, the greatest 6-digit perfect square is $999^2 = 998001$."}
        ]
    },
    {
        "q": "19. Find the smallest six-digit number which is a perfect square.",
        "subs": [
            {"q": "", "a": "The smallest 6-digit number is 100000.<br>$\\sqrt{100000} \\approx 316.22$<br>So, the smallest 6-digit perfect square is $317^2 = 100489$."}
        ]
    },
    {
        "q": "20. Find the value of each of the following.",
        "subs": [
            {"q": "(i) $\\sqrt{\\frac{1.44}{0.49}}$", "a": "$\\sqrt{\\frac{144/100}{49/100}} = \\sqrt{\\frac{144}{49}} = \\frac{12}{7}$"},
            {"q": "(ii) $\\sqrt{\\frac{32.4}{28.9}}$", "a": "$\\sqrt{\\frac{324/10}{289/10}} = \\sqrt{\\frac{324}{289}} = \\frac{18}{17}$"},
            {"q": "(iii) $\\sqrt{\\frac{0.0025}{0.0196}}$", "a": "$\\sqrt{\\frac{25/10000}{196/10000}} = \\sqrt{\\frac{25}{196}} = \\frac{5}{14}$"},
            {"q": "(iv) $\\sqrt{1 + \\frac{25}{144}}$", "a": "$\\sqrt{\\frac{144 + 25}{144}} = \\sqrt{\\frac{169}{144}} = \\frac{13}{12}$"},
            {"q": "(v) $\\sqrt{1 - \\frac{64}{289}}$", "a": "$\\sqrt{\\frac{289 - 64}{289}} = \\sqrt{\\frac{225}{289}} = \\frac{15}{17}$"},
            {"q": "(vi) $\\sqrt{2^3 \\times 6^3 \\times 27}$", "a": "$\\sqrt{8 \\times 216 \\times 27} = \\sqrt{46656} = 216$<br>(Alternative: $\\sqrt{2^3 \\times (2 \\times 3)^3 \\times 3^3} = \\sqrt{2^6 \\times 3^6} = 2^3 \\times 3^3 = 8 \\times 27 = 216$)"},
            {"q": "(vii) $\\frac{\\sqrt{9}}{\\sqrt{0.09}} + \\frac{\\sqrt{16}}{\\sqrt{0.16}} + \\frac{\\sqrt{25}}{\\sqrt{0.25}}$", "a": "$\\frac{3}{0.3} + \\frac{4}{0.4} + \\frac{5}{0.5} = 10 + 10 + 10 = 30$"},
            {"q": "(viii) $\\sqrt{400} + \\sqrt{4} + \\sqrt{0.04} + \\sqrt{0.0004}$", "a": "$20 + 2 + 0.2 + 0.02 = 22.22$"},
            {"q": "(ix) $\\sqrt{182 - \\sqrt{156 + \\sqrt{169}}}$", "a": "$\\sqrt{182 - \\sqrt{156 + 13}} = \\sqrt{182 - \\sqrt{169}} = \\sqrt{182 - 13} = \\sqrt{169} = 13$"},
            {"q": "(x) $\\sqrt{382 + \\sqrt{341 - \\sqrt{289}}}$", "a": "$\\sqrt{382 + \\sqrt{341 - 17}} = \\sqrt{382 + \\sqrt{324}} = \\sqrt{382 + 18} = \\sqrt{400} = 20$"}
        ]
    },
    {
        "q": "21. Fill in the blanks.",
        "subs": [
            {"q": "(i) The units digit of the square of a number ending in 2 is ...... ", "a": "<b>4</b>"},
            {"q": "(ii) The units digit of the square of a number ending in 9 is ...... ", "a": "<b>1</b>"},
            {"q": "(iii) The units digit of the square root of a number ending in 6 is ...... or ...... ", "a": "<b>4</b> or <b>6</b>"},
            {"q": "(iv) There are ...... natural numbers between the squares of 8 and 9.", "a": "<b>16</b> (since $2 \\times 8 = 16$)"},
            {"q": "(v) $9^2 - 8^2$ = ...... + 8.", "a": "<b>9</b> (since $a^2 - b^2 = (a-b)(a+b)$, here $(9-8)(9+8) = 1(9+8) = 9+8$)"},
            {"q": "(vi) $19^2$ - ...... = 19 + 18.", "a": "<b>$18^2$</b> (since $19^2 - 18^2 = (19-18)(19+18) = 19+18$)"},
            {"q": "(vii) If $\\sqrt{4096} = 64$ then $\\sqrt{4096} + \\sqrt{40.96}$ = ....... ", "a": "$\\sqrt{4096} + \\sqrt{40.96} = 64 + 6.4 = $ <b>70.4</b>"},
            {"q": "(viii) $\\sqrt{4} + \\sqrt{0.04} + \\sqrt{0.0004}$ = .......", "a": "$2 + 0.2 + 0.02 = $ <b>2.22</b>"},
            {"q": "(ix) 3, 4 and ...... form a Pythagorean triple.", "a": "<b>5</b> (since $3^2 + 4^2 = 5^2$)"}
        ]
    }
]

questions_ch4 = [
    {
        "q": "1. Find the value of each of the following.",
        "subs": [
            {"q": "(i) $\\left(\\frac{5}{6}\\right)^3$", "a": "$\\left(\\frac{5}{6}\\right)^3 = \\frac{5^3}{6^3} = \\frac{125}{216}$"},
            {"q": "(ii) $\\left(-1 \\frac{7}{11}\\right)^3$", "a": "$\\left(-1 \\frac{7}{11}\\right)^3 = \\left(\\frac{-18}{11}\\right)^3 = \\frac{(-18)^3}{11^3} = \\frac{-5832}{1331} = -4 \\frac{508}{1331}$"},
            {"q": "(iii) $(2.5)^3$", "a": "$(2.5)^3 = \\left(\\frac{25}{10}\\right)^3 = \\frac{15625}{1000} = 15.625$"},
            {"q": "(iv) $(0.08)^3$", "a": "$(0.08)^3 = \\left(\\frac{8}{100}\\right)^3 = \\frac{512}{1000000} = 0.000512$"},
            {"q": "(v) $(-1.1)^3$", "a": "$(-1.1)^3 = \\left(\\frac{-11}{10}\\right)^3 = \\frac{-1331}{1000} = -1.331$"},
            {"q": "(vi) $\\left(-\\frac{7}{3}\\right)^3$", "a": "$\\left(-\\frac{7}{3}\\right)^3 = \\frac{(-7)^3}{3^3} = \\frac{-343}{27}$"},
            {"q": "(vii) $(-9)^3$", "a": "$(-9)^3 = -729$"},
            {"q": "(viii) $(-0.5)^3$", "a": "$(-0.5)^3 = \\left(\\frac{-5}{10}\\right)^3 = \\frac{-125}{1000} = -0.125$"},
            {"q": "(ix) $(-20)^3$", "a": "$(-20)^3 = -8000$"},
            {"q": "(x) $(-0.013)^3$", "a": "$(-0.013)^3 = \\left(\\frac{-13}{1000}\\right)^3 = \\frac{-2197}{1000000000} = -0.000002197$"},
            {"q": "(xi) $(25)^3$", "a": "$(25)^3 = 15625$"},
            {"q": "(xii) $\\left(2 \\frac{1}{7}\\right)^3$", "a": "$\\left(2 \\frac{1}{7}\\right)^3 = \\left(\\frac{15}{7}\\right)^3 = \\frac{15^3}{7^3} = \\frac{3375}{343} = 9 \\frac{288}{343}$"}
        ]
    },
    {
        "q": "2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.",
        "subs": [
            {"q": "(i) 128", "a": "$128 = 2^7$. (Not a perfect cube)"},
            {"q": "(ii) 243", "a": "$243 = 3^5$. (Not a perfect cube)"},
            {"q": "(iii) 343", "a": "$343 = 7^3$. (Perfect cube of 7)"},
            {"q": "(iv) 4000", "a": "$4000 = 2^5 \\times 5^3$. (Not a perfect cube)"},
            {"q": "(v) 3456", "a": "$3456 = 2^7 \\times 3^3$. (Not a perfect cube)"},
            {"q": "(vi) 2048", "a": "$2048 = 2^{11}$. (Not a perfect cube)"},
            {"q": "(vii) 2197", "a": "$2197 = 13^3$. (Perfect cube of 13)"},
            {"q": "(viii) 1000000", "a": "$1000000 = 100^3$. (Perfect cube of 100)"},
            {"q": "(ix) 2744", "a": "$2744 = 14^3$. (Perfect cube of 14)"}
        ]
    },
    {
        "q": "3. Which of the following are cubes of even numbers and which are of odd numbers?",
        "subs": [
            {"q": "(i) 8000", "a": "8000 is an even number, so it is the cube of an **even** number."},
            {"q": "(ii) 9261", "a": "9261 is an odd number, so it is the cube of an **odd** number."},
            {"q": "(iii) 4096", "a": "4096 is an even number, so it is the cube of an **even** number."},
            {"q": "(iv) 6859", "a": "6859 is an odd number, so it is the cube of an **odd** number."},
            {"q": "(v) 12167", "a": "12167 is an odd number, so it is the cube of an **odd** number."},
            {"q": "(vi) 4913", "a": "4913 is an odd number, so it is the cube of an **odd** number."},
            {"q": "(vii) 13824", "a": "13824 is an even number, so it is the cube of an **even** number."},
            {"q": "(viii) 17576", "a": "17576 is an even number, so it is the cube of an **even** number."}
        ]
    },
    {
        "q": "4. Find each of the following.",
        "subs": [
            {"q": "(i) $\\sqrt[3]{512}$", "a": "$\\sqrt[3]{512} = \\sqrt[3]{8^3} = 8$"},
            {"q": "(ii) $\\sqrt[3]{2744}$", "a": "$\\sqrt[3]{2744} = \\sqrt[3]{14^3} = 14$"},
            {"q": "(iii) $\\sqrt[3]{729}$", "a": "$\\sqrt[3]{729} = \\sqrt[3]{9^3} = 9$"},
            {"q": "(iv) $\\sqrt[3]{1728}$", "a": "$\\sqrt[3]{1728} = \\sqrt[3]{12^3} = 12$"},
            {"q": "(v) $\\sqrt[3]{1000}$", "a": "$\\sqrt[3]{1000} = \\sqrt[3]{10^3} = 10$"},
            {"q": "(vi) $\\sqrt[3]{-8000}$", "a": "$\\sqrt[3]{-8000} = \\sqrt[3]{(-20)^3} = -20$"},
            {"q": "(vii) $\\sqrt[3]{-4096}$", "a": "$\\sqrt[3]{-4096} = \\sqrt[3]{(-16)^3} = -16$"},
            {"q": "(viii) $\\sqrt[3]{\\frac{27}{125}}$", "a": "$\\sqrt[3]{\\frac{27}{125}} = \\frac{\\sqrt[3]{27}}{\\sqrt[3]{125}} = \\frac{3}{5}$"},
            {"q": "(ix) $\\sqrt[3]{\\frac{-125}{64}}$", "a": "$\\sqrt[3]{\\frac{-125}{64}} = \\frac{\\sqrt[3]{-125}}{\\sqrt[3]{64}} = \\frac{-5}{4}$"},
            {"q": "(x) $\\sqrt[3]{0.001}$", "a": "$\\sqrt[3]{0.001} = \\sqrt[3]{\\frac{1}{1000}} = \\frac{1}{10} = 0.1$"},
            {"q": "(xi) $\\sqrt[3]{0.125}$", "a": "$\\sqrt[3]{0.125} = \\sqrt[3]{\\frac{125}{1000}} = \\frac{5}{10} = 0.5$"},
            {"q": "(xii) $\\sqrt[3]{\\frac{27}{64 \\times 125}}$", "a": "$\\frac{\\sqrt[3]{27}}{\\sqrt[3]{64} \\times \\sqrt[3]{125}} = \\frac{3}{4 \\times 5} = \\frac{3}{20}$"},
            {"q": "(xiii) $\\sqrt[3]{\\frac{729}{125 \\times 1000}}$", "a": "$\\frac{\\sqrt[3]{729}}{\\sqrt[3]{125} \\times \\sqrt[3]{1000}} = \\frac{9}{5 \\times 10} = \\frac{9}{50}$"},
            {"q": "(xiv) $\\sqrt[3]{125 \\times 64 \\times 8}$", "a": "$\\sqrt[3]{125} \\times \\sqrt[3]{64} \\times \\sqrt[3]{8} = 5 \\times 4 \\times 2 = 40$"},
            {"q": "(xv) $\\sqrt[3]{16 \\times 500}$", "a": "$\\sqrt[3]{8000} = 20$"},
            {"q": "(xvi) $\\sqrt[3]{625 \\times (-1600)}$", "a": "$\\sqrt[3]{-1000000} = -100$"},
            {"q": "(xvii) $\\sqrt[3]{\\frac{343}{2500 \\times 400}}$", "a": "$\\sqrt[3]{\\frac{343}{1000000}} = \\frac{7}{100}$"},
            {"q": "(xviii) $\\sqrt[3]{1 - \\frac{854}{729}}$", "a": "$\\sqrt[3]{\\frac{729 - 854}{729}} = \\sqrt[3]{\\frac{-125}{729}} = \\frac{-5}{9}$"},
            {"q": "(xix) $\\sqrt[3]{4 + \\sqrt[3]{61 + \\sqrt[3]{27}}}$", "a": "$\\sqrt[3]{4 + \\sqrt[3]{61 + 3}}$<br>$= \\sqrt[3]{4 + \\sqrt[3]{64}}$<br>$= \\sqrt[3]{4 + 4} = \\sqrt[3]{8} = 2$"}
        ]
    },
    {
        "q": "5. Find the least number by which each of the following numbers should be multiplied to make it a perfect cube. Also, find the cube root of the product in each case.",
        "subs": [
            {"q": "(i) 5488", "a": "Prime factorization: $5488 = 2^4 \\times 7^3$<br>To make the powers multiples of 3, multiply by $2^2 = 4$.<br>Least number = 4<br>New product = $2^6 \\times 7^3$<br>Cube root = $2^2 \\times 7 = 4 \\times 7 = 28$"},
            {"q": "(ii) 34992", "a": "Prime factorization: $34992 = 2^4 \\times 3^7$<br>To make the powers multiples of 3, multiply by $2^2 \\times 3^2 = 4 \\times 9 = 36$.<br>Least number = 36<br>New product = $2^6 \\times 3^9$<br>Cube root = $2^2 \\times 3^3 = 4 \\times 27 = 108$"},
            {"q": "(iii) 15552", "a": "Prime factorization: $15552 = 2^6 \\times 3^5$<br>To make the powers multiples of 3, multiply by $3^1 = 3$.<br>Least number = 3<br>New product = $2^6 \\times 3^6$<br>Cube root = $2^2 \\times 3^2 = 4 \\times 9 = 36$"}
        ]
    },
    {
        "q": "6. Find the least number by which each of the following numbers should be divided to make it a perfect cube. Also, find the cube root of each perfect cube.",
        "subs": [
            {"q": "(i) 5184", "a": "Prime factorization: $5184 = 2^6 \\times 3^4$<br>To leave powers as multiples of 3, divide by $3^1 = 3$.<br>Least number = 3<br>New quotient = $2^6 \\times 3^3$<br>Cube root = $2^2 \\times 3 = 4 \\times 3 = 12$"},
            {"q": "(ii) 5488", "a": "Prime factorization: $5488 = 2^4 \\times 7^3$<br>To leave powers as multiples of 3, divide by $2^1 = 2$.<br>Least number = 2<br>New quotient = $2^3 \\times 7^3$<br>Cube root = $2 \\times 7 = 14$"},
            {"q": "(iii) 23328", "a": "Prime factorization: $23328 = 2^5 \\times 3^6$<br>To leave powers as multiples of 3, divide by $2^2 = 4$.<br>Least number = 4<br>New quotient = $2^3 \\times 3^6$<br>Cube root = $2 \\times 3^2 = 2 \\times 9 = 18$"}
        ]
    },
    {
        "q": "7. Fill in the blanks.",
        "subs": [
            {"q": "(i) The units digit in the cube of 1137 is ...... ", "a": "<b>3</b> (since $7^3 = 343$, unit digit is 3)"},
            {"q": "(ii) The ones digit in the cube of 1004 is ...... ", "a": "<b>4</b> (since $4^3 = 64$, unit digit is 4)"},
            {"q": "(iii) The cube of an odd number is always an ...... number.", "a": "<b>odd</b>"},
            {"q": "(iv) The cube of an even number is always an ...... number.", "a": "<b>even</b>"},
            {"q": "(v) The least natural number by which 1600 is to be multiplied to make it a perfect cube is ....... ", "a": "$1600 = 2^6 \\times 5^2$. Needs to be multiplied by <b>5</b>."},
            {"q": "(vi) The least natural number by which 1024 is to be divided to make it a perfect cube is ....... ", "a": "$1024 = 2^{10}$. Needs to be divided by $2^1$ = <b>2</b>."}
        ]
    },
    {
        "q": "8. Identify the false statements only.",
        "subs": [
            {"q": "(i) The cube of an odd number is odd.", "a": "True"},
            {"q": "(ii) The cube of an even number is even.", "a": "True"},
            {"q": "(iii) The cube of a negative number is positive.", "a": "<b>False</b> (It is negative)"},
            {"q": "(iv) The cube roots of 27 are 3 and -3.", "a": "<b>False</b> (The only real cube root is 3)"},
            {"q": "(v) 333 is a perfect cube.", "a": "<b>False</b> (7^3 = 343)"},
            {"q": "(vi) $\\sqrt[3]{27+8} = \\sqrt[3]{27} + \\sqrt[3]{8}$.", "a": "<b>False</b> ($\\sqrt[3]{35} \\neq 3 + 2$)"},
            {"q": "(vii) There is no cube root of a negative number.", "a": "<b>False</b> (e.g., $\\sqrt[3]{-8} = -2$)"}
        ]
    }
]

chapters = [
    {"id": "ch1", "title": "Chapter 1: Rational Numbers", "data": questions_ch1},
    {"id": "ch3", "title": "Chapter 3: Squares and Square Roots", "data": questions_ch3},
    {"id": "ch4", "title": "Chapter 4: Cubes and Cube Roots", "data": questions_ch4}
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 8 Maths Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Georgia&display=swap" rel="stylesheet">
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0;
            padding: 0;
            background-color: #f4f6f9;
            font-family: 'Georgia', serif;
            color: #333;
            line-height: 1.6;
            transition: background-color 0.3s, color 0.3s;
        }
        
        .container {
            background: #fff;
            width: 100%;
            max-width: 900px;
            min-height: 100vh;
            margin: 0 auto;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            padding: 40px 60px;
            position: relative;
            transition: background-color 0.3s, color 0.3s;
        }
        
        .header {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 30px;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 15px;
        }
        
        /* Dark Mode Styles */
        body.dark-mode {
            background-color: #1a1a1a;
            color: #f4f4f4;
        }
        body.dark-mode .container {
            background-color: #2d2d2d;
            box-shadow: none;
            border: 1px solid #444;
        }
        body.dark-mode .header {
            color: #66b3ff;
            border-bottom: 2px solid #66b3ff;
        }
        body.dark-mode .question, body.dark-mode .pres-q {
            color: #e0e0e0;
        }
        body.dark-mode .sub-q {
            color: #cccccc;
        }
        body.dark-mode .solution {
            background-color: #3a3a3a;
            border-left: 4px solid #66b3ff;
            color: #b3d4ff;
        }
        body.dark-mode .sol-label {
            color: #ff6666;
        }
        body.dark-mode .teach-view li.main-q-li {
            color: #e0e0e0;
        }
        body.dark-mode .teach-view li.clickable-q {
            background: #333;
            border-left: 4px solid #66b3ff;
            color: #ddd;
        }
        body.dark-mode .teach-view li.clickable-q:hover {
            background: #444;
        }
        body.dark-mode .pres-step {
            color: #b3d4ff;
        }

        /* Home view */
        .home-btn {
            display: block;
            width: 80%;
            margin: 20px auto;
            padding: 20px;
            background-color: #3498db;
            color: white;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .home-btn:hover {
            background-color: #2980b9;
            transform: translateY(-2px);
        }

        .q-block {
            margin-bottom: 40px;
            border-bottom: 1px dashed #eee;
            padding-bottom: 20px;
        }
        .question {
            color: #2c3e50;
            font-weight: bold;
            font-size: 20px;
            margin-bottom: 10px;
        }
        .sub-q {
            color: #34495e;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .solution {
            color: #1a5276;
            margin-top: 10px;
            margin-left: 20px;
            background-color: #fcfcfc;
            padding: 15px;
            border-left: 4px solid #3498db;
            border-radius: 4px;
        }
        .sol-label {
            font-weight: bold;
            color: #e74c3c;
            margin-right: 5px;
        }
        mjx-container {
            font-size: 1.1em;
        }
        
        /* Teach Mode Buttons */
        .btn-teach {
            display: block;
            width: 250px;
            margin: 0 auto 40px auto;
            padding: 15px 20px;
            background-color: #e74c3c;
            color: white;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .btn-teach:hover {
            background-color: #c0392b;
            transform: translateY(-2px);
        }
        .btn-top-back {
            display: inline-block;
            background: #7f8c8d;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .btn-close {
            position: absolute;
            top: 15px;
            right: 15px;
            background: #e74c3c;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            font-size: 14px;
            z-index: 100;
        }
        
        /* Teach View List */
        .teach-view ul {
            list-style: none;
            padding: 0;
        }
        .teach-view li.main-q-li {
            font-size: 22px;
            font-weight: bold;
            margin-top: 25px;
            color: #2c3e50;
        }
        .teach-view li.clickable-q {
            font-size: 20px;
            margin: 15px 0 15px 30px;
            padding: 15px;
            background: #ecf0f1;
            border-left: 4px solid #2980b9;
            cursor: pointer;
            border-radius: 4px;
            transition: 0.2s;
        }
        .teach-view li.clickable-q:hover {
            background: #d4e6f1;
            transform: translateX(5px);
        }
        
        /* Presentation View */
        #presentation-view {
            text-align: center;
            font-size: 28px;
            cursor: pointer;
            min-height: 100vh;
            user-select: none;
        }
        .pres-q {
            font-size: 34px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #3498db;
        }
        .pres-step {
            opacity: 0;
            margin-bottom: 20px;
            color: #1a5276;
            transition: opacity 0.4s ease-in-out;
        }
        
        /* Tools Floating Panel */
        .tools-panel {
            position: fixed;
            right: 20px;
            bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 1000;
        }
        .tools-panel button {
            width: 45px;
            height: 45px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 50%;
            border: none;
            background-color: #2c3e50;
            color: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            cursor: pointer;
            transition: 0.2s;
        }
        .tools-panel button:active {
            transform: scale(0.9);
        }

        /* Mobile Optimization */
        @media (max-width: 768px) {
            body { padding: 0 !important; }
            .container { padding: 15px !important; border-radius: 0 !important; box-shadow: none !important; border: none !important; min-height: 100vh; }
            .header { font-size: 24px; margin-bottom: 20px; }
            .question { font-size: 17px; }
            .sub-q { font-size: 16px; margin-top: 15px; }
            .solution { padding: 10px; margin-left: 0; }
            .btn-teach, .home-btn { width: 100%; font-size: 18px; margin: 20px 0; }
            .teach-view li.main-q-li { font-size: 18px; margin-top: 15px; }
            .teach-view li.clickable-q { font-size: 16px; margin: 10px 0; padding: 10px; }
            .pres-q { font-size: 22px; margin-bottom: 20px; padding-bottom: 10px; }
            #presentation-view { font-size: 20px; }
            .btn-close { padding: 5px 10px; font-size: 12px; top: 10px; right: 10px; }
        }
    </style>
</head>
<body>
    <div class="tools-panel">
        <button onclick="toggleDarkMode()" title="Dark Mode">🌙</button>
        <button onclick="zoomIn()" title="Zoom In">+</button>
        <button onclick="zoomOut()" title="Zoom Out">-</button>
    </div>
    
    <script>
        let currentZoom = 1;
        function zoomIn() {
            currentZoom += 0.1;
            document.body.style.zoom = currentZoom;
        }
        function zoomOut() {
            if (currentZoom > 0.5) {
                currentZoom -= 0.1;
                document.body.style.zoom = currentZoom;
            }
        }
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
        }
    </script>

    <!-- HOME VIEW -->
    <div class="container" id="home-view">
        <div class="header">Class 8 Mathematics Solutions</div>
"""

for ch in chapters:
    html_template += f'        <button class="home-btn" onclick="openChapter(\'{ch["id"]}\')">{ch["title"]}</button>\n'

html_template += """
    </div>
"""

# Build each chapter's normal view and teach view
presentation_html = ""
pres_id_counter = 0

chapter_pres_map = {}

for ch in chapters:
    chapter_pres_map[ch["id"]] = []
    
    # NORMAL VIEW
    html_template += f'    <div class="container chapter-view" id="normal-view-{ch["id"]}" style="display: none;">\n'
    html_template += f'        <button class="btn-top-back" onclick="goHome()">⬅ Back to Home</button>\n'
    html_template += f'        <div class="header">{ch["title"]}</div>\n'
    html_template += f'        <button class="btn-teach" onclick="enterTeachMode(\'{ch["id"]}\')">👨‍🏫 Teach Mode</button>\n'
    
    for item in ch["data"]:
        html_template += f'        <div class="q-block">\n'
        html_template += f'            <div class="question">{item["q"]}</div>\n'
        for sub in item["subs"]:
            if sub["q"]:
                html_template += f'            <div class="sub-q">{sub["q"]}</div>\n'
            html_template += f'            <div class="solution"><span class="sol-label">Solution:</span><br>{sub["a"]}</div>\n'
        html_template += f'        </div>\n'
    html_template += f'    </div>\n'

    # TEACH VIEW
    html_template += f'    <div class="container teach-view" id="teach-view-{ch["id"]}" style="display: none;">\n'
    html_template += f'        <button class="btn-close" onclick="exitTeachMode(\'{ch["id"]}\')">X Exit Teach</button>\n'
    html_template += f'        <div class="header">Teach Mode - {ch["title"]}</div>\n'
    html_template += f'        <ul>\n'
    
    for item in ch["data"]:
        html_template += f'            <li class="main-q-li">{item["q"]}</li>\n'
        for sub in item["subs"]:
            pres_id = f'pres-{pres_id_counter}'
            chapter_pres_map[ch["id"]].append(pres_id)
            pres_id_counter += 1
            
            display_text = sub["q"] if sub["q"] else "Solution"
            html_template += f'            <li class="clickable-q" onclick="startPresentation(\'{pres_id}\', \'{ch["id"]}\')">{display_text}</li>\n'
            
            presentation_html += f'        <div id="{pres_id}" class="pres-container" style="display:none;">\n'
            presentation_html += f'            <div class="pres-q">{item["q"]}<br>{sub["q"]}</div>\n'
            
            steps = sub["a"].split("<br>")
            for step in steps:
                presentation_html += f'            <div class="pres-step">{step.strip()}</div>\n'
                
            presentation_html += f'        </div>\n'
    
    html_template += f'        </ul>\n'
    html_template += f'    </div>\n'

html_template += """
    <!-- PRESENTATION VIEW -->
    <div class="container" id="presentation-view" style="display: none;">
        <button class="btn-close" onclick="closePresentation()">X Close</button>
"""

html_template += presentation_html

html_template += f"""
    </div>

    <script>
        const chapterPresMap = {json.dumps(chapter_pres_map)};
        
        let currentSteps = [];
        let currentStepIndex = -1;
        let savedNormalScroll = {{}};
        let savedTeachScroll = {{}};
        let activeTeachCh = null;
        let activePresId = null;

        function openChapter(chId) {{
            document.getElementById('home-view').style.display = 'none';
            document.getElementById('normal-view-' + chId).style.display = 'block';
            window.scrollTo(0, 0);
        }}

        function goHome() {{
            const views = document.querySelectorAll('.chapter-view');
            views.forEach(v => v.style.display = 'none');
            document.getElementById('home-view').style.display = 'block';
            window.scrollTo(0, 0);
        }}

        function enterTeachMode(chId) {{
            savedNormalScroll[chId] = window.scrollY;
            document.getElementById('normal-view-' + chId).style.display = 'none';
            document.getElementById('teach-view-' + chId).style.display = 'block';
            window.scrollTo(0, 0);
        }}

        function exitTeachMode(chId) {{
            document.getElementById('teach-view-' + chId).style.display = 'none';
            document.getElementById('normal-view-' + chId).style.display = 'block';
            window.scrollTo(0, savedNormalScroll[chId] || 0);
        }}

        function startPresentation(id, chId) {{
            activeTeachCh = chId;
            activePresId = id;
            savedTeachScroll[chId] = window.scrollY;
            
            document.getElementById('teach-view-' + chId).style.display = 'none';
            document.getElementById('presentation-view').style.display = 'block';
            
            const containers = document.querySelectorAll('.pres-container');
            containers.forEach(c => c.style.display = 'none');
            
            const target = document.getElementById(id);
            target.style.display = 'block';
            
            currentSteps = target.querySelectorAll('.pres-step');
            currentSteps.forEach(step => {{
                step.style.opacity = '0';
            }});
            
            currentStepIndex = -1;
            window.scrollTo(0, 0);
        }}

        function closePresentation() {{
            if (!activeTeachCh) return;
            document.getElementById('presentation-view').style.display = 'none';
            document.getElementById('teach-view-' + activeTeachCh).style.display = 'block';
            window.scrollTo(0, savedTeachScroll[activeTeachCh] || 0);
        }}
        
        function nextQuestion() {{
            const list = chapterPresMap[activeTeachCh];
            const idx = list.indexOf(activePresId);
            if (idx < list.length - 1) {{
                startPresentation(list[idx + 1], activeTeachCh);
            }}
        }}
        
        function prevQuestion() {{
            const list = chapterPresMap[activeTeachCh];
            const idx = list.indexOf(activePresId);
            if (idx > 0) {{
                startPresentation(list[idx - 1], activeTeachCh);
            }}
        }}

        const presView = document.getElementById('presentation-view');
        
        presView.addEventListener('click', (e) => {{
            if (e.target.tagName.toLowerCase() === 'button') return;
            nextStep();
        }});

        presView.addEventListener('contextmenu', (e) => {{
            e.preventDefault();
            prevStep();
        }});

        function nextStep() {{
            if (currentStepIndex < currentSteps.length - 1) {{
                currentStepIndex++;
                currentSteps[currentStepIndex].style.opacity = '1';
            }}
        }}

        function prevStep() {{
            if (currentStepIndex >= 0) {{
                currentSteps[currentStepIndex].style.opacity = '0';
                currentStepIndex--;
            }}
        }}
        
        // Scroll to change questions
        let wheelTimeout;
        presView.addEventListener('wheel', (e) => {{
            // Prevent multiple triggers
            if (wheelTimeout) return;
            wheelTimeout = setTimeout(() => {{ wheelTimeout = null; }}, 800);
            
            if (e.deltaY > 50) {{
                nextQuestion();
            }} else if (e.deltaY < -50) {{
                prevQuestion();
            }}
        }});
        
        let touchStartY = 0;
        let touchEndY = 0;
        
        presView.addEventListener('touchstart', e => {{
            touchStartY = e.changedTouches[0].screenY;
        }}, {{passive: true}});
        
        presView.addEventListener('touchend', e => {{
            touchEndY = e.changedTouches[0].screenY;
            handleSwipe();
        }}, {{passive: true}});
        
        function handleSwipe() {{
            // swipe up -> next question
            if (touchStartY - touchEndY > 100) {{
                nextQuestion();
            }}
            // swipe down -> prev question
            else if (touchEndY - touchStartY > 100) {{
                prevQuestion();
            }}
        }}

        document.addEventListener('keydown', (e) => {{
            if (document.getElementById('presentation-view').style.display === 'block') {{
                if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {{
                    e.preventDefault();
                    nextStep();
                }} else if (e.key === 'ArrowLeft') {{
                    e.preventDefault();
                    prevStep();
                }} else if (e.key === 'ArrowDown') {{
                    e.preventDefault();
                    nextQuestion();
                }} else if (e.key === 'ArrowUp') {{
                    e.preventDefault();
                    prevQuestion();
                }} else if (e.key === 'Escape') {{
                    closePresentation();
                }}
            }}
        }});
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
