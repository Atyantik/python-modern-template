#!/usr/bin/env bash
# Generate all example projects from the template

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_DIR="$(dirname "$SCRIPT_DIR")"

echo " Generating all example projects from template..."
echo "Template location: $TEMPLATE_DIR"
echo ""

# Ensure we have copier installed
if ! command -v copier &> /dev/null; then
    echo "ERROR: Copier not found. Installing..."
    uv tool install copier
fi

# Clean up old examples if they exist
echo " Cleaning up old examples..."
rm -rf "$SCRIPT_DIR/01-minimal-package"
rm -rf "$SCRIPT_DIR/02-cli-tool"
rm -rf "$SCRIPT_DIR/03-library"
rm -rf "$SCRIPT_DIR/04-data-science"
rm -rf "$SCRIPT_DIR/05-web-api"
rm -rf "$SCRIPT_DIR/06-ai-assisted"
rm -rf "$SCRIPT_DIR/07-full-featured"

echo ""
echo " Generating examples..."
echo ""

# 1. Minimal Package
echo "[0-9].  Generating minimal-package..."
uv tool run copier copy \
  --trust \
  --defaults \
  --data project_name="Minimal Package Example" \
  --data project_description="A minimal Python package without extra tooling" \
  --data project_slug="minimal-package-example" \
  --data author_name="Example Author" \
  --data author_email="author@example.com" \
  --data include_quality_scripts=false \
  --data include_ai_tools=false \
  --data include_docker=false \
  --data include_docs=false \
  --data include_pre_commit=false \
  --data include_github_actions=false \
  "$TEMPLATE_DIR" "$SCRIPT_DIR/01-minimal-package"

echo "   ✅ Minimal package created ($(find "$SCRIPT_DIR/01-minimal-package" -type f | wc -l | tr -d ' ') files)"
echo ""

# 2. CLI Tool
echo "[0-9].  Generating cli-tool..."
uv tool run copier copy \
  --trust \
  --defaults \
  --data project_name="CLI Tool Example" \
  --data project_description="A command-line tool with quality enforcement" \
  --data project_slug="cli-tool-example" \
  --data author_name="Example Author" \
  --data author_email="author@example.com" \
  --data include_cli=true \
  --data cli_framework=typer \
  --data include_quality_scripts=true \
  --data include_ai_tools=false \
  --data include_docker=false \
  --data include_docs=false \
  --data include_pre_commit=true \
  "$TEMPLATE_DIR" "$SCRIPT_DIR/02-cli-tool"

echo "   ✅ CLI tool created ($(find "$SCRIPT_DIR/02-cli-tool" -type f | wc -l | tr -d ' ') files)"
echo ""

# 3. Library
echo "[0-9].  Generating library..."
uv tool run copier copy \
  --trust \
  --defaults \
  --data project_name="Library Example" \
  --data project_description="A reusable Python library with strict quality standards" \
  --data project_slug="library-example" \
  --data author_name="Example Author" \
  --data author_email="author@example.com" \
  --data include_quality_scripts=true \
  --data min_coverage=90 \
  --data include_pre_commit=true \
  --data include_ai_tools=false \
  --data include_docker=false \
  --data include_docs=false \
  "$TEMPLATE_DIR" "$SCRIPT_DIR/03-library"

echo "   ✅ Library created ($(find "$SCRIPT_DIR/03-library" -type f | wc -l | tr -d ' ') files)"
echo ""

# 4. Data Science
echo "[0-9].  Generating data-science..."
uv tool run copier copy \
  --trust \
  --defaults \
  --data project_name="Data Science Project" \
  --data project_description="ML and data analysis project with reproducibility" \
  --data project_slug="data-science-project" \
  --data author_name="Example Author" \
  --data author_email="author@example.com" \
  --data include_quality_scripts=true \
  --data include_docker=true \
  --data include_docs=true \
  --data include_ai_tools=false \
  --data min_coverage=70 \
  "$TEMPLATE_DIR" "$SCRIPT_DIR/04-data-science"

echo "   ✅ Data science project created ($(find "$SCRIPT_DIR/04-data-science" -type f | wc -l | tr -d ' ') files)"
echo ""

# 5. Web API
echo "[0-9].  Generating web-api..."
uv tool run copier copy \
  --trust \
  --defaults \
  --data project_name="Web API Example" \
  --data project_description="RESTful API service with Docker" \
  --data project_slug="web-api-example" \
  --data author_name="Example Author" \
  --data author_email="author@example.com" \
  --data include_quality_scripts=true \
  --data include_docker=true \
  --data include_docs=true \
  --data include_pre_commit=true \
  --data include_ai_tools=false \
  "$TEMPLATE_DIR" "$SCRIPT_DIR/05-web-api"

echo "   ✅ Web API created ($(find "$SCRIPT_DIR/05-web-api" -type f | wc -l | tr -d ' ') files)"
echo ""

# 6. AI-Assisted
echo "[0-9].  Generating ai-assisted..."
uv tool run copier copy \
  --trust \
  --defaults \
  --data project_name="AI Assisted Project" \
  --data project_description="Development with AI coding assistants" \
  --data project_slug="ai-assisted-project" \
  --data author_name="Example Author" \
  --data author_email="author@example.com" \
  --data include_ai_tools=true \
  --data ai_tools_preset=all \
  --data include_quality_scripts=true \
  --data include_docker=false \
  --data include_docs=false \
  "$TEMPLATE_DIR" "$SCRIPT_DIR/06-ai-assisted"

echo "   ✅ AI-assisted project created ($(find "$SCRIPT_DIR/06-ai-assisted" -type f | wc -l | tr -d ' ') files)"
echo ""

# 7. Full-Featured
echo "[0-9].  Generating full-featured..."
uv tool run copier copy \
  --trust \
  --defaults \
  --data project_name="Full Featured Application" \
  --data project_description="Production-ready application with all features" \
  --data project_slug="full-featured-app" \
  --data author_name="Example Author" \
  --data author_email="author@example.com" \
  --data include_quality_scripts=true \
  --data include_ai_tools=true \
  --data include_docker=true \
  --data include_docs=true \
  --data include_pre_commit=true \
  --data include_cli=true \
  --data cli_framework=typer \
  "$TEMPLATE_DIR" "$SCRIPT_DIR/07-full-featured"

echo "   ✅ Full-featured app created ($(find "$SCRIPT_DIR/07-full-featured" -type f | wc -l | tr -d ' ') files)"
echo ""

echo " All examples generated successfully!"
echo ""
echo "Examples created in:"
echo "  - examples/01-minimal-package/"
echo "  - examples/02-cli-tool/"
echo "  - examples/03-library/"
echo "  - examples/04-data-science/"
echo "  - examples/05-web-api/"
echo "  - examples/06-ai-assisted/"
echo "  - examples/07-full-featured/"
echo ""
echo " See examples/README.md for details on each configuration"
