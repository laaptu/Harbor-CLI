from lib.constants.paths import paths
from lib.constants.build_platforms import build_platforms
from lib.utils.decorators import requires_presence_of_dir

'''
Build strategies for different platforms.
Only RN for now.
'''
def build_strategies():
    return {
        build_platforms['REACT_NATIVE']: strategy_react_native
    }

@requires_presence_of_dir(paths['REACT_NATIVE_ANDROID_DIR'])
def strategy_react_native():
    print('Will build react native apk.')
