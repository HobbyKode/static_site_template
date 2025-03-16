# Ensure we're in the correct project root
cd "$(dirname "$0")"



# Disable bytecode compilation (no __pycache__)
export PYTHONDONTWRITEBYTECODE=1


#Building the site for GitHub Pages
echo  "🚀 Building site for GitHub Pages with basepath:  /static_site_template/"
python3 src/main.py "/static_site_template/" 