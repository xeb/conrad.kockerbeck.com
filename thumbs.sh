#!/bin/bash

# Directory containing the .avi files
VIDEO_DIR="vids"

# Directory to save the screenshots
OUTPUT_DIR="screenshots"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all .avi files in the VIDEO_DIR
for video in "$VIDEO_DIR"/*.avi; do
    # Check if there are any .avi files
    [ -e "$video" ] || continue

    # Get the filename without the path and extension
    filename=$(basename "$video" .avi)

    # Extract a screenshot at 1 second into the video
    ffmpeg -i "$video" -ss 00:00:01 -frames:v 1 "$OUTPUT_DIR/${filename}_screenshot.png"

    echo "Screenshot extracted from $video"
done

echo "All screenshots have been extracted to $OUTPUT_DIR"