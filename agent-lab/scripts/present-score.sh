#!/usr/bin/env bash
# Present whatever is in agent-lab/out/. No file picking.
#
# Opens MuseScore, opens the PDF, plays the audio.
# Optional argument: a score file to copy into out/ first.
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/.." && pwd)
OUT="$ROOT/out"
SCORE="$OUT/output.musicxml"
PDF="$OUT/output.pdf"
AUDIO="$OUT/output.ogg"
MUSESCORE="${MUSESCORE:-musescore}"
OPEN="${OPENER:-xdg-open}"

mkdir -p "$OUT"

if [[ $# -ge 1 ]]; then
  src=$1
  if [[ ! -f "$src" ]]; then
    echo "not a file: $src" >&2
    exit 1
  fi
  cp -f "$(readlink -f "$src")" "$SCORE"
fi

if [[ ! -f "$SCORE" ]]; then
  echo "nothing to present: $SCORE missing" >&2
  exit 1
fi

echo "exporting PDF"
QT_QPA_PLATFORM=offscreen "$MUSESCORE" -o "$PDF" "$SCORE"
echo "exporting audio"
QT_QPA_PLATFORM=offscreen "$MUSESCORE" -o "$AUDIO" "$SCORE"

if [[ ! -f "$PDF" ]]; then
  echo "PDF export failed" >&2
  exit 1
fi

"$OPEN" "$PDF" >/dev/null 2>&1 || true

env -u QT_QPA_PLATFORM "$MUSESCORE" "$SCORE" >/tmp/musescore-present.log 2>&1 &
disown

if [[ -f "$AUDIO" ]]; then
  echo "playing $AUDIO"
  paplay "$AUDIO" >/dev/null 2>&1 &
  disown
else
  echo "audio export failed; MuseScore and PDF should still be open" >&2
fi
