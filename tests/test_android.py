''' Tests for android.py module. '''
import os
import pytest

from lib.android import (
    is_android,
    get_manifest_path,
    is_native_android,
    is_react_native,
    REACT_NATIVE_MANIFEST,
    NATIVE_ANDROID_MANIFEST,
)

def test_isnativeproject_v0():
    ''' Returns True for native android projects. '''
    path = os.getcwd() + '/app/src/main'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(NATIVE_ANDROID_MANIFEST, 'w+'):
        assert is_native_android() is True

    os.remove(path + '/AndroidManifest.xml')
    os.rmdir(path)

def test_isnativeproject_v1():
    ''' Test dir is not a native project - it should return false.'''
    assert is_native_android() is False


def test_manifestpath_v0():
    ''' Should return correct path for native android project. '''
    path = os.getcwd() + '/app/src/main'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(NATIVE_ANDROID_MANIFEST, 'w+'):
        assert get_manifest_path() == NATIVE_ANDROID_MANIFEST

    os.remove(path + '/AndroidManifest.xml')
    os.rmdir(path)

def test_manifestpath_v1():
    ''' Should return correct path for native android project. '''
    path = os.getcwd() + '/android/app/src/main'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(REACT_NATIVE_MANIFEST, 'w+'):
        assert get_manifest_path() == REACT_NATIVE_MANIFEST

    os.remove(path + '/AndroidManifest.xml')
    os.rmdir(path)

def test_manifestpath_v2():
    ''' Should throw exception when not an android/RN project. '''
    with pytest.raises(Exception):
        assert get_manifest_path() == NATIVE_ANDROID_MANIFEST
        assert get_manifest_path() == REACT_NATIVE_MANIFEST

def test_isreactnative_v0():
    ''' Returns True for react native android projects. '''
    path = os.getcwd() + '/android/app/src/main'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(REACT_NATIVE_MANIFEST, 'w+'):
        assert is_react_native() is True
        assert is_native_android() is False

    os.remove(path + '/AndroidManifest.xml')
    os.rmdir(path)

def test_is_android_v0():
    ''' Returns True for react native android projects. '''
    path = os.getcwd() + '/android/app/src/main'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(REACT_NATIVE_MANIFEST, 'w+'):
        assert is_android() is True

    os.remove(path + '/AndroidManifest.xml')
    os.rmdir(path)

def test_is_android_v1():
    ''' Returns True for react native android projects. '''
    path = os.getcwd() + '/app/src/main'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(NATIVE_ANDROID_MANIFEST, 'w+'):
        assert is_android() is True

    os.remove(path + '/AndroidManifest.xml')
    os.rmdir(path)

def test_is_android_v2():
    ''' Returns True for react native android projects. '''
    assert is_android() is False
