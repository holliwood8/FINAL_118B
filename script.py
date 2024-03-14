import os
import nibabel as nib
import glob

# Function to save arrays with their original file names
def save_nifti(paths, output_directory):
    for img_path in paths:
        img_data = nib.load(img_path).get_fdata()
        # Create a Nifti image from the numpy array
        img = nib.Nifti1Image(img_data, np.eye(4))
        # Extract the original file name without its path
        original_name = os.path.basename(img_path)
        # Construct the file path for the output
        file_path = os.path.join(output_directory, original_name)
        # Save the Nifti image to the new file path
        nib.save(img, file_path)


# do NOT run this -- used to create new dataset

# save flair images
# output_directory = 'flair_imgs'
# os.makedirs(output_directory, exist_ok=True)
# path = glob.glob('MICCAI_BraTS_2018_Data_Validation/**/**/*_flair.nii') + glob.glob('MICCAI_BraTS_2018_Data_Training/**/**/*_flair.nii') + glob.glob('MICCAI_BraTS_2019_Data_Training/**/**/*_flair.nii') + glob.glob('MICCAI_BraTS2020_TrainingData/**/*_flair.nii') + glob.glob('BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData/**/*_flair.nii')
# save_nifti(path, output_directory)

# Save segmented images
# path = glob.glob('MICCAI_BraTS_2018_Data_Training/**/**/*_seg.nii')+glob.glob('MICCAI_BraTS_2019_Data_Training/**/**/*_seg.nii')+glob.glob('MICCAI_BraTS2020_TrainingData/**/*_seg.nii')
# output_directory = 'seg_imgs'
# os.makedirs(output_directory, exist_ok=True)
# save_nifti(path, output_directory)