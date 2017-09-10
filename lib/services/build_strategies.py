import sys

from lib.utils import gradle
from lib.constants.paths import paths
from lib.utils.json_parser import json_parse
from lib.constants.build_platforms import BuildPlatforms
from lib.utils.decorators import requires_presence_of_dir, requires_presence_of_file

'''
Build strategies for different platforms.
Only RN for now.
'''
def build_strategies():
    return {
        BuildPlatforms.REACT_NATIVE: strategy_react_native
    }


@requires_presence_of_file(
    paths['REACT_NATIVE_PACKAGE_JSON'],
    lambda path: 'Cannot find {0}. Please make sure you are in the root of a valid React Native Project.'.format(path)
)
@requires_presence_of_dir(
    paths['REACT_NATIVE_ANDROID_DIR'],
    lambda path: 'Cannot find the Android directory ({0}). Please make sure you are in the root of a valid React Native Project.'.format(path)
)
def strategy_react_native():
  print('Building the project. Please be patient... ')
  build_details = gradle.build_react_native()

  if  build_details['returncode'] == 0:
      print('\nBuild successful. APK is %s.' % ('signed' if build_details['isSigned'] else 'not signed'))

      project_data = json_parse(paths['REACT_NATIVE_PACKAGE_JSON'])

      build_details.update({
          'metainf': {
              'name': project_data['name'],
              'package_name': gradle.get_react_native_project_name()
          }
      })

      return build_details

  elif build_details['returncode'] == -1:
      print('Something went wrong. Please check the error messages and try again.')
      sys.exit(1)

  elif build_details['returncode'] == -13:
      print('Something went wrong. This generally happens when Java is not properly configured.')
      sys.exit(1)
