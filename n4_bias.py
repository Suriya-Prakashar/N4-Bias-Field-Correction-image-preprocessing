import SimpleITK as sitk
import os
from tqdm import tqdm

INPUT_DIR = "input_images/10"
OUTPUT_DIR = "output_n4_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in tqdm(os.listdir(INPUT_DIR)):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        # Read image
        image = sitk.ReadImage(input_path, sitk.sitkFloat32)

        # Create mask
        mask = sitk.OtsuThreshold(image, 0, 1, 200)

        # N4 correction
        corrector = sitk.N4BiasFieldCorrectionImageFilter()
        corrector.SetMaximumNumberOfIterations([50, 50, 30])
        corrector.SetConvergenceThreshold(0.001)

        corrected = corrector.Execute(image, mask)

        # Normalize + convert to uint8 (CRITICAL STEP)
        corrected = sitk.RescaleIntensity(corrected, 0, 255)
        corrected = sitk.Cast(corrected, sitk.sitkUInt8)

        # Save
        sitk.WriteImage(corrected, output_path)

print("✅ N4 Bias Correction completed (images saved correctly)")
