from setuptools import setup, find_packages
import versioneer

extras = {
  'atari': ['gym[atari]'],
  'box2d': ['gym[box2d]', 'opencv-python'],
  'pybullet': ['pybullet'],
  'procgen': ['procgen'],
  'cloud': ['boto3', 'awscli'],
  'pettingzoo': ['supersuit'],
}

extras['all'] = [item for group in extras.values() for item in group]

setup(
    name='cleanrl',
    install_requires=[
        'gym',
        'torch',
        'tensorboard',
        'wandb',
        'stable_baselines3',
        'seaborn',],
    extras_require=extras,
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
