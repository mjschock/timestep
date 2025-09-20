#!/bin/bash

# Timestep Version Bump Script
# Automatically bumps the version in package.json, package-lock.json, and example files using yyyy.m.ddhhmm format (semver-compliant)

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory and project paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")/typescript/timestep"
PACKAGE_JSON="$PROJECT_DIR/package.json"
PACKAGE_LOCK="$PROJECT_DIR/package-lock.json"
EXAMPLES_DIR="$PROJECT_DIR/examples"

echo -e "${BLUE}🔧 Timestep Version Bump Tool${NC}"
echo "==============================================="

# Check if we're in the right directory structure
if [[ ! -f "$PACKAGE_JSON" ]]; then
    echo -e "${RED}❌ Error: package.json not found at $PACKAGE_JSON${NC}"
    echo "   Make sure you're running this from the timestep project root"
    exit 1
fi

if [[ ! -f "$PACKAGE_LOCK" ]]; then
    echo -e "${RED}❌ Error: package-lock.json not found at $PACKAGE_LOCK${NC}"
    exit 1
fi

# Get current version
CURRENT_VERSION=$(grep '"version":' "$PACKAGE_JSON" | head -1 | sed 's/.*"version": *"\([^"]*\)".*/\1/')
echo -e "${YELLOW}📦 Current version: ${CURRENT_VERSION}${NC}"

# Generate new version using current timestamp (semver-compliant format)
NEW_VERSION=$(date '+%Y.%-m.%d%H%M')
echo -e "${YELLOW}🚀 New version: ${NEW_VERSION}${NC}"

# Check if version actually changed
if [[ "$CURRENT_VERSION" == "$NEW_VERSION" ]]; then
    echo -e "${YELLOW}⚠️  Warning: Version unchanged (${NEW_VERSION})${NC}"
    echo "   This can happen if you run the script multiple times in the same minute"
    
    # Check if running in non-interactive mode (e.g., from make)
    if [[ ! -t 0 ]]; then
        echo -e "${YELLOW}   Non-interactive mode detected, continuing anyway...${NC}"
    else
        read -p "   Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${BLUE}🛑 Version bump cancelled${NC}"
            exit 1
        fi
    fi
fi

echo
echo -e "${BLUE}📝 Updating version files...${NC}"

# Create backup files
echo -e "${YELLOW}💾 Creating backups...${NC}"
cp "$PACKAGE_JSON" "$PACKAGE_JSON.backup"
cp "$PACKAGE_LOCK" "$PACKAGE_LOCK.backup"

# Create backup of examples directory if it exists
if [[ -d "$EXAMPLES_DIR" ]]; then
    cp -r "$EXAMPLES_DIR" "$EXAMPLES_DIR.backup"
    echo -e "${YELLOW}💾 Examples directory backed up${NC}"
fi

# Update package.json
echo -e "${YELLOW}📦 Updating package.json...${NC}"
if sed -i.tmp "s/\"version\": *\"[^\"]*\"/\"version\": \"$NEW_VERSION\"/" "$PACKAGE_JSON"; then
    rm "$PACKAGE_JSON.tmp" 2>/dev/null || true
    echo -e "${GREEN}✅ package.json updated${NC}"
else
    echo -e "${RED}❌ Failed to update package.json${NC}"
    exit 1
fi

# Update package-lock.json (replace all occurrences)
echo -e "${YELLOW}🔒 Updating package-lock.json...${NC}"
if sed -i.tmp "s/\"version\": *\"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/g" "$PACKAGE_LOCK"; then
    rm "$PACKAGE_LOCK.tmp" 2>/dev/null || true
    echo -e "${GREEN}✅ package-lock.json updated${NC}"
else
    echo -e "${RED}❌ Failed to update package-lock.json${NC}"
    exit 1
fi

# Update example files
echo -e "${YELLOW}📚 Updating example files...${NC}"
EXAMPLE_FILES_UPDATED=0
if [[ -d "$EXAMPLES_DIR" ]]; then
    # Find all .ts files in examples directory
    for file in "$EXAMPLES_DIR"/*.ts; do
        if [[ -f "$file" ]]; then
            echo -e "${YELLOW}   Checking $(basename "$file")...${NC}"
            if grep -q "npm:@timestep-ai/timestep@" "$file"; then
                echo -e "${YELLOW}   Updating $(basename "$file")...${NC}"
                sed -i.tmp "s/npm:@timestep-ai\/timestep@[^']*/npm:@timestep-ai\/timestep@$NEW_VERSION/g" "$file"
                rm "$file.tmp" 2>/dev/null || true
                echo -e "${GREEN}   ✅ $(basename "$file") updated${NC}"
                EXAMPLE_FILES_UPDATED=$((EXAMPLE_FILES_UPDATED + 1))
            else
                echo -e "${YELLOW}   Skipping $(basename "$file") - no version references${NC}"
            fi
        fi
    done
    
    if [[ $EXAMPLE_FILES_UPDATED -gt 0 ]]; then
        echo -e "${GREEN}✅ Updated $EXAMPLE_FILES_UPDATED example file(s)${NC}"
    else
        echo -e "${YELLOW}⚠️  No example files found with version references${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Examples directory not found: $EXAMPLES_DIR${NC}"
fi

# Verify the changes
echo
echo -e "${BLUE}🔍 Verifying changes...${NC}"
NEW_PACKAGE_VERSION=$(grep '"version":' "$PACKAGE_JSON" | head -1 | sed 's/.*"version": *"\([^"]*\)".*/\1/')
if [[ "$NEW_PACKAGE_VERSION" == "$NEW_VERSION" ]]; then
    echo -e "${GREEN}✅ package.json version confirmed: ${NEW_VERSION}${NC}"
else
    echo -e "${RED}❌ package.json version verification failed${NC}"
    echo -e "${RED}   Expected: ${NEW_VERSION}, Got: ${NEW_PACKAGE_VERSION}${NC}"
    exit 1
fi

# Test build
echo
echo -e "${BLUE}🏗️  Testing build...${NC}"
cd "$PROJECT_DIR"
if npm run build > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Build successful${NC}"
else
    echo -e "${RED}❌ Build failed${NC}"
    echo -e "${YELLOW}🔄 Restoring backup files...${NC}"
    mv "$PACKAGE_JSON.backup" "$PACKAGE_JSON"
    mv "$PACKAGE_LOCK.backup" "$PACKAGE_LOCK"
    if [[ -d "$EXAMPLES_DIR.backup" ]]; then
        rm -rf "$EXAMPLES_DIR"
        mv "$EXAMPLES_DIR.backup" "$EXAMPLES_DIR"
        echo -e "${YELLOW}💾 Examples directory restored${NC}"
    fi
    echo -e "${YELLOW}💾 Backup files restored${NC}"
    exit 1
fi

# Clean up backup files
rm "$PACKAGE_JSON.backup" "$PACKAGE_LOCK.backup"
if [[ -d "$EXAMPLES_DIR.backup" ]]; then
    rm -rf "$EXAMPLES_DIR.backup"
fi

# Success message
echo
echo -e "${GREEN}🎉 Version bump complete!${NC}"
echo -e "${GREEN}   ${CURRENT_VERSION} → ${NEW_VERSION}${NC}"
echo
echo -e "${BLUE}📋 Summary:${NC}"
echo -e "${BLUE}   • package.json updated${NC}"
echo -e "${BLUE}   • package-lock.json updated${NC}"
if [[ $EXAMPLE_FILES_UPDATED -gt 0 ]]; then
    echo -e "${BLUE}   • $EXAMPLE_FILES_UPDATED example file(s) updated${NC}"
fi
echo -e "${BLUE}   • Build verified${NC}"
echo -e "${BLUE}   • Backup files cleaned up${NC}"
echo
echo -e "${YELLOW}💡 Next steps:${NC}"
echo -e "${YELLOW}   • Review changes: git diff${NC}"
echo -e "${YELLOW}   • Commit changes: git add . && git commit -m 'Bump version to ${NEW_VERSION}'${NC}"
echo -e "${YELLOW}   • Create release tag: git tag v${NEW_VERSION}${NC}"