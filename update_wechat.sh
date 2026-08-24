#!/bin/bash

set -e

# 1. Pull: only allow fast-forward
echo "==> Pulling latest changes..."
if ! git pull --ff-only; then
    echo "Error: git pull --ff-only failed. Aborting."
    exit 1
fi


# 2. Try to activate RoboTwin conda environment if it exists
if command -v conda >/dev/null 2>&1; then
    # Make `conda activate` available in non-interactive shell
    CONDA_BASE="$(conda info --base 2>/dev/null || true)"

    if [ -n "$CONDA_BASE" ] && [ -f "$CONDA_BASE/etc/profile.d/conda.sh" ]; then
        source "$CONDA_BASE/etc/profile.d/conda.sh"

        if conda env list | awk '{print $1}' | grep -qx "RoboTwin"; then
            echo "==> Activating conda environment: RoboTwin"
            conda activate RoboTwin
        fi
    fi
fi


# 3. Check mkdocs
if ! command -v mkdocs >/dev/null 2>&1; then
    echo "Error: mkdocs not found."
    exit 1
fi


# 4. Find source image
jpg_file=$(find . -maxdepth 1 -type f \( -iname '*.jpg' -o -iname '*.jpeg' \) -print -quit)

if [ -n "$jpg_file" ]; then
    image_file="$jpg_file"
else
    png_file=$(find . -maxdepth 1 -type f -iname '*.png' -print -quit)

    if [ -z "$png_file" ]; then
        echo "Error: No jpg, jpeg, or png file found in the current directory."
        exit 1
    fi

    image_file="$png_file"
fi

echo "==> Using image: $image_file"


# 5. Copy image first; keep original until everything succeeds
target_file="./docs/community/images/wechat-group.jpg"

echo "==> Copying image to $target_file"
cp "$image_file" "$target_file"


# 6. Deploy
echo "==> Deploying MkDocs..."
if ! mkdocs gh-deploy \
    --remote-name origin \
    --remote-branch gh-pages; then
    echo "Error: mkdocs gh-deploy failed."
    exit 1
fi


# 7. Commit source branch
echo "==> Committing changes..."
git add .

# Avoid failing when there is nothing to commit
if ! git diff --cached --quiet; then
    git commit -m "update"
else
    echo "==> No changes to commit."
fi


# 8. Push
echo "==> Pushing changes..."
if ! git push; then
    echo "Error: git push failed. Original image will NOT be deleted."
    exit 1
fi


# 9. Everything succeeded; now remove original image
echo "==> Everything succeeded. Removing original image: $image_file"
rm -- "$image_file"

echo "==> Done."