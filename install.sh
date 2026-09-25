#!/usr/bin/env bash
# Install or update the SEO-knowledge skill at ~/.claude/skills/SEO-knowledge (a git clone of
# github.com/aleksandark-bot/seo-knowledge-skill). Works on a private repo: a read token from
# $PABAU_REPO_TOKEN, else ~/.claude/factcheck-flow/.repo-token (where the factcheck-flow
# installer saves it), else the factcheck-flow cluster token, is sent as a one-off HTTP
# header — never written to .git/config or into the remote URL, and off the command line on
# git 2.31+. A tokened attempt that fails is retried once without the token. Neither attempt
# ever prompts, and an SSH insteadOf rule in ~/.gitconfig cannot divert it off HTTPS.
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

# Token lookup, same order as factcheck-flow: env, its saved repo token, its cluster token.
_tok() { printf '%s' "${1:-}" | tr -d '[:space:]'; }
FFD="$HOME/.claude/factcheck-flow"
TOKEN="$(_tok "${PABAU_REPO_TOKEN:-}")"
[ -n "$TOKEN" ] || [ ! -s "$FFD/.repo-token" ] || TOKEN="$(_tok "$(cat "$FFD/.repo-token" 2>/dev/null || true)")"
[ -n "$TOKEN" ] || TOKEN="$(_tok "${PABAU_CLUSTERS_TOKEN:-}")"
[ -n "$TOKEN" ] || [ ! -s "$FFD/.clusters-token" ] || TOKEN="$(_tok "$(cat "$FFD/.clusters-token" 2>/dev/null || true)")"

# Never prompt, on either attempt: no terminal prompt, no askpass, no credential helper (Git
# Credential Manager would open a browser window), no SSH passphrase prompt.
export GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never GIT_ASKPASS=true SSH_ASKPASS=true \
       GIT_SSH_COMMAND='ssh -oBatchMode=yes'
# A user rule like url."git@github.com:".insteadOf=https://github.com/ would send this repo
# over SSH and past the token; the longest insteadOf wins, so map this repo onto itself.
PIN="url.https://github.com/aleksandark-bot/seo-knowledge-skill.insteadOf=https://github.com/aleksandark-bot/seo-knowledge-skill"
git_ge() { # git_ge MAJOR MINOR — the installed git is at least that version
  local v maj min
  v="$(git --version 2>/dev/null || true)"; v="${v#git version }"
  maj="${v%%.*}"; min="${v#*.}"; min="${min%%[!0-9]*}"
  case "$maj" in ''|*[!0-9]*) return 1 ;; esac
  [ -n "$min" ] || min=0
  [ "$maj" -gt "$1" ] && return 0
  [ "$maj" -eq "$1" ] && [ "$min" -ge "$2" ]
}
gitx() { # gitx <use-token 1|0> <git args...>
  local use="$1" hdr i
  shift
  set -- -c credential.helper= -c "$PIN" -c gc.auto=0 -c maintenance.auto=false "$@"
  if [ "$use" = 1 ] && [ -n "$TOKEN" ]; then
    hdr="$(printf 'x-access-token:%s' "$TOKEN" | base64 | tr -d '\n\r')"
    if git_ge 2 31; then
      # Off argv (not visible in ps): config from the environment, appended to any the user has.
      i="${GIT_CONFIG_COUNT:-0}"
      case "$i" in ''|*[!0-9]*) i=0 ;; esac
      ( export "GIT_CONFIG_KEY_$i=http.https://github.com/.extraheader" \
               "GIT_CONFIG_VALUE_$i=AUTHORIZATION: basic $hdr" "GIT_CONFIG_COUNT=$((i + 1))"
        exec git "$@" )
    else
      git -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $hdr" "$@"
    fi
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
