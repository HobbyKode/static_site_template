# Ensure we're in the correct project root
cd "$(dirname "$0")"

# Define the GitHub repository name (replace with your actual repo)
REPO_NAME="static_site_template"

# Disable bytecode compilation (no __pycache__)
export PYTHONDONTWRITEBYTECODE=1

# Building the site for GitHub Pages
BASEPATH="/$REPO_NAME"  # ✅ Remove trailing slash
echo "🚀 Building site for GitHub Pages with basepath: $BASEPATH"
python3 src/main.py "$BASEPATH"