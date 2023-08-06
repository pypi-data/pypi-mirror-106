from setuptools import setup, find_packages



setup_args = dict(
    name='HandTrackModules',
    version='0.1.6',
    description='Useful tools to work with Hand Detection with cv2 and mediapipe',
    license='MIT',
    packages=find_packages(),
    author='Joshua Paul',
    author_email='joshblue2005@gmail.com',
    keywords=['cv2','mediapipe', 'Hand Track Module', 'Python 3'],
    url='https://github.com/joshuapaul2005/HandTrackingModule',
)

install_requires = [
    'mediapipe',
    'opencv-python',
    'numpy'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)