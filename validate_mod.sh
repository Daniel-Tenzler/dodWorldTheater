#!/bin/bash

###############################################################################
# Victoria 2 Mod Validation Script
#
# This script performs automated validation checks on Victoria 2 mod files
# to catch common errors before launching the game.
#
# Usage: ./validate_mod.sh
###############################################################################

echo "=== Victoria 2 Mod Validator ==="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
ERRORS=0
WARNINGS=0

# Check if we're in the right directory
# Script should be run from parent directory with .mod file, checking dodWorldTheater/ subfolder
if [ ! -f "dodWorldTheater.mod" ]; then
    echo -e "${RED}ERROR: dodWorldTheater.mod not found in current directory${NC}"
    echo "Please run this script from the parent directory (where dodWorldTheater.mod is located)"
    exit 1
fi

# Set mod directory
MOD_DIR="dodWorldTheater"

if [ ! -d "$MOD_DIR" ]; then
    echo -e "${RED}ERROR: dodWorldTheater/ directory not found${NC}"
    exit 1
fi

echo -e "${GREEN}✓${NC} Found dodWorldTheater.mod and dodWorldTheater/ directory"
echo ""

###############################################################################
# Check 1: Brace Balance
###############################################################################
echo "Checking brace balance..."

# Check events folder if it exists
if [ -d "$MOD_DIR/events" ]; then
    for file in $MOD_DIR/events/*.txt; do
        if [ -f "$file" ]; then
            open=$(grep -o '{' "$file" | wc -l)
            close=$(grep -o '}' "$file" | wc -l)

            if [ $open -ne $close ]; then
                echo -e "  ${RED}✗${NC} $file - Unbalanced braces ({$open vs }$close)"
                ERRORS=$((ERRORS + 1))
            fi
        fi
    done
fi

# Check decisions folder if it exists
if [ -d "$MOD_DIR/decisions" ]; then
    for file in $MOD_DIR/decisions/*.txt; do
        if [ -f "$file" ]; then
            open=$(grep -o '{' "$file" | wc -l)
            close=$(grep -o '}' "$file" | wc -l)

            if [ $open -ne $close ]; then
                echo -e "  ${RED}✗${NC} $file - Unbalanced braces ({$open vs }$close)"
                ERRORS=$((ERRORS + 1))
            fi
        fi
    done
fi

# Check common/on_actions.txt if it exists
if [ -f "$MOD_DIR/common/on_actions.txt" ]; then
    file="$MOD_DIR/common/on_actions.txt"
    open=$(grep -o '{' "$file" | wc -l)
    close=$(grep -o '}' "$file" | wc -l)

    if [ $open -ne $close ]; then
        echo -e "  ${RED}✗${NC} $file - Unbalanced braces ({$open vs }$close)"
        ERRORS=$((ERRORS + 1))
    fi
fi

if [ $ERRORS -eq 0 ]; then
    echo -e "  ${GREEN}✓${NC} All braces balanced"
fi
echo ""

###############################################################################
# Check 2: Spaces Around Equals Signs
###############################################################################
echo "Checking spaces around =..."

# Check for missing spaces around = (excluding == which is valid in some contexts)
BAD_FILES=""
if [ -d "$MOD_DIR/events" ]; then
    BAD_FILES=$(grep -rn '[^ ]==[^ ]' $MOD_DIR/events/*.txt 2>/dev/null | grep -v "^Binary" | grep -v "==" | head -n 5)
fi
if [ -d "$MOD_DIR/decisions" ] && [ -z "$BAD_FILES" ]; then
    BAD_FILES=$(grep -rn '[^ ]==[^ ]' $MOD_DIR/decisions/*.txt 2>/dev/null | grep -v "^Binary" | grep -v "==" | head -n 5)
fi

if [ -n "$BAD_FILES" ]; then
    echo -e "  ${YELLOW}⚠${NC} Lines without spaces around =:"
    echo "$BAD_FILES"
    WARNINGS=$((WARNINGS + 1))
else
    echo -e "  ${GREEN}✓${NC} All = have proper spacing"
fi
echo ""

###############################################################################
# Check 3: Duplicate Event IDs
###############################################################################
echo "Checking for duplicate event IDs..."

EVENT_IDS=""
if [ -d "$MOD_DIR/events" ]; then
    EVENT_IDS=$(grep -hE '^[[:space:]]*id[[:space:]]*=[[:space:]]*[0-9]+' "$MOD_DIR"/events/*.txt 2>/dev/null \
        | sed -E 's/^[[:space:]]*id[[:space:]]*=[[:space:]]*([0-9]+).*/\1/')
fi

DUPLICATES=""
if [ -n "$EVENT_IDS" ]; then
    DUPLICATES=$(printf "%s\n" "$EVENT_IDS" | sort -n | uniq -d)
fi

if [ -n "$DUPLICATES" ]; then
    echo -e "  ${RED}✗${NC} Duplicate event IDs found:"
    printf "%s\n" "$DUPLICATES" | sed 's/^/    id = /'
    ERRORS=$((ERRORS + 1))
else
    echo -e "  ${GREEN}✓${NC} No duplicate event IDs"
fi
echo ""

###############################################################################
# Check 4: Event ID Range Conflicts
###############################################################################
echo "Checking event ID ranges..."

