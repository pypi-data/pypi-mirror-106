# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shellcode']

package_data = \
{'': ['*']}

install_requires = \
['capstone>=4.0.2,<5.0.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['shellcode = shellcode.__main__:app']}

setup_kwargs = {
    'name': 'shellcode',
    'version': '0.2.1',
    'description': 'CLI to turn shellcode back to asm.',
    'long_description': '# shellcode\n![shellcode logo](https://raw.githubusercontent.com/4thel00z/shellcode/master/logo.png)\n\n## Motivation\n\nIn the course of pawning n00bs often the need arises to introspect some (generated) shellcode or check\nit for sanity.\n\nThis tools does exactly that.\n\n## Installation\n\n```\npip install shellcode\n```\n\n## Usage\n\n### With defaults (x86 in 32bit mode)\n\n```\necho "\\x48\\x83\\xEC\\x40\\xB0\\x3B\\x48\\x31\\xD2\\x48\\x31\\xF6\\x52\\x48\\xBB\\x2F\\x2F\\x62\\x69\\x6E\\x2F\\x73\\x68\\x53\\x54\\x5F\\x0F\\x05" | shellcode \n```\n\nOutputs:\n\n```\n0x0:\tdec\teax\n0x1:\tsub\tesp, 0x40\n0x4:\tmov\tal, 0x3b\n0x6:\tdec\teax\n0x7:\txor\tedx, edx\n0x9:\tdec\teax\n0xa:\txor\tesi, esi\n0xc:\tpush\tedx\n0xd:\tdec\teax\n0xe:\tmov\tebx, 0x69622f2f\n0x13:\toutsb\tdx, byte ptr [esi]\n0x14:\tdas\t\n0x15:\tjae\t0x7f\n0x17:\tpush\tebx\n0x18:\tpush\tesp\n0x19:\tpop\tedi\n0x1a:\tsyscall\n```\n\n### Fullblown\n\n```\nUsage: shellcode [OPTIONS] COMMAND [ARGS]...\n\n  Supported archs are (default: CS_ARCH_X86):\n\n          - CS_ARCH_ARM\n\n          - CS_ARCH_ARM64\n\n          - CS_ARCH_MIPS\n\n          - CS_ARCH_X86\n\n          - CS_ARCH_PPC\n\n          - CS_ARCH_SPARC\n\n          - CS_ARCH_SYSZ\n\n          - CS_ARCH_XCORE\n\n          - CS_ARCH_M68K\n\n          - CS_ARCH_TMS320C64X\n\n          - CS_ARCH_M680X\n\n          - CS_ARCH_EVM\n\n          - CS_ARCH_ALL\n\n  Supported modes are (default: CS_MODE_32):\n\n          - CS_MODE_LITTLE_ENDIAN\n\n          - CS_MODE_BIG_ENDIAN\n\n          - CS_MODE_16\n\n          - CS_MODE_32\n\n          - CS_MODE_64\n\n          - CS_MODE_ARM\n\n          - CS_MODE_THUMB\n\n          - CS_MODE_MCLASS\n\n          - CS_MODE_MICRO\n\n          - CS_MODE_MIPS3\n\n          - CS_MODE_MIPS32R6\n\n          - CS_MODE_MIPS2\n\n          - CS_MODE_V8\n\n          - CS_MODE_V9\n\n          - CS_MODE_QPX\n\n          - CS_MODE_M68K_000\n\n          - CS_MODE_M68K_010\n\n          - CS_MODE_M68K_020\n\n          - CS_MODE_M68K_030\n\n          - CS_MODE_M68K_040\n\n          - CS_MODE_M68K_060\n\n          - CS_MODE_MIPS32\n\n          - CS_MODE_MIPS64\n\n          - CS_MODE_M680X_6301\n\n          - CS_MODE_M680X_6309\n\n          - CS_MODE_M680X_6800\n\n          - CS_MODE_M680X_6801\n\n          - CS_MODE_M680X_6805\n\n          - CS_MODE_M680X_6808\n\n          - CS_MODE_M680X_6809\n\n          - CS_MODE_M680X_6811\n\n          - CS_MODE_M680X_CPU12\n\n          - CS_MODE_M680X_HCS08\n\nOptions:\n  --arch TEXT                     [default: CS_ARCH_X86]\n  --mode TEXT                     [default: CS_MODE_32]\n  --color / --no-color            [default: True]\n  --verbose / --no-verbose        [default: False]\n  --b64 / --no-b64                [default: False]\n  --start INTEGER                 [default: 0]\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n\n  --help                          Show this message and exit.\n```\n\n## License\n\nThis project is licensed under the GPL-3 license.\n',
    'author': '4thel00z',
    'author_email': '4thel00z@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/4thel00z/shellcode',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
