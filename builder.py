<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 8 Maths Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Georgia&display=swap" rel="stylesheet">
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']]
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

        .nav-q-btn {
            position: fixed;
            bottom: 20px;
            padding: 15px 25px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            z-index: 1000;
        }
        .nav-q-btn:hover { background-color: #2980b9; }
        .btn-prev-q { left: 20px; }
        .btn-next-q { right: 80px; }
        
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
            .btn-prev-q { left: 10px; bottom: 80px; padding: 10px 15px; font-size: 14px; }
            .btn-next-q { right: 10px; bottom: 80px; padding: 10px 15px; font-size: 14px; }
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
        <button class="home-btn" onclick="openChapter('ch3')">Chapter 3: Squares and Square Roots</button>
        <button class="home-btn" onclick="openChapter('ch4')">Chapter 4: Cubes and Cube Roots</button>

    </div>
    <div class="container chapter-view" id="normal-view-ch3" style="display: none;">
        <button class="btn-top-back" onclick="goHome()">⬅ Back to Home</button>
        <div class="header">Chapter 3: Squares and Square Roots</div>
        <button class="btn-teach" onclick="enterTeachMode('ch3')">👨‍🏫 Teach Mode</button>
        <div class="q-block">
            <div class="question">1. Find the value of each of the following.</div>
            <div class="sub-q">(i) $\left(\frac{11}{13}\right)^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\left(\frac{11}{13}\right)^2 = \frac{11^2}{13^2} = \frac{121}{169}$</div>
            <div class="sub-q">(ii) $\left(-1 \frac{7}{11}\right)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\left(-1 \frac{7}{11}\right)^3 = \left(\frac{-18}{11}\right)^3 = \frac{(-18)^3}{11^3} = \frac{-5832}{1331}$</div>
            <div class="sub-q">(iii) $(3.5)^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(3.5)^2 = \left(\frac{35}{10}\right)^2 = \frac{1225}{100} = 12.25$</div>
            <div class="sub-q">(iv) $(0.08)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(0.08)^3 = \left(\frac{8}{100}\right)^3 = \frac{512}{1000000} = 0.000512$</div>
        </div>
        <div class="q-block">
            <div class="question">2. Find the square root of each of the following by prime factorisation.</div>
            <div class="sub-q">(i) 256</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$256 = 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 = 2^8$<br>$\sqrt{256} = \sqrt{2^8} = 2^4 = 16$</div>
            <div class="sub-q">(ii) 324</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$324 = 2 \times 2 \times 3 \times 3 \times 3 \times 3 = 2^2 \times 3^4$<br>$\sqrt{324} = 2 \times 3^2 = 2 \times 9 = 18$</div>
            <div class="sub-q">(iii) 784</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$784 = 2 \times 2 \times 2 \times 2 \times 7 \times 7 = 2^4 \times 7^2$<br>$\sqrt{784} = 2^2 \times 7 = 4 \times 7 = 28$</div>
            <div class="sub-q">(iv) 7056</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$7056 = 2^4 \times 3^2 \times 7^2$<br>$\sqrt{7056} = 2^2 \times 3 \times 7 = 4 \times 21 = 84$</div>
            <div class="sub-q">(v) 28224</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$28224 = 2^6 \times 3^2 \times 7^2$<br>$\sqrt{28224} = 2^3 \times 3 \times 7 = 8 \times 21 = 168$</div>
            <div class="sub-q">(vi) 60025</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$60025 = 5^2 \times 7^4$<br>$\sqrt{60025} = 5 \times 7^2 = 5 \times 49 = 245$</div>
        </div>
        <div class="q-block">
            <div class="question">3. Find the square root of each of the following by division.</div>
            <div class="sub-q">(i) 841</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$$\begin{array}{r|l} & 29 \\ \hline 2 & \overline{8}\overline{41} \\ & -4 \\ \hline 49 & 441 \\ & -441 \\ \hline & 0 \end{array}$$ <br>$\sqrt{841} = 29$</div>
            <div class="sub-q">(ii) 2304</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$$\begin{array}{r|l} & 48 \\ \hline 4 & \overline{23}\overline{04} \\ & -16 \\ \hline 88 & 704 \\ & -704 \\ \hline & 0 \end{array}$$ <br>$\sqrt{2304} = 48$</div>
            <div class="sub-q">(iii) 39204</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$$\begin{array}{r|l} & 198 \\ \hline 1 & \overline{3}\overline{92}\overline{04} \\ & -1 \\ \hline 29 & 292 \\ & -261 \\ \hline 388 & 3104 \\ & -3104 \\ \hline & 0 \end{array}$$ <br>$\sqrt{39204} = 198$</div>
            <div class="sub-q">(iv) 55225</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$$\begin{array}{r|l} & 235 \\ \hline 2 & \overline{5}\overline{52}\overline{25} \\ & -4 \\ \hline 43 & 152 \\ & -129 \\ \hline 465 & 2325 \\ & -2325 \\ \hline & 0 \end{array}$$ <br>$\sqrt{55225} = 235$</div>
            <div class="sub-q">(v) 177241</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$$\begin{array}{r|l} & 421 \\ \hline 4 & \overline{17}\overline{72}\overline{41} \\ & -16 \\ \hline 82 & 172 \\ & -164 \\ \hline 841 & 841 \\ & -841 \\ \hline & 0 \end{array}$$ <br>$\sqrt{177241} = 421$</div>
            <div class="sub-q">(vi) 425104</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$$\begin{array}{r|l} & 652 \\ \hline 6 & \overline{42}\overline{51}\overline{04} \\ & -36 \\ \hline 125 & 651 \\ & -625 \\ \hline 1302 & 2604 \\ & -2604 \\ \hline & 0 \end{array}$$ <br>$\sqrt{425104} = 652$</div>
        </div>
        <div class="q-block">
            <div class="question">4. Find the square root of each of the following.</div>
            <div class="sub-q">(i) 13.69</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{13.69} = \sqrt{\frac{1369}{100}} = \frac{37}{10} = 3.7$</div>
            <div class="sub-q">(ii) 0.002025</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{0.002025} = \sqrt{\frac{2025}{1000000}} = \frac{45}{1000} = 0.045$</div>
            <div class="sub-q">(iii) 1.5129</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{1.5129} = \sqrt{\frac{15129}{10000}} = \frac{123}{100} = 1.23$</div>
            <div class="sub-q">(iv) 20.7936</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{20.7936} = \sqrt{\frac{207936}{10000}} = \frac{456}{100} = 4.56$</div>
            <div class="sub-q">(v) 6146.56</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{6146.56} = \sqrt{\frac{614656}{100}} = \frac{784}{10} = 78.4$</div>
            <div class="sub-q">(vi) 1.024144</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{1.024144} = \sqrt{\frac{1024144}{1000000}} = \frac{1012}{1000} = 1.012$</div>
        </div>
        <div class="q-block">
            <div class="question">5. Find the square root of each of the following.</div>
            <div class="sub-q">(i) $\frac{169}{484}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{169}{484}} = \frac{\sqrt{169}}{\sqrt{484}} = \frac{13}{22}$</div>
            <div class="sub-q">(ii) $5 \frac{580}{729}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{(5 \times 729) + 580}{729}} = \sqrt{\frac{3645 + 580}{729}} = \sqrt{\frac{4225}{729}} = \frac{65}{27}$</div>
            <div class="sub-q">(iii) $12 \frac{52}{81}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{(12 \times 81) + 52}{81}} = \sqrt{\frac{972 + 52}{81}} = \sqrt{\frac{1024}{81}} = \frac{32}{9}$</div>
            <div class="sub-q">(iv) 0.0009</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{0.0009} = \sqrt{\frac{9}{10000}} = \frac{3}{100} = 0.03$</div>
            <div class="sub-q">(v) 4.41</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{4.41} = \sqrt{\frac{441}{100}} = \frac{21}{10} = 2.1$</div>
        </div>
        <div class="q-block">
            <div class="question">6. Find the square root of each of the following correct to two decimal places.</div>
            <div class="sub-q">(i) 2</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{2} \approx 1.41$</div>
            <div class="sub-q">(ii) 3</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{3} \approx 1.73$</div>
            <div class="sub-q">(iii) 8</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{8} \approx 2.83$</div>
            <div class="sub-q">(iv) 11</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{11} \approx 3.32$</div>
            <div class="sub-q">(v) 35</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{35} \approx 5.92$</div>
            <div class="sub-q">(vi) 99</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{99} \approx 9.95$</div>
        </div>
        <div class="q-block">
            <div class="question">7. Find the value of $\sqrt{5}$ correct to two decimal places. Then, find the value of the square root of $\frac{3-\sqrt{5}}{3+\sqrt{5}}$ correct to two decimal places.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{5} \approx 2.24$<br>$\sqrt{\frac{3-\sqrt{5}}{3+\sqrt{5}}} = \sqrt{\frac{(3-\sqrt{5})(3-\sqrt{5})}{(3+\sqrt{5})(3-\sqrt{5})}}$<br>$= \sqrt{\frac{(3-\sqrt{5})^2}{9-5}} = \frac{3-\sqrt{5}}{\sqrt{4}} = \frac{3-\sqrt{5}}{2}$<br>Using $\sqrt{5} = 2.236$ (taking 3 decimal places for calculation accuracy):<br>$\frac{3 - 2.236}{2} = \frac{0.764}{2} = 0.382$<br>Correct to two decimal places: $0.38$</div>
        </div>
        <div class="q-block">
            <div class="question">8. Find the square root of each of the following correct to three decimal places.</div>
            <div class="sub-q">(i) 2.5</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{2.5} \approx 1.581$</div>
            <div class="sub-q">(ii) 0.036</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{0.036} \approx 0.190$</div>
            <div class="sub-q">(iii) 6.4</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{6.4} \approx 2.530$</div>
            <div class="sub-q">(iv) 0.100</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{0.100} \approx 0.316$</div>
        </div>
        <div class="q-block">
            <div class="question">9. Find the least number by which 10368 should be (i) increased (ii) decreased (iii) multiplied (iv) divided to make it a perfect square.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>We find the square root of 10368. $101^2 = 10201$ and $102^2 = 10404$.<br>So, $101^2 < 10368 < 102^2$<br>(i) Increased: To get the next perfect square ($10404$), we add: $10404 - 10368 = 36$<br>(ii) Decreased: To get the previous perfect square ($10201$), we subtract: $10368 - 10201 = 167$<br>Now, prime factorization of $10368 = 2^7 \times 3^4$<br>(iii) Multiplied: To make all powers even, we need to multiply by $2$. (Result will be $2^8 \times 3^4$)<br>(iv) Divided: To make all powers even, we need to divide by $2$. (Result will be $2^6 \times 3^4$)</div>
        </div>
        <div class="q-block">
            <div class="question">10. Find the following.</div>
            <div class="sub-q">(i) $55^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$55^2 = 3025$</div>
            <div class="sub-q">(ii) $98^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$98^2 = 9604$</div>
            <div class="sub-q">(iii) $\sqrt{38}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{38} \approx 6.164$ (to 3 decimal places)</div>
            <div class="sub-q">(iv) $\sqrt{89}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{89} \approx 9.43$ (to 2 decimal places)</div>
            <div class="sub-q">(v) $\sqrt{38.83}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{38.83} \approx 6.23$ (to 2 decimal places)</div>
            <div class="sub-q">(vi) $\sqrt{64.25}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{64.25} \approx 8.016$ (to 3 decimal places)</div>
        </div>
        <div class="q-block">
            <div class="question">11. Use algebraic methods to find the following.</div>
            <div class="sub-q">(i) $52^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(50 + 2)^2 = 50^2 + 2(50)(2) + 2^2 = 2500 + 200 + 4 = 2704$</div>
            <div class="sub-q">(ii) $98^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(100 - 2)^2 = 100^2 - 2(100)(2) + 2^2 = 10000 - 400 + 4 = 9604$</div>
            <div class="sub-q">(iii) $309^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(300 + 9)^2 = 300^2 + 2(300)(9) + 9^2 = 90000 + 5400 + 81 = 95481$</div>
            <div class="sub-q">(iv) $495^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(500 - 5)^2 = 500^2 - 2(500)(5) + 5^2 = 250000 - 5000 + 25 = 245025$</div>
            <div class="sub-q">(v) $96^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(100 - 4)^2 = 100^2 - 2(100)(4) + 4^2 = 10000 - 800 + 16 = 9216$</div>
            <div class="sub-q">(vi) $305^2$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(300 + 5)^2 = 300^2 + 2(300)(5) + 5^2 = 90000 + 3000 + 25 = 93025$</div>
        </div>
        <div class="q-block">
            <div class="question">12. Find in each case the smallest perfect square divisible by the given numbers.</div>
            <div class="sub-q">(i) 2, 4 and 5</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>LCM of $2, 4, 5$ is $20$. <br>Prime factors of $20 = 2^2 \times 5$.<br>To make it a perfect square, we need to multiply by $5$.<br>Smallest perfect square = $20 \times 5 = 100$.</div>
            <div class="sub-q">(ii) 3, 4, 5 and 6</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>LCM of $3, 4, 5, 6$ is $60$. <br>Prime factors of $60 = 2^2 \times 3 \times 5$.<br>To make it a perfect square, we need to multiply by $3 \times 5 = 15$.<br>Smallest perfect square = $60 \times 15 = 900$.</div>
            <div class="sub-q">(iii) 6, 8, 10 and 12</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>LCM of $6, 8, 10, 12$ is $120$. <br>Prime factors of $120 = 2^3 \times 3 \times 5$.<br>To make it a perfect square, we need to multiply by $2 \times 3 \times 5 = 30$.<br>Smallest perfect square = $120 \times 30 = 3600$.</div>
        </div>
        <div class="q-block">
            <div class="question">13. In an auditorium, the number of rows is equal to the number of chairs in each row. If the capacity of the auditorium is 2304, find the number of chairs in a row.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Let the number of rows be $x$. <br>Then, the number of chairs in each row is also $x$.<br>Total capacity = $x \times x = x^2$<br>$x^2 = 2304$<br>$x = \sqrt{2304} = 48$<br>Number of chairs in a row is 48.</div>
        </div>
        <div class="q-block">
            <div class="question">14. In a garden, 1089 rose plants are arranged in such a way that there are as many rows as there are plants in each row. Find the number of rows in the garden.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Let the number of rows be $x$. <br>Then, the number of plants per row is $x$.<br>Total plants = $x \times x = x^2$<br>$x^2 = 1089$<br>$x = \sqrt{1089} = 33$<br>Number of rows in the garden is 33.</div>
        </div>
        <div class="q-block">
            <div class="question">15. An army officer wishes to arrange 4770 soldiers in the form of a square. After arranging he finds that nine soldiers are left out. Find the number of soldiers in each row.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Soldiers placed in the square = $4770 - 9 = 4761$.<br>Let the number of soldiers in each row be $x$.<br>Total soldiers in square = $x^2 = 4761$<br>$x = \sqrt{4761} = 69$<br>Number of soldiers in each row is 69.</div>
        </div>
        <div class="q-block">
            <div class="question">16. Find the least number that must be subtracted from each of the following numbers to get a perfect square. Also, find the square root of this perfect square.</div>
            <div class="sub-q">(i) 9845</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{9845} \approx 99.22$<br>The perfect square just below it is $99^2 = 9801$.<br>Least number to subtract = $9845 - 9801 = 44$.<br>Square root of the perfect square is 99.</div>
            <div class="sub-q">(ii) 7585</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{7585} \approx 87.09$<br>The perfect square just below it is $87^2 = 7569$.<br>Least number to subtract = $7585 - 7569 = 16$.<br>Square root of the perfect square is 87.</div>
            <div class="sub-q">(iii) 786</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{786} \approx 28.03$<br>The perfect square just below it is $28^2 = 784$.<br>Least number to subtract = $786 - 784 = 2$.<br>Square root of the perfect square is 28.</div>
        </div>
        <div class="q-block">
            <div class="question">17. Find the least number which must be added to each of the following numbers to make it a perfect square. Also, find the square root of this perfect square.</div>
            <div class="sub-q">(i) 9389</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{9389} \approx 96.89$<br>The perfect square just above it is $97^2 = 9409$.<br>Least number to add = $9409 - 9389 = 20$.<br>Square root of the perfect square is 97.</div>
            <div class="sub-q">(ii) 5601</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{5601} \approx 74.83$<br>The perfect square just above it is $75^2 = 5625$.<br>Least number to add = $5625 - 5601 = 24$.<br>Square root of the perfect square is 75.</div>
            <div class="sub-q">(iii) 4725</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{4725} \approx 68.73$<br>The perfect square just above it is $69^2 = 4761$.<br>Least number to add = $4761 - 4725 = 36$.<br>Square root of the perfect square is 69.</div>
        </div>
        <div class="q-block">
            <div class="question">18. Find the greatest six-digit number which is a perfect square.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>The greatest 6-digit number is 999999.<br>$\sqrt{999999} \approx 999.999$<br>So, the greatest 6-digit perfect square is $999^2 = 998001$.</div>
        </div>
        <div class="q-block">
            <div class="question">19. Find the smallest six-digit number which is a perfect square.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>The smallest 6-digit number is 100000.<br>$\sqrt{100000} \approx 316.22$<br>So, the smallest 6-digit perfect square is $317^2 = 100489$.</div>
        </div>
        <div class="q-block">
            <div class="question">20. Find the value of each of the following.</div>
            <div class="sub-q">(i) $\sqrt{\frac{1.44}{0.49}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{144/100}{49/100}} = \sqrt{\frac{144}{49}} = \frac{12}{7}$</div>
            <div class="sub-q">(ii) $\sqrt{\frac{32.4}{28.9}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{324/10}{289/10}} = \sqrt{\frac{324}{289}} = \frac{18}{17}$</div>
            <div class="sub-q">(iii) $\sqrt{\frac{0.0025}{0.0196}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{25/10000}{196/10000}} = \sqrt{\frac{25}{196}} = \frac{5}{14}$</div>
            <div class="sub-q">(iv) $\sqrt{1 + \frac{25}{144}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{144 + 25}{144}} = \sqrt{\frac{169}{144}} = \frac{13}{12}$</div>
            <div class="sub-q">(v) $\sqrt{1 - \frac{64}{289}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{\frac{289 - 64}{289}} = \sqrt{\frac{225}{289}} = \frac{15}{17}$</div>
            <div class="sub-q">(vi) $\sqrt{2^3 \times 6^3 \times 27}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{8 \times 216 \times 27} = \sqrt{46656} = 216$<br>(Alternative: $\sqrt{2^3 \times (2 \times 3)^3 \times 3^3} = \sqrt{2^6 \times 3^6} = 2^3 \times 3^3 = 8 \times 27 = 216$)</div>
            <div class="sub-q">(vii) $\frac{\sqrt{9}}{\sqrt{0.09}} + \frac{\sqrt{16}}{\sqrt{0.16}} + \frac{\sqrt{25}}{\sqrt{0.25}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\frac{3}{0.3} + \frac{4}{0.4} + \frac{5}{0.5} = 10 + 10 + 10 = 30$</div>
            <div class="sub-q">(viii) $\sqrt{400} + \sqrt{4} + \sqrt{0.04} + \sqrt{0.0004}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$20 + 2 + 0.2 + 0.02 = 22.22$</div>
            <div class="sub-q">(ix) $\sqrt{182 - \sqrt{156 + \sqrt{169}}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{182 - \sqrt{156 + 13}} = \sqrt{182 - \sqrt{169}} = \sqrt{182 - 13} = \sqrt{169} = 13$</div>
            <div class="sub-q">(x) $\sqrt{382 + \sqrt{341 - \sqrt{289}}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{382 + \sqrt{341 - 17}} = \sqrt{382 + \sqrt{324}} = \sqrt{382 + 18} = \sqrt{400} = 20$</div>
        </div>
        <div class="q-block">
            <div class="question">21. Fill in the blanks.</div>
            <div class="sub-q">(i) The units digit of the square of a number ending in 2 is ...... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>4</b></div>
            <div class="sub-q">(ii) The units digit of the square of a number ending in 9 is ...... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>1</b></div>
            <div class="sub-q">(iii) The units digit of the square root of a number ending in 6 is ...... or ...... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>4</b> or <b>6</b></div>
            <div class="sub-q">(iv) There are ...... natural numbers between the squares of 8 and 9.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>16</b> (since $2 \times 8 = 16$)</div>
            <div class="sub-q">(v) $9^2 - 8^2$ = ...... + 8.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>9</b> (since $a^2 - b^2 = (a-b)(a+b)$, here $(9-8)(9+8) = 1(9+8) = 9+8$)</div>
            <div class="sub-q">(vi) $19^2$ - ...... = 19 + 18.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>$18^2$</b> (since $19^2 - 18^2 = (19-18)(19+18) = 19+18$)</div>
            <div class="sub-q">(vii) If $\sqrt{4096} = 64$ then $\sqrt{4096} + \sqrt{40.96}$ = ....... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt{4096} + \sqrt{40.96} = 64 + 6.4 = $ <b>70.4</b></div>
            <div class="sub-q">(viii) $\sqrt{4} + \sqrt{0.04} + \sqrt{0.0004}$ = .......</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$2 + 0.2 + 0.02 = $ <b>2.22</b></div>
            <div class="sub-q">(ix) 3, 4 and ...... form a Pythagorean triple.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>5</b> (since $3^2 + 4^2 = 5^2$)</div>
        </div>
    </div>
    <div class="container teach-view" id="teach-view-ch3" style="display: none;">
        <button class="btn-close" onclick="exitTeachMode('ch3')">X Exit Teach</button>
        <div class="header">Teach Mode - Chapter 3: Squares and Square Roots</div>
        <ul>
            <li class="main-q-li">1. Find the value of each of the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-0', 'ch3')">(i) $\left(\frac{11}{13}\right)^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-1', 'ch3')">(ii) $\left(-1 \frac{7}{11}\right)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-2', 'ch3')">(iii) $(3.5)^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-3', 'ch3')">(iv) $(0.08)^3$</li>
            <li class="main-q-li">2. Find the square root of each of the following by prime factorisation.</li>
            <li class="clickable-q" onclick="startPresentation('pres-4', 'ch3')">(i) 256</li>
            <li class="clickable-q" onclick="startPresentation('pres-5', 'ch3')">(ii) 324</li>
            <li class="clickable-q" onclick="startPresentation('pres-6', 'ch3')">(iii) 784</li>
            <li class="clickable-q" onclick="startPresentation('pres-7', 'ch3')">(iv) 7056</li>
            <li class="clickable-q" onclick="startPresentation('pres-8', 'ch3')">(v) 28224</li>
            <li class="clickable-q" onclick="startPresentation('pres-9', 'ch3')">(vi) 60025</li>
            <li class="main-q-li">3. Find the square root of each of the following by division.</li>
            <li class="clickable-q" onclick="startPresentation('pres-10', 'ch3')">(i) 841</li>
            <li class="clickable-q" onclick="startPresentation('pres-11', 'ch3')">(ii) 2304</li>
            <li class="clickable-q" onclick="startPresentation('pres-12', 'ch3')">(iii) 39204</li>
            <li class="clickable-q" onclick="startPresentation('pres-13', 'ch3')">(iv) 55225</li>
            <li class="clickable-q" onclick="startPresentation('pres-14', 'ch3')">(v) 177241</li>
            <li class="clickable-q" onclick="startPresentation('pres-15', 'ch3')">(vi) 425104</li>
            <li class="main-q-li">4. Find the square root of each of the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-16', 'ch3')">(i) 13.69</li>
            <li class="clickable-q" onclick="startPresentation('pres-17', 'ch3')">(ii) 0.002025</li>
            <li class="clickable-q" onclick="startPresentation('pres-18', 'ch3')">(iii) 1.5129</li>
            <li class="clickable-q" onclick="startPresentation('pres-19', 'ch3')">(iv) 20.7936</li>
            <li class="clickable-q" onclick="startPresentation('pres-20', 'ch3')">(v) 6146.56</li>
            <li class="clickable-q" onclick="startPresentation('pres-21', 'ch3')">(vi) 1.024144</li>
            <li class="main-q-li">5. Find the square root of each of the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-22', 'ch3')">(i) $\frac{169}{484}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-23', 'ch3')">(ii) $5 \frac{580}{729}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-24', 'ch3')">(iii) $12 \frac{52}{81}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-25', 'ch3')">(iv) 0.0009</li>
            <li class="clickable-q" onclick="startPresentation('pres-26', 'ch3')">(v) 4.41</li>
            <li class="main-q-li">6. Find the square root of each of the following correct to two decimal places.</li>
            <li class="clickable-q" onclick="startPresentation('pres-27', 'ch3')">(i) 2</li>
            <li class="clickable-q" onclick="startPresentation('pres-28', 'ch3')">(ii) 3</li>
            <li class="clickable-q" onclick="startPresentation('pres-29', 'ch3')">(iii) 8</li>
            <li class="clickable-q" onclick="startPresentation('pres-30', 'ch3')">(iv) 11</li>
            <li class="clickable-q" onclick="startPresentation('pres-31', 'ch3')">(v) 35</li>
            <li class="clickable-q" onclick="startPresentation('pres-32', 'ch3')">(vi) 99</li>
            <li class="main-q-li">7. Find the value of $\sqrt{5}$ correct to two decimal places. Then, find the value of the square root of $\frac{3-\sqrt{5}}{3+\sqrt{5}}$ correct to two decimal places.</li>
            <li class="clickable-q" onclick="startPresentation('pres-33', 'ch3')">Solution</li>
            <li class="main-q-li">8. Find the square root of each of the following correct to three decimal places.</li>
            <li class="clickable-q" onclick="startPresentation('pres-34', 'ch3')">(i) 2.5</li>
            <li class="clickable-q" onclick="startPresentation('pres-35', 'ch3')">(ii) 0.036</li>
            <li class="clickable-q" onclick="startPresentation('pres-36', 'ch3')">(iii) 6.4</li>
            <li class="clickable-q" onclick="startPresentation('pres-37', 'ch3')">(iv) 0.100</li>
            <li class="main-q-li">9. Find the least number by which 10368 should be (i) increased (ii) decreased (iii) multiplied (iv) divided to make it a perfect square.</li>
            <li class="clickable-q" onclick="startPresentation('pres-38', 'ch3')">Solution</li>
            <li class="main-q-li">10. Find the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-39', 'ch3')">(i) $55^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-40', 'ch3')">(ii) $98^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-41', 'ch3')">(iii) $\sqrt{38}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-42', 'ch3')">(iv) $\sqrt{89}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-43', 'ch3')">(v) $\sqrt{38.83}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-44', 'ch3')">(vi) $\sqrt{64.25}$</li>
            <li class="main-q-li">11. Use algebraic methods to find the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-45', 'ch3')">(i) $52^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-46', 'ch3')">(ii) $98^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-47', 'ch3')">(iii) $309^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-48', 'ch3')">(iv) $495^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-49', 'ch3')">(v) $96^2$</li>
            <li class="clickable-q" onclick="startPresentation('pres-50', 'ch3')">(vi) $305^2$</li>
            <li class="main-q-li">12. Find in each case the smallest perfect square divisible by the given numbers.</li>
            <li class="clickable-q" onclick="startPresentation('pres-51', 'ch3')">(i) 2, 4 and 5</li>
            <li class="clickable-q" onclick="startPresentation('pres-52', 'ch3')">(ii) 3, 4, 5 and 6</li>
            <li class="clickable-q" onclick="startPresentation('pres-53', 'ch3')">(iii) 6, 8, 10 and 12</li>
            <li class="main-q-li">13. In an auditorium, the number of rows is equal to the number of chairs in each row. If the capacity of the auditorium is 2304, find the number of chairs in a row.</li>
            <li class="clickable-q" onclick="startPresentation('pres-54', 'ch3')">Solution</li>
            <li class="main-q-li">14. In a garden, 1089 rose plants are arranged in such a way that there are as many rows as there are plants in each row. Find the number of rows in the garden.</li>
            <li class="clickable-q" onclick="startPresentation('pres-55', 'ch3')">Solution</li>
            <li class="main-q-li">15. An army officer wishes to arrange 4770 soldiers in the form of a square. After arranging he finds that nine soldiers are left out. Find the number of soldiers in each row.</li>
            <li class="clickable-q" onclick="startPresentation('pres-56', 'ch3')">Solution</li>
            <li class="main-q-li">16. Find the least number that must be subtracted from each of the following numbers to get a perfect square. Also, find the square root of this perfect square.</li>
            <li class="clickable-q" onclick="startPresentation('pres-57', 'ch3')">(i) 9845</li>
            <li class="clickable-q" onclick="startPresentation('pres-58', 'ch3')">(ii) 7585</li>
            <li class="clickable-q" onclick="startPresentation('pres-59', 'ch3')">(iii) 786</li>
            <li class="main-q-li">17. Find the least number which must be added to each of the following numbers to make it a perfect square. Also, find the square root of this perfect square.</li>
            <li class="clickable-q" onclick="startPresentation('pres-60', 'ch3')">(i) 9389</li>
            <li class="clickable-q" onclick="startPresentation('pres-61', 'ch3')">(ii) 5601</li>
            <li class="clickable-q" onclick="startPresentation('pres-62', 'ch3')">(iii) 4725</li>
            <li class="main-q-li">18. Find the greatest six-digit number which is a perfect square.</li>
            <li class="clickable-q" onclick="startPresentation('pres-63', 'ch3')">Solution</li>
            <li class="main-q-li">19. Find the smallest six-digit number which is a perfect square.</li>
            <li class="clickable-q" onclick="startPresentation('pres-64', 'ch3')">Solution</li>
            <li class="main-q-li">20. Find the value of each of the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-65', 'ch3')">(i) $\sqrt{\frac{1.44}{0.49}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-66', 'ch3')">(ii) $\sqrt{\frac{32.4}{28.9}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-67', 'ch3')">(iii) $\sqrt{\frac{0.0025}{0.0196}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-68', 'ch3')">(iv) $\sqrt{1 + \frac{25}{144}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-69', 'ch3')">(v) $\sqrt{1 - \frac{64}{289}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-70', 'ch3')">(vi) $\sqrt{2^3 \times 6^3 \times 27}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-71', 'ch3')">(vii) $\frac{\sqrt{9}}{\sqrt{0.09}} + \frac{\sqrt{16}}{\sqrt{0.16}} + \frac{\sqrt{25}}{\sqrt{0.25}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-72', 'ch3')">(viii) $\sqrt{400} + \sqrt{4} + \sqrt{0.04} + \sqrt{0.0004}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-73', 'ch3')">(ix) $\sqrt{182 - \sqrt{156 + \sqrt{169}}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-74', 'ch3')">(x) $\sqrt{382 + \sqrt{341 - \sqrt{289}}}$</li>
            <li class="main-q-li">21. Fill in the blanks.</li>
            <li class="clickable-q" onclick="startPresentation('pres-75', 'ch3')">(i) The units digit of the square of a number ending in 2 is ...... </li>
            <li class="clickable-q" onclick="startPresentation('pres-76', 'ch3')">(ii) The units digit of the square of a number ending in 9 is ...... </li>
            <li class="clickable-q" onclick="startPresentation('pres-77', 'ch3')">(iii) The units digit of the square root of a number ending in 6 is ...... or ...... </li>
            <li class="clickable-q" onclick="startPresentation('pres-78', 'ch3')">(iv) There are ...... natural numbers between the squares of 8 and 9.</li>
            <li class="clickable-q" onclick="startPresentation('pres-79', 'ch3')">(v) $9^2 - 8^2$ = ...... + 8.</li>
            <li class="clickable-q" onclick="startPresentation('pres-80', 'ch3')">(vi) $19^2$ - ...... = 19 + 18.</li>
            <li class="clickable-q" onclick="startPresentation('pres-81', 'ch3')">(vii) If $\sqrt{4096} = 64$ then $\sqrt{4096} + \sqrt{40.96}$ = ....... </li>
            <li class="clickable-q" onclick="startPresentation('pres-82', 'ch3')">(viii) $\sqrt{4} + \sqrt{0.04} + \sqrt{0.0004}$ = .......</li>
            <li class="clickable-q" onclick="startPresentation('pres-83', 'ch3')">(ix) 3, 4 and ...... form a Pythagorean triple.</li>
        </ul>
    </div>
    <div class="container chapter-view" id="normal-view-ch4" style="display: none;">
        <button class="btn-top-back" onclick="goHome()">⬅ Back to Home</button>
        <div class="header">Chapter 4: Cubes and Cube Roots</div>
        <button class="btn-teach" onclick="enterTeachMode('ch4')">👨‍🏫 Teach Mode</button>
        <div class="q-block">
            <div class="question">1. Find the value of each of the following.</div>
            <div class="sub-q">(i) $\left(\frac{5}{6}\right)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\left(\frac{5}{6}\right)^3 = \frac{5^3}{6^3} = \frac{125}{216}$</div>
            <div class="sub-q">(ii) $\left(-1 \frac{7}{11}\right)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\left(-1 \frac{7}{11}\right)^3 = \left(\frac{-18}{11}\right)^3 = \frac{(-18)^3}{11^3} = \frac{-5832}{1331} = -4 \frac{508}{1331}$</div>
            <div class="sub-q">(iii) $(2.5)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(2.5)^3 = \left(\frac{25}{10}\right)^3 = \frac{15625}{1000} = 15.625$</div>
            <div class="sub-q">(iv) $(0.08)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(0.08)^3 = \left(\frac{8}{100}\right)^3 = \frac{512}{1000000} = 0.000512$</div>
            <div class="sub-q">(v) $(-1.1)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(-1.1)^3 = \left(\frac{-11}{10}\right)^3 = \frac{-1331}{1000} = -1.331$</div>
            <div class="sub-q">(vi) $\left(-\frac{7}{3}\right)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\left(-\frac{7}{3}\right)^3 = \frac{(-7)^3}{3^3} = \frac{-343}{27}$</div>
            <div class="sub-q">(vii) $(-9)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(-9)^3 = -729$</div>
            <div class="sub-q">(viii) $(-0.5)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(-0.5)^3 = \left(\frac{-5}{10}\right)^3 = \frac{-125}{1000} = -0.125$</div>
            <div class="sub-q">(ix) $(-20)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(-20)^3 = -8000$</div>
            <div class="sub-q">(x) $(-0.013)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(-0.013)^3 = \left(\frac{-13}{1000}\right)^3 = \frac{-2197}{1000000000} = -0.000002197$</div>
            <div class="sub-q">(xi) $(25)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$(25)^3 = 15625$</div>
            <div class="sub-q">(xii) $\left(2 \frac{1}{7}\right)^3$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\left(2 \frac{1}{7}\right)^3 = \left(\frac{15}{7}\right)^3 = \frac{15^3}{7^3} = \frac{3375}{343} = 9 \frac{288}{343}$</div>
        </div>
        <div class="q-block">
            <div class="question">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.</div>
            <div class="sub-q">(i) 128</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$128 = 2^7$. (Not a perfect cube)</div>
            <div class="sub-q">(ii) 243</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$243 = 3^5$. (Not a perfect cube)</div>
            <div class="sub-q">(iii) 343</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$343 = 7^3$. (Perfect cube of 7)</div>
            <div class="sub-q">(iv) 4000</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$4000 = 2^5 \times 5^3$. (Not a perfect cube)</div>
            <div class="sub-q">(v) 3456</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$3456 = 2^7 \times 3^3$. (Not a perfect cube)</div>
            <div class="sub-q">(vi) 2048</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$2048 = 2^{11}$. (Not a perfect cube)</div>
            <div class="sub-q">(vii) 2197</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$2197 = 13^3$. (Perfect cube of 13)</div>
            <div class="sub-q">(viii) 1000000</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$1000000 = 100^3$. (Perfect cube of 100)</div>
            <div class="sub-q">(ix) 2744</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$2744 = 14^3$. (Perfect cube of 14)</div>
        </div>
        <div class="q-block">
            <div class="question">3. Which of the following are cubes of even numbers and which are of odd numbers?</div>
            <div class="sub-q">(i) 8000</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>8000 is an even number, so it is the cube of an **even** number.</div>
            <div class="sub-q">(ii) 9261</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>9261 is an odd number, so it is the cube of an **odd** number.</div>
            <div class="sub-q">(iii) 4096</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>4096 is an even number, so it is the cube of an **even** number.</div>
            <div class="sub-q">(iv) 6859</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>6859 is an odd number, so it is the cube of an **odd** number.</div>
            <div class="sub-q">(v) 12167</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>12167 is an odd number, so it is the cube of an **odd** number.</div>
            <div class="sub-q">(vi) 4913</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>4913 is an odd number, so it is the cube of an **odd** number.</div>
            <div class="sub-q">(vii) 13824</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>13824 is an even number, so it is the cube of an **even** number.</div>
            <div class="sub-q">(viii) 17576</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>17576 is an even number, so it is the cube of an **even** number.</div>
        </div>
        <div class="q-block">
            <div class="question">4. Find each of the following.</div>
            <div class="sub-q">(i) $\sqrt[3]{512}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{512} = \sqrt[3]{8^3} = 8$</div>
            <div class="sub-q">(ii) $\sqrt[3]{2744}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{2744} = \sqrt[3]{14^3} = 14$</div>
            <div class="sub-q">(iii) $\sqrt[3]{729}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{729} = \sqrt[3]{9^3} = 9$</div>
            <div class="sub-q">(iv) $\sqrt[3]{1728}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{1728} = \sqrt[3]{12^3} = 12$</div>
            <div class="sub-q">(v) $\sqrt[3]{1000}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{1000} = \sqrt[3]{10^3} = 10$</div>
            <div class="sub-q">(vi) $\sqrt[3]{-8000}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{-8000} = \sqrt[3]{(-20)^3} = -20$</div>
            <div class="sub-q">(vii) $\sqrt[3]{-4096}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{-4096} = \sqrt[3]{(-16)^3} = -16$</div>
            <div class="sub-q">(viii) $\sqrt[3]{\frac{27}{125}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{\frac{27}{125}} = \frac{\sqrt[3]{27}}{\sqrt[3]{125}} = \frac{3}{5}$</div>
            <div class="sub-q">(ix) $\sqrt[3]{\frac{-125}{64}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{\frac{-125}{64}} = \frac{\sqrt[3]{-125}}{\sqrt[3]{64}} = \frac{-5}{4}$</div>
            <div class="sub-q">(x) $\sqrt[3]{0.001}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{0.001} = \sqrt[3]{\frac{1}{1000}} = \frac{1}{10} = 0.1$</div>
            <div class="sub-q">(xi) $\sqrt[3]{0.125}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{0.125} = \sqrt[3]{\frac{125}{1000}} = \frac{5}{10} = 0.5$</div>
            <div class="sub-q">(xii) $\sqrt[3]{\frac{27}{64 \times 125}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\frac{\sqrt[3]{27}}{\sqrt[3]{64} \times \sqrt[3]{125}} = \frac{3}{4 \times 5} = \frac{3}{20}$</div>
            <div class="sub-q">(xiii) $\sqrt[3]{\frac{729}{125 \times 1000}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\frac{\sqrt[3]{729}}{\sqrt[3]{125} \times \sqrt[3]{1000}} = \frac{9}{5 \times 10} = \frac{9}{50}$</div>
            <div class="sub-q">(xiv) $\sqrt[3]{125 \times 64 \times 8}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{125} \times \sqrt[3]{64} \times \sqrt[3]{8} = 5 \times 4 \times 2 = 40$</div>
            <div class="sub-q">(xv) $\sqrt[3]{16 \times 500}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{8000} = 20$</div>
            <div class="sub-q">(xvi) $\sqrt[3]{625 \times (-1600)}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{-1000000} = -100$</div>
            <div class="sub-q">(xvii) $\sqrt[3]{\frac{343}{2500 \times 400}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{\frac{343}{1000000}} = \frac{7}{100}$</div>
            <div class="sub-q">(xviii) $\sqrt[3]{1 - \frac{854}{729}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{\frac{729 - 854}{729}} = \sqrt[3]{\frac{-125}{729}} = \frac{-5}{9}$</div>
            <div class="sub-q">(xix) $\sqrt[3]{4 + \sqrt[3]{61 + \sqrt[3]{27}}}$</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$\sqrt[3]{4 + \sqrt[3]{61 + 3}}$<br>$= \sqrt[3]{4 + \sqrt[3]{64}}$<br>$= \sqrt[3]{4 + 4} = \sqrt[3]{8} = 2$</div>
        </div>
        <div class="q-block">
            <div class="question">5. Find the least number by which each of the following numbers should be multiplied to make it a perfect cube. Also, find the cube root of the product in each case.</div>
            <div class="sub-q">(i) 5488</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Prime factorization: $5488 = 2^4 \times 7^3$<br>To make the powers multiples of 3, multiply by $2^2 = 4$.<br>Least number = 4<br>New product = $2^6 \times 7^3$<br>Cube root = $2^2 \times 7 = 4 \times 7 = 28$</div>
            <div class="sub-q">(ii) 34992</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Prime factorization: $34992 = 2^4 \times 3^7$<br>To make the powers multiples of 3, multiply by $2^2 \times 3^2 = 4 \times 9 = 36$.<br>Least number = 36<br>New product = $2^6 \times 3^9$<br>Cube root = $2^2 \times 3^3 = 4 \times 27 = 108$</div>
            <div class="sub-q">(iii) 15552</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Prime factorization: $15552 = 2^6 \times 3^5$<br>To make the powers multiples of 3, multiply by $3^1 = 3$.<br>Least number = 3<br>New product = $2^6 \times 3^6$<br>Cube root = $2^2 \times 3^2 = 4 \times 9 = 36$</div>
        </div>
        <div class="q-block">
            <div class="question">6. Find the least number by which each of the following numbers should be divided to make it a perfect cube. Also, find the cube root of each perfect cube.</div>
            <div class="sub-q">(i) 5184</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Prime factorization: $5184 = 2^6 \times 3^4$<br>To leave powers as multiples of 3, divide by $3^1 = 3$.<br>Least number = 3<br>New quotient = $2^6 \times 3^3$<br>Cube root = $2^2 \times 3 = 4 \times 3 = 12$</div>
            <div class="sub-q">(ii) 5488</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Prime factorization: $5488 = 2^4 \times 7^3$<br>To leave powers as multiples of 3, divide by $2^1 = 2$.<br>Least number = 2<br>New quotient = $2^3 \times 7^3$<br>Cube root = $2 \times 7 = 14$</div>
            <div class="sub-q">(iii) 23328</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>Prime factorization: $23328 = 2^5 \times 3^6$<br>To leave powers as multiples of 3, divide by $2^2 = 4$.<br>Least number = 4<br>New quotient = $2^3 \times 3^6$<br>Cube root = $2 \times 3^2 = 2 \times 9 = 18$</div>
        </div>
        <div class="q-block">
            <div class="question">7. Fill in the blanks.</div>
            <div class="sub-q">(i) The units digit in the cube of 1137 is ...... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>3</b> (since $7^3 = 343$, unit digit is 3)</div>
            <div class="sub-q">(ii) The ones digit in the cube of 1004 is ...... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>4</b> (since $4^3 = 64$, unit digit is 4)</div>
            <div class="sub-q">(iii) The cube of an odd number is always an ...... number.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>odd</b></div>
            <div class="sub-q">(iv) The cube of an even number is always an ...... number.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>even</b></div>
            <div class="sub-q">(v) The least natural number by which 1600 is to be multiplied to make it a perfect cube is ....... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$1600 = 2^6 \times 5^2$. Needs to be multiplied by <b>5</b>.</div>
            <div class="sub-q">(vi) The least natural number by which 1024 is to be divided to make it a perfect cube is ....... </div>
            <div class="solution"><span class="sol-label">Solution:</span><br>$1024 = 2^{10}$. Needs to be divided by $2^1$ = <b>2</b>.</div>
        </div>
        <div class="q-block">
            <div class="question">8. Identify the false statements only.</div>
            <div class="sub-q">(i) The cube of an odd number is odd.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>True</div>
            <div class="sub-q">(ii) The cube of an even number is even.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br>True</div>
            <div class="sub-q">(iii) The cube of a negative number is positive.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>False</b> (It is negative)</div>
            <div class="sub-q">(iv) The cube roots of 27 are 3 and -3.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>False</b> (The only real cube root is 3)</div>
            <div class="sub-q">(v) 333 is a perfect cube.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>False</b> (7^3 = 343)</div>
            <div class="sub-q">(vi) $\sqrt[3]{27+8} = \sqrt[3]{27} + \sqrt[3]{8}$.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>False</b> ($\sqrt[3]{35} \neq 3 + 2$)</div>
            <div class="sub-q">(vii) There is no cube root of a negative number.</div>
            <div class="solution"><span class="sol-label">Solution:</span><br><b>False</b> (e.g., $\sqrt[3]{-8} = -2$)</div>
        </div>
    </div>
    <div class="container teach-view" id="teach-view-ch4" style="display: none;">
        <button class="btn-close" onclick="exitTeachMode('ch4')">X Exit Teach</button>
        <div class="header">Teach Mode - Chapter 4: Cubes and Cube Roots</div>
        <ul>
            <li class="main-q-li">1. Find the value of each of the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-84', 'ch4')">(i) $\left(\frac{5}{6}\right)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-85', 'ch4')">(ii) $\left(-1 \frac{7}{11}\right)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-86', 'ch4')">(iii) $(2.5)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-87', 'ch4')">(iv) $(0.08)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-88', 'ch4')">(v) $(-1.1)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-89', 'ch4')">(vi) $\left(-\frac{7}{3}\right)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-90', 'ch4')">(vii) $(-9)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-91', 'ch4')">(viii) $(-0.5)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-92', 'ch4')">(ix) $(-20)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-93', 'ch4')">(x) $(-0.013)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-94', 'ch4')">(xi) $(25)^3$</li>
            <li class="clickable-q" onclick="startPresentation('pres-95', 'ch4')">(xii) $\left(2 \frac{1}{7}\right)^3$</li>
            <li class="main-q-li">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.</li>
            <li class="clickable-q" onclick="startPresentation('pres-96', 'ch4')">(i) 128</li>
            <li class="clickable-q" onclick="startPresentation('pres-97', 'ch4')">(ii) 243</li>
            <li class="clickable-q" onclick="startPresentation('pres-98', 'ch4')">(iii) 343</li>
            <li class="clickable-q" onclick="startPresentation('pres-99', 'ch4')">(iv) 4000</li>
            <li class="clickable-q" onclick="startPresentation('pres-100', 'ch4')">(v) 3456</li>
            <li class="clickable-q" onclick="startPresentation('pres-101', 'ch4')">(vi) 2048</li>
            <li class="clickable-q" onclick="startPresentation('pres-102', 'ch4')">(vii) 2197</li>
            <li class="clickable-q" onclick="startPresentation('pres-103', 'ch4')">(viii) 1000000</li>
            <li class="clickable-q" onclick="startPresentation('pres-104', 'ch4')">(ix) 2744</li>
            <li class="main-q-li">3. Which of the following are cubes of even numbers and which are of odd numbers?</li>
            <li class="clickable-q" onclick="startPresentation('pres-105', 'ch4')">(i) 8000</li>
            <li class="clickable-q" onclick="startPresentation('pres-106', 'ch4')">(ii) 9261</li>
            <li class="clickable-q" onclick="startPresentation('pres-107', 'ch4')">(iii) 4096</li>
            <li class="clickable-q" onclick="startPresentation('pres-108', 'ch4')">(iv) 6859</li>
            <li class="clickable-q" onclick="startPresentation('pres-109', 'ch4')">(v) 12167</li>
            <li class="clickable-q" onclick="startPresentation('pres-110', 'ch4')">(vi) 4913</li>
            <li class="clickable-q" onclick="startPresentation('pres-111', 'ch4')">(vii) 13824</li>
            <li class="clickable-q" onclick="startPresentation('pres-112', 'ch4')">(viii) 17576</li>
            <li class="main-q-li">4. Find each of the following.</li>
            <li class="clickable-q" onclick="startPresentation('pres-113', 'ch4')">(i) $\sqrt[3]{512}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-114', 'ch4')">(ii) $\sqrt[3]{2744}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-115', 'ch4')">(iii) $\sqrt[3]{729}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-116', 'ch4')">(iv) $\sqrt[3]{1728}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-117', 'ch4')">(v) $\sqrt[3]{1000}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-118', 'ch4')">(vi) $\sqrt[3]{-8000}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-119', 'ch4')">(vii) $\sqrt[3]{-4096}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-120', 'ch4')">(viii) $\sqrt[3]{\frac{27}{125}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-121', 'ch4')">(ix) $\sqrt[3]{\frac{-125}{64}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-122', 'ch4')">(x) $\sqrt[3]{0.001}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-123', 'ch4')">(xi) $\sqrt[3]{0.125}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-124', 'ch4')">(xii) $\sqrt[3]{\frac{27}{64 \times 125}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-125', 'ch4')">(xiii) $\sqrt[3]{\frac{729}{125 \times 1000}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-126', 'ch4')">(xiv) $\sqrt[3]{125 \times 64 \times 8}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-127', 'ch4')">(xv) $\sqrt[3]{16 \times 500}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-128', 'ch4')">(xvi) $\sqrt[3]{625 \times (-1600)}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-129', 'ch4')">(xvii) $\sqrt[3]{\frac{343}{2500 \times 400}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-130', 'ch4')">(xviii) $\sqrt[3]{1 - \frac{854}{729}}$</li>
            <li class="clickable-q" onclick="startPresentation('pres-131', 'ch4')">(xix) $\sqrt[3]{4 + \sqrt[3]{61 + \sqrt[3]{27}}}$</li>
            <li class="main-q-li">5. Find the least number by which each of the following numbers should be multiplied to make it a perfect cube. Also, find the cube root of the product in each case.</li>
            <li class="clickable-q" onclick="startPresentation('pres-132', 'ch4')">(i) 5488</li>
            <li class="clickable-q" onclick="startPresentation('pres-133', 'ch4')">(ii) 34992</li>
            <li class="clickable-q" onclick="startPresentation('pres-134', 'ch4')">(iii) 15552</li>
            <li class="main-q-li">6. Find the least number by which each of the following numbers should be divided to make it a perfect cube. Also, find the cube root of each perfect cube.</li>
            <li class="clickable-q" onclick="startPresentation('pres-135', 'ch4')">(i) 5184</li>
            <li class="clickable-q" onclick="startPresentation('pres-136', 'ch4')">(ii) 5488</li>
            <li class="clickable-q" onclick="startPresentation('pres-137', 'ch4')">(iii) 23328</li>
            <li class="main-q-li">7. Fill in the blanks.</li>
            <li class="clickable-q" onclick="startPresentation('pres-138', 'ch4')">(i) The units digit in the cube of 1137 is ...... </li>
            <li class="clickable-q" onclick="startPresentation('pres-139', 'ch4')">(ii) The ones digit in the cube of 1004 is ...... </li>
            <li class="clickable-q" onclick="startPresentation('pres-140', 'ch4')">(iii) The cube of an odd number is always an ...... number.</li>
            <li class="clickable-q" onclick="startPresentation('pres-141', 'ch4')">(iv) The cube of an even number is always an ...... number.</li>
            <li class="clickable-q" onclick="startPresentation('pres-142', 'ch4')">(v) The least natural number by which 1600 is to be multiplied to make it a perfect cube is ....... </li>
            <li class="clickable-q" onclick="startPresentation('pres-143', 'ch4')">(vi) The least natural number by which 1024 is to be divided to make it a perfect cube is ....... </li>
            <li class="main-q-li">8. Identify the false statements only.</li>
            <li class="clickable-q" onclick="startPresentation('pres-144', 'ch4')">(i) The cube of an odd number is odd.</li>
            <li class="clickable-q" onclick="startPresentation('pres-145', 'ch4')">(ii) The cube of an even number is even.</li>
            <li class="clickable-q" onclick="startPresentation('pres-146', 'ch4')">(iii) The cube of a negative number is positive.</li>
            <li class="clickable-q" onclick="startPresentation('pres-147', 'ch4')">(iv) The cube roots of 27 are 3 and -3.</li>
            <li class="clickable-q" onclick="startPresentation('pres-148', 'ch4')">(v) 333 is a perfect cube.</li>
            <li class="clickable-q" onclick="startPresentation('pres-149', 'ch4')">(vi) $\sqrt[3]{27+8} = \sqrt[3]{27} + \sqrt[3]{8}$.</li>
            <li class="clickable-q" onclick="startPresentation('pres-150', 'ch4')">(vii) There is no cube root of a negative number.</li>
        </ul>
    </div>

    <!-- PRESENTATION VIEW -->
    <div class="container" id="presentation-view" style="display: none;">
        <button class="btn-close" style="z-index: 100;" onclick="closePresentation()">X Close</button>
        <button class="nav-q-btn btn-prev-q" id="btn-prev-q" onclick="prevQuestion()" style="display:none;">⬅ Prev Q</button>
        <button class="nav-q-btn btn-next-q" id="btn-next-q" onclick="nextQuestion()" style="display:none;">Next Q ➡</button>
        <div id="pres-0" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(i) $\left(\frac{11}{13}\right)^2$</div>
            <div class="pres-step">$\left(\frac{11}{13}\right)^2 = \frac{11^2}{13^2} = \frac{121}{169}$</div>
        </div>
        <div id="pres-1" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(ii) $\left(-1 \frac{7}{11}\right)^3$</div>
            <div class="pres-step">$\left(-1 \frac{7}{11}\right)^3 = \left(\frac{-18}{11}\right)^3 = \frac{(-18)^3}{11^3} = \frac{-5832}{1331}$</div>
        </div>
        <div id="pres-2" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(iii) $(3.5)^2$</div>
            <div class="pres-step">$(3.5)^2 = \left(\frac{35}{10}\right)^2 = \frac{1225}{100} = 12.25$</div>
        </div>
        <div id="pres-3" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(iv) $(0.08)^3$</div>
            <div class="pres-step">$(0.08)^3 = \left(\frac{8}{100}\right)^3 = \frac{512}{1000000} = 0.000512$</div>
        </div>
        <div id="pres-4" class="pres-container" style="display:none;">
            <div class="pres-q">2. Find the square root of each of the following by prime factorisation.<br>(i) 256</div>
            <div class="pres-step">$256 = 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 = 2^8$</div>
            <div class="pres-step">$\sqrt{256} = \sqrt{2^8} = 2^4 = 16$</div>
        </div>
        <div id="pres-5" class="pres-container" style="display:none;">
            <div class="pres-q">2. Find the square root of each of the following by prime factorisation.<br>(ii) 324</div>
            <div class="pres-step">$324 = 2 \times 2 \times 3 \times 3 \times 3 \times 3 = 2^2 \times 3^4$</div>
            <div class="pres-step">$\sqrt{324} = 2 \times 3^2 = 2 \times 9 = 18$</div>
        </div>
        <div id="pres-6" class="pres-container" style="display:none;">
            <div class="pres-q">2. Find the square root of each of the following by prime factorisation.<br>(iii) 784</div>
            <div class="pres-step">$784 = 2 \times 2 \times 2 \times 2 \times 7 \times 7 = 2^4 \times 7^2$</div>
            <div class="pres-step">$\sqrt{784} = 2^2 \times 7 = 4 \times 7 = 28$</div>
        </div>
        <div id="pres-7" class="pres-container" style="display:none;">
            <div class="pres-q">2. Find the square root of each of the following by prime factorisation.<br>(iv) 7056</div>
            <div class="pres-step">$7056 = 2^4 \times 3^2 \times 7^2$</div>
            <div class="pres-step">$\sqrt{7056} = 2^2 \times 3 \times 7 = 4 \times 21 = 84$</div>
        </div>
        <div id="pres-8" class="pres-container" style="display:none;">
            <div class="pres-q">2. Find the square root of each of the following by prime factorisation.<br>(v) 28224</div>
            <div class="pres-step">$28224 = 2^6 \times 3^2 \times 7^2$</div>
            <div class="pres-step">$\sqrt{28224} = 2^3 \times 3 \times 7 = 8 \times 21 = 168$</div>
        </div>
        <div id="pres-9" class="pres-container" style="display:none;">
            <div class="pres-q">2. Find the square root of each of the following by prime factorisation.<br>(vi) 60025</div>
            <div class="pres-step">$60025 = 5^2 \times 7^4$</div>
            <div class="pres-step">$\sqrt{60025} = 5 \times 7^2 = 5 \times 49 = 245$</div>
        </div>
        <div id="pres-10" class="pres-container" style="display:none;">
            <div class="pres-q">3. Find the square root of each of the following by division.<br>(i) 841</div>
            <div class="pres-step">$$\begin{array}{r|l} & 29 \\ \hline 2 & \overline{8}\overline{41} \\ & -4 \\ \hline 49 & 441 \\ & -441 \\ \hline & 0 \end{array}$$</div>
            <div class="pres-step">$\sqrt{841} = 29$</div>
        </div>
        <div id="pres-11" class="pres-container" style="display:none;">
            <div class="pres-q">3. Find the square root of each of the following by division.<br>(ii) 2304</div>
            <div class="pres-step">$$\begin{array}{r|l} & 48 \\ \hline 4 & \overline{23}\overline{04} \\ & -16 \\ \hline 88 & 704 \\ & -704 \\ \hline & 0 \end{array}$$</div>
            <div class="pres-step">$\sqrt{2304} = 48$</div>
        </div>
        <div id="pres-12" class="pres-container" style="display:none;">
            <div class="pres-q">3. Find the square root of each of the following by division.<br>(iii) 39204</div>
            <div class="pres-step">$$\begin{array}{r|l} & 198 \\ \hline 1 & \overline{3}\overline{92}\overline{04} \\ & -1 \\ \hline 29 & 292 \\ & -261 \\ \hline 388 & 3104 \\ & -3104 \\ \hline & 0 \end{array}$$</div>
            <div class="pres-step">$\sqrt{39204} = 198$</div>
        </div>
        <div id="pres-13" class="pres-container" style="display:none;">
            <div class="pres-q">3. Find the square root of each of the following by division.<br>(iv) 55225</div>
            <div class="pres-step">$$\begin{array}{r|l} & 235 \\ \hline 2 & \overline{5}\overline{52}\overline{25} \\ & -4 \\ \hline 43 & 152 \\ & -129 \\ \hline 465 & 2325 \\ & -2325 \\ \hline & 0 \end{array}$$</div>
            <div class="pres-step">$\sqrt{55225} = 235$</div>
        </div>
        <div id="pres-14" class="pres-container" style="display:none;">
            <div class="pres-q">3. Find the square root of each of the following by division.<br>(v) 177241</div>
            <div class="pres-step">$$\begin{array}{r|l} & 421 \\ \hline 4 & \overline{17}\overline{72}\overline{41} \\ & -16 \\ \hline 82 & 172 \\ & -164 \\ \hline 841 & 841 \\ & -841 \\ \hline & 0 \end{array}$$</div>
            <div class="pres-step">$\sqrt{177241} = 421$</div>
        </div>
        <div id="pres-15" class="pres-container" style="display:none;">
            <div class="pres-q">3. Find the square root of each of the following by division.<br>(vi) 425104</div>
            <div class="pres-step">$$\begin{array}{r|l} & 652 \\ \hline 6 & \overline{42}\overline{51}\overline{04} \\ & -36 \\ \hline 125 & 651 \\ & -625 \\ \hline 1302 & 2604 \\ & -2604 \\ \hline & 0 \end{array}$$</div>
            <div class="pres-step">$\sqrt{425104} = 652$</div>
        </div>
        <div id="pres-16" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find the square root of each of the following.<br>(i) 13.69</div>
            <div class="pres-step">$\sqrt{13.69} = \sqrt{\frac{1369}{100}} = \frac{37}{10} = 3.7$</div>
        </div>
        <div id="pres-17" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find the square root of each of the following.<br>(ii) 0.002025</div>
            <div class="pres-step">$\sqrt{0.002025} = \sqrt{\frac{2025}{1000000}} = \frac{45}{1000} = 0.045$</div>
        </div>
        <div id="pres-18" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find the square root of each of the following.<br>(iii) 1.5129</div>
            <div class="pres-step">$\sqrt{1.5129} = \sqrt{\frac{15129}{10000}} = \frac{123}{100} = 1.23$</div>
        </div>
        <div id="pres-19" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find the square root of each of the following.<br>(iv) 20.7936</div>
            <div class="pres-step">$\sqrt{20.7936} = \sqrt{\frac{207936}{10000}} = \frac{456}{100} = 4.56$</div>
        </div>
        <div id="pres-20" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find the square root of each of the following.<br>(v) 6146.56</div>
            <div class="pres-step">$\sqrt{6146.56} = \sqrt{\frac{614656}{100}} = \frac{784}{10} = 78.4$</div>
        </div>
        <div id="pres-21" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find the square root of each of the following.<br>(vi) 1.024144</div>
            <div class="pres-step">$\sqrt{1.024144} = \sqrt{\frac{1024144}{1000000}} = \frac{1012}{1000} = 1.012$</div>
        </div>
        <div id="pres-22" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the square root of each of the following.<br>(i) $\frac{169}{484}$</div>
            <div class="pres-step">$\sqrt{\frac{169}{484}} = \frac{\sqrt{169}}{\sqrt{484}} = \frac{13}{22}$</div>
        </div>
        <div id="pres-23" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the square root of each of the following.<br>(ii) $5 \frac{580}{729}$</div>
            <div class="pres-step">$\sqrt{\frac{(5 \times 729) + 580}{729}} = \sqrt{\frac{3645 + 580}{729}} = \sqrt{\frac{4225}{729}} = \frac{65}{27}$</div>
        </div>
        <div id="pres-24" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the square root of each of the following.<br>(iii) $12 \frac{52}{81}$</div>
            <div class="pres-step">$\sqrt{\frac{(12 \times 81) + 52}{81}} = \sqrt{\frac{972 + 52}{81}} = \sqrt{\frac{1024}{81}} = \frac{32}{9}$</div>
        </div>
        <div id="pres-25" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the square root of each of the following.<br>(iv) 0.0009</div>
            <div class="pres-step">$\sqrt{0.0009} = \sqrt{\frac{9}{10000}} = \frac{3}{100} = 0.03$</div>
        </div>
        <div id="pres-26" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the square root of each of the following.<br>(v) 4.41</div>
            <div class="pres-step">$\sqrt{4.41} = \sqrt{\frac{441}{100}} = \frac{21}{10} = 2.1$</div>
        </div>
        <div id="pres-27" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the square root of each of the following correct to two decimal places.<br>(i) 2</div>
            <div class="pres-step">$\sqrt{2} \approx 1.41$</div>
        </div>
        <div id="pres-28" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the square root of each of the following correct to two decimal places.<br>(ii) 3</div>
            <div class="pres-step">$\sqrt{3} \approx 1.73$</div>
        </div>
        <div id="pres-29" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the square root of each of the following correct to two decimal places.<br>(iii) 8</div>
            <div class="pres-step">$\sqrt{8} \approx 2.83$</div>
        </div>
        <div id="pres-30" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the square root of each of the following correct to two decimal places.<br>(iv) 11</div>
            <div class="pres-step">$\sqrt{11} \approx 3.32$</div>
        </div>
        <div id="pres-31" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the square root of each of the following correct to two decimal places.<br>(v) 35</div>
            <div class="pres-step">$\sqrt{35} \approx 5.92$</div>
        </div>
        <div id="pres-32" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the square root of each of the following correct to two decimal places.<br>(vi) 99</div>
            <div class="pres-step">$\sqrt{99} \approx 9.95$</div>
        </div>
        <div id="pres-33" class="pres-container" style="display:none;">
            <div class="pres-q">7. Find the value of $\sqrt{5}$ correct to two decimal places. Then, find the value of the square root of $\frac{3-\sqrt{5}}{3+\sqrt{5}}$ correct to two decimal places.<br></div>
            <div class="pres-step">$\sqrt{5} \approx 2.24$</div>
            <div class="pres-step">$\sqrt{\frac{3-\sqrt{5}}{3+\sqrt{5}}} = \sqrt{\frac{(3-\sqrt{5})(3-\sqrt{5})}{(3+\sqrt{5})(3-\sqrt{5})}}$</div>
            <div class="pres-step">$= \sqrt{\frac{(3-\sqrt{5})^2}{9-5}} = \frac{3-\sqrt{5}}{\sqrt{4}} = \frac{3-\sqrt{5}}{2}$</div>
            <div class="pres-step">Using $\sqrt{5} = 2.236$ (taking 3 decimal places for calculation accuracy):</div>
            <div class="pres-step">$\frac{3 - 2.236}{2} = \frac{0.764}{2} = 0.382$</div>
            <div class="pres-step">Correct to two decimal places: $0.38$</div>
        </div>
        <div id="pres-34" class="pres-container" style="display:none;">
            <div class="pres-q">8. Find the square root of each of the following correct to three decimal places.<br>(i) 2.5</div>
            <div class="pres-step">$\sqrt{2.5} \approx 1.581$</div>
        </div>
        <div id="pres-35" class="pres-container" style="display:none;">
            <div class="pres-q">8. Find the square root of each of the following correct to three decimal places.<br>(ii) 0.036</div>
            <div class="pres-step">$\sqrt{0.036} \approx 0.190$</div>
        </div>
        <div id="pres-36" class="pres-container" style="display:none;">
            <div class="pres-q">8. Find the square root of each of the following correct to three decimal places.<br>(iii) 6.4</div>
            <div class="pres-step">$\sqrt{6.4} \approx 2.530$</div>
        </div>
        <div id="pres-37" class="pres-container" style="display:none;">
            <div class="pres-q">8. Find the square root of each of the following correct to three decimal places.<br>(iv) 0.100</div>
            <div class="pres-step">$\sqrt{0.100} \approx 0.316$</div>
        </div>
        <div id="pres-38" class="pres-container" style="display:none;">
            <div class="pres-q">9. Find the least number by which 10368 should be (i) increased (ii) decreased (iii) multiplied (iv) divided to make it a perfect square.<br></div>
            <div class="pres-step">We find the square root of 10368. $101^2 = 10201$ and $102^2 = 10404$.</div>
            <div class="pres-step">So, $101^2 < 10368 < 102^2$</div>
            <div class="pres-step">(i) Increased: To get the next perfect square ($10404$), we add: $10404 - 10368 = 36$</div>
            <div class="pres-step">(ii) Decreased: To get the previous perfect square ($10201$), we subtract: $10368 - 10201 = 167$</div>
            <div class="pres-step">Now, prime factorization of $10368 = 2^7 \times 3^4$</div>
            <div class="pres-step">(iii) Multiplied: To make all powers even, we need to multiply by $2$. (Result will be $2^8 \times 3^4$)</div>
            <div class="pres-step">(iv) Divided: To make all powers even, we need to divide by $2$. (Result will be $2^6 \times 3^4$)</div>
        </div>
        <div id="pres-39" class="pres-container" style="display:none;">
            <div class="pres-q">10. Find the following.<br>(i) $55^2$</div>
            <div class="pres-step">$55^2 = 3025$</div>
        </div>
        <div id="pres-40" class="pres-container" style="display:none;">
            <div class="pres-q">10. Find the following.<br>(ii) $98^2$</div>
            <div class="pres-step">$98^2 = 9604$</div>
        </div>
        <div id="pres-41" class="pres-container" style="display:none;">
            <div class="pres-q">10. Find the following.<br>(iii) $\sqrt{38}$</div>
            <div class="pres-step">$\sqrt{38} \approx 6.164$ (to 3 decimal places)</div>
        </div>
        <div id="pres-42" class="pres-container" style="display:none;">
            <div class="pres-q">10. Find the following.<br>(iv) $\sqrt{89}$</div>
            <div class="pres-step">$\sqrt{89} \approx 9.43$ (to 2 decimal places)</div>
        </div>
        <div id="pres-43" class="pres-container" style="display:none;">
            <div class="pres-q">10. Find the following.<br>(v) $\sqrt{38.83}$</div>
            <div class="pres-step">$\sqrt{38.83} \approx 6.23$ (to 2 decimal places)</div>
        </div>
        <div id="pres-44" class="pres-container" style="display:none;">
            <div class="pres-q">10. Find the following.<br>(vi) $\sqrt{64.25}$</div>
            <div class="pres-step">$\sqrt{64.25} \approx 8.016$ (to 3 decimal places)</div>
        </div>
        <div id="pres-45" class="pres-container" style="display:none;">
            <div class="pres-q">11. Use algebraic methods to find the following.<br>(i) $52^2$</div>
            <div class="pres-step">$(50 + 2)^2 = 50^2 + 2(50)(2) + 2^2 = 2500 + 200 + 4 = 2704$</div>
        </div>
        <div id="pres-46" class="pres-container" style="display:none;">
            <div class="pres-q">11. Use algebraic methods to find the following.<br>(ii) $98^2$</div>
            <div class="pres-step">$(100 - 2)^2 = 100^2 - 2(100)(2) + 2^2 = 10000 - 400 + 4 = 9604$</div>
        </div>
        <div id="pres-47" class="pres-container" style="display:none;">
            <div class="pres-q">11. Use algebraic methods to find the following.<br>(iii) $309^2$</div>
            <div class="pres-step">$(300 + 9)^2 = 300^2 + 2(300)(9) + 9^2 = 90000 + 5400 + 81 = 95481$</div>
        </div>
        <div id="pres-48" class="pres-container" style="display:none;">
            <div class="pres-q">11. Use algebraic methods to find the following.<br>(iv) $495^2$</div>
            <div class="pres-step">$(500 - 5)^2 = 500^2 - 2(500)(5) + 5^2 = 250000 - 5000 + 25 = 245025$</div>
        </div>
        <div id="pres-49" class="pres-container" style="display:none;">
            <div class="pres-q">11. Use algebraic methods to find the following.<br>(v) $96^2$</div>
            <div class="pres-step">$(100 - 4)^2 = 100^2 - 2(100)(4) + 4^2 = 10000 - 800 + 16 = 9216$</div>
        </div>
        <div id="pres-50" class="pres-container" style="display:none;">
            <div class="pres-q">11. Use algebraic methods to find the following.<br>(vi) $305^2$</div>
            <div class="pres-step">$(300 + 5)^2 = 300^2 + 2(300)(5) + 5^2 = 90000 + 3000 + 25 = 93025$</div>
        </div>
        <div id="pres-51" class="pres-container" style="display:none;">
            <div class="pres-q">12. Find in each case the smallest perfect square divisible by the given numbers.<br>(i) 2, 4 and 5</div>
            <div class="pres-step">LCM of $2, 4, 5$ is $20$.</div>
            <div class="pres-step">Prime factors of $20 = 2^2 \times 5$.</div>
            <div class="pres-step">To make it a perfect square, we need to multiply by $5$.</div>
            <div class="pres-step">Smallest perfect square = $20 \times 5 = 100$.</div>
        </div>
        <div id="pres-52" class="pres-container" style="display:none;">
            <div class="pres-q">12. Find in each case the smallest perfect square divisible by the given numbers.<br>(ii) 3, 4, 5 and 6</div>
            <div class="pres-step">LCM of $3, 4, 5, 6$ is $60$.</div>
            <div class="pres-step">Prime factors of $60 = 2^2 \times 3 \times 5$.</div>
            <div class="pres-step">To make it a perfect square, we need to multiply by $3 \times 5 = 15$.</div>
            <div class="pres-step">Smallest perfect square = $60 \times 15 = 900$.</div>
        </div>
        <div id="pres-53" class="pres-container" style="display:none;">
            <div class="pres-q">12. Find in each case the smallest perfect square divisible by the given numbers.<br>(iii) 6, 8, 10 and 12</div>
            <div class="pres-step">LCM of $6, 8, 10, 12$ is $120$.</div>
            <div class="pres-step">Prime factors of $120 = 2^3 \times 3 \times 5$.</div>
            <div class="pres-step">To make it a perfect square, we need to multiply by $2 \times 3 \times 5 = 30$.</div>
            <div class="pres-step">Smallest perfect square = $120 \times 30 = 3600$.</div>
        </div>
        <div id="pres-54" class="pres-container" style="display:none;">
            <div class="pres-q">13. In an auditorium, the number of rows is equal to the number of chairs in each row. If the capacity of the auditorium is 2304, find the number of chairs in a row.<br></div>
            <div class="pres-step">Let the number of rows be $x$.</div>
            <div class="pres-step">Then, the number of chairs in each row is also $x$.</div>
            <div class="pres-step">Total capacity = $x \times x = x^2$</div>
            <div class="pres-step">$x^2 = 2304$</div>
            <div class="pres-step">$x = \sqrt{2304} = 48$</div>
            <div class="pres-step">Number of chairs in a row is 48.</div>
        </div>
        <div id="pres-55" class="pres-container" style="display:none;">
            <div class="pres-q">14. In a garden, 1089 rose plants are arranged in such a way that there are as many rows as there are plants in each row. Find the number of rows in the garden.<br></div>
            <div class="pres-step">Let the number of rows be $x$.</div>
            <div class="pres-step">Then, the number of plants per row is $x$.</div>
            <div class="pres-step">Total plants = $x \times x = x^2$</div>
            <div class="pres-step">$x^2 = 1089$</div>
            <div class="pres-step">$x = \sqrt{1089} = 33$</div>
            <div class="pres-step">Number of rows in the garden is 33.</div>
        </div>
        <div id="pres-56" class="pres-container" style="display:none;">
            <div class="pres-q">15. An army officer wishes to arrange 4770 soldiers in the form of a square. After arranging he finds that nine soldiers are left out. Find the number of soldiers in each row.<br></div>
            <div class="pres-step">Soldiers placed in the square = $4770 - 9 = 4761$.</div>
            <div class="pres-step">Let the number of soldiers in each row be $x$.</div>
            <div class="pres-step">Total soldiers in square = $x^2 = 4761$</div>
            <div class="pres-step">$x = \sqrt{4761} = 69$</div>
            <div class="pres-step">Number of soldiers in each row is 69.</div>
        </div>
        <div id="pres-57" class="pres-container" style="display:none;">
            <div class="pres-q">16. Find the least number that must be subtracted from each of the following numbers to get a perfect square. Also, find the square root of this perfect square.<br>(i) 9845</div>
            <div class="pres-step">$\sqrt{9845} \approx 99.22$</div>
            <div class="pres-step">The perfect square just below it is $99^2 = 9801$.</div>
            <div class="pres-step">Least number to subtract = $9845 - 9801 = 44$.</div>
            <div class="pres-step">Square root of the perfect square is 99.</div>
        </div>
        <div id="pres-58" class="pres-container" style="display:none;">
            <div class="pres-q">16. Find the least number that must be subtracted from each of the following numbers to get a perfect square. Also, find the square root of this perfect square.<br>(ii) 7585</div>
            <div class="pres-step">$\sqrt{7585} \approx 87.09$</div>
            <div class="pres-step">The perfect square just below it is $87^2 = 7569$.</div>
            <div class="pres-step">Least number to subtract = $7585 - 7569 = 16$.</div>
            <div class="pres-step">Square root of the perfect square is 87.</div>
        </div>
        <div id="pres-59" class="pres-container" style="display:none;">
            <div class="pres-q">16. Find the least number that must be subtracted from each of the following numbers to get a perfect square. Also, find the square root of this perfect square.<br>(iii) 786</div>
            <div class="pres-step">$\sqrt{786} \approx 28.03$</div>
            <div class="pres-step">The perfect square just below it is $28^2 = 784$.</div>
            <div class="pres-step">Least number to subtract = $786 - 784 = 2$.</div>
            <div class="pres-step">Square root of the perfect square is 28.</div>
        </div>
        <div id="pres-60" class="pres-container" style="display:none;">
            <div class="pres-q">17. Find the least number which must be added to each of the following numbers to make it a perfect square. Also, find the square root of this perfect square.<br>(i) 9389</div>
            <div class="pres-step">$\sqrt{9389} \approx 96.89$</div>
            <div class="pres-step">The perfect square just above it is $97^2 = 9409$.</div>
            <div class="pres-step">Least number to add = $9409 - 9389 = 20$.</div>
            <div class="pres-step">Square root of the perfect square is 97.</div>
        </div>
        <div id="pres-61" class="pres-container" style="display:none;">
            <div class="pres-q">17. Find the least number which must be added to each of the following numbers to make it a perfect square. Also, find the square root of this perfect square.<br>(ii) 5601</div>
            <div class="pres-step">$\sqrt{5601} \approx 74.83$</div>
            <div class="pres-step">The perfect square just above it is $75^2 = 5625$.</div>
            <div class="pres-step">Least number to add = $5625 - 5601 = 24$.</div>
            <div class="pres-step">Square root of the perfect square is 75.</div>
        </div>
        <div id="pres-62" class="pres-container" style="display:none;">
            <div class="pres-q">17. Find the least number which must be added to each of the following numbers to make it a perfect square. Also, find the square root of this perfect square.<br>(iii) 4725</div>
            <div class="pres-step">$\sqrt{4725} \approx 68.73$</div>
            <div class="pres-step">The perfect square just above it is $69^2 = 4761$.</div>
            <div class="pres-step">Least number to add = $4761 - 4725 = 36$.</div>
            <div class="pres-step">Square root of the perfect square is 69.</div>
        </div>
        <div id="pres-63" class="pres-container" style="display:none;">
            <div class="pres-q">18. Find the greatest six-digit number which is a perfect square.<br></div>
            <div class="pres-step">The greatest 6-digit number is 999999.</div>
            <div class="pres-step">$\sqrt{999999} \approx 999.999$</div>
            <div class="pres-step">So, the greatest 6-digit perfect square is $999^2 = 998001$.</div>
        </div>
        <div id="pres-64" class="pres-container" style="display:none;">
            <div class="pres-q">19. Find the smallest six-digit number which is a perfect square.<br></div>
            <div class="pres-step">The smallest 6-digit number is 100000.</div>
            <div class="pres-step">$\sqrt{100000} \approx 316.22$</div>
            <div class="pres-step">So, the smallest 6-digit perfect square is $317^2 = 100489$.</div>
        </div>
        <div id="pres-65" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(i) $\sqrt{\frac{1.44}{0.49}}$</div>
            <div class="pres-step">$\sqrt{\frac{144/100}{49/100}} = \sqrt{\frac{144}{49}} = \frac{12}{7}$</div>
        </div>
        <div id="pres-66" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(ii) $\sqrt{\frac{32.4}{28.9}}$</div>
            <div class="pres-step">$\sqrt{\frac{324/10}{289/10}} = \sqrt{\frac{324}{289}} = \frac{18}{17}$</div>
        </div>
        <div id="pres-67" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(iii) $\sqrt{\frac{0.0025}{0.0196}}$</div>
            <div class="pres-step">$\sqrt{\frac{25/10000}{196/10000}} = \sqrt{\frac{25}{196}} = \frac{5}{14}$</div>
        </div>
        <div id="pres-68" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(iv) $\sqrt{1 + \frac{25}{144}}$</div>
            <div class="pres-step">$\sqrt{\frac{144 + 25}{144}} = \sqrt{\frac{169}{144}} = \frac{13}{12}$</div>
        </div>
        <div id="pres-69" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(v) $\sqrt{1 - \frac{64}{289}}$</div>
            <div class="pres-step">$\sqrt{\frac{289 - 64}{289}} = \sqrt{\frac{225}{289}} = \frac{15}{17}$</div>
        </div>
        <div id="pres-70" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(vi) $\sqrt{2^3 \times 6^3 \times 27}$</div>
            <div class="pres-step">$\sqrt{8 \times 216 \times 27} = \sqrt{46656} = 216$</div>
            <div class="pres-step">(Alternative: $\sqrt{2^3 \times (2 \times 3)^3 \times 3^3} = \sqrt{2^6 \times 3^6} = 2^3 \times 3^3 = 8 \times 27 = 216$)</div>
        </div>
        <div id="pres-71" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(vii) $\frac{\sqrt{9}}{\sqrt{0.09}} + \frac{\sqrt{16}}{\sqrt{0.16}} + \frac{\sqrt{25}}{\sqrt{0.25}}$</div>
            <div class="pres-step">$\frac{3}{0.3} + \frac{4}{0.4} + \frac{5}{0.5} = 10 + 10 + 10 = 30$</div>
        </div>
        <div id="pres-72" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(viii) $\sqrt{400} + \sqrt{4} + \sqrt{0.04} + \sqrt{0.0004}$</div>
            <div class="pres-step">$20 + 2 + 0.2 + 0.02 = 22.22$</div>
        </div>
        <div id="pres-73" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(ix) $\sqrt{182 - \sqrt{156 + \sqrt{169}}}$</div>
            <div class="pres-step">$\sqrt{182 - \sqrt{156 + 13}} = \sqrt{182 - \sqrt{169}} = \sqrt{182 - 13} = \sqrt{169} = 13$</div>
        </div>
        <div id="pres-74" class="pres-container" style="display:none;">
            <div class="pres-q">20. Find the value of each of the following.<br>(x) $\sqrt{382 + \sqrt{341 - \sqrt{289}}}$</div>
            <div class="pres-step">$\sqrt{382 + \sqrt{341 - 17}} = \sqrt{382 + \sqrt{324}} = \sqrt{382 + 18} = \sqrt{400} = 20$</div>
        </div>
        <div id="pres-75" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(i) The units digit of the square of a number ending in 2 is ...... </div>
            <div class="pres-step"><b>4</b></div>
        </div>
        <div id="pres-76" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(ii) The units digit of the square of a number ending in 9 is ...... </div>
            <div class="pres-step"><b>1</b></div>
        </div>
        <div id="pres-77" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(iii) The units digit of the square root of a number ending in 6 is ...... or ...... </div>
            <div class="pres-step"><b>4</b> or <b>6</b></div>
        </div>
        <div id="pres-78" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(iv) There are ...... natural numbers between the squares of 8 and 9.</div>
            <div class="pres-step"><b>16</b> (since $2 \times 8 = 16$)</div>
        </div>
        <div id="pres-79" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(v) $9^2 - 8^2$ = ...... + 8.</div>
            <div class="pres-step"><b>9</b> (since $a^2 - b^2 = (a-b)(a+b)$, here $(9-8)(9+8) = 1(9+8) = 9+8$)</div>
        </div>
        <div id="pres-80" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(vi) $19^2$ - ...... = 19 + 18.</div>
            <div class="pres-step"><b>$18^2$</b> (since $19^2 - 18^2 = (19-18)(19+18) = 19+18$)</div>
        </div>
        <div id="pres-81" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(vii) If $\sqrt{4096} = 64$ then $\sqrt{4096} + \sqrt{40.96}$ = ....... </div>
            <div class="pres-step">$\sqrt{4096} + \sqrt{40.96} = 64 + 6.4 = $ <b>70.4</b></div>
        </div>
        <div id="pres-82" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(viii) $\sqrt{4} + \sqrt{0.04} + \sqrt{0.0004}$ = .......</div>
            <div class="pres-step">$2 + 0.2 + 0.02 = $ <b>2.22</b></div>
        </div>
        <div id="pres-83" class="pres-container" style="display:none;">
            <div class="pres-q">21. Fill in the blanks.<br>(ix) 3, 4 and ...... form a Pythagorean triple.</div>
            <div class="pres-step"><b>5</b> (since $3^2 + 4^2 = 5^2$)</div>
        </div>
        <div id="pres-84" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(i) $\left(\frac{5}{6}\right)^3$</div>
            <div class="pres-step">$\left(\frac{5}{6}\right)^3 = \frac{5^3}{6^3} = \frac{125}{216}$</div>
        </div>
        <div id="pres-85" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(ii) $\left(-1 \frac{7}{11}\right)^3$</div>
            <div class="pres-step">$\left(-1 \frac{7}{11}\right)^3 = \left(\frac{-18}{11}\right)^3 = \frac{(-18)^3}{11^3} = \frac{-5832}{1331} = -4 \frac{508}{1331}$</div>
        </div>
        <div id="pres-86" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(iii) $(2.5)^3$</div>
            <div class="pres-step">$(2.5)^3 = \left(\frac{25}{10}\right)^3 = \frac{15625}{1000} = 15.625$</div>
        </div>
        <div id="pres-87" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(iv) $(0.08)^3$</div>
            <div class="pres-step">$(0.08)^3 = \left(\frac{8}{100}\right)^3 = \frac{512}{1000000} = 0.000512$</div>
        </div>
        <div id="pres-88" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(v) $(-1.1)^3$</div>
            <div class="pres-step">$(-1.1)^3 = \left(\frac{-11}{10}\right)^3 = \frac{-1331}{1000} = -1.331$</div>
        </div>
        <div id="pres-89" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(vi) $\left(-\frac{7}{3}\right)^3$</div>
            <div class="pres-step">$\left(-\frac{7}{3}\right)^3 = \frac{(-7)^3}{3^3} = \frac{-343}{27}$</div>
        </div>
        <div id="pres-90" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(vii) $(-9)^3$</div>
            <div class="pres-step">$(-9)^3 = -729$</div>
        </div>
        <div id="pres-91" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(viii) $(-0.5)^3$</div>
            <div class="pres-step">$(-0.5)^3 = \left(\frac{-5}{10}\right)^3 = \frac{-125}{1000} = -0.125$</div>
        </div>
        <div id="pres-92" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(ix) $(-20)^3$</div>
            <div class="pres-step">$(-20)^3 = -8000$</div>
        </div>
        <div id="pres-93" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(x) $(-0.013)^3$</div>
            <div class="pres-step">$(-0.013)^3 = \left(\frac{-13}{1000}\right)^3 = \frac{-2197}{1000000000} = -0.000002197$</div>
        </div>
        <div id="pres-94" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(xi) $(25)^3$</div>
            <div class="pres-step">$(25)^3 = 15625$</div>
        </div>
        <div id="pres-95" class="pres-container" style="display:none;">
            <div class="pres-q">1. Find the value of each of the following.<br>(xii) $\left(2 \frac{1}{7}\right)^3$</div>
            <div class="pres-step">$\left(2 \frac{1}{7}\right)^3 = \left(\frac{15}{7}\right)^3 = \frac{15^3}{7^3} = \frac{3375}{343} = 9 \frac{288}{343}$</div>
        </div>
        <div id="pres-96" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(i) 128</div>
            <div class="pres-step">$128 = 2^7$. (Not a perfect cube)</div>
        </div>
        <div id="pres-97" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(ii) 243</div>
            <div class="pres-step">$243 = 3^5$. (Not a perfect cube)</div>
        </div>
        <div id="pres-98" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(iii) 343</div>
            <div class="pres-step">$343 = 7^3$. (Perfect cube of 7)</div>
        </div>
        <div id="pres-99" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(iv) 4000</div>
            <div class="pres-step">$4000 = 2^5 \times 5^3$. (Not a perfect cube)</div>
        </div>
        <div id="pres-100" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(v) 3456</div>
            <div class="pres-step">$3456 = 2^7 \times 3^3$. (Not a perfect cube)</div>
        </div>
        <div id="pres-101" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(vi) 2048</div>
            <div class="pres-step">$2048 = 2^{11}$. (Not a perfect cube)</div>
        </div>
        <div id="pres-102" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(vii) 2197</div>
            <div class="pres-step">$2197 = 13^3$. (Perfect cube of 13)</div>
        </div>
        <div id="pres-103" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(viii) 1000000</div>
            <div class="pres-step">$1000000 = 100^3$. (Perfect cube of 100)</div>
        </div>
        <div id="pres-104" class="pres-container" style="display:none;">
            <div class="pres-q">2. Identify the perfect cubes among the following. Find the number whose cube is the given number in each case of the perfect cubes.<br>(ix) 2744</div>
            <div class="pres-step">$2744 = 14^3$. (Perfect cube of 14)</div>
        </div>
        <div id="pres-105" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(i) 8000</div>
            <div class="pres-step">8000 is an even number, so it is the cube of an **even** number.</div>
        </div>
        <div id="pres-106" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(ii) 9261</div>
            <div class="pres-step">9261 is an odd number, so it is the cube of an **odd** number.</div>
        </div>
        <div id="pres-107" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(iii) 4096</div>
            <div class="pres-step">4096 is an even number, so it is the cube of an **even** number.</div>
        </div>
        <div id="pres-108" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(iv) 6859</div>
            <div class="pres-step">6859 is an odd number, so it is the cube of an **odd** number.</div>
        </div>
        <div id="pres-109" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(v) 12167</div>
            <div class="pres-step">12167 is an odd number, so it is the cube of an **odd** number.</div>
        </div>
        <div id="pres-110" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(vi) 4913</div>
            <div class="pres-step">4913 is an odd number, so it is the cube of an **odd** number.</div>
        </div>
        <div id="pres-111" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(vii) 13824</div>
            <div class="pres-step">13824 is an even number, so it is the cube of an **even** number.</div>
        </div>
        <div id="pres-112" class="pres-container" style="display:none;">
            <div class="pres-q">3. Which of the following are cubes of even numbers and which are of odd numbers?<br>(viii) 17576</div>
            <div class="pres-step">17576 is an even number, so it is the cube of an **even** number.</div>
        </div>
        <div id="pres-113" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(i) $\sqrt[3]{512}$</div>
            <div class="pres-step">$\sqrt[3]{512} = \sqrt[3]{8^3} = 8$</div>
        </div>
        <div id="pres-114" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(ii) $\sqrt[3]{2744}$</div>
            <div class="pres-step">$\sqrt[3]{2744} = \sqrt[3]{14^3} = 14$</div>
        </div>
        <div id="pres-115" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(iii) $\sqrt[3]{729}$</div>
            <div class="pres-step">$\sqrt[3]{729} = \sqrt[3]{9^3} = 9$</div>
        </div>
        <div id="pres-116" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(iv) $\sqrt[3]{1728}$</div>
            <div class="pres-step">$\sqrt[3]{1728} = \sqrt[3]{12^3} = 12$</div>
        </div>
        <div id="pres-117" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(v) $\sqrt[3]{1000}$</div>
            <div class="pres-step">$\sqrt[3]{1000} = \sqrt[3]{10^3} = 10$</div>
        </div>
        <div id="pres-118" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(vi) $\sqrt[3]{-8000}$</div>
            <div class="pres-step">$\sqrt[3]{-8000} = \sqrt[3]{(-20)^3} = -20$</div>
        </div>
        <div id="pres-119" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(vii) $\sqrt[3]{-4096}$</div>
            <div class="pres-step">$\sqrt[3]{-4096} = \sqrt[3]{(-16)^3} = -16$</div>
        </div>
        <div id="pres-120" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(viii) $\sqrt[3]{\frac{27}{125}}$</div>
            <div class="pres-step">$\sqrt[3]{\frac{27}{125}} = \frac{\sqrt[3]{27}}{\sqrt[3]{125}} = \frac{3}{5}$</div>
        </div>
        <div id="pres-121" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(ix) $\sqrt[3]{\frac{-125}{64}}$</div>
            <div class="pres-step">$\sqrt[3]{\frac{-125}{64}} = \frac{\sqrt[3]{-125}}{\sqrt[3]{64}} = \frac{-5}{4}$</div>
        </div>
        <div id="pres-122" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(x) $\sqrt[3]{0.001}$</div>
            <div class="pres-step">$\sqrt[3]{0.001} = \sqrt[3]{\frac{1}{1000}} = \frac{1}{10} = 0.1$</div>
        </div>
        <div id="pres-123" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xi) $\sqrt[3]{0.125}$</div>
            <div class="pres-step">$\sqrt[3]{0.125} = \sqrt[3]{\frac{125}{1000}} = \frac{5}{10} = 0.5$</div>
        </div>
        <div id="pres-124" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xii) $\sqrt[3]{\frac{27}{64 \times 125}}$</div>
            <div class="pres-step">$\frac{\sqrt[3]{27}}{\sqrt[3]{64} \times \sqrt[3]{125}} = \frac{3}{4 \times 5} = \frac{3}{20}$</div>
        </div>
        <div id="pres-125" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xiii) $\sqrt[3]{\frac{729}{125 \times 1000}}$</div>
            <div class="pres-step">$\frac{\sqrt[3]{729}}{\sqrt[3]{125} \times \sqrt[3]{1000}} = \frac{9}{5 \times 10} = \frac{9}{50}$</div>
        </div>
        <div id="pres-126" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xiv) $\sqrt[3]{125 \times 64 \times 8}$</div>
            <div class="pres-step">$\sqrt[3]{125} \times \sqrt[3]{64} \times \sqrt[3]{8} = 5 \times 4 \times 2 = 40$</div>
        </div>
        <div id="pres-127" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xv) $\sqrt[3]{16 \times 500}$</div>
            <div class="pres-step">$\sqrt[3]{8000} = 20$</div>
        </div>
        <div id="pres-128" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xvi) $\sqrt[3]{625 \times (-1600)}$</div>
            <div class="pres-step">$\sqrt[3]{-1000000} = -100$</div>
        </div>
        <div id="pres-129" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xvii) $\sqrt[3]{\frac{343}{2500 \times 400}}$</div>
            <div class="pres-step">$\sqrt[3]{\frac{343}{1000000}} = \frac{7}{100}$</div>
        </div>
        <div id="pres-130" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xviii) $\sqrt[3]{1 - \frac{854}{729}}$</div>
            <div class="pres-step">$\sqrt[3]{\frac{729 - 854}{729}} = \sqrt[3]{\frac{-125}{729}} = \frac{-5}{9}$</div>
        </div>
        <div id="pres-131" class="pres-container" style="display:none;">
            <div class="pres-q">4. Find each of the following.<br>(xix) $\sqrt[3]{4 + \sqrt[3]{61 + \sqrt[3]{27}}}$</div>
            <div class="pres-step">$\sqrt[3]{4 + \sqrt[3]{61 + 3}}$</div>
            <div class="pres-step">$= \sqrt[3]{4 + \sqrt[3]{64}}$</div>
            <div class="pres-step">$= \sqrt[3]{4 + 4} = \sqrt[3]{8} = 2$</div>
        </div>
        <div id="pres-132" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the least number by which each of the following numbers should be multiplied to make it a perfect cube. Also, find the cube root of the product in each case.<br>(i) 5488</div>
            <div class="pres-step">Prime factorization: $5488 = 2^4 \times 7^3$</div>
            <div class="pres-step">To make the powers multiples of 3, multiply by $2^2 = 4$.</div>
            <div class="pres-step">Least number = 4</div>
            <div class="pres-step">New product = $2^6 \times 7^3$</div>
            <div class="pres-step">Cube root = $2^2 \times 7 = 4 \times 7 = 28$</div>
        </div>
        <div id="pres-133" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the least number by which each of the following numbers should be multiplied to make it a perfect cube. Also, find the cube root of the product in each case.<br>(ii) 34992</div>
            <div class="pres-step">Prime factorization: $34992 = 2^4 \times 3^7$</div>
            <div class="pres-step">To make the powers multiples of 3, multiply by $2^2 \times 3^2 = 4 \times 9 = 36$.</div>
            <div class="pres-step">Least number = 36</div>
            <div class="pres-step">New product = $2^6 \times 3^9$</div>
            <div class="pres-step">Cube root = $2^2 \times 3^3 = 4 \times 27 = 108$</div>
        </div>
        <div id="pres-134" class="pres-container" style="display:none;">
            <div class="pres-q">5. Find the least number by which each of the following numbers should be multiplied to make it a perfect cube. Also, find the cube root of the product in each case.<br>(iii) 15552</div>
            <div class="pres-step">Prime factorization: $15552 = 2^6 \times 3^5$</div>
            <div class="pres-step">To make the powers multiples of 3, multiply by $3^1 = 3$.</div>
            <div class="pres-step">Least number = 3</div>
            <div class="pres-step">New product = $2^6 \times 3^6$</div>
            <div class="pres-step">Cube root = $2^2 \times 3^2 = 4 \times 9 = 36$</div>
        </div>
        <div id="pres-135" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the least number by which each of the following numbers should be divided to make it a perfect cube. Also, find the cube root of each perfect cube.<br>(i) 5184</div>
            <div class="pres-step">Prime factorization: $5184 = 2^6 \times 3^4$</div>
            <div class="pres-step">To leave powers as multiples of 3, divide by $3^1 = 3$.</div>
            <div class="pres-step">Least number = 3</div>
            <div class="pres-step">New quotient = $2^6 \times 3^3$</div>
            <div class="pres-step">Cube root = $2^2 \times 3 = 4 \times 3 = 12$</div>
        </div>
        <div id="pres-136" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the least number by which each of the following numbers should be divided to make it a perfect cube. Also, find the cube root of each perfect cube.<br>(ii) 5488</div>
            <div class="pres-step">Prime factorization: $5488 = 2^4 \times 7^3$</div>
            <div class="pres-step">To leave powers as multiples of 3, divide by $2^1 = 2$.</div>
            <div class="pres-step">Least number = 2</div>
            <div class="pres-step">New quotient = $2^3 \times 7^3$</div>
            <div class="pres-step">Cube root = $2 \times 7 = 14$</div>
        </div>
        <div id="pres-137" class="pres-container" style="display:none;">
            <div class="pres-q">6. Find the least number by which each of the following numbers should be divided to make it a perfect cube. Also, find the cube root of each perfect cube.<br>(iii) 23328</div>
            <div class="pres-step">Prime factorization: $23328 = 2^5 \times 3^6$</div>
            <div class="pres-step">To leave powers as multiples of 3, divide by $2^2 = 4$.</div>
            <div class="pres-step">Least number = 4</div>
            <div class="pres-step">New quotient = $2^3 \times 3^6$</div>
            <div class="pres-step">Cube root = $2 \times 3^2 = 2 \times 9 = 18$</div>
        </div>
        <div id="pres-138" class="pres-container" style="display:none;">
            <div class="pres-q">7. Fill in the blanks.<br>(i) The units digit in the cube of 1137 is ...... </div>
            <div class="pres-step"><b>3</b> (since $7^3 = 343$, unit digit is 3)</div>
        </div>
        <div id="pres-139" class="pres-container" style="display:none;">
            <div class="pres-q">7. Fill in the blanks.<br>(ii) The ones digit in the cube of 1004 is ...... </div>
            <div class="pres-step"><b>4</b> (since $4^3 = 64$, unit digit is 4)</div>
        </div>
        <div id="pres-140" class="pres-container" style="display:none;">
            <div class="pres-q">7. Fill in the blanks.<br>(iii) The cube of an odd number is always an ...... number.</div>
            <div class="pres-step"><b>odd</b></div>
        </div>
        <div id="pres-141" class="pres-container" style="display:none;">
            <div class="pres-q">7. Fill in the blanks.<br>(iv) The cube of an even number is always an ...... number.</div>
            <div class="pres-step"><b>even</b></div>
        </div>
        <div id="pres-142" class="pres-container" style="display:none;">
            <div class="pres-q">7. Fill in the blanks.<br>(v) The least natural number by which 1600 is to be multiplied to make it a perfect cube is ....... </div>
            <div class="pres-step">$1600 = 2^6 \times 5^2$. Needs to be multiplied by <b>5</b>.</div>
        </div>
        <div id="pres-143" class="pres-container" style="display:none;">
            <div class="pres-q">7. Fill in the blanks.<br>(vi) The least natural number by which 1024 is to be divided to make it a perfect cube is ....... </div>
            <div class="pres-step">$1024 = 2^{10}$. Needs to be divided by $2^1$ = <b>2</b>.</div>
        </div>
        <div id="pres-144" class="pres-container" style="display:none;">
            <div class="pres-q">8. Identify the false statements only.<br>(i) The cube of an odd number is odd.</div>
            <div class="pres-step">True</div>
        </div>
        <div id="pres-145" class="pres-container" style="display:none;">
            <div class="pres-q">8. Identify the false statements only.<br>(ii) The cube of an even number is even.</div>
            <div class="pres-step">True</div>
        </div>
        <div id="pres-146" class="pres-container" style="display:none;">
            <div class="pres-q">8. Identify the false statements only.<br>(iii) The cube of a negative number is positive.</div>
            <div class="pres-step"><b>False</b> (It is negative)</div>
        </div>
        <div id="pres-147" class="pres-container" style="display:none;">
            <div class="pres-q">8. Identify the false statements only.<br>(iv) The cube roots of 27 are 3 and -3.</div>
            <div class="pres-step"><b>False</b> (The only real cube root is 3)</div>
        </div>
        <div id="pres-148" class="pres-container" style="display:none;">
            <div class="pres-q">8. Identify the false statements only.<br>(v) 333 is a perfect cube.</div>
            <div class="pres-step"><b>False</b> (7^3 = 343)</div>
        </div>
        <div id="pres-149" class="pres-container" style="display:none;">
            <div class="pres-q">8. Identify the false statements only.<br>(vi) $\sqrt[3]{27+8} = \sqrt[3]{27} + \sqrt[3]{8}$.</div>
            <div class="pres-step"><b>False</b> ($\sqrt[3]{35} \neq 3 + 2$)</div>
        </div>
        <div id="pres-150" class="pres-container" style="display:none;">
            <div class="pres-q">8. Identify the false statements only.<br>(vii) There is no cube root of a negative number.</div>
            <div class="pres-step"><b>False</b> (e.g., $\sqrt[3]{-8} = -2$)</div>
        </div>

    </div>

    <script>
        const chapterPresMap = {"ch3": ["pres-0", "pres-1", "pres-2", "pres-3", "pres-4", "pres-5", "pres-6", "pres-7", "pres-8", "pres-9", "pres-10", "pres-11", "pres-12", "pres-13", "pres-14", "pres-15", "pres-16", "pres-17", "pres-18", "pres-19", "pres-20", "pres-21", "pres-22", "pres-23", "pres-24", "pres-25", "pres-26", "pres-27", "pres-28", "pres-29", "pres-30", "pres-31", "pres-32", "pres-33", "pres-34", "pres-35", "pres-36", "pres-37", "pres-38", "pres-39", "pres-40", "pres-41", "pres-42", "pres-43", "pres-44", "pres-45", "pres-46", "pres-47", "pres-48", "pres-49", "pres-50", "pres-51", "pres-52", "pres-53", "pres-54", "pres-55", "pres-56", "pres-57", "pres-58", "pres-59", "pres-60", "pres-61", "pres-62", "pres-63", "pres-64", "pres-65", "pres-66", "pres-67", "pres-68", "pres-69", "pres-70", "pres-71", "pres-72", "pres-73", "pres-74", "pres-75", "pres-76", "pres-77", "pres-78", "pres-79", "pres-80", "pres-81", "pres-82", "pres-83"], "ch4": ["pres-84", "pres-85", "pres-86", "pres-87", "pres-88", "pres-89", "pres-90", "pres-91", "pres-92", "pres-93", "pres-94", "pres-95", "pres-96", "pres-97", "pres-98", "pres-99", "pres-100", "pres-101", "pres-102", "pres-103", "pres-104", "pres-105", "pres-106", "pres-107", "pres-108", "pres-109", "pres-110", "pres-111", "pres-112", "pres-113", "pres-114", "pres-115", "pres-116", "pres-117", "pres-118", "pres-119", "pres-120", "pres-121", "pres-122", "pres-123", "pres-124", "pres-125", "pres-126", "pres-127", "pres-128", "pres-129", "pres-130", "pres-131", "pres-132", "pres-133", "pres-134", "pres-135", "pres-136", "pres-137", "pres-138", "pres-139", "pres-140", "pres-141", "pres-142", "pres-143", "pres-144", "pres-145", "pres-146", "pres-147", "pres-148", "pres-149", "pres-150"]};
        
        let currentSteps = [];
        let currentStepIndex = -1;
        let savedNormalScroll = {};
        let savedTeachScroll = {};
        let activeTeachCh = null;
        let activePresId = null;

        function openChapter(chId) {
            document.getElementById('home-view').style.display = 'none';
            document.getElementById('normal-view-' + chId).style.display = 'block';
            window.scrollTo(0, 0);
        }

        function goHome() {
            const views = document.querySelectorAll('.chapter-view');
            views.forEach(v => v.style.display = 'none');
            document.getElementById('home-view').style.display = 'block';
            window.scrollTo(0, 0);
        }

        function enterTeachMode(chId) {
            savedNormalScroll[chId] = window.scrollY;
            document.getElementById('normal-view-' + chId).style.display = 'none';
            document.getElementById('teach-view-' + chId).style.display = 'block';
            window.scrollTo(0, 0);
        }

        function exitTeachMode(chId) {
            document.getElementById('teach-view-' + chId).style.display = 'none';
            document.getElementById('normal-view-' + chId).style.display = 'block';
            window.scrollTo(0, savedNormalScroll[chId] || 0);
        }

        function startPresentation(id, chId) {
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
            currentSteps.forEach(step => {
                step.style.opacity = '0';
            });
            
            currentStepIndex = -1;
            window.scrollTo(0, 0);
            updateNavButtons();
        }

        function closePresentation() {
            if (!activeTeachCh) return;
            document.getElementById('presentation-view').style.display = 'none';
            document.getElementById('teach-view-' + activeTeachCh).style.display = 'block';
            window.scrollTo(0, savedTeachScroll[activeTeachCh] || 0);
        }
        
        function updateNavButtons() {
            const list = chapterPresMap[activeTeachCh];
            const idx = list.indexOf(activePresId);
            
            document.getElementById('btn-prev-q').style.display = (idx > 0) ? 'block' : 'none';
            document.getElementById('btn-next-q').style.display = (idx < list.length - 1) ? 'block' : 'none';
        }
        
        function nextQuestion() {
            const list = chapterPresMap[activeTeachCh];
            const idx = list.indexOf(activePresId);
            if (idx < list.length - 1) {
                startPresentation(list[idx + 1], activeTeachCh);
            }
        }
        
        function prevQuestion() {
            const list = chapterPresMap[activeTeachCh];
            const idx = list.indexOf(activePresId);
            if (idx > 0) {
                startPresentation(list[idx - 1], activeTeachCh);
            }
        }

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
            } else {
                // Optional: Auto advance to next question if steps are done
                // nextQuestion();
            }
        }

        function prevStep() {
            if (currentStepIndex >= 0) {
                currentSteps[currentStepIndex].style.opacity = '0';
                currentStepIndex--;
            } else {
                // Optional: Auto advance to prev question if going back at step 0
                // prevQuestion();
            }
        }
        
        // Scroll to change questions
        let wheelTimeout;
        presView.addEventListener('wheel', (e) => {
            // Prevent multiple triggers
            if (wheelTimeout) return;
            wheelTimeout = setTimeout(() => { wheelTimeout = null; }, 800);
            
            if (e.deltaY > 50) {
                nextQuestion();
            } else if (e.deltaY < -50) {
                prevQuestion();
            }
        });
        
        let touchStartY = 0;
        let touchEndY = 0;
        
        presView.addEventListener('touchstart', e => {
            touchStartY = e.changedTouches[0].screenY;
        }, {passive: true});
        
        presView.addEventListener('touchend', e => {
            touchEndY = e.changedTouches[0].screenY;
            handleSwipe();
        }, {passive: true});
        
        function handleSwipe() {
            // swipe up -> next question
            if (touchStartY - touchEndY > 100) {
                nextQuestion();
            }
            // swipe down -> prev question
            else if (touchEndY - touchStartY > 100) {
                prevQuestion();
            }
        }

        document.addEventListener('keydown', (e) => {
            if (document.getElementById('presentation-view').style.display === 'block') {
                if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
                    e.preventDefault();
                    nextStep();
                } else if (e.key === 'ArrowLeft') {
                    e.preventDefault();
                    prevStep();
                } else if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    nextQuestion();
                } else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    prevQuestion();
                } else if (e.key === 'Escape') {
                    closePresentation();
                }
            }
        });
    </script>
</body>
</html>
