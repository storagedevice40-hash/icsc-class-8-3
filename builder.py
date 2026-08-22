import json

questions = [
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

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 8 Maths - Squares and Square Roots</title>
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
        body {
            background-color: #f4f6f9;
            font-family: 'Georgia', serif;
            font-size: 18px;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
            color: #333;
            line-height: 1.6;
        }
        .container {
            background: #fff;
            width: 100%;
            max-width: 900px;
            min-height: 100vh;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            padding: 40px 60px;
            border-radius: 8px;
            border: 1px solid #ddd;
            position: relative;
        }
        .header {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 40px;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 15px;
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
            margin: 30px auto;
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
        .btn-close {
            position: absolute;
            top: 20px;
            right: 20px;
            background: #e74c3c;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        
        /* Teach View List */
        #teach-view ul {
            list-style: none;
            padding: 0;
        }
        #teach-view li.main-q-li {
            font-size: 22px;
            font-weight: bold;
            margin-top: 25px;
            color: #2c3e50;
        }
        #teach-view li.clickable-q {
            font-size: 20px;
            margin: 15px 0 15px 30px;
            padding: 15px;
            background: #ecf0f1;
            border-left: 4px solid #2980b9;
            cursor: pointer;
            border-radius: 4px;
            transition: 0.2s;
        }
        #teach-view li.clickable-q:hover {
            background: #d4e6f1;
            transform: translateX(5px);
        }
        
        /* Presentation View */
        #presentation-view {
            text-align: center;
            font-size: 28px;
            cursor: pointer;
            min-height: 80vh;
            user-select: none; /* prevent text selection on rapid click */
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
        
        /* Zoom Controls */
        .zoom-controls {
            position: fixed;
            right: 20px;
            bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 1000;
        }
        .zoom-controls button {
            width: 45px;
            height: 45px;
            font-size: 28px;
            font-weight: bold;
            border-radius: 50%;
            border: none;
            background-color: #2c3e50;
            color: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            cursor: pointer;
            transition: 0.2s;
        }
        .zoom-controls button:active {
            transform: scale(0.9);
        }

        /* Mobile Portrait Optimization */
        @media (max-width: 768px) and (orientation: portrait) {
            body { padding: 10px; font-size: 14px; }
            .container { padding: 20px; border-radius: 4px; }
            .header { font-size: 24px; margin-bottom: 20px; }
            .question { font-size: 17px; }
            .sub-q { font-size: 16px; margin-top: 15px; }
            .solution { padding: 10px; margin-left: 0; }
            .btn-teach { width: 100%; font-size: 18px; margin: 20px 0; }
            #teach-view li.main-q-li { font-size: 18px; margin-top: 15px; }
            #teach-view li.clickable-q { font-size: 16px; margin: 10px 0; padding: 10px; }
            .pres-q { font-size: 22px; margin-bottom: 20px; padding-bottom: 10px; }
            #presentation-view { font-size: 20px; }
        }
    </style>
</head>
<body>
    <div class="zoom-controls">
        <button onclick="zoomIn()">+</button>
        <button onclick="zoomOut()">-</button>
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
    </script>

    <!-- NORMAL VIEW -->
    <div class="container" id="normal-view">
        <div class="header">Exercise 3: Squares and Square Roots (Detailed Solutions)</div>
        <button class="btn-teach" onclick="enterTeachMode()" style="margin-top: 0; margin-bottom: 40px;">👨‍🏫 Teach Mode</button>
        
"""

# Build normal view HTML
for item in questions:
    html_template += f'        <div class="q-block">\n'
    html_template += f'            <div class="question">{item["q"]}</div>\n'
    for sub in item["subs"]:
        if sub["q"]:
            html_template += f'            <div class="sub-q">{sub["q"]}</div>\n'
        html_template += f'            <div class="solution"><span class="sol-label">Solution:</span><br>{sub["a"]}</div>\n'
    html_template += f'        </div>\n'

html_template += """
    </div>

    <!-- TEACH VIEW (Question List) -->
    <div class="container" id="teach-view" style="display: none;">
        <button class="btn-close" onclick="exitTeachMode()">Back</button>
        <div class="header">Teach Mode - Select a Question</div>
        <ul>
"""

# Build teach view list and presentation containers
presentation_html = ""
pres_id_counter = 0

for item in questions:
    html_template += f'            <li class="main-q-li">{item["q"]}</li>\n'
    for sub in item["subs"]:
        pres_id = f'pres-{pres_id_counter}'
        pres_id_counter += 1
        
        display_text = sub["q"] if sub["q"] else "Solution"
        html_template += f'            <li class="clickable-q" onclick="startPresentation(\'{pres_id}\')">{display_text}</li>\n'
        
        # Build corresponding presentation container
        presentation_html += f'        <div id="{pres_id}" class="pres-container" style="display:none;">\n'
        presentation_html += f'            <div class="pres-q">{item["q"]}<br>{sub["q"]}</div>\n'
        
        # Split answer into steps by <br>
        steps = sub["a"].split("<br>")
        for step in steps:
            presentation_html += f'            <div class="pres-step">{step.strip()}</div>\n'
            
        presentation_html += f'        </div>\n'

html_template += """
        </ul>
    </div>

    <!-- PRESENTATION VIEW -->
    <div class="container" id="presentation-view" style="display: none;">
        <button class="btn-close" style="z-index: 100;" onclick="closePresentation()">X Close</button>
"""

html_template += presentation_html

html_template += """
    </div>

    <script>
        let currentSteps = [];
        let currentStepIndex = -1;
        let savedNormalScroll = 0;
        let savedTeachScroll = 0;

        function enterTeachMode() {
            savedNormalScroll = window.scrollY;
            document.getElementById('normal-view').style.display = 'none';
            document.getElementById('teach-view').style.display = 'block';
            window.scrollTo(0, 0);
        }

        function exitTeachMode() {
            document.getElementById('teach-view').style.display = 'none';
            document.getElementById('normal-view').style.display = 'block';
            window.scrollTo(0, savedNormalScroll);
        }

        function startPresentation(id) {
            savedTeachScroll = window.scrollY;
            document.getElementById('teach-view').style.display = 'none';
            document.getElementById('presentation-view').style.display = 'block';
            
            // Hide all presentation containers
            const containers = document.querySelectorAll('.pres-container');
            containers.forEach(c => c.style.display = 'none');
            
            // Show the selected one
            const target = document.getElementById(id);
            target.style.display = 'block';
            
            // Get all steps in this container
            currentSteps = target.querySelectorAll('.pres-step');
            currentSteps.forEach(step => {
                step.style.opacity = '0';
            });
            
            currentStepIndex = -1;
            window.scrollTo(0, 0);
        }

        function closePresentation() {
            document.getElementById('presentation-view').style.display = 'none';
            document.getElementById('teach-view').style.display = 'block';
            window.scrollTo(0, savedTeachScroll);
        }

        // Click handlers for presentation
        const presView = document.getElementById('presentation-view');
        
        presView.addEventListener('click', (e) => {
            if (e.target.tagName.toLowerCase() === 'button') return;
            nextStep();
        });

        presView.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            prevStep();
        });

        function nextStep() {
            if (currentStepIndex < currentSteps.length - 1) {
                currentStepIndex++;
                currentSteps[currentStepIndex].style.opacity = '1';
            }
        }

        function prevStep() {
            if (currentStepIndex >= 0) {
                currentSteps[currentStepIndex].style.opacity = '0';
                currentStepIndex--;
            }
        }

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (document.getElementById('presentation-view').style.display === 'block') {
                if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
                    e.preventDefault();
                    nextStep();
                } else if (e.key === 'ArrowLeft') {
                    e.preventDefault();
                    prevStep();
                } else if (e.key === 'Escape') {
                    closePresentation();
                }
            }
        });
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
