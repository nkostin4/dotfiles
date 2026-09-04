#!/bin/sh

INPUT="audio.mp3"
TIMESTAMPS="timestamps"

prev=""

while IFS= read -r ts || [ -n "$ts" ]; do
    # Skip blank lines
    [ -z "$ts" ] && continue

    if [ -n "$prev" ]; then
        outfile=$(printf '%s.mp3' "$(printf '%s' "$prev" | tr ':' '_')")

        ffmpeg -hide_banner -loglevel error \
            -ss "$prev" \
            -to "$ts" \
            -i "$INPUT" \
            -c copy \
            "$outfile"
    fi

    prev="$ts"
done < "$TIMESTAMPS"

# Extract the final segment (last timestamp -> end of file)
if [ -n "$prev" ]; then
    outfile=$(printf '%s.mp3' "$(printf '%s' "$prev" | tr ':' '_')")

    ffmpeg -hide_banner -loglevel error \
        -ss "$prev" \
        -i "$INPUT" \
        -c copy \
        "$outfile"
fi
