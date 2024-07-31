from flask import Flask, render_template, send_from_directory, request
import os
import yaml 

app = Flask(__name__)

# Assuming your HTML files are in a directory named 'templates'
# and your videos are in a directory named 'videos'
app.template_folder = 'templates'
app.static_folder = 'static'

def get_data():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data.yaml file
    yaml_path = os.path.join(current_dir, 'data.yaml')
    
    # Read and parse the YAML file
    try:
        with open(yaml_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {yaml_path} was not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

def get_dynamic_data(pic_path):
    # Get all files in the pic_path in a list
    files = os.listdir(os.path.join("static", "pics", pic_path))
    return [{ 'title': file.split('.')[0], 'source': f'{pic_path}/{file}' } for file in files]

@app.route('/')
def index():
    data = get_data()
    galleries = data.get('galleries', [])
    for key in galleries.keys():
        pic_defs = galleries[key].get('pics', False)
        pic_dyno = get_dynamic_data(key)

        # If there are no overrides, use the dynamic discovered pics
        if not pic_defs and pic_dyno:
            galleries[key]['pics'] =  pic_dyno# we could have a path, but key is fine for this hack
        
        # If we do have some overrides, we need to merge them
        if pic_defs and pic_dyno:
            for item in pic_dyno:
                for defi in pic_defs:
                    if item['source'] == defi['source']:
                        item.update(defi)
                        
            galleries[key]['pics'] = pic_dyno

    return render_template('index.html', vids=data["vids"], pics=data["pics"], galleries=galleries)

@app.route('/video/<name>')
def serve_video(name):   
    # Construct the video URL
    video_src = f"/static/vids/{name}.avi"
    return render_template('player.html', video_src=video_src)

# @app.route('/videos/<path:filename>')
# def serve_video_file(filename):
#     return send_from_directory("vids", filename)

if __name__ == '__main__':
    app.run(debug=True, port=8007, host="0.0.0.0", extra_files=['data.yaml'])
