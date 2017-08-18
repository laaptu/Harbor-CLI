from lib.constants.build_platforms import build_platforms

'''
Build strategies for different platforms.
Only RN for now.
'''
build_strategies = {
    build_platforms['REACT_NATIVE']: strategy_react_native
}

def strategy_react_native():
    print('Will build react native apk.')
