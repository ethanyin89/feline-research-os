#!/bin/bash
# scripts/setup_cron.sh
# Set up automated health checks for feline-research-os
#
# Usage:
#   ./scripts/setup_cron.sh          # Install launchd plist
#   ./scripts/setup_cron.sh --remove # Remove launchd plist

set -e

PLIST_NAME="com.feline-research.health"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV_PYTHON="${PROJECT_ROOT}/.venv/bin/python"

if [ "$1" = "--remove" ]; then
    echo "Removing launchd plist..."
    launchctl unload "$PLIST_PATH" 2>/dev/null || true
    rm -f "$PLIST_PATH"
    echo "Done."
    exit 0
fi

# Check venv exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "ERROR: .venv not found at $PROJECT_ROOT/.venv"
    echo "Run: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
    exit 1
fi

echo "Creating launchd plist for daily health checks..."

cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>${VENV_PYTHON}</string>
        <string>${PROJECT_ROOT}/scripts/health.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>${PROJECT_ROOT}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>${PROJECT_ROOT}/logs/health-stdout.log</string>
    <key>StandardErrorPath</key>
    <string>${PROJECT_ROOT}/logs/health-stderr.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin</string>
    </dict>
</dict>
</plist>
EOF

# Create logs directory
mkdir -p "${PROJECT_ROOT}/logs"

# Load the plist
launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH"

echo "Done. Health check scheduled for 9:00 AM daily."
echo ""
echo "To run manually: .venv/bin/python scripts/health.py"
echo "To check status: launchctl list | grep feline"
echo "To remove: ./scripts/setup_cron.sh --remove"
