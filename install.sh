#!/usr/bin/env bash
# Install or update the SEO-knowledge skill into ~/.claude/skills/SEO-knowledge (git clone or pull).
set -euo pipefail
DEST="$HOME/.claude/skills/SEO-knowledge"
REPO="https://github.com/aleksandark-bot/seo-knowledge-skill.git"
command -v git >/dev/null || { echo "git is required"; exit 1; }
command -v python3 >/dev/null || { echo "python3 is required"; exit 1; }
if [[ -d "$DEST/.git" ]]; then
  git -C "$DEST" pull -q --ff-only && echo "SEO-knowledge updated: $(git -C "$DEST" log -1 --format=%s)"
else
  mkdir -p "$HOME/.claude/skills"
  git clone -q "$REPO" "$DEST" && echo "SEO-knowledge installed to $DEST"
fi
python3 "$DEST/scripts/kb.py" stats
echo "Restart Claude Code. Optional: tell it in ~/.claude/CLAUDE.md to invoke SEO-knowledge at the start of every SEO task."
