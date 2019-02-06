import setuptools

setuptools.setup(
    name='spln_utils',
    version='0.0.5',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'normText=spln_utils.paragraphs:normTextScript',
            'marcarNomes=spln_utils.names:marcarNomesScript',
            'findPairs=spln_utils.names:findPairsScript'
        ],
    },
)
