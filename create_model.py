"""
Script to create a demo MRI tumor detection model
Run this before starting the Flask app
"""

import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.applications import VGG16
from tensorflow.keras.optimizers import Adam

def create_model():
    """Create and save a pre-trained MRI tumor detection model"""
    
    print("=" * 60)
    print("Creating MRI Tumor Detection Model...")
    print("=" * 60)
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    try:
        # Load pre-trained VGG16 model
        print("\n[1/4] Loading VGG16 base model...")
        base_model = VGG16(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
        
        # Freeze base model layers
        base_model.trainable = False
        print("✓ VGG16 base model loaded and frozen")
        
        # Create sequential model
        print("\n[2/4] Building model architecture...")
        model = Sequential([
            base_model,
            Flatten(),
            Dense(512, activation='relu'),
            Dropout(0.5),
            Dense(256, activation='relu'),
            Dropout(0.5),
            Dense(128, activation='relu'),
            Dropout(0.3),
            Dense(4, activation='softmax')  # 4 tumor classes
        ])
        print("✓ Model architecture created")
        
        # Compile the model
        print("\n[3/4] Compiling model...")
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        print("✓ Model compiled successfully")
        
        # Display model summary
        print("\n[4/4] Model Summary:")
        print("-" * 60)
        model.summary()
        print("-" * 60)
        
        # Save the model
        print("\nSaving model...")
        model.save('models/model.h5')
        print("✓ Model saved to: models/model.h5")
        
        print("\n" + "=" * 60)
        print("SUCCESS! Model created and ready to use.")
        print("You can now run: python main.py")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nTroubleshooting:")
        print("- Make sure TensorFlow is installed: pip install tensorflow")
        print("- Make sure you have internet for downloading VGG16 weights")
        print("- Check your disk space (VGG16 weights are ~58MB)")
        return False

if __name__ == "__main__":
    success = create_model()
    if not success:
        exit(1)
