# -*- coding: utf-8 -*-
import sys

import pytest

import depthai as dai

def test_utf8_path_asset_manager(tmp_path):

    FILE_CONTENTS="Hello World π"

    tmp_sneaky_file_dir = tmp_path / "UTF-8 dir πππ"
    tmp_sneaky_file_dir.mkdir()
    tmp_sneaky_file_path = tmp_sneaky_file_dir / "sneaky π ΔΔΕ‘ΔΕΎΔΔLpΔΕ‘lΔk file.txt"
    tmp_sneaky_file_path.write_bytes(FILE_CONTENTS.encode("utf-8"))

    assetManager = dai.AssetManager()
    asset = assetManager.set('test', tmp_sneaky_file_path)
    assert(bytes(asset.data) == FILE_CONTENTS.encode("utf-8"))
