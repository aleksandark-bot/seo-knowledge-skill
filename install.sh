#!/usr/bin/env bash
# Install or update the SEO-knowledge skill at ~/.claude/skills/SEO-knowledge (a git clone of
# github.com/aleksandark-bot/seo-knowledge-skill). Works on a private repo: a read token from
# $PABAU_REPO_TOKEN, else ~/.claude/factcheck-flow/.repo-token (where the factcheck-flow
# installer saves it), is sent as a one-off HTTP header — never written to .git/config or
# into the remote URL. A tokened attempt that fails is retried once without the token.
# Updates are fast-forward only and are skipped when the clone has local changes or commits.
# Most people never need this: the factcheck-flow installer sets the skill up and its
# auto-updater keeps it current. Safe under macOS bash 3.2.
set -euo pipefail
DEST="$HOME/.claude/skills/SEO-knowledge"
REPO="https://github.com/aleksandark-bot/seo-knowledge-skill.git"

# A real git — on a Mac, /usr/bin/git is only a stub until the developer tools are installed.
g="$(command -v git 2>/dev/null || true)"
if [ -z "$g" ]; then echo "git is required (install it, then re-run)"; exit 1; fi
if [ "$(uname -s)" = Darwin ] && [ "$g" = /usr/bin/git ]; then
  dev="$(xcode-select -p 2>/dev/null || true)"
  if [ -z "$dev" ] || [ ! -x "$dev/usr/bin/git" ]; then
    echo "git needs the Mac developer tools: run  xcode-select --install , then re-run"; exit 1
  fi
fi
command -v python3 >/dev/null || { echo "python3 is required"; exit 1; }

TOKEN="$(printf '%s' "${PABAU_REPO_TOKEN:-}" | tr -d '[:space:]')"
[ -n "$TOKEN" ] || TOKEN="$(tr -d '[:space:]' < "$HOME/.claude/factcheck-flow/.repo-token" 2>/dev/null || true)"

export GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never
gitx() { # gitx <use-token 1|0> <git args...>
  local use="$1" hdr
  shift
  if [ "$use" = 1 ] && [ -n "$TOKEN" ]; then
    hdr="$(printf 'x-access-token:%s' "$TOKEN" | base64 | tr -d '\n\r')"
    git -c credential.helper= -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $hdr" "$@"
  else
    git "$@"
  fi
}
try() { # tokened first when there is a token, then once without
  if [ -n "$TOKEN" ] && gitx 1 "$@" 2>/dev/null; then return 0; fi
  gitx 0 "$@"
}

if [ -d "$DEST/.git" ]; then
  if [ -n "$(git -C "$DEST" status --porcelain)" ]; then
    echo "SEO-knowledge has local changes in $DEST — not updating"; exit 1
  fi
  try -C "$DEST" fetch -q --no-tags origin main
  new="$(git -C "$DEST" rev-parse FETCH_HEAD)"
  if [ "$new" = "$(git -C "$DEST" rev-parse HEAD)" ]; then
    echo "SEO-knowledge already up to date"
  elif git -C "$DEST" merge-base --is-ancestor HEAD "$new"; then
    git -C "$DEST" merge -q --ff-only "$new"
    echo "SEO-knowledge updated: $(git -C "$DEST" log -1 --format=%s)"
  else
    echo "SEO-knowledge has local commits that are not on GitHub — not updating"; exit 1
  fi
elif [ -e "$DEST" ]; then
  echo "$DEST exists but is not a git clone — move it aside, then re-run"; exit 1
else
  mkdir -p "$HOME/.claude/skills"
  tmp="$(mktemp -d "$HOME/.claude/skills/.SEO-knowledge.tmp.XXXXXX")"
  trap 'rm -rf "$tmp"' EXIT
  if [ -n "$TOKEN" ] && gitx 1 clone -q "$REPO" "$tmp/repo" 2>/dev/null; then :
  else rm -rf "$tmp/repo"; gitx 0 clone -q "$REPO" "$tmp/repo"
  fi
  mv "$tmp/repo" "$DEST"
  echo "SEO-knowledge installed to $DEST"
fi
python3 "$DEST/scripts/kb.py" stats
echo "Restart Claude Code. Optional: tell it in ~/.claude/CLAUDE.md to invoke SEO-knowledge at the start of every SEO task."
