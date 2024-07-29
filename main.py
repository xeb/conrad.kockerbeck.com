# main.py
from jinja2 import Environment, FileSystemLoader
import json

# Load data from a JSON file
with open('data.json', 'r') as f:
    raw_data = json.load(f)

# Process the data into a new structure
data = {
    'title': raw_data.get('title', ''),
    'intro': {
        'title': raw_data.get('intro', {}).get('title', ''),
        'content': raw_data.get('intro', {}).get('content', ''),
        'image': raw_data.get('intro', {}).get('image', '')
    },
    'banner': {
        'title': raw_data.get('banner', {}).get('title', ''),
        'content': raw_data.get('banner', {}).get('content', ''),
        'button_text': raw_data.get('banner', {}).get('button_text', ''),
        'image': raw_data.get('banner', {}).get('image', '')
    },
    'spotlights': raw_data.get('spotlights', []),
    'gallery': {
        'title': raw_data.get('gallery', {}).get('title', ''),
        'description': raw_data.get('gallery', {}).get('description', ''),
        'gallery_items': [
            {
                'full_image': item.get('full_image', ''),
                'thumb_image': item.get('thumb_image', ''),
                'title': item.get('title', ''),
                'description': item.get('description', ''),
                'button_text': item.get('button_text', '')
            }
            for item in raw_data.get('gallery', {}).get('items', [])
        ]
    }
}

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the processed data
output = template.render(data=data)

# Write the output to a file
with open('output.html', 'w') as f:
    f.write(output)

print("HTML file generated successfully!")