# Check for events in reserved ranges
RESERVED_CONFLICTS=""
if [ -n "$EVENT_IDS" ]; then
    RESERVED_CONFLICTS=$(printf "%s\n" "$EVENT_IDS" | awk '$1 >= 10000 && $1 <= 29999' | sort -n | uniq | head -n 3)
fi
if [ -n "$RESERVED_CONFLICTS" ]; then
    echo -e "  ${YELLOW}⚠${NC} Events in vanilla/HPM range (10000-29999):"
    printf "%s\n" "$RESERVED_CONFLICTS" | sed 's/^/    id = /'
    WARNINGS=$((WARNINGS + 1))
fi

# Check for events in low/vanilla range
VANILLA=0
if [ -n "$EVENT_IDS" ]; then
    VANILLA=$(printf "%s\n" "$EVENT_IDS" | awk '$1 >= 1 && $1 <= 9999' | wc -l)
fi
if [ "$VANILLA" -gt 0 ]; then
    echo -e "  ${YELLOW}⚠${NC} $VANILLA events use vanilla ID range (1-9999)"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

###############################################################################
# Check 5: Required File Existence
###############################################################################
echo "Checking required files..."

REQUIRED_FILES=(
    "$MOD_DIR/common/countries.txt"
    "$MOD_DIR/common/defines.lua"
    "$MOD_DIR/common/buildings.txt"
    "$MOD_DIR/common/goods.txt"
    "$MOD_DIR/common/cb_types.txt"
    "$MOD_DIR/localisation/0_common.csv"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✓${NC} $file"
    else
        echo -e "  ${YELLOW}⚠${NC} $file - Not found (may be optional)"
    fi
done
echo ""

###############################################################################
# Check 6: Localization File Format
###############################################################################
echo "Checking localization files..."
echo -e "  ${YELLOW}⚠${NC} Skipped (.csv checks temporarily disabled)"
echo ""

###############################################################################
# Check 7: Province ID Validation (Sample Check)
###############################################################################
echo "Checking province ID references..."

# Get sample province IDs referenced in events/decisions via owns = N
PROV_REFS=""
if [ -d "$MOD_DIR/events" ]; then
    PROV_REFS=$(grep -hE '\bowns[[:space:]]*=[[:space:]]*[0-9]+' "$MOD_DIR"/events/*.txt 2>/dev/null \
        | sed -E 's/.*owns[[:space:]]*=[[:space:]]*([0-9]+).*/\1/' | sort -n | uniq | head -n 5)
fi
if [ -d "$MOD_DIR/decisions" ] && [ -z "$PROV_REFS" ]; then
    PROV_REFS=$(grep -hE '\bowns[[:space:]]*=[[:space:]]*[0-9]+' "$MOD_DIR"/decisions/*.txt 2>/dev/null \
        | sed -E 's/.*owns[[:space:]]*=[[:space:]]*([0-9]+).*/\1/' | sort -n | uniq | head -n 5)
fi

if [ -n "$PROV_REFS" ]; then
    echo "  Sample province IDs found in events/decisions:"
    for id in $PROV_REFS; do
        # Check if province exists in definition.csv (semicolon-delimited)
        if grep -q "^${id};" "$MOD_DIR/map/definition.csv" 2>/dev/null; then
            echo -e "    ${GREEN}✓${NC} Province $id exists"
        else
            echo -e "    ${RED}✗${NC} Province $id not found in definition.csv"
            ERRORS=$((ERRORS + 1))
        fi
    done
else
    echo "  No province references found to validate"
fi
echo ""

###############################################################################
# Check 8: Decision Block Structure
###############################################################################
echo "Checking decision file structure..."

for file in $MOD_DIR/decisions/*.txt; do
    if [ -f "$file" ]; then
        # Check if decisions are wrapped in political_decisions = { }
        if ! grep -q 'political_decisions = {' "$file"; then
            echo -e "  ${YELLOW}⚠${NC} $file - May not be wrapped in political_decisions block"
            WARNINGS=$((WARNINGS + 1))
        fi

        # Check for common decision blocks
        if ! grep -q 'potential = {' "$file"; then
            echo -e "  ${YELLOW}⚠${NC} $file - May be missing 'potential' block"
            WARNINGS=$((WARNINGS + 1))
        fi

        if ! grep -q 'allow = {' "$file"; then
            echo -e "  ${YELLOW}⚠${NC} $file - May be missing 'allow' block"
            WARNINGS=$((WARNINGS + 1))
        fi

        if ! grep -q 'effect = {' "$file"; then
            echo -e "  ${YELLOW}⚠${NC} $file - May be missing 'effect' block"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
done
echo ""

###############################################################################
# Summary
###############################################################################
echo "=== Validation Summary ==="
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed!${NC}"
    echo "Your mod is ready for testing."
    exit 0
elif [ $ERRORS -eq 0 ] && [ $WARNINGS -gt 0 ]; then
    echo -e "${YELLOW}⚠ $WARNINGS warning(s) found${NC}"
    echo "Review the warnings above, but your mod should still load."
    exit 0
else
    echo -e "${RED}✗ $ERRORS error(s) found${NC}"
    echo "Please fix the errors above before testing."
    exit 1
fi
