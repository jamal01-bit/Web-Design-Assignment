import os
import re

files = [
    "index.html", "science.html", "causes.html", "effects.html",
    "wildlife.html", "human_impact.html", "solutions.html",
    "global_action.html", "take_action.html", "dev_notes.html",
    "thank_you.html"
]

dir_path = "/home/jamal012004/web.design/climate_change_site/"

def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Extract head and body
    head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)

    if not head_match or not body_match:
        print(f"Skipping {file_path}: could not find head or body")
        return

    head_content = head_match.group(1).strip()
    body_content = body_match.group(1).strip()

    # Extract nav and main
    nav_match = re.search(r'<nav>(.*?)</nav>', body_content, re.DOTALL | re.IGNORECASE)
    main_match = re.search(r'<main>(.*?)</main>', body_content, re.DOTALL | re.IGNORECASE)

    if not nav_match or not main_match:
        print(f"Skipping {file_path}: could not find nav or main")
        return

    nav_inner = nav_match.group(1)
    main_inner = main_match.group(1)

    # Simplify nav structure: keep only <a> tags
    links = re.findall(r'<a\s+[^>]*>.*?</a>', nav_inner, re.DOTALL | re.IGNORECASE)
    simplified_nav = "\n" + "\n".join([f"        {link.strip()}" for link in links]) + "\n    "

    # Construct new content
    new_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {head_content}
</head>
<body>

    <nav>{simplified_nav}</nav>

    <main>{main_inner}</main>

</body>
</html>"""

    # Cleanup extra newlines and formatting
    new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path}")

for file_name in files:
    full_path = os.path.join(dir_path, file_name)
    if os.path.exists(full_path):
        update_html(full_path)
    else:
        print(f"File {file_name} not found")
