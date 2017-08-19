import os

from subprocess import Popen, PIPE

def build_react_native():
    with Popen( ['./android/gradlew', '-p', 'android', 'assembleRelease'], bufsize=-1, stdout=PIPE, stderr=PIPE,
               universal_newlines=True) as process:
        for line in process.stderr:
            print(line)

    apk_signed_path = './android/app/build/outputs/apk/app-release.apk'
    apk_unsigned_path = './android/app/build/outputs/apk/app-release_unsigned.apk'

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
