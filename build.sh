# Ensure we're in the correct project root
cd "$(dirname "$0")"

# Define the GitHub repository name (replace with your actual repo)
REPO_NAME="static_site_template"

# Disable bytecode compilation (no __pycache__)
export PYTHONDONTWRITEBYTECODE=1


#Building the site for GitHub Pages
echo  "🚀 Building site for GitHub Pages with basepath:  /$REPO_NAME/"
python3 src/main.py "/$REPO_NAME/" 