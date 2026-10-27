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
            {"q": "(i) $\\frac{3}{7} \\times \\frac{4}{5}$", "a": "$= \\frac{3 \\times 4}{7 \\times 5} =$ <b>$\\frac{12}{35}$</b>"},
            {"q": "(ii) $\\frac{-4}{9} \\times \\frac{10}{7}$", "a": "$= \\frac{-4 \\times 10}{9 \\times 7} =$ <b>$\\frac{-40}{63}$</b>"},
            {"q": "(iii) $\\frac{-1}{2} \\times \\frac{-9}{8}$", "a": "$= \\frac{-1 \\times -9}{2 \\times 8} =$ <b>$\\frac{9}{16}$</b>"},
            {"q": "(iv) $\\frac{-3}{4} \\times \\frac{8}{-15}$", "a": "$= \\frac{-3 \\times 8}{4 \\times -15} = \\frac{-24}{-60}$<br>Dividing numerator and denominator by $-12$, we get:<br>$=$ <b>$\\frac{2}{5}$</b>"},
            {"q": "(v) $\\frac{21}{-2} \\times \\frac{-4}{7}$", "a": "$= \\frac{21 \\times -4}{-2 \\times 7} = \\frac{-84}{-14}$<br>Dividing numerator and denominator by $-14$, we get:<br>$=$ <b>$6$</b>"},
            {"q": "(vi) $\\frac{-7}{10} \\times \\frac{6}{-35}$", "a": "$= \\frac{-7 \\times 6}{10 \\times -35} = \\frac{-42}{-350}$<br>Dividing numerator and denominator by $-14$, we get:<br>$=$ <b>$\\frac{3}{25}$</b>"},
            {"q": "(vii) $\\frac{-14}{15} \\times \\frac{-25}{42}$", "a": "Cancelling out common factors (14 and 42 by 14; 15 and 25 by 5):<br>$= \\frac{-1}{3} \\times \\frac{-5}{3} = \\frac{(-1) \\times (-5)}{3 \\times 3} =$ <b>$\\frac{5}{9}$</b>"},
            {"q": "(viii) $\\frac{-35}{-18} \\times \\frac{8}{-15}$", "a": "$\\frac{-35}{-18} = \\frac{35}{18}$<br>$= \\frac{35}{18} \\times \\frac{8}{-15}$<br>Cancelling 35 and 15 by 5; 18 and 8 by 2:<br>$= \\frac{7}{9} \\times \\frac{4}{-3} =$ <b>$\\frac{-28}{27}$</b>"},
            {"q": "(ix) $\\frac{-7}{11} \\times 22$", "a": "$= \\frac{-7 \\times 22}{11}$<br>Cancelling 22 and 11 by 11:<br>$= -7 \\times 2 =$ <b>$-14$</b>"},
            {"q": "(x) $\\frac{14}{25} \\times (-100)$", "a": "$= \\frac{14 \\times -100}{25}$<br>Cancelling 100 and 25 by 25:<br>$= 14 \\times -4 =$ <b>$-56$</b>"},
            {"q": "(xi) $\\frac{-13}{-12} \\times (-3)$", "a": "$\\frac{-13}{-12} = \\frac{13}{12}$<br>$= \\frac{13}{12} \\times (-3)$<br>Cancelling 12 and 3 by 3:<br>$= \\frac{13}{4} \\times (-1) =$ <b>$\\frac{-13}{4}$</b>"},
            {"q": "(xii) $\\frac{-12}{85} \\times (-17)$", "a": "$= \\frac{-12 \\times -17}{85}$<br>Cancelling 85 and 17 by 17:<br>$= \\frac{12}{5}$<br>$=$ <b>$\\frac{12}{5}$</b>"}
        ]
    },
    {
        "q": "2. Verify the commutative law of multiplication for the following pairs of rational numbers.",
        "subs": [
            {"q": "(i) $\\frac{2}{3}$ and $\\frac{-7}{5}$", "a": "<b>LHS:</b> $\\frac{2}{3} \\times \\frac{-7}{5} = \\frac{-14}{15}$<br><b>RHS:</b> $\\frac{-7}{5} \\times \\frac{2}{3} = \\frac{-14}{15}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(ii) $\\frac{-1}{7}$ and $\\frac{14}{3}$", "a": "<b>LHS:</b> $\\frac{-1}{7} \\times \\frac{14}{3} = \\frac{-14}{21} = \\frac{-2}{3}$<br><b>RHS:</b> $\\frac{14}{3} \\times \\frac{-1}{7} = \\frac{-14}{21} = \\frac{-2}{3}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(iii) $\\frac{3}{-8}$ and $\\frac{-16}{15}$", "a": "<b>LHS:</b> $\\frac{3}{-8} \\times \\frac{-16}{15} = \\frac{-48}{-120} = \\frac{2}{5}$<br><b>RHS:</b> $\\frac{-16}{15} \\times \\frac{3}{-8} = \\frac{-48}{-120} = \\frac{2}{5}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(iv) $\\frac{11}{13}$ and $\\frac{-26}{-55}$", "a": "$\\frac{-26}{-55} = \\frac{26}{55}$<br><b>LHS:</b> $\\frac{11}{13} \\times \\frac{26}{55} = \\frac{1 \\times 2}{1 \\times 5} = \\frac{2}{5}$<br><b>RHS:</b> $\\frac{26}{55} \\times \\frac{11}{13} = \\frac{2 \\times 1}{5 \\times 1} = \\frac{2}{5}$<br>Since LHS = RHS, the law is verified."}
        ]
    },
    {
        "q": "3. Verify the associative law of multiplication for the following groups of rational numbers.",
        "subs": [
            {"q": "(i) $\\frac{2}{3}, \\frac{-1}{5}$ and $\\frac{7}{12}$", "a": "<b>LHS:</b> $\\left(\\frac{2}{3} \\times \\frac{-1}{5}\\right) \\times \\frac{7}{12} = \\frac{-2}{15} \\times \\frac{7}{12} = \\frac{-14}{180} = \\frac{-7}{90}$<br><b>RHS:</b> $\\frac{2}{3} \\times \\left(\\frac{-1}{5} \\times \\frac{7}{12}\\right) = \\frac{2}{3} \\times \\frac{-7}{60} = \\frac{-14}{180} = \\frac{-7}{90}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(ii) $\\frac{-5}{7}, \\frac{1}{2}$ and $\\frac{-21}{20}$", "a": "<b>LHS:</b> $\\left(\\frac{-5}{7} \\times \\frac{1}{2}\\right) \\times \\frac{-21}{20} = \\frac{-5}{14} \\times \\frac{-21}{20} = \\frac{105}{280} = \\frac{3}{8}$<br><b>RHS:</b> $\\frac{-5}{7} \\times \\left(\\frac{1}{2} \\times \\frac{-21}{20}\\right) = \\frac{-5}{7} \\times \\frac{-21}{40} = \\frac{105}{280} = \\frac{3}{8}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(iii) $\\frac{-8}{9}, \\frac{-3}{4}$ and $\\frac{15}{16}$", "a": "<b>LHS:</b> $\\left(\\frac{-8}{9} \\times \\frac{-3}{4}\\right) \\times \\frac{15}{16} = \\frac{24}{36} \\times \\frac{15}{16} = \\frac{2}{3} \\times \\frac{15}{16} = \\frac{30}{48} = \\frac{5}{8}$<br><b>RHS:</b> $\\frac{-8}{9} \\times \\left(\\frac{-3}{4} \\times \\frac{15}{16}\\right) = \\frac{-8}{9} \\times \\frac{-45}{64} = \\frac{360}{576} = \\frac{5}{8}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(iv) $\\frac{-3}{11}, \\frac{-7}{4}$ and $\\frac{-1}{2}$", "a": "<b>LHS:</b> $\\left(\\frac{-3}{11} \\times \\frac{-7}{4}\\right) \\times \\frac{-1}{2} = \\frac{21}{44} \\times \\frac{-1}{2} = \\frac{-21}{88}$<br><b>RHS:</b> $\\frac{-3}{11} \\times \\left(\\frac{-7}{4} \\times \\frac{-1}{2}\\right) = \\frac{-3}{11} \\times \\frac{7}{8} = \\frac{-21}{88}$<br>Since LHS = RHS, the law is verified."}
        ]
    },
    {
        "q": "4. Find the multiplicative inverse of each of the following.",
        "subs": [
            {"q": "(i) $1$", "a": "The multiplicative inverse is <b>$1$</b>."},
            {"q": "(ii) $-1$", "a": "The multiplicative inverse is <b>$-1$</b>."},
            {"q": "(iii) $\\frac{3}{4}$", "a": "The multiplicative inverse is <b>$\\frac{4}{3}$</b>."},
            {"q": "(iv) $\\frac{5}{-7}$", "a": "$\\frac{5}{-7} = \\frac{-5}{7}$<br>The multiplicative inverse is <b>$\\frac{-7}{5}$</b>."},
            {"q": "(v) $\\frac{-11}{-13}$", "a": "$\\frac{-11}{-13} = \\frac{11}{13}$<br>The multiplicative inverse is <b>$\\frac{13}{11}$</b>."},
            {"q": "(vi) $\\frac{-7}{17}$", "a": "The multiplicative inverse is <b>$\\frac{-17}{7}$</b>."},
            {"q": "(vii) $3 \\frac{1}{4}$", "a": "$3 \\frac{1}{4} = \\frac{13}{4}$<br>The multiplicative inverse is <b>$\\frac{4}{13}$</b>."},
            {"q": "(viii) $\\frac{-26}{5}$", "a": "The multiplicative inverse is <b>$\\frac{-5}{26}$</b>."},
            {"q": "(ix) $\\frac{3}{-4} \\times \\frac{-8}{9}$", "a": "$\\frac{3}{-4} \\times \\frac{-8}{9} = \\frac{-24}{-36} = \\frac{2}{3}$<br>The multiplicative inverse of $\\frac{2}{3}$ is <b>$\\frac{3}{2}$</b>."},
            {"q": "(x) $\\frac{5}{13} \\times \\frac{-26}{-35}$", "a": "$\\frac{5}{13} \\times \\frac{26}{35} = \\frac{130}{455} = \\frac{2}{7}$<br>The multiplicative inverse of $\\frac{2}{7}$ is <b>$\\frac{7}{2}$</b>."},
            {"q": "(xi) $\\frac{-13}{-14} \\times \\frac{70}{-39}$", "a": "$\\frac{13}{14} \\times \\frac{-70}{39} = \\frac{-910}{546} = \\frac{-5}{3}$<br>The multiplicative inverse of $\\frac{-5}{3}$ is <b>$\\frac{-3}{5}$</b>."},
            {"q": "(xii) $3 \\frac{1}{3} \\times 1 \\frac{1}{2}$", "a": "$3 \\frac{1}{3} = \\frac{10}{3}$ and $1 \\frac{1}{2} = \\frac{3}{2}$<br>$\\frac{10}{3} \\times \\frac{3}{2} = \\frac{30}{6} = 5$<br>The multiplicative inverse of $5$ is <b>$\\frac{1}{5}$</b>."}
        ]
    },
    {
        "q": "5. Verify each of the following.",
        "subs": [
            {"q": "(i) $\\frac{3}{5} \\times \\left(\\frac{7}{12} + \\frac{1}{2}\\right) = \\frac{3}{5} \\times \\frac{7}{12} + \\frac{3}{5} \\times \\frac{1}{2}$", "a": "<b>LHS:</b> $\\frac{3}{5} \\times \\left(\\frac{7+6}{12}\\right) = \\frac{3}{5} \\times \\frac{13}{12} = \\frac{39}{60} = \\frac{13}{20}$<br><b>RHS:</b> $\\frac{21}{60} + \\frac{3}{10} = \\frac{21}{60} + \\frac{18}{60} = \\frac{39}{60} = \\frac{13}{20}$<br>LHS = RHS. (Verified)"},
            {"q": "(ii) $\\frac{-2}{3} \\times \\left(\\frac{-5}{4} + \\frac{4}{7}\\right) = \\frac{-2}{3} \\times \\frac{-5}{4} + \\frac{-2}{3} \\times \\frac{4}{7}$", "a": "<b>LHS:</b> $\\frac{-2}{3} \\times \\left(\\frac{-35+16}{28}\\right) = \\frac{-2}{3} \\times \\frac{-19}{28} = \\frac{38}{84} = \\frac{19}{42}$<br><b>RHS:</b> $\\frac{10}{12} + \\frac{-8}{21} = \\frac{5}{6} - \\frac{8}{21} = \\frac{35-16}{42} = \\frac{19}{42}$<br>LHS = RHS. (Verified)"},
            {"q": "(iii) $\\frac{8}{11} \\times \\left(\\frac{-3}{2} - \\frac{1}{5}\\right) = \\frac{8}{11} \\times \\frac{-3}{2} - \\frac{8}{11} \\times \\frac{1}{5}$", "a": "<b>LHS:</b> $\\frac{8}{11} \\times \\left(\\frac{-15-2}{10}\\right) = \\frac{8}{11} \\times \\frac{-17}{10} = \\frac{-136}{110} = \\frac{-68}{55}$<br><b>RHS:</b> $\\frac{-24}{22} - \\frac{8}{55} = \\frac{-12}{11} - \\frac{8}{55} = \\frac{-60-8}{55} = \\frac{-68}{55}$<br>LHS = RHS. (Verified)"},
            {"q": "(iv) $\\frac{-3}{2} \\times \\left(\\frac{-5}{7} + \\frac{-5}{2}\\right) = \\frac{-3}{2} \\times \\frac{-5}{7} + \\frac{-3}{2} \\times \\frac{-5}{2}$", "a": "<b>LHS:</b> $\\frac{-3}{2} \\times \\left(\\frac{-10-35}{14}\\right) = \\frac{-3}{2} \\times \\frac{-45}{14} = \\frac{135}{28}$<br><b>RHS:</b> $\\frac{15}{14} + \\frac{15}{4} = \\frac{30+105}{28} = \\frac{135}{28}$<br>LHS = RHS. (Verified)"},
            {"q": "(v) $\\left(\\frac{7}{5} + \\frac{3}{2}\\right) \\times \\frac{2}{3} = \\frac{7}{5} \\times \\frac{2}{3} + \\frac{3}{2} \\times \\frac{2}{3}$", "a": "<b>LHS:</b> $\\left(\\frac{14+15}{10}\\right) \\times \\frac{2}{3} = \\frac{29}{10} \\times \\frac{2}{3} = \\frac{58}{30} = \\frac{29}{15}$<br><b>RHS:</b> $\\frac{14}{15} + \\frac{6}{6} = \\frac{14}{15} + 1 = \\frac{14+15}{15} = \\frac{29}{15}$<br>LHS = RHS. (Verified)"}
        ]
    },
    {
        "q": "6. Using the distributive property, find the value of each of the following.",
        "subs": [
            {"q": "(i) $\\frac{3}{5} \\times \\frac{-20}{9} + \\frac{3}{5} \\times \\frac{-1}{3}$", "a": "Using distributive law, $a \\times b + a \\times c = a \\times (b + c)$<br>$= \\frac{3}{5} \\times \\left(\\frac{-20}{9} + \\frac{-1}{3}\\right) = \\frac{3}{5} \\times \\left(\\frac{-20 - 3}{9}\\right)$<br>$= \\frac{3}{5} \\times \\frac{-23}{9} =$ <b>$\\frac{-23}{15}$</b>"},
            {"q": "(ii) $\\frac{7}{15} \\times \\frac{-50}{49} + \\frac{7}{15} \\times \\frac{1}{49}$", "a": "$= \\frac{7}{15} \\times \\left(\\frac{-50}{49} + \\frac{1}{49}\\right) = \\frac{7}{15} \\times \\left(\\frac{-49}{49}\\right)$<br>$= \\frac{7}{15} \\times (-1) =$ <b>$\\frac{-7}{15}$</b>"},
            {"q": "(iii) $\\left(\\frac{-13}{5} \\times \\frac{16}{7}\\right) + \\left(\\frac{-13}{5} \\times \\frac{19}{7}\\right)$", "a": "$= \\frac{-13}{5} \\times \\left(\\frac{16}{7} + \\frac{19}{7}\\right) = \\frac{-13}{5} \\times \\left(\\frac{35}{7}\\right)$<br>$= \\frac{-13}{5} \\times 5 =$ <b>$-13$</b>"},
            {"q": "(iv) $\\left(\\frac{-1}{3} \\times \\frac{-3}{5}\\right) + \\left(\\frac{-1}{3} \\times \\frac{7}{11}\\right)$", "a": "$= \\frac{-1}{3} \\times \\left(\\frac{-3}{5} + \\frac{7}{11}\\right) = \\frac{-1}{3} \\times \\left(\\frac{-33 + 35}{55}\\right)$<br>$= \\frac{-1}{3} \\times \\frac{2}{55} =$ <b>$\\frac{-2}{165}$</b>"},
            {"q": "(v) $\\left(\\frac{2}{3} \\times \\frac{9}{10}\\right) + \\left(\\frac{2}{3} \\times \\frac{-4}{10}\\right)$", "a": "$= \\frac{2}{3} \\times \\left(\\frac{9}{10} + \\frac{-4}{10}\\right) = \\frac{2}{3} \\times \\left(\\frac{5}{10}\\right)$<br>$= \\frac{2}{3} \\times \\frac{1}{2} =$ <b>$\\frac{1}{3}$</b>"}
        ]
    },
    {
        "q": "7. Fill in the blanks.",
        "subs": [
            {"q": "(i) $\\frac{-7}{17} \\times \\frac{27}{35} = \\frac{27}{35} \\times \\dots\\dots$", "a": "<b>$\\frac{-7}{17}$</b>"},
            {"q": "(ii) $\\frac{3}{29} \\times \\left(\\frac{-7}{31} \\times \\frac{-9}{35}\\right) = \\left(\\frac{3}{29} \\times \\dots\\dots\\right) \\times \\frac{-9}{35}$", "a": "<b>$\\frac{-7}{31}$</b>"},
            {"q": "(iii) $\\frac{-11}{13} \\times \\left(\\frac{17}{47} \\times \\frac{-3}{5}\\right) = \\left(\\frac{-11}{13} \\times \\frac{17}{47}\\right) \\times \\dots\\dots$", "a": "<b>$\\frac{-3}{5}$</b>"},
            {"q": "(iv) $\\frac{3}{5} \\times \\left(\\frac{-7}{27} + \\frac{49}{\\dots\\dots}\\right) = \\frac{3}{5} \\times \\frac{-7}{27} + \\frac{3}{5} \\times \\frac{49}{23}$", "a": "<b>$23$</b>"},
            {"q": "(v) $\\frac{13}{15} \\times \\left(\\frac{-3}{2} + \\dots\\dots\\right) = \\frac{13}{15} \\times \\frac{-3}{2} + \\frac{13}{15} \\times \\frac{-5}{6}$", "a": "<b>$\\frac{-5}{6}$</b>"},
            {"q": "(vi) $\\dots\\dots \\times \\left(\\frac{7}{3} + \\frac{-5}{11}\\right) = \\frac{2}{3} \\times \\frac{7}{3} + \\frac{2}{3} \\times \\frac{-5}{11}$", "a": "<b>$\\frac{2}{3}$</b>"},
            {"q": "(vii) The reciprocal of $\\frac{2}{3}$ is $\\dots\\dots$", "a": "<b>$\\frac{3}{2}$</b>"},
            {"q": "(viii) $\\left(\\frac{7}{8}\\right)^{-1} = \\dots\\dots$", "a": "<b>$\\frac{8}{7}$</b>"},
            {"q": "(ix) The reciprocal of $-1$ is $\\dots\\dots$", "a": "<b>$-1$</b>"},
            {"q": "(x) $-2$ is the reciprocal of $\\dots\\dots$", "a": "<b>$\\frac{-1}{2}$</b>"},
            {"q": "(xi) The product of a nonzero rational number and its reciprocal is $\\dots\\dots$", "a": "<b>$1$</b>"},
            {"q": "(xii) The reciprocal of a positive rational number is $\\dots\\dots$", "a": "<b>a positive rational number</b>"},
            {"q": "(xiii) The reciprocal of a negative rational number is $\\dots\\dots$", "a": "<b>a negative rational number</b>"},
            {"q": "(xiv) $\\dots\\dots$ is the only rational number whose reciprocal is not defined.", "a": "<b>$0$</b>"}
        ]
    },
    {
        "q": "8. Identify the false statements only.",
        "subs": [
            {"q": "(i) The product of two rational numbers is not necessarily a rational number.", "a": "<b>False</b>"},
            {"q": "(ii) Multiplication of rational numbers obeys the commutative property.", "a": "<b>True</b>"},
            {"q": "(iii) Multiplication of rational numbers obeys the associative property.", "a": "<b>True</b>"},
            {"q": "(iv) Zero is the multiplicative identity for rational numbers.", "a": "<b>False</b> (1 is the multiplicative identity)."},
            {"q": "(v) The product of a rational number and its multiplicative inverse is 1.", "a": "<b>True</b>"},
            {"q": "(vi) If $\\frac{a}{b}$ is a rational number then $\\frac{b}{a} = \\left(\\frac{a}{b}\\right)^{-1}$.", "a": "<b>True</b>"},
            {"q": "(vii) The reciprocal of $\\frac{5}{-6}$ is $\\frac{-5}{6}$.", "a": "<b>False</b> (The reciprocal is $\\frac{-6}{5}$)."},
            {"q": "(viii) Zero has no reciprocal.", "a": "<b>True</b>"},
            {"q": "<b>Answer to Q8:</b> Identify the false statements only.", "a": "The false statements are <b>(i), (iv), and (vii)</b>."}
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

questions_ch5 = [
    {
        "q": "Exercise 5B",
        "subs": []
    },
    {
        "q": "1. Six more than four times a number is four less than five times the number. Find the number.",
        "subs": [
            {
                "q": "",
                "a": "Let the required number be $x$.<br>Four times the number = $4x$<br>Six more than four times the number = $4x + 6$<br>Five times the number = $5x$<br>Four less than five times the number = $5x - 4$<br>According to the given condition:<br>$$4x + 6 = 5x - 4$$<br>Transposing $4x$ to the RHS and $-4$ to the LHS:<br>$$6 + 4 = 5x - 4x$$<br>$$10 = x \\implies x = 10$$<br>Therefore, the required number is <b>10</b>."
            }
        ]
    },
    {
        "q": "2. Consecutive numbers problems.",
        "subs": [
            {
                "q": "(i) The difference between the squares of two consecutive numbers is 141. Find the numbers.",
                "a": "Let the two consecutive numbers be $x$ and $x + 1$.<br>According to the given condition:<br>$$(x + 1)^2 - x^2 = 141$$<br>Expanding $(x + 1)^2$:<br>$$x^2 + 2x + 1 - x^2 = 141$$<br>$$2x + 1 = 141$$<br>$$2x = 141 - 1 = 140$$<br>$$x = \\frac{140}{2} = 70$$<br>The numbers are $x = 70$ and $x + 1 = 70 + 1 = 71$.<br>Therefore, the required numbers are <b>70 and 71</b>."
            },
            {
                "q": "(ii) The difference between the squares of two consecutive even numbers is 36. Find the numbers.",
                "a": "Let the two consecutive even numbers be $x$ and $x + 2$.<br>According to the given condition:<br>$$(x + 2)^2 - x^2 = 36$$<br>Expanding $(x + 2)^2$:<br>$$x^2 + 4x + 4 - x^2 = 36$$<br>$$4x + 4 = 36$$<br>$$4x = 36 - 4 = 32$$<br>$$x = \\frac{32}{4} = 8$$<br>The consecutive even numbers are $x = 8$ and $x + 2 = 8 + 2 = 10$.<br>Therefore, the required even numbers are <b>8 and 10</b>."
            },
            {
                "q": "(iii) The difference between the squares of two consecutive odd numbers is 56. Find the numbers.",
                "a": "Let the two consecutive odd numbers be $x$ and $x + 2$.<br>According to the given condition:<br>$$(x + 2)^2 - x^2 = 56$$<br>Expanding $(x + 2)^2$:<br>$$x^2 + 4x + 4 - x^2 = 56$$<br>$$4x + 4 = 56$$<br>$$4x = 56 - 4 = 52$$<br>$$x = \\frac{52}{4} = 13$$<br>The consecutive odd numbers are $x = 13$ and $x + 2 = 13 + 2 = 15$.<br>Therefore, the required odd numbers are <b>13 and 15</b>."
            }
        ]
    },
    {
        "q": "3. The sum of two numbers is 90. One third of the larger number is 9 more than twice the smaller one. What are the numbers?",
        "subs": [
            {
                "q": "",
                "a": "Let the smaller number be $x$.<br>Since the sum of both numbers is 90, the larger number is $(90 - x)$.<br>One-third of the larger number = $\\frac{1}{3}(90 - x)$<br>Twice the smaller number = $2x$<br>According to the given condition:<br>$$\\frac{1}{3}(90 - x) = 2x + 9$$<br>Multiplying both sides by 3:<br>$$90 - x = 3(2x + 9)$$<br>$$90 - x = 6x + 27$$<br>Transposing terms:<br>$$90 - 27 = 6x + x$$<br>$$63 = 7x$$<br>$$x = \\frac{63}{7} = 9$$<br>Smaller number = $9$<br>Larger number = $90 - 9 = 81$<br>Therefore, the required numbers are <b>81 and 9</b>."
            }
        ]
    },
    {
        "q": "4. Proportion and square relations.",
        "subs": [
            {
                "q": "(i) If the same number be added to the numbers 2, 4, 14 and 22 then the resultant numbers are in proportion. Find the number.",
                "a": "Let the number to be added be $x$.<br>The resultant numbers are $(2 + x), (4 + x), (14 + x)$ and $(22 + x)$.<br>Since they are in proportion:<br>$$\\frac{2 + x}{4 + x} = \\frac{14 + x}{22 + x}$$<br>By cross-multiplication:<br>$$(2 + x)(22 + x) = (4 + x)(14 + x)$$<br>$$44 + 2x + 22x + x^2 = 56 + 4x + 14x + x^2$$<br>$$x^2 + 24x + 44 = x^2 + 18x + 56$$<br>Subtracting $x^2$ from both sides:<br>$$24x + 44 = 18x + 56$$<br>$$24x - 18x = 56 - 44$$<br>$$6x = 12$$<br>$$x = \\frac{12}{6} = 2$$<br>Therefore, the required number is <b>2</b>."
            },
            {
                "q": "(ii) Find a number such that if 25, 7 and 1 are added to it, the product of the first and third results is equal to the square of the second.",
                "a": "Let the required number be $x$.<br>Adding 25, 7 and 1 gives $(x + 25), (x + 7)$ and $(x + 1)$.<br>According to the condition:<br>$$(x + 25)(x + 1) = (x + 7)^2$$<br>Expanding both sides:<br>$$x^2 + 26x + 25 = x^2 + 14x + 49$$<br>Subtracting $x^2$ from both sides:<br>$$26x + 25 = 14x + 49$$<br>$$26x - 14x = 49 - 25$$<br>$$12x = 24$$<br>$$x = \\frac{24}{12} = 2$$<br>Therefore, the required number is <b>2</b>."
            }
        ]
    },
    {
        "q": "5. Problems on fractions.",
        "subs": [
            {
                "q": "(i) What must be added to the numerator and the denominator of the fraction $\\frac{5}{12}$ to make it equal to $\\frac{2}{3}$?",
                "a": "Let the number to be added be $x$.<br>According to the problem:<br>$$\\frac{5 + x}{12 + x} = \\frac{2}{3}$$<br>By cross-multiplication:<br>$$3(5 + x) = 2(12 + x)$$<br>$$15 + 3x = 24 + 2x$$<br>$$3x - 2x = 24 - 15$$<br>$$x = 9$$<br>Therefore, the required number is <b>9</b>."
            },
            {
                "q": "(ii) The denominator of a fraction is greater than the numerator by 3. If 7 is added to the numerator, the fraction increases by unity. Find the fraction.",
                "a": "Let the numerator of the fraction be $x$.<br>Then the denominator is $x + 3$.<br>Original fraction = $\\frac{x}{x + 3}$<br>When 7 is added to the numerator, new fraction = $\\frac{x + 7}{x + 3}$<br>According to the problem, the fraction increases by 1 (unity):<br>$$\\frac{x + 7}{x + 3} - \\frac{x}{x + 3} = 1$$<br>$$\\frac{(x + 7) - x}{x + 3} = 1$$<br>$$\\frac{7}{x + 3} = 1$$<br>$$7 = x + 3 \\implies x = 7 - 3 = 4$$<br>Numerator = $4$, Denominator = $4 + 3 = 7$<br>Therefore, the required original fraction is <b>$\\frac{4}{7}$</b>."
            },
            {
                "q": "(iii) If the same integer is added to the numerator of the fraction $\\frac{2}{7}$ and subtracted from the denominator, the fraction becomes 2. What is the integer?",
                "a": "Let the integer be $x$.<br>According to the problem:<br>$$\\frac{2 + x}{7 - x} = 2$$<br>By cross-multiplication:<br>$$2 + x = 2(7 - x)$$<br>$$2 + x = 14 - 2x$$<br>$$x + 2x = 14 - 2$$<br>$$3x = 12$$<br>$$x = \\frac{12}{3} = 4$$<br>Therefore, the required integer is <b>4</b>."
            }
        ]
    },
    {
        "q": "6. In a two-digit number, the digit in the tens place is four times the digit in the units place. If the sum of the digits is 10, find the number.",
        "subs": [
            {
                "q": "",
                "a": "Let the digit in the units place be $x$.<br>Then the digit in the tens place is $4x$.<br>According to the question, the sum of the digits is 10:<br>$$x + 4x = 10$$<br>$$5x = 10$$<br>$$x = \\frac{10}{5} = 2$$<br>Digit in units place = $2$<br>Digit in tens place = $4 \\times 2 = 8$<br>Original number = $10 \\times (\\text{tens digit}) + (\\text{units digit})$<br>$$= 10(8) + 2 = 80 + 2 = 82$$<br>Therefore, the required number is <b>82</b>."
            }
        ]
    },
    {
        "q": "7. In a two-digit number, the digit in the tens place is three times the digit in the units place. If the digits are reversed, the number decreases by 36. Find the number.",
        "subs": [
            {
                "q": "",
                "a": "Let the digit in the units place be $x$.<br>Then the digit in the tens place is $3x$.<br>Original number = $10(3x) + x = 30x + x = 31x$<br>When digits are reversed, units digit becomes $3x$ and tens digit becomes $x$.<br>Reversed number = $10(x) + 3x = 13x$<br>According to the problem:<br>$$\\text{Original number} - \\text{Reversed number} = 36$$<br>$$31x - 13x = 36$$<br>$$18x = 36$$<br>$$x = \\frac{36}{18} = 2$$<br>Units digit = $2$, Tens digit = $3 \\times 2 = 6$<br>Original number = $10(6) + 2 = 62$<br>Therefore, the required number is <b>62</b>."
            }
        ]
    },
    {
        "q": "8. The sum of the digits of a two-digit number is 6. If 18 is subtracted from the number, the digits of the number are interchanged. Find the number.",
        "subs": [
            {
                "q": "",
                "a": "Let the digit in the units place be $x$.<br>Since the sum of the digits is 6, the digit in the tens place is $(6 - x)$.<br>Original number = $10(6 - x) + x = 60 - 10x + x = 60 - 9x$<br>When digits are interchanged, new units digit is $6 - x$ and tens digit is $x$.<br>New number = $10x + (6 - x) = 9x + 6$<br>According to the question:<br>$$\\text{Original number} - 18 = \\text{New number}$$<br>$$(60 - 9x) - 18 = 9x + 6$$<br>$$42 - 9x = 9x + 6$$<br>$$42 - 6 = 9x + 9x$$<br>$$36 = 18x$$<br>$$x = \\frac{36}{18} = 2$$<br>Units digit = $2$, Tens digit = $6 - 2 = 4$<br>Original number = $10(4) + 2 = 42$<br>Therefore, the required number is <b>42</b>."
            }
        ]
    },
    {
        "q": "9. Age problems.",
        "subs": [
            {
                "q": "(i) In five years from now, Shyam will be thrice as old as he was 9 years ago. Find his present age.",
                "a": "Let Shyam's present age be $x$ years.<br>In 5 years from now, his age will be $(x + 5)$ years.<br>9 years ago, his age was $(x - 9)$ years.<br>According to the given condition:<br>$$x + 5 = 3(x - 9)$$<br>$$x + 5 = 3x - 27$$<br>$$5 + 27 = 3x - x$$<br>$$32 = 2x$$<br>$$x = \\frac{32}{2} = 16$$<br>Therefore, Shyam's present age is <b>16 years</b>."
            },
            {
                "q": "(ii) 4 years ago, Lal was twice as old as he was 9 years ago. Find his present age.",
                "a": "Let Lal's present age be $x$ years.<br>4 years ago, his age was $(x - 4)$ years.<br>9 years ago, his age was $(x - 9)$ years.<br>According to the given condition:<br>$$x - 4 = 2(x - 9)$$<br>$$x - 4 = 2x - 18$$<br>$$18 - 4 = 2x - x$$<br>$$14 = x \\implies x = 14$$<br>Therefore, Lal's present age is <b>14 years</b>."
            }
        ]
    },
    {
        "q": "10. A man's age is seven times that of his son. In 5 years, he will be four times as old as his son. What are the present ages of the man and his son?",
        "subs": [
            {
                "q": "",
                "a": "Let the present age of the son be $x$ years.<br>Then the present age of the man is $7x$ years.<br>In 5 years:<br>Son's age = $(x + 5)$ years<br>Man's age = $(7x + 5)$ years<br>According to the given condition:<br>$$7x + 5 = 4(x + 5)$$<br>$$7x + 5 = 4x + 20$$<br>$$7x - 4x = 20 - 5$$<br>$$3x = 15$$<br>$$x = \\frac{15}{3} = 5$$<br>Son's present age = $5$ years<br>Man's present age = $7 \\times 5 = 35$ years<br>Therefore, the present ages are <b>35 years and 5 years respectively</b>."
            }
        ]
    },
    {
        "q": "11. Age comparisons after years.",
        "subs": [
            {
                "q": "(i) A man's age is 42 years and his son's age is 12 years. After how many years will the man be thrice as old as his son?",
                "a": "Let the required number of years be $x$.<br>After $x$ years:<br>Man's age = $(42 + x)$ years<br>Son's age = $(12 + x)$ years<br>According to the given condition:<br>$$42 + x = 3(12 + x)$$<br>$$42 + x = 36 + 3x$$<br>$$42 - 36 = 3x - x$$<br>$$6 = 2x$$<br>$$x = \\frac{6}{2} = 3$$<br>Therefore, after <b>3</b> years, the man will be thrice as old as his son."
            },
            {
                "q": "(ii) A man's age is 32 years and his son's age is 5 years. In how many years will the man's age be four times that of his son?",
                "a": "Let the required number of years be $x$.<br>After $x$ years:<br>Man's age = $(32 + x)$ years<br>Son's age = $(5 + x)$ years<br>According to the given condition:<br>$$32 + x = 4(5 + x)$$<br>$$32 + x = 20 + 4x$$<br>$$32 - 20 = 4x - x$$<br>$$12 = 3x$$<br>$$x = \\frac{12}{3} = 4$$<br>Therefore, in <b>4</b> years, the man's age will be four times that of his son."
            }
        ]
    },
    {
        "q": "12. Problems based on coins.",
        "subs": [
            {
                "q": "(i) A purse contains some coins. Of these, the number of one-rupee coins is three times the number of five-rupee coins and twice the number of two-rupee coins. If the total number of coins is 66, what is the value of the five-rupee coins?",
                "a": "Let the number of one-rupee coins be $x$.<br>Then:<br>Number of five-rupee coins = $\\frac{x}{3}$<br>Number of two-rupee coins = $\\frac{x}{2}$<br>Total number of coins is 66:<br>$$x + \\frac{x}{2} + \\frac{x}{3} = 66$$<br>Taking LCM of denominators (LCM of 1, 2, 3 is 6):<br>$$\\frac{6x + 3x + 2x}{6} = 66$$<br>$$\\frac{11x}{6} = 66$$<br>$$11x = 66 \\times 6 = 396$$<br>$$x = \\frac{396}{11} = 36$$<br>Number of one-rupee coins = $36$<br>Number of five-rupee coins = $\\frac{36}{3} = 12$<br>Value of five-rupee coins = $12 \\times \\text{\u20b9}5 =$ <b>\u20b960</b>."
            },
            {
                "q": "(ii) Anuj has an equal number of two-rupee and five-rupee coins. He has also some one-rupee coins. If the total number of coins is 40 and their value is \u20b9120, how many five-rupee and two-rupee coins does he have?",
                "a": "Let the number of two-rupee coins be $x$.<br>Then the number of five-rupee coins is also $x$.<br>Total number of coins is 40, so:<br>Number of one-rupee coins = $40 - (x + x) = 40 - 2x$<br>Total value of the coins = \u20b9120:<br>$$2(x) + 5(x) + 1(40 - 2x) = 120$$<br>$$2x + 5x + 40 - 2x = 120$$<br>$$5x + 40 = 120$$<br>$$5x = 120 - 40 = 80$$<br>$$x = \\frac{80}{5} = 16$$<br>Therefore, he has <b>16 each</b> of two-rupee and five-rupee coins."
            }
        ]
    },
    {
        "q": "13. A plane takes 2 hours and 45 minutes to cover the distance between two airports. If it travels 20 km/h slower then it takes 3 hours. Find the speed of the plane. Also, find the distance between the two airports.",
        "subs": [
            {
                "q": "",
                "a": "Let the original speed of the plane be $x\\text{ km/h}$.<br>Time taken originally = $2\\text{ hours } 45\\text{ minutes} = 2 + \\frac{45}{60} = 2 + \\frac{3}{4} = \\frac{11}{4}\\text{ hours}$.<br>Distance = $\\text{Speed} \\times \\text{Time} = x \\times \\frac{11}{4} = \\frac{11x}{4}\\text{ km}$.<br>When the speed is reduced by $20\\text{ km/h}$:<br>New speed = $(x - 20)\\text{ km/h}$<br>New time taken = $3\\text{ hours}$<br>Distance = $3(x - 20)\\text{ km}$<br>Since the distance between the two airports remains the same:<br>$$\\frac{11x}{4} = 3(x - 20)$$<br>$$11x = 12(x - 20)$$<br>$$11x = 12x - 240$$<br>$$12x - 11x = 240$$<br>$$x = 240$$<br>Original speed of the plane = <b>240 km/h</b>.<br>Distance between the two airports = $3(240 - 20) = 3 \\times 220 =$ <b>660 km</b>."
            }
        ]
    },
    {
        "q": "14. Two cyclists make the same trip. The first one takes 3.5 hours and the second, with a speed that is 1 km/h greater than that of the first, takes 3 hours. Find the speeds of the two cyclists. Also, find the distance covered in the trip.",
        "subs": [
            {
                "q": "",
                "a": "Let the speed of the first cyclist be $x\\text{ km/h}$.<br>Then the speed of the second cyclist is $(x + 1)\\text{ km/h}$.<br>Time taken by the first cyclist = $3.5\\text{ hours}$<br>Distance covered by the first cyclist = $3.5x\\text{ km}$<br>Time taken by the second cyclist = $3\\text{ hours}$<br>Distance covered by the second cyclist = $3(x + 1)\\text{ km}$<br>Since both cover the same distance:<br>$$3.5x = 3(x + 1)$$<br>$$3.5x = 3x + 3$$<br>$$3.5x - 3x = 3$$<br>$$0.5x = 3$$<br>$$x = \\frac{3}{0.5} = 6$$<br>Speed of first cyclist = <b>6 km/h</b><br>Speed of second cyclist = $6 + 1 =$ <b>7 km/h</b><br>Distance covered = $3.5 \\times 6 =$ <b>21 km</b>."
            }
        ]
    },
    {
        "q": "15. The length of a rectangle is 1 m greater than its width. If the length is increased by 2 m and the width is decreased by 6 m, the area decreases by 50 m^2. What are the dimensions of the rectangle?",
        "subs": [
            {
                "q": "",
                "a": "Let the width of the rectangle be $x\\text{ m}$.<br>Then its length is $(x + 1)\\text{ m}$.<br>Original area = $\\text{Length} \\times \\text{Width} = (x + 1)x = (x^2 + x)\\text{ m}^2$<br>New length = $(x + 1) + 2 = (x + 3)\\text{ m}$<br>New width = $(x - 6)\\text{ m}$<br>New area = $(x + 3)(x - 6) = x^2 - 6x + 3x - 18 = (x^2 - 3x - 18)\\text{ m}^2$<br>According to the question, the area decreases by $50\\text{ m}^2$:<br>$$(x^2 + x) - (x^2 - 3x - 18) = 50$$<br>$$x^2 + x - x^2 + 3x + 18 = 50$$<br>$$4x + 18 = 50$$<br>$$4x = 50 - 18 = 32$$<br>$$x = \\frac{32}{4} = 8$$<br>Width = $8\\text{ m}$<br>Length = $x + 1 = 8 + 1 = 9\\text{ m}$<br>Therefore, <b>Length = 9 m; width = 8 m</b>."
            }
        ]
    },
    {
        "q": "16. The length of a rectangle is 5 m greater than its width. If the perimeter of the rectangle is 50 m, find its length.",
        "subs": [
            {
                "q": "",
                "a": "Let the width of the rectangle be $x\\text{ m}$.<br>Then its length is $(x + 5)\\text{ m}$.<br>Perimeter of the rectangle = $2(\\text{length} + \\text{width})$<br>According to the given condition:<br>$$2[(x + 5) + x] = 50$$<br>$$2(2x + 5) = 50$$<br>$$2x + 5 = \\frac{50}{2} = 25$$<br>$$2x = 25 - 5 = 20$$<br>$$x = \\frac{20}{2} = 10$$<br>Width = $10\\text{ m}$<br>Length = $x + 5 = 10 + 5 =$ <b>15 m</b>."
            }
        ]
    },
    {
        "q": "17. In a right-angled triangle, one of the acute angles is one fifth the other. Find the measure of the smallest angle.",
        "subs": [
            {
                "q": "",
                "a": "In a right-angled triangle, one angle is $90^\\circ$.<br>The sum of the two acute angles is $180^\\circ - 90^\\circ = 90^\\circ$.<br>Let one acute angle be $x^\\circ$.<br>Then the other acute angle is $\\frac{1}{5}x^\\circ$.<br>Sum of the two acute angles:<br>$$x + \\frac{x}{5} = 90$$<br>$$\\frac{5x + x}{5} = 90$$<br>$$\\frac{6x}{5} = 90$$<br>$$6x = 90 \\times 5 = 450$$<br>$$x = \\frac{450}{6} = 75^\\circ$$<br>The two acute angles are $75^\\circ$ and $\\frac{75^\\circ}{5} = 15^\\circ$.<br>Therefore, the measure of the smallest angle is <b>$15^\\circ$</b>."
            }
        ]
    },
    {
        "q": "18. The base of an isosceles triangle is 3 cm longer than each of the other sides. If the perimeter is 54 cm, find the lengths of the sides.",
        "subs": [
            {
                "q": "",
                "a": "Let the length of each of the two equal sides be $x\\text{ cm}$.<br>Then the length of the base is $(x + 3)\\text{ cm}$.<br>Perimeter of the triangle = sum of all three sides:<br>$$x + x + (x + 3) = 54$$<br>$$3x + 3 = 54$$<br>$$3x = 54 - 3 = 51$$<br>$$x = \\frac{51}{3} = 17$$<br>Length of equal sides = $17\\text{ cm}$<br>Length of the base = $x + 3 = 17 + 3 = 20\\text{ cm}$<br>Therefore, the lengths of the sides are <b>17 cm, 17 cm and 20 cm</b>."
            }
        ]
    },
    {
        "q": "Exercise 5C",
        "subs": []
    },
    {
        "q": "1. If the replacement set is {0, 1, 2, 3, 4, 5, 6, 7}, find the solution set for each inequation.",
        "subs": [
            {
                "q": "(i) $x < 2$",
                "a": "Replacement set = $\\{0, 1, 2, 3, 4, 5, 6, 7\\}$<br>The elements strictly less than 2 are 0 and 1.<br>Solution set = <b>$\\{0, 1\\}$</b>"
            },
            {
                "q": "(ii) $x > 0$",
                "a": "The elements strictly greater than 0 are 1, 2, 3, 4, 5, 6, 7.<br>Solution set = <b>$\\{1, 2, 3, 4, 5, 6, 7\\}$</b>"
            },
            {
                "q": "(iii) $x \\le 4$",
                "a": "The elements less than or equal to 4 are 0, 1, 2, 3, 4.<br>Solution set = <b>$\\{0, 1, 2, 3, 4\\}$</b>"
            },
            {
                "q": "(iv) $x + 4 \\ge 8$",
                "a": "$$x \\ge 8 - 4 \\implies x \\ge 4$$<br>The elements greater than or equal to 4 are 4, 5, 6, 7.<br>Solution set = <b>$\\{4, 5, 6, 7\\}$</b>"
            },
            {
                "q": "(v) $4 - x \\le -3$",
                "a": "$$-x \\le -3 - 4 \\implies -x \\le -7$$<br>Dividing by $-1$ reverses the inequality sign:<br>$$x \\ge 7$$<br>From the replacement set, only 7 satisfies this.<br>Solution set = <b>$\\{7\\}$</b>"
            },
            {
                "q": "(vi) $12 - x > 16$",
                "a": "$$-x > 16 - 12 \\implies -x > 4$$<br>Dividing by $-1$ reverses the inequality:<br>$$x < -4$$<br>Since no element in $\\{0, 1, 2, 3, 4, 5, 6, 7\\}$ is less than $-4$:<br>Solution set = <b>No solution</b>"
            },
            {
                "q": "(vii) $3x < 9$",
                "a": "$$x < \\frac{9}{3} \\implies x < 3$$<br>The elements strictly less than 3 are 0, 1, 2.<br>Solution set = <b>$\\{0, 1, 2\\}$</b>"
            },
            {
                "q": "(viii) $\\frac{x}{2} \\ge 3$",
                "a": "$$x \\ge 3 \\times 2 \\implies x \\ge 6$$<br>The elements greater than or equal to 6 are 6, 7.<br>Solution set = <b>$\\{6, 7\\}$</b>"
            },
            {
                "q": "(ix) $-2x \\le -8$",
                "a": "Dividing both sides by $-2$ reverses the inequality:<br>$$x \\ge \\frac{-8}{-2} \\implies x \\ge 4$$<br>The elements greater than or equal to 4 are 4, 5, 6, 7.<br>Solution set = <b>$\\{4, 5, 6, 7\\}$</b>"
            },
            {
                "q": "(x) $-2x + \\frac{7}{2} < \\frac{1}{2}$",
                "a": "$$-2x < \\frac{1}{2} - \\frac{7}{2} = -\\frac{6}{2} = -3$$<br>Dividing both sides by $-2$ reverses the inequality:<br>$$x > \\frac{-3}{-2} \\implies x > 1.5$$<br>The elements greater than 1.5 are 2, 3, 4, 5, 6, 7.<br>Solution set = <b>$\\{2, 3, 4, 5, 6, 7\\}$</b>"
            },
            {
                "q": "(xi) $11 - 3x \\ge 9$",
                "a": "$$-3x \\ge 9 - 11 \\implies -3x \\ge -2$$<br>Dividing both sides by $-3$ reverses the inequality:<br>$$x \\le \\frac{2}{3}$$<br>The only whole number in the replacement set that is $\\le \\frac{2}{3}$ is 0.<br>Solution set = <b>$\\{0\\}$</b>"
            },
            {
                "q": "(xii) $\\frac{15}{2} < 2x + \\frac{5}{2}$",
                "a": "$$\\frac{15}{2} - \\frac{5}{2} < 2x$$<br>$$\\frac{10}{2} < 2x \\implies 5 < 2x \\implies x > 2.5$$<br>The elements greater than 2.5 are 3, 4, 5, 6, 7.<br>Solution set = <b>$\\{3, 4, 5, 6, 7\\}$</b>"
            },
            {
                "q": "(xiii) $4(x - 2) < 3x + 1$",
                "a": "$$4x - 8 < 3x + 1$$<br>$$4x - 3x < 1 + 8$$<br>$$x < 9$$<br>All elements of $\\{0, 1, 2, 3, 4, 5, 6, 7\\}$ are less than 9.<br>Solution set = <b>$\\{0, 1, 2, 3, 4, 5, 6, 7\\}$</b>"
            },
            {
                "q": "(xiv) $n + 2 > \\frac{3n - 1}{2}$",
                "a": "Multiplying both sides by 2:<br>$$2(n + 2) > 3n - 1$$<br>$$2n + 4 > 3n - 1$$<br>$$4 + 1 > 3n - 2n$$<br>$$5 > n \\implies n < 5$$<br>The elements strictly less than 5 are 0, 1, 2, 3, 4.<br>Solution set = <b>$\\{0, 1, 2, 3, 4\\}$</b>"
            }
        ]
    },
    {
        "q": "2. Represent the solution set graphically.",
        "subs": [
            {
                "q": "(i) $x - 2 < 3$, where $x \\in W$",
                "a": "$$x < 3 + 2 \\implies x < 5$$<br>Since $x \\in W$ (Whole Numbers):<br>Solution set = <b>$\\{0, 1, 2, 3, 4\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">0</text><circle cx=\"35.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"73.75\" y1=\"21\" x2=\"73.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"73.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><circle cx=\"73.75\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"112.5\" y1=\"21\" x2=\"112.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"112.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><circle cx=\"112.5\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"151.25\" y1=\"21\" x2=\"151.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"151.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><circle cx=\"151.25\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"190.0\" y1=\"21\" x2=\"190.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"190.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><circle cx=\"190.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"228.75\" y1=\"21\" x2=\"228.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"228.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><line x1=\"267.5\" y1=\"21\" x2=\"267.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"267.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">6</text><line x1=\"306.25\" y1=\"21\" x2=\"306.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"306.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">7</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">8</text></svg>"
            },
            {
                "q": "(ii) $-3 + x \\ge \\frac{1}{2}$, where $x \\in N$",
                "a": "$$x \\ge \\frac{1}{2} + 3 = \\frac{7}{2} = 3.5$$<br>Since $x \\in N$ (Natural Numbers):<br>Solution set = <b>$\\{4, 5, 6, \\dots\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><line x1=\"79.28571428571428\" y1=\"21\" x2=\"79.28571428571428\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"79.28571428571428\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><line x1=\"123.57142857142857\" y1=\"21\" x2=\"123.57142857142857\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"123.57142857142857\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><line x1=\"167.85714285714286\" y1=\"21\" x2=\"167.85714285714286\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"167.85714285714286\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><circle cx=\"167.85714285714286\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"212.14285714285714\" y1=\"21\" x2=\"212.14285714285714\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"212.14285714285714\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><circle cx=\"212.14285714285714\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"256.42857142857144\" y1=\"21\" x2=\"256.42857142857144\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"256.42857142857144\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">6</text><circle cx=\"256.42857142857144\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"300.7142857142857\" y1=\"21\" x2=\"300.7142857142857\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"300.7142857142857\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">7</text><circle cx=\"300.7142857142857\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">8</text><circle cx=\"345.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><polygon points=\"374,25 362,20 362,30\" fill=\"#e74c3c\"/></svg>"
            },
            {
                "q": "(iii) $2x < 6$, where $x \\in W$",
                "a": "$$x < \\frac{6}{2} \\implies x < 3$$<br>Since $x \\in W$:<br>Solution set = <b>$\\{0, 1, 2\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">0</text><circle cx=\"35.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"86.66666666666666\" y1=\"21\" x2=\"86.66666666666666\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"86.66666666666666\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><circle cx=\"86.66666666666666\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"138.33333333333331\" y1=\"21\" x2=\"138.33333333333331\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"138.33333333333331\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><circle cx=\"138.33333333333331\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"190.0\" y1=\"21\" x2=\"190.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"190.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><line x1=\"241.66666666666666\" y1=\"21\" x2=\"241.66666666666666\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"241.66666666666666\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><line x1=\"293.3333333333333\" y1=\"21\" x2=\"293.3333333333333\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"293.3333333333333\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">6</text></svg>"
            },
            {
                "q": "(iv) $4p > -12$, where $p \\in I$",
                "a": "$$p > \\frac{-12}{4} \\implies p > -3$$<br>Since $p \\in I$ (Integers):<br>Solution set = <b>$\\{-2, -1, 0, 1, 2, 3, \\dots\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-4</text><line x1=\"69.44444444444444\" y1=\"21\" x2=\"69.44444444444444\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"69.44444444444444\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-3</text><line x1=\"103.88888888888889\" y1=\"21\" x2=\"103.88888888888889\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"103.88888888888889\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-2</text><circle cx=\"103.88888888888889\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"138.33333333333331\" y1=\"21\" x2=\"138.33333333333331\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"138.33333333333331\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-1</text><circle cx=\"138.33333333333331\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"172.77777777777777\" y1=\"21\" x2=\"172.77777777777777\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"172.77777777777777\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">0</text><circle cx=\"172.77777777777777\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"207.22222222222223\" y1=\"21\" x2=\"207.22222222222223\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"207.22222222222223\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><circle cx=\"207.22222222222223\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"241.66666666666666\" y1=\"21\" x2=\"241.66666666666666\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"241.66666666666666\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><circle cx=\"241.66666666666666\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"276.1111111111111\" y1=\"21\" x2=\"276.1111111111111\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"276.1111111111111\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><circle cx=\"276.1111111111111\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"310.55555555555554\" y1=\"21\" x2=\"310.55555555555554\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"310.55555555555554\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><circle cx=\"310.55555555555554\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><circle cx=\"345.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><polygon points=\"374,25 362,20 362,30\" fill=\"#e74c3c\"/></svg>"
            },
            {
                "q": "(v) $-2m \\le -8$, where $m \\in N$",
                "a": "Dividing by $-2$ reverses the inequality:<br>$$m \\ge \\frac{-8}{-2} \\implies m \\ge 4$$<br>Since $m \\in N$:<br>Solution set = <b>$\\{4, 5, 6, \\dots\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><line x1=\"79.28571428571428\" y1=\"21\" x2=\"79.28571428571428\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"79.28571428571428\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><line x1=\"123.57142857142857\" y1=\"21\" x2=\"123.57142857142857\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"123.57142857142857\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><line x1=\"167.85714285714286\" y1=\"21\" x2=\"167.85714285714286\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"167.85714285714286\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><circle cx=\"167.85714285714286\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"212.14285714285714\" y1=\"21\" x2=\"212.14285714285714\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"212.14285714285714\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><circle cx=\"212.14285714285714\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"256.42857142857144\" y1=\"21\" x2=\"256.42857142857144\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"256.42857142857144\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">6</text><circle cx=\"256.42857142857144\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"300.7142857142857\" y1=\"21\" x2=\"300.7142857142857\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"300.7142857142857\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">7</text><circle cx=\"300.7142857142857\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">8</text><circle cx=\"345.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><polygon points=\"374,25 362,20 362,30\" fill=\"#e74c3c\"/></svg>"
            },
            {
                "q": "(vi) $\\frac{5}{2} - 2x \\ge \\frac{1}{2}$, where $x \\in W$",
                "a": "$$-2x \\ge \\frac{1}{2} - \\frac{5}{2} = -2$$<br>Dividing by $-2$ reverses the inequality:<br>$$x \\le 1$$<br>Since $x \\in W$:<br>Solution set = <b>$\\{0, 1\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">0</text><circle cx=\"35.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"97.0\" y1=\"21\" x2=\"97.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"97.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><circle cx=\"97.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"159.0\" y1=\"21\" x2=\"159.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"159.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><line x1=\"221.0\" y1=\"21\" x2=\"221.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"221.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><line x1=\"283.0\" y1=\"21\" x2=\"283.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"283.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text></svg>"
            }
        ]
    },
    {
        "q": "3. Solve the following inequations.",
        "subs": [
            {
                "q": "(i) $\\frac{1}{2}x + 2 \\ge x - 1$, where $x \\in N$",
                "a": "$$2 + 1 \\ge x - \\frac{1}{2}x$$<br>$$3 \\ge \\frac{1}{2}x \\implies x \\le 6$$<br>Since $x \\in N$:<br>Solution set = <b>$\\{1, 2, 3, 4, 5, 6\\}$</b>"
            },
            {
                "q": "(ii) $4(x - 3) < x + 3$, where $x \\in W$",
                "a": "$$4x - 12 < x + 3$$<br>$$4x - x < 3 + 12$$<br>$$3x < 15 \\implies x < 5$$<br>Since $x \\in W$:<br>Solution set = <b>$\\{0, 1, 2, 3, 4\\}$</b>"
            },
            {
                "q": "(iii) $3(2x - 1) \\ge 2(2x + 3)$, where $x \\in I$",
                "a": "$$6x - 3 \\ge 4x + 6$$<br>$$6x - 4x \\ge 6 + 3$$<br>$$2x \\ge 9 \\implies x \\ge 4.5$$<br>Since $x \\in I$ (Integers):<br>Solution set = <b>$\\{5, 6, 7, \\dots\\}$</b>"
            },
            {
                "q": "(iv) $2(4 - 3x) \\le 4(x - 5)$, where $x \\in W$",
                "a": "$$8 - 6x \\le 4x - 20$$<br>$$8 + 20 \\le 4x + 6x$$<br>$$28 \\le 10x \\implies x \\ge 2.8$$<br>Since $x \\in W$:<br>Solution set = <b>$\\{3, 4, 5, \\dots\\}$</b>"
            },
            {
                "q": "(v) $2(4x - 1) < 4(3x + 1)$, where $x \\in \\{\\text{set of all negative integers}\\}$",
                "a": "$$8x - 2 < 12x + 4$$<br>$$-2 - 4 < 12x - 8x$$<br>$$-6 < 4x \\implies 4x > -6 \\implies x > -1.5$$<br>Negative integers greater than $-1.5$ is only $-1$.<br>Solution set = <b>$\\{-1\\}$</b>"
            }
        ]
    },
    {
        "q": "4. Represent the solution set graphically.",
        "subs": [
            {
                "q": "(i) $2x - 3(x - 4) \\ge 4 - 2(x - 7)$, where $x \\in W$",
                "a": "$$2x - 3x + 12 \\ge 4 - 2x + 14$$<br>$$-x + 12 \\ge 18 - 2x$$<br>$$-x + 2x \\ge 18 - 12$$<br>$$x \\ge 6$$<br>Since $x \\in W$:<br>Solution set = <b>$\\{6, 7, 8, \\dots\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><line x1=\"73.75\" y1=\"21\" x2=\"73.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"73.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><line x1=\"112.5\" y1=\"21\" x2=\"112.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"112.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><line x1=\"151.25\" y1=\"21\" x2=\"151.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"151.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">6</text><circle cx=\"151.25\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"190.0\" y1=\"21\" x2=\"190.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"190.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">7</text><circle cx=\"190.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"228.75\" y1=\"21\" x2=\"228.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"228.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">8</text><circle cx=\"228.75\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"267.5\" y1=\"21\" x2=\"267.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"267.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">9</text><circle cx=\"267.5\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"306.25\" y1=\"21\" x2=\"306.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"306.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">10</text><circle cx=\"306.25\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">11</text><circle cx=\"345.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><polygon points=\"374,25 362,20 362,30\" fill=\"#e74c3c\"/></svg>"
            },
            {
                "q": "(ii) $5(x - 2) > 9x - 3(2x - 4)$, where $x \\in N$",
                "a": "$$5x - 10 > 9x - 6x + 12$$<br>$$5x - 10 > 3x + 12$$<br>$$5x - 3x > 12 + 10$$<br>$$2x > 22 \\implies x > 11$$<br>Since $x \\in N$:<br>Solution set = <b>$\\{12, 13, 14, \\dots\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">8</text><line x1=\"73.75\" y1=\"21\" x2=\"73.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"73.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">9</text><line x1=\"112.5\" y1=\"21\" x2=\"112.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"112.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">10</text><line x1=\"151.25\" y1=\"21\" x2=\"151.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"151.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">11</text><line x1=\"190.0\" y1=\"21\" x2=\"190.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"190.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">12</text><circle cx=\"190.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"228.75\" y1=\"21\" x2=\"228.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"228.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">13</text><circle cx=\"228.75\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"267.5\" y1=\"21\" x2=\"267.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"267.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">14</text><circle cx=\"267.5\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"306.25\" y1=\"21\" x2=\"306.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"306.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">15</text><circle cx=\"306.25\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">16</text><circle cx=\"345.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><polygon points=\"374,25 362,20 362,30\" fill=\"#e74c3c\"/></svg>"
            },
            {
                "q": "(iii) $3\\{4(n - 2) - (1 - n)\\} \\le n + 1$, where $n \\in W$",
                "a": "Simplifying inside braces:<br>$$4n - 8 - 1 + n = 5n - 9$$<br>$$3(5n - 9) \\le n + 1$$<br>$$15n - 27 \\le n + 1$$<br>$$15n - n \\le 1 + 27$$<br>$$14n \\le 28 \\implies n \\le 2$$<br>Since $n \\in W$:<br>Solution set = <b>$\\{0, 1, 2\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">0</text><circle cx=\"35.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"97.0\" y1=\"21\" x2=\"97.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"97.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><circle cx=\"97.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"159.0\" y1=\"21\" x2=\"159.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"159.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><circle cx=\"159.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"221.0\" y1=\"21\" x2=\"221.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"221.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><line x1=\"283.0\" y1=\"21\" x2=\"283.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"283.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text></svg>"
            }
        ]
    },
    {
        "q": "5. Find the solution set and represent graphically.",
        "subs": [
            {
                "q": "(i) $4 < -(x + 2) < 9$, where $x \\in I$",
                "a": "$$4 < -x - 2 < 9$$<br>Adding 2 throughout:<br>$$6 < -x < 11$$<br>Multiplying by $-1$ reverses the inequality:<br>$$-11 < x < -6$$<br>Since $x \\in I$ (Integers):<br>Solution set = <b>$\\{-10, -9, -8, -7\\}$</b><br><b>Graphical representation on the number line:</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-12</text><line x1=\"73.75\" y1=\"21\" x2=\"73.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"73.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-11</text><line x1=\"112.5\" y1=\"21\" x2=\"112.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"112.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-10</text><circle cx=\"112.5\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"151.25\" y1=\"21\" x2=\"151.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"151.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-9</text><circle cx=\"151.25\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"190.0\" y1=\"21\" x2=\"190.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"190.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-8</text><circle cx=\"190.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"228.75\" y1=\"21\" x2=\"228.75\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"228.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-7</text><circle cx=\"228.75\" cy=\"25\" r=\"5\" fill=\"#e74c3c\"/><line x1=\"267.5\" y1=\"21\" x2=\"267.5\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"267.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-6</text><line x1=\"306.25\" y1=\"21\" x2=\"306.25\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"306.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-5</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#666\" stroke-width=\"1.5\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-4</text></svg>"
            },
            {
                "q": "(ii) $15 > 2x - 7 > 7$, where $x \\in R$",
                "a": "Adding 7 throughout:<br>$$15 + 7 > 2x > 7 + 7$$<br>$$22 > 2x > 14$$<br>Dividing by 2:<br>$$11 > x > 7 \\implies 7 < x < 11$$<br>Solution set = <b>$\\{x \\in R : 7 < x < 11\\}$</b><br><b>Graphical representation on the number line (open circles at 7 and 11):</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><line x1=\"73.75\" y1=\"21\" x2=\"73.75\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"73.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">6</text><line x1=\"112.5\" y1=\"21\" x2=\"112.5\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"112.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">7</text><line x1=\"151.25\" y1=\"21\" x2=\"151.25\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"151.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">8</text><line x1=\"190.0\" y1=\"21\" x2=\"190.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"190.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">9</text><line x1=\"228.75\" y1=\"21\" x2=\"228.75\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"228.75\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">10</text><line x1=\"267.5\" y1=\"21\" x2=\"267.5\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"267.5\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">11</text><line x1=\"306.25\" y1=\"21\" x2=\"306.25\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"306.25\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">12</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">13</text><line x1=\"112.5\" y1=\"25\" x2=\"267.5\" y2=\"25\" stroke=\"#e74c3c\" stroke-width=\"4\"/><circle cx=\"112.5\" cy=\"25\" r=\"5\" fill=\"#ffffff\" stroke=\"#e74c3c\" stroke-width=\"2\"/><circle cx=\"267.5\" cy=\"25\" r=\"5\" fill=\"#ffffff\" stroke=\"#e74c3c\" stroke-width=\"2\"/></svg>"
            },
            {
                "q": "(iii) $0 \\le \\frac{4 - x}{2} < 2$, where $x \\in R$",
                "a": "Multiplying by 2:<br>$$0 \\le 4 - x < 4$$<br>Subtracting 4 throughout:<br>$$-4 \\le -x < 0$$<br>Multiplying by $-1$ reverses the inequality signs:<br>$$4 \\ge x > 0 \\implies 0 < x \\le 4$$<br>Solution set = <b>$\\{x \\in R : 0 < x \\le 4\\}$</b><br><b>Graphical representation on the number line (open circle at 0, closed circle at 4):</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-1</text><line x1=\"79.28571428571428\" y1=\"21\" x2=\"79.28571428571428\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"79.28571428571428\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">0</text><line x1=\"123.57142857142857\" y1=\"21\" x2=\"123.57142857142857\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"123.57142857142857\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">1</text><line x1=\"167.85714285714286\" y1=\"21\" x2=\"167.85714285714286\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"167.85714285714286\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">2</text><line x1=\"212.14285714285714\" y1=\"21\" x2=\"212.14285714285714\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"212.14285714285714\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">3</text><line x1=\"256.42857142857144\" y1=\"21\" x2=\"256.42857142857144\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"256.42857142857144\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">4</text><line x1=\"300.7142857142857\" y1=\"21\" x2=\"300.7142857142857\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"300.7142857142857\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">5</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">6</text><line x1=\"79.28571428571428\" y1=\"25\" x2=\"256.42857142857144\" y2=\"25\" stroke=\"#e74c3c\" stroke-width=\"4\"/><circle cx=\"79.28571428571428\" cy=\"25\" r=\"5\" fill=\"#ffffff\" stroke=\"#e74c3c\" stroke-width=\"2\"/><circle cx=\"256.42857142857144\" cy=\"25\" r=\"5\" fill=\"#e74c3c\" stroke=\"#e74c3c\" stroke-width=\"2\"/></svg>"
            },
            {
                "q": "(iv) $-4 \\le -2(x + 8) < 8$, where $x \\in R$",
                "a": "Dividing by $-2$ reverses the inequality signs:<br>$$\\frac{-4}{-2} \\ge x + 8 > \\frac{8}{-2}$$<br>$$2 \\ge x + 8 > -4$$<br>Subtracting 8 throughout:<br>$$2 - 8 \\ge x > -4 - 8$$<br>$$-6 \\ge x > -12 \\implies -12 < x \\le -6$$<br>Solution set = <b>$\\{x \\in R : -12 < x \\le -6\\}$</b><br><b>Graphical representation on the number line (open circle at -12, closed circle at -6):</b><br><svg width=\"380\" height=\"50\" viewBox=\"0 0 380 50\" style=\"background:#ffffff;border:1px solid #ddd;border-radius:6px;display:block;margin:10px 0;padding:2px;\"><line x1=\"12\" y1=\"25\" x2=\"368\" y2=\"25\" stroke=\"#333\" stroke-width=\"2\"/><polygon points=\"8,25 16,21 16,29\" fill=\"#333\"/><polygon points=\"372,25 364,21 364,29\" fill=\"#333\"/><line x1=\"35.0\" y1=\"21\" x2=\"35.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"35.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-14</text><line x1=\"66.0\" y1=\"21\" x2=\"66.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"66.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-13</text><line x1=\"97.0\" y1=\"21\" x2=\"97.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"97.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-12</text><line x1=\"128.0\" y1=\"21\" x2=\"128.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"128.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-11</text><line x1=\"159.0\" y1=\"21\" x2=\"159.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"159.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-10</text><line x1=\"190.0\" y1=\"21\" x2=\"190.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"190.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-9</text><line x1=\"221.0\" y1=\"21\" x2=\"221.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"221.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-8</text><line x1=\"252.0\" y1=\"21\" x2=\"252.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"252.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-7</text><line x1=\"283.0\" y1=\"21\" x2=\"283.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"283.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-6</text><line x1=\"314.0\" y1=\"21\" x2=\"314.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"314.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-5</text><line x1=\"345.0\" y1=\"21\" x2=\"345.0\" y2=\"29\" stroke=\"#777\" stroke-width=\"1\"/><text x=\"345.0\" y=\"43\" font-size=\"11\" font-family=\"Georgia, serif\" text-anchor=\"middle\" fill=\"#333\">-4</text><line x1=\"97.0\" y1=\"25\" x2=\"283.0\" y2=\"25\" stroke=\"#e74c3c\" stroke-width=\"4\"/><circle cx=\"97.0\" cy=\"25\" r=\"5\" fill=\"#ffffff\" stroke=\"#e74c3c\" stroke-width=\"2\"/><circle cx=\"283.0\" cy=\"25\" r=\"5\" fill=\"#e74c3c\" stroke=\"#e74c3c\" stroke-width=\"2\"/></svg>"
            }
        ]
    }
]

chapters = [
    {"id": "ch1", "title": "Chapter 1: Rational Numbers", "data": questions_ch1},
    {"id": "ch3", "title": "Chapter 3: Squares and Square Roots", "data": questions_ch3},
    {"id": "ch4", "title": "Chapter 4: Cubes and Cube Roots", "data": questions_ch4},
    {"id": "ch5", "title": "Chapter 5: Linear Equations and Inequations", "data": questions_ch5}
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
