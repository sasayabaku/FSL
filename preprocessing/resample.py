from nilearn import image as nilimg
from nilearn.datasets import load_mni152_template
from nilearn.image import resample_to_img


def resampling_MNI(image):

    """
    Resample Nifti image to MNI standard brain
    :param image: Nifti image to be resampled
    :return: Resampled Nifti image
    """

    template = load_mni152_template()
    resampled_img = resample_to_img(image, template)

    return resampled_img