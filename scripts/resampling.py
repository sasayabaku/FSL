import os

import nilearn.image as nilimg
import nibabel

from preprocessing.resample import resampling_MNI

"""
Please change root directory
"""
ROOT_DIR = '/Users/sasayabaku/data'

if __name__ == '__main__':

    subjects = os.listdir(ROOT_DIR)

    for subject in subjects:

        nifti_files = os.listdir(os.path.join(ROOT_DIR, subject))

        raw_file = [file for file in nifti_files if file.startswith('2018') & file.endswith('.nii')][0]

        image = nilimg.load_img(os.path.join(ROOT_DIR, subject, raw_file))

        resampled_img = resampling_MNI(image)

        print(resampled_img.get_data().shape)

        nibabel.save(resampled_img, os.path.join(ROOT_DIR, subject, 'resampled' + str(raw_file)))

