import argparse
import pkg_resources
import sys
import os
from honu import HonuTest


def main():
    parser = argparse.ArgumentParser(
        description='Test Honu code for a given level.')

    parser.add_argument('level', metavar='level', type=str,
                        help='The level to run the code on, either a number or a filename')

    parser.add_argument('code', metavar='code', type=str,
                        help='The Honu code python file to run')

    args = parser.parse_args()
    print(args.level)
    if args.level.isdigit():
        # do the thing
        level_json_path = get_numbered_level_path(args.level)
    else:
        level_json_path = args.level

    ht: HonuTest = import_honu_test_from_file(args.code)

    ht.run_test(level_json_path)

def get_numbered_level_path(level_num:str):
    if not pkg_resources.resource_exists('honu.static.levels', f'{level_num}.json'):
        raise Exception(f'Level {level_num} does not exist! Is the honu package up to date?')

    file_name = pkg_resources.resource_filename('honu.static.levels', f'{level_num}.json')
    return file_name

def import_honu_test_from_file(path: str) -> HonuTest:
    import_name = prepare_import(path)

    __import__(import_name)
    module = sys.modules[import_name]

    return find_best_honu_test(module)


def prepare_import(path: str) -> str:
    """Given a filename this will try to calculate the python path, add it
    to the search path and return the actual module name that is expected.
    Taken from the Flask repo
    """
    path = os.path.realpath(path)

    fname, ext = os.path.splitext(path)
    if ext == ".py":
        path = fname

    if os.path.basename(path) == "__init__":
        path = os.path.dirname(path)

    module_name = []

    # move up until outside package structure (no __init__.py)
    while True:
        path, name = os.path.split(path)
        module_name.append(name)

        if not os.path.exists(os.path.join(path, "__init__.py")):
            break

    if sys.path[0] != path:
        sys.path.insert(0, path)

    return ".".join(module_name[::-1])


def find_best_honu_test(module) -> HonuTest:
    """Given a module instance this tries to find the best possible
    application in the module or raises an exception.
    Taken from the Flask repo and modified
    """

    # Search for the most common names first.
    for attr_name in ("h", "ht", "honu"):
        game = getattr(module, attr_name, None)

        if isinstance(game, HonuTest):
            return game

    # Otherwise find the only object that is a Flask instance.
    matches = [v for v in module.__dict__.values() if isinstance(v, HonuTest)]

    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        raise Exception(
            "Detected multiple honu test instances in module"
        )
    raise Exception(
        "Could not find a honu test instance in the file! Did you create a HonuTest() instance?"
    )


if __name__ == '__main__':
    main()
