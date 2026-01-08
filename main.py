from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import random

# Initialize Flask app
app = Flask(__name__)

# Class labels
class_labels = ['pituitary', 'glioma', 'notumor', 'meningioma']

# Define the uploads folder
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to predict tumor type (Demo version)
def predict_tumor(image_path):
    """
    Demo prediction function for testing
    In production, this would use the actual model
    """
    # For demo purposes, return random prediction
    predicted_class_index = random.randint(0, 3)
    confidence_score = random.uniform(0.7, 0.99)
    
    tumor_type = class_labels[predicted_class_index]
    
    if tumor_type == 'notumor':
        return "No Tumor Detected", confidence_score
    else:
        return f"Tumor Detected: {tumor_type.upper()}", confidence_score

# Route for the main page (index.html)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        file = request.files.get('file')
        if file and file.filename != '':
            try:
                # Save the file
                filename = file.filename
                file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_location)

                # Predict the tumor
                result, confidence = predict_tumor(file_location)

                # Return result along with image path for display
                return render_template('INDEX.html', 
                                     result=result, 
                                     confidence=f"{confidence*100:.2f}%", 
                                     file_path=f'/uploads/{filename}')
            except Exception as e:
                return render_template('INDEX.html', 
                                     result=f"Error: {str(e)}", 
                                     confidence="0%",
                                     file_path=None)

    return render_template('INDEX.html', result=None)

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def get_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Health check route
@app.route('/health')
def health():
    return jsonify({"status": "ok", "app": "MRI Tumor Detection System"})

if __name__ == '__main__':
    print("=" * 60)
    print("MRI Tumor Detection System - Flask App")
    print("=" * 60)
    print("\n✓ Flask app starting...")
    print("✓ Visit: http://127.0.0.1:5000")
    print("✓ Press Ctrl+C to stop\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)