import re

ch1b_data = r"""    {
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
            {"q": "(viii) \\frac{-35}{-18} \\times \\frac{8}{-15}", "a": "$\\frac{-35}{-18} = \\frac{35}{18}$<br>$= \\frac{35}{18} \\times \\frac{8}{-15}$<br>Cancelling 35 and 15 by 5; 18 and 8 by 2:<br>$= \\frac{7}{9} \\times \\frac{4}{-3} =$ <b>$\\frac{-28}{27}$</b>"},
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
            {"q": "(i) $\\frac{2}{3}, \\frac{-1}{5}$ and $\\frac{7}{12}$", "a": "<b>LHS:</b> $(\\frac{2}{3} \\times \\frac{-1}{5}) \\times \\frac{7}{12} = \\frac{-2}{15} \\times \\frac{7}{12} = \\frac{-14}{180} = \\frac{-7}{90}$<br><b>RHS:</b> $\\frac{2}{3} \\times (\\frac{-1}{5} \\times \\frac{7}{12}) = \\frac{2}{3} \\times \\frac{-7}{60} = \\frac{-14}{180} = \\frac{-7}{90}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(ii) $\\frac{-5}{7}, \\frac{1}{2}$ and $\\frac{-21}{20}$", "a": "<b>LHS:</b> $(\\frac{-5}{7} \\times \\frac{1}{2}) \\times \\frac{-21}{20} = \\frac{-5}{14} \\times \\frac{-21}{20} = \\frac{105}{280} = \\frac{3}{8}$<br><b>RHS:</b> $\\frac{-5}{7} \\times (\\frac{1}{2} \\times \\frac{-21}{20}) = \\frac{-5}{7} \\times \\frac{-21}{40} = \\frac{105}{280} = \\frac{3}{8}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(iii) $\\frac{-8}{9}, \\frac{-3}{4}$ and $\\frac{15}{16}$", "a": "<b>LHS:</b> $(\\frac{-8}{9} \\times \\frac{-3}{4}) \\times \\frac{15}{16} = \\frac{24}{36} \\times \\frac{15}{16} = \\frac{2}{3} \\times \\frac{15}{16} = \\frac{30}{48} = \\frac{5}{8}$<br><b>RHS:</b> $\\frac{-8}{9} \\times (\\frac{-3}{4} \\times \\frac{15}{16}) = \\frac{-8}{9} \\times \\frac{-45}{64} = \\frac{360}{576} = \\frac{5}{8}$<br>Since LHS = RHS, the law is verified."},
            {"q": "(iv) $\\frac{-3}{11}, \\frac{-7}{4}$ and $\\frac{-1}{2}$", "a": "<b>LHS:</b> $(\\frac{-3}{11} \\times \\frac{-7}{4}) \\times \\frac{-1}{2} = \\frac{21}{44} \\times \\frac{-1}{2} = \\frac{-21}{88}$<br><b>RHS:</b> $\\frac{-3}{11} \\times (\\frac{-7}{4} \\times \\frac{-1}{2}) = \\frac{-3}{11} \\times \\frac{7}{8} = \\frac{-21}{88}$<br>Since LHS = RHS, the law is verified."}
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
"""

import os

filepath = r"d:\Guna Shekhar\My Classes\Class 8th icsc\generator.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# We need to slice content up to the string "Exercise 1B" inside questions_ch1.
# The structure is:
#         "q": "13. Identify the true statements only.",
#         ...
#     },
#     {
#         "q": "Exercise 1B",

idx = content.find('{"q": "Exercise 1B",')
if idx != -1:
    # Find the preceding comma and brace
    preceding_bracket = content.rfind('}', 0, idx)
    content = content[:preceding_bracket+1] + ",\n" + ch1b_data + "\n\nquestions_ch3 =" + content.split("questions_ch3 =", 1)[1]
else:
    print("Could not find Exercise 1B")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated generator.py with proper Exercise 1B.")
