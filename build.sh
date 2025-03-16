# Ensure we're in the correct project root
cd "$(dirname "$0")"

# Disable bytecode compilation (no __pycache__)
export PYTHONDONTWRITEBYTECODE=1

# Define the GitHub repository name (replace with your actual repo)
REPO_NAME="static_site_template"

# Fix: Ensure basepath does not have an extra slash
BASEPATH="/$REPO_NAME"
BASEPATH=${BASEPATH%/}  # ✅ Removes trailing slash if it exists

echo "🚀 Building site for GitHub Pages with basepath: $BASEPATH"
python3 src/main.py "$BASEPATH"