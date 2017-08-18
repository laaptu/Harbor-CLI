from lib.constants.build_platforms import build_platforms

def build_strategies():
    return {
        build_platforms['REACT_NATIVE']: strategy_react_native
    }

def strategy_react_native():
    print('Will build react native apk.')
