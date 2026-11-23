#!/usr/bin/env bash
# Back-compat wrapper. Prefer present-score.sh (no path needed).
exec "$(cd "$(dirname "$0")" && pwd)/present-score.sh" "$@"
