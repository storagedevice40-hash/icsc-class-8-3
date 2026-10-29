with open("generator.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add id="tools-panel" to <div class="tools-panel">
old_panel = '<div class="tools-panel">'
new_panel = '<div class="tools-panel" id="tools-panel">'
if old_panel in text:
    text = text.replace(old_panel, new_panel, 1)

# 2. Add CSS rule to hide tools-panel in teach mode and add right padding to pres-q
teach_css = """
        /* Hide all tools in teach & presentation mode */
        body.in-teach-mode #tools-panel,
        body.in-teach-mode .tools-panel {
            display: none !important;
        }
        .pres-q {
            padding-right: 85px;
        }
"""
if "body.in-teach-mode" not in text:
    text = text.replace("/* Presentation View */", teach_css + "\n        /* Presentation View */", 1)

# 3. Update JS functions
old_funcs = """        function openChapter(chId) {{
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
        }}"""

new_funcs = """        function openChapter(chId) {{
            document.body.classList.remove('in-teach-mode');
            const tp = document.getElementById('tools-panel');
            if (tp) tp.style.display = 'flex';
            document.getElementById('home-view').style.display = 'none';
            document.getElementById('normal-view-' + chId).style.display = 'block';
            window.scrollTo(0, 0);
        }}

        function goHome() {{
            document.body.classList.remove('in-teach-mode');
            const tp = document.getElementById('tools-panel');
            if (tp) tp.style.display = 'flex';
            const views = document.querySelectorAll('.chapter-view');
            views.forEach(v => v.style.display = 'none');
            document.getElementById('home-view').style.display = 'block';
            window.scrollTo(0, 0);
        }}

        function enterTeachMode(chId) {{
            savedNormalScroll[chId] = window.scrollY;
            document.body.classList.add('in-teach-mode');
            const tp = document.getElementById('tools-panel');
            if (tp) tp.style.display = 'none';
            document.getElementById('normal-view-' + chId).style.display = 'none';
            document.getElementById('teach-view-' + chId).style.display = 'block';
            window.scrollTo(0, 0);
        }}

        function exitTeachMode(chId) {{
            document.body.classList.remove('in-teach-mode');
            const tp = document.getElementById('tools-panel');
            if (tp) tp.style.display = 'flex';
            document.getElementById('teach-view-' + chId).style.display = 'none';
            document.getElementById('normal-view-' + chId).style.display = 'block';
            window.scrollTo(0, savedNormalScroll[chId] || 0);
        }}

        function startPresentation(id, chId) {{
            activeTeachCh = chId;
            activePresId = id;
            savedTeachScroll[chId] = window.scrollY;
            document.body.classList.add('in-teach-mode');
            const tp = document.getElementById('tools-panel');
            if (tp) tp.style.display = 'none';
            
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
            document.body.classList.add('in-teach-mode');
            const tp = document.getElementById('tools-panel');
            if (tp) tp.style.display = 'none';
            document.getElementById('presentation-view').style.display = 'none';
            document.getElementById('teach-view-' + activeTeachCh).style.display = 'block';
            window.scrollTo(0, savedTeachScroll[activeTeachCh] || 0);
        }}"""

if old_funcs in text:
    text = text.replace(old_funcs, new_funcs, 1)
    print("Replaced JS functions successfully!")
else:
    print("Could not match old_funcs!")

with open("generator.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated generator.py")
