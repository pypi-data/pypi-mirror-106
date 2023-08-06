# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mcblueprints',
 'mcblueprints.build',
 'mcblueprints.cli',
 'mcblueprints.lib',
 'mcblueprints.lib.resource',
 'mcblueprints.lib.resource.blueprint',
 'mcblueprints.lib.resource.blueprint.palette_entry',
 'mcblueprints.lib.resource.blueprint.palette_entry.abc',
 'mcblueprints.lib.resource.filter',
 'mcblueprints.lib.resource.filter.rule',
 'mcblueprints.lib.resource.filter.rule.abc',
 'mcblueprints.lib.resource.material']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'nbtlib>=1.12.0,<2.0.0', 'pyckaxe>=0.2.0,<0.3.0']

extras_require = \
{'colors': ['colorama>=0.4.3,<0.5.0', 'colorlog>=4.2.1,<5.0.0'],
 'yaml': ['pyyaml>=5.3.1,<6.0.0']}

setup_kwargs = {
    'name': 'mcblueprints',
    'version': '0.1.0',
    'description': 'Text-based structures for Minecraft.',
    'long_description': '![logo]\n\n# Blueprints\n\n> Text-based structures for Minecraft.\n\n[![package-badge]](https://pypi.python.org/pypi/mcblueprints/)\n[![version-badge]](https://pypi.python.org/pypi/mcblueprints/)\n[![style-badge]](https://github.com/ambv/black)\n\nBlueprints are a text-based structure format for Minecraft optimized for human-readability. A blueprint compiles-down to a single NBT structure file that can be loaded with a structure block.\n\nHere are some reasons you may want to use blueprints:\n\n- They can be diff\'d and _properly_ included in version control, unlike their NBT equivalent.\n- They are far smaller and less repetitive than their SNBT equivalent, which is often used for version control.\n- They can be expressed purely through text, without having to think about the underlying structure format (and without having to open the game).\n- They can be updated to (and optimized for) a newer version of the game, just by re-running the CLI with the `--data_version` argument.\n- They have the potential to take up significantly less space than their NBT equivalent, for codebases that take advantage of composition.\n\nKeep in mind that - although they are optimized for human-readbility - blueprints aren\'t nearly as "hands-on" as editing structures in-game. There are pros and cons to either approach, and the case for blueprints should be weighed carefully based on project size and complexity.\n\n## Usage\n\nBlueprints are created and maintained in the same way as vanilla resources, but under a made-up `blueprints` folder.\n\nSee the [examples](#examples) and the [demo pack](https://github.com/Arcensoth/blueprints/tree/main/tests/datapacks/demo-datapack/data) for reference.\n\nThe most basic invocation of the CLI looks like this:\n\n```bash\npython -m blueprints build --input path/to/input/pack --output path/to/output/pack --data_version 2715\n```\n\n- `--input` is the path to the input pack. This is where your blueprints reside.\n- `--output` is the path to the output pack. This is where the generated structures files will be placed. This can be the same as the input pack, but beware of overwriting existing files.\n- `--data_version` is required and `2715` should be replaced with the [version of the game](https://minecraft.fandom.com/wiki/Data_version#List_of_data_versions) you are targeting.\n\nRun `python -m mcblueprints build --help` for a complete list of options.\n\n## Examples\n\nAll examples use YAML instead of JSON, but the YAML used is 1:1 convertible to/from JSON.\n\nSee the full [demo pack](https://github.com/Arcensoth/blueprints/tree/main/tests/datapacks/demo-datapack/data) for a complete set of examples.\n\nThis first example uses basic blocks to create a simple structure.\n\n![image](https://user-images.githubusercontent.com/1885643/118862799-20da5f80-b8ac-11eb-9ad3-23b50f251e32.png)\n\n**`fleecy_box:base`**\n\n[`data/fleecy_box/blueprints/base.yaml`](https://github.com/Arcensoth/blueprints/blob/main/tests/datapacks/demo-datapack/data/fleecy_box/blueprints/base.yaml)\n\n```yaml\n# Restrict the size of the structure. An error will be raised if anything extends\n# outside of these bounds. This goes by (x, y, z) or (length x height x width).\nsize: [5, 5, 5]\n\n# The palette maps characters to different types of palette entries that describe how to\n# populate the structure. These can be blocks as well as other blueprints.\npalette:\n  # Strings are assumed to be basic blocks.\n  _: minecraft:air\n  g: minecraft:glass\n  c: minecraft:glowstone\n  b: minecraft:bricks\n  # To define block states, use the block type entry.\n  P:\n    type: block\n    name: minecraft:quartz_pillar\n    state:\n      axis: y\n  X:\n    type: block\n    name: minecraft:tnt\n    state:\n      unstable: true\n  # To define NBT data, use the block type entry.\n  T:\n    type: block\n    name: minecraft:trapped_chest\n    data:\n      Items:\n        - id: minecraft:diamond\n          Count: 1b\n          Slot: 13b\n\n# The layout is a 2-D list of strings (a 3-D list of characters) that says how to build\n# the structure, piece by piece, using the palette. Note that the first section of the\n# layout corresponds to the top-most layer of blocks in the structure.\nlayout:\n  - - ggggg\n    - ggggg\n    - ggggg\n    - ggggg\n    - ggggg\n\n  - - ggggg\n    - g___g\n    - g___g\n    - g___g\n    - ggggg\n\n  - - ggggg\n    - g___g\n    - g_T_g\n    - g___g\n    - ggggg\n\n  - - cgggc\n    - g___g\n    - g_P_g\n    - g___g\n    - cgggc\n\n  - - bbbbb\n    - bbbbb\n    - bbXbb\n    - bbbbb\n    - bbbbb\n```\n\nThis next example uses composition and a filter to include a modified version of another blueprint.\n\n![image](https://user-images.githubusercontent.com/1885643/118862891-3c456a80-b8ac-11eb-94a7-763484c12069.png)\n\n**`fleecy_box:copper`**\n\n[`data/fleecy_box/blueprints/copper.yaml`](https://github.com/Arcensoth/blueprints/blob/main/tests/datapacks/demo-datapack/data/fleecy_box/blueprints/copper.yaml)\n\n```yaml\n# Make sure to account for any included structures in the final structure.\nsize: [5, 5, 5]\n\npalette:\n  # Blueprints are composable. They can be included within one another, and the final\n  # structure will be a flattened version with a minimal palette.\n  B:\n    type: blueprint\n    blueprint: fleecy_box:base\n    # A filter changes the way blocks are included from other blueprints.\n    filter: fleecy_box:copperize\n\nlayout:\n  - - B\n```\n\nNote the use of a filter: these can be used to change the way blocks are included from other blueprints.\n\n**`fleecy_box:copperize`**\n\n[`data/fleecy_box/filters/copperize.yaml`](https://github.com/Arcensoth/blueprints/blob/main/tests/datapacks/demo-datapack/data/fleecy_box/filters/copperize.yaml)\n\n```yaml\n# Replace one block with another block.\n- type: replace_blocks\n  blocks:\n    - minecraft:bricks\n  replacement: minecraft:cut_copper\n\n- type: replace_blocks\n  blocks:\n    - minecraft:glowstone\n    - minecraft:quartz_pillar\n  replacement: minecraft:copper_block\n\n# Keep only the listed blocks, discarding the rest.\n- type: keep_blocks\n  blocks:\n    - minecraft:copper_block\n    - minecraft:cut_copper\n```\n\n[logo]: ./logo.png\n[package-badge]: https://img.shields.io/pypi/v/blueprints.svg\n[version-badge]: https://img.shields.io/pypi/pyversions/blueprints.svg\n[style-badge]: https://img.shields.io/badge/code%20style-black-000000.svg\n',
    'author': 'Arcensoth',
    'author_email': 'arcensoth@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Arcensoth/blueprints',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
