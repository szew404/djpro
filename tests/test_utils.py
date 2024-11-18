# This file is part of the django-environ.
#
# Copyright (c) 2021-2022, Serghei Iakovlev <egrep@protonmail.ch>
# Copyright (c) 2013-2021, Daniele Faraglia <daniele.faraglia@gmail.com>
#
# For the full copyright and license information, please view
# the LICENSE.txt file that was distributed with this source code.

import pytest

from djpro import utils
from unittest.mock import patch


@pytest.fixture
def temp_path(tmp_path):
    """Fixture for temporary directories"""
    return tmp_path


def test_create_dirs(temp_path):
    """Test for create_dirs"""
    dirs = [temp_path / "dir1", temp_path / "dir2/subdir"]
    utils.create_dirs(dirs)

    for dir_path in dirs:
        assert dir_path.exists()
        assert dir_path.is_dir()


def test_create_files(temp_path):
    """Test for create_files"""
    files = [temp_path / "file1.txt", temp_path / "subdir/file2.txt"]
    utils.create_files(files)

    for file_path in files:
        assert file_path.exists()
        assert file_path.is_file()


def test_write_to_file(temp_path):
    """Test for write_to_file."""
    file_path = temp_path / "file.txt"
    content = "Hello, djpro!"

    utils.write_to_file(file_path, content)

    assert file_path.exists()
    with open(file_path, "r") as f:
        assert f.read() == content


def test_configure_requirements():
    """Test for configure_requirements."""

    # API and Unfold case
    result = utils.configure_requirements(api=True, unfold=True)
    assert (
        result
        == utils.files_content.requirements_api
        + utils.files_content.requirements_unfold
    )

    # API case
    result = utils.configure_requirements(api=True, unfold=False)
    assert result == utils.files_content.requirements_api

    # Unfold case
    result = utils.configure_requirements(api=False, unfold=True)
    assert result == utils.files_content.requirements_unfold

    # No option case
    result = utils.configure_requirements(api=False, unfold=False)
    assert result == ""


@patch("..djpro.utils.logging.log_with_color")
def test_configure_settings_base(mock_log):
    """Test for configure_settings_base."""

    # API and Unfold case
    result = utils.configure_settings_base(api=True, unfold=True)
    assert result == utils.files_content.settings_api_unfold

    # API case
    result = utils.configure_settings_base(api=True, unfold=False)
    mock_log.assert_not_called()
    assert result == utils.files_content.settings_api

    # Unfold case
    result = utils.configure_settings_base(api=False, unfold=True)
    assert result == utils.files_content.settings_unfold

    # No option case
    result = utils.configure_settings_base(api=False, unfold=False)
    mock_log.assert_not_called()
    assert result == utils.files_content.settings_base_content
