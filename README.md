## Project Overview:
This project implements N4 Bias Field Correction to improve image quality by removing uneven illumination and brightness artifacts. The preprocessing pipeline is designed to clean images before using them in machine learning and computer vision models.
The script processes images in bulk, applies N4 bias correction using SimpleITK, normalizes the output, and saves viewable images ready for annotation and training platforms like Roboflow.

# Key Features:
Removes non-uniform lighting (bias field) from images
Batch processing for large datasets (thousands of images)
Converts corrected images to standard viewable format
Optimized for Windows laptops (CPU-based, no GPU required)
Suitable for ML, CV, and medical imaging preprocessing



## Technologies Used:
Python
SimpleITK
NumPy
tqdm

#Workflow:

Raw Images
   ↓
   
N4 Bias Field Correction
   ↓
   
Normalized & Clean Images
   ↓
   
Upload to Roboflow / ML Training 


## Sample Input & Output (N4 Bias Correction)
This section demonstrates how N4 Bias Field Correction improves image quality by removing uneven illumination.

# Sample Input Image (Before N4 Bias Correction)
This image contains non-uniform brightness caused by lighting or sensor artifacts.

 ![11](https://github.com/user-attachments/assets/54377b80-9544-4b01-a8fd-be26cbe7ed0e)


#Sample Output Image (After N4 Bias Correction)
After applying N4 Bias Field Correction, the illumination becomes uniform while preserving important image details.


![11](https://github.com/user-attachments/assets/2aa43b6f-2f07-4bec-b925-201d57e17215)


# What changed?

Uneven brightness is reduced
Image intensity becomes more uniform
Important structures/features remain intact
Image becomes more suitable for ML training



# Why this matters
Machine learning models can be sensitive to lighting variations.
By applying N4 Bias Correction before annotation and training, the model focuses on real features instead of illumination noise.

## Note
Only sample images are included in this repository for demonstration purposes.
The full dataset is processed locally before uploading to training platforms like Roboflow.

## Folder structure

project/

├── input_images/       # your original images

├── output_n4_images/  # corrected images will appear here

└── n4_bias.py

# How to reproduce this result

Place your raw images inside input_images/
Run the N4 bias correction script:
python n4_bias.py
Processed images will be saved in output_n4_images/


## Result

Clean, illumination-corrected images ready for:

Annotation

Roboflow preprocessing

YOLO / ML model training




