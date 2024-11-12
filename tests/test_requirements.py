import os.path
from pathlib import Path


def test_requirements_ensure_static_versions():
    """
    Ensure that the requirements file contains static versions.
    """
    #
    root_dir = str(Path(__file__).parent.parent)
    examples_dir = os.path.join(root_dir, "examples")
    for subdir in os.listdir(examples_dir):
        subdir_path = os.path.join(examples_dir, subdir)
        requirements_txt_path = os.path.join(subdir_path, "requirements.txt")
        assert os.path.exists(requirements_txt_path), f"Expected to find a requirements.txt file in {subdir_path}."
        with open(requirements_txt_path) as f:
            requirements = f.read().split("\n")
        for requirement in requirements:
            if requirement.strip() and not requirement.startswith("#") and not requirement.startswith("git+"):
                # TODO: this is a naive checks you may have commit based versions, etc using git+https://
                assert "==" in requirement, f"Expected to find a static version in {requirement} in {requirements_txt_path}."
            if requirement.strip() and not requirement.startswith("#") and requirement.startswith("git+"):
                assert "@" in requirement, f"Expected to find a commit based version in {requirement} in {requirements_txt_path}."