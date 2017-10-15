'''
Manage Android/ReactNative related actions through here.
'''
import os
from lib.shell import run

BASE_MANIFEST = '/app/src/main/AndroidManifest.xml'
BASE_APK_PATH = '/app/build/outputs/apk/'

NATIVE_ANDROID_MANIFEST = ''.join([os.getcwd(), BASE_MANIFEST])
REACT_NATIVE_MANIFEST = ''.join([os.getcwd(), '/android', BASE_MANIFEST])

SIGNED_ANDROID_PATH = ''.join([os.getcwd(), BASE_APK_PATH, 'app-release.apk'])
UNSIGNED_ANDROID_PATH = ''.join([os.getcwd(), BASE_APK_PATH, 'app-release-unsigned.apk'])

SIGNED_REACT_NATIVE_PATH = ''.join([os.getcwd(), '/android', BASE_APK_PATH, 'app-release.apk'])
UNSIGNED_REACT_NATIVE_PATH = ''.join([
    os.getcwd(), '/android', BASE_APK_PATH, 'app-release-unsigned.apk'
])

def is_android():
    ''' Returns true for any android project (native/RN) '''
    if is_native_android() or is_react_native():
        return True

    return False

def get_manifest_path():
    '''
    Returns native manifest path for native projects,
    and prefixes the native path by a "/android" for RN projects
    '''
    if os.path.isfile(NATIVE_ANDROID_MANIFEST):
        return NATIVE_ANDROID_MANIFEST
    elif os.path.isfile(REACT_NATIVE_MANIFEST):
        return REACT_NATIVE_MANIFEST
    else:
        raise Exception('Not an android project.')

def is_native_android():
    ''' Returns True if the project in cwd is native android project. '''
    if os.path.isfile(NATIVE_ANDROID_MANIFEST):
        return True

    return False

def is_react_native():
    ''' Returns True if the project in cwd is native android project. '''
    if os.path.isfile(REACT_NATIVE_MANIFEST):
        return True

    return False

def build():
    ''' Builds the android project. '''
    if is_react_native():
        return run('./android/gradlew -p android assembleRelease')
    elif is_native_android():
        return run('./android/gradlew assembleRelease')
    else:
        raise Exception('Not an android project.')

def clean():
    ''' Builds the android project. '''
    if is_react_native():
        return run('./android/gradlew -p android clean')
    elif is_native_android():
        return run('./android/gradlew clean')
    else:
        raise Exception('Not an android project.')

def signed(path):
    ''' If path matches signed path returns True, else returns False '''
    if path == UNSIGNED_REACT_NATIVE_PATH or path == UNSIGNED_ANDROID_PATH:
        return False

    if path == SIGNED_REACT_NATIVE_PATH or path == SIGNED_ANDROID_PATH:
        return True

    raise Exception('Not an android project.')

def apk_path():
    ''' Returns path to apk. '''
    paths = [
        UNSIGNED_REACT_NATIVE_PATH,
        UNSIGNED_ANDROID_PATH,
        SIGNED_ANDROID_PATH,
        SIGNED_REACT_NATIVE_PATH
    ]

    addexistence = lambda path: {'path': path, 'exists': os.path.isfile(path)}
    removenonexisting = lambda path: path['exists'] is True

    pathexists = list(filter(removenonexisting, map(addexistence, paths)))

    # Only take the first entry. (there should be only one)
    return pathexists[0]['path']

def apk_size(path):
    ''' Returns size of apk. '''
    return os.path.getsize(path)

def build_details():
    ''' Returns the build details of the apks currently in output. '''
    path = apk_path()
    size = apk_size(path)
    is_signed = signed(path)

    return {
        'size': size,
        'apk_path': path,
        'is_signed': is_signed
    }
