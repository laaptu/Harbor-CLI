import os
import xml.etree.ElementTree as ET
from subprocess import Popen, PIPE

from lib.constants.paths import paths

def build_react_native():
    '''
    Builds a React Native project using gradle cli.
    Availability of the command is assumed.
    '''
    with Popen( ['./android/gradlew', '-p', 'android', 'assembleRelease'], bufsize=-1, stdout=PIPE, stderr=PIPE,
               universal_newlines=True) as process:
        for line in process.stderr:
            print(line)

    apk_signed_path = os.getcwd() + '/android/app/build/outputs/apk/app-release.apk'
    apk_unsigned_path = os.getcwd() + '/android/app/build/outputs/apk/app-release-unsigned.apk'

    build_type = None
    apk_path = None
    if os.path.isfile(apk_unsigned_path):
        build_type = 'unsigned'
        apk_path = apk_unsigned_path
    elif os.path.isfile(apk_signed_path):
        build_type = 'signed'
        apk_path = apk_signed_path

    return {
        'returncode': process.returncode,
        'isSigned': True if build_type == 'signed' else False,
        'apk_path': apk_path
    }


def get_react_native_project_name():
    ''' Returns the project name by extracting it from the AndroidManifest.xml file.'''
    android_manifest_tree = ET.parse(paths['REACT_NATIVE_MANIFEST'])
    manifest_element = android_manifest_tree.getroot()

    return manifest_element.attrib['package']
