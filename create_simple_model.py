"""
Simple model creation for testing Flask app
This creates a placeholder model file
"""

import pickle
import os

# Create a simple model dictionary
demo_model = {
    'name': 'MRI Tumor Detection Model',
    'type': 'VGG16-based',
    'classes': ['pituitary', 'glioma', 'notumor', 'meningioma'],
    'version': '1.0 (Demo)'
}

# Create models directory
os.makedirs('models', exist_ok=True)

# Save as pickle (simpler than h5)
model_path = 'models/model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(demo_model, f)

print("✓ Demo model created at: models/model.pkl")
print(f"  Model Info: {demo_model}")
