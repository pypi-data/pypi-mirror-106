from setuptools import setup , find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="PersonalExerciseTrainer",
    version="1.0.3",
    description="This package will help users to create its own AI based exercise trainer",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://www.besingular.com/",
    author="BeSingular",
    author_email="hitesh.gupta@besingular.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9"
    ],
    package_dir={'': 'PersonalExerciseTrainer'},
    packages=find_packages(where='PersonalExerciseTrainer'),
    include_package_data=True,
    install_requires=["mediapipe","pyautogui", "opencv-python"],
    python_requires=">=3.7.9"
)