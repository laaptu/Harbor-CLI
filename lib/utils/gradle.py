from subprocess import Popen, PIPE

def build_react_native():
    with Popen( ['./android/gradlew', '-p', 'android', 'assembleRelease'], bufsize=-1, stdout=PIPE, stderr=PIPE,
               universal_newlines=True) as process:
        for line in process.stdout:
             print(line)

        for line in process.stderr:
            print(line)

    return process.returncode
