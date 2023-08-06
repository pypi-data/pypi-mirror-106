# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oracle4grid',
 'oracle4grid.core',
 'oracle4grid.core.actions_utils',
 'oracle4grid.core.agent',
 'oracle4grid.core.graph',
 'oracle4grid.core.replay',
 'oracle4grid.core.reward_computation',
 'oracle4grid.core.utils',
 'oracle4grid.test',
 'oracle4grid.test_resourses.grids.rte_case14_realistic',
 'oracle4grid.test_resourses.grids.rte_case14_realistic_overload']

package_data = \
{'': ['*'],
 'oracle4grid': ['output/Ieee14_Sandbox_test/scenario_0/unitary_actions_l2rpn_2019/*',
                 'output/input_data_test_otherReward/scenario_0/agg_unitary_actions/*',
                 'output/input_data_test_otherReward/scenario_0/agg_unitary_actions/replay_logs/*',
                 'output/input_data_test_otherReward/scenario_0/agg_unitary_actions/replay_logs/apr42.1/*',
                 'output/input_data_test_otherReward/scenario_0/agg_unitary_actions/replay_logs_no_overload/*',
                 'output/input_data_test_otherReward/scenario_0/agg_unitary_actions/replay_logs_no_overload/apr42.1/*',
                 'output/rte_case14_realistic/scenario_0/test_unitary_actions/*',
                 'output/rte_case14_realistic/scenario_0/test_unitary_actions_3/*',
                 'output/rte_case14_realistic/scenario_0/test_unitary_actions_5/*',
                 'output/rte_case14_realistic/scenario_0/unitary_actions_l2rpn_2019/*',
                 'output/rte_case14_realistic/scenario_000/test_unitary_actions/*',
                 'output/scenario_000/ExpertActions_Track1_action_list_score4_reduite/*',
                 'output/scenario_000/agg_unitary_actions/*',
                 'output/scenario_000/agg_unitary_actions/replay_logs/*',
                 'output/scenario_000/agg_unitary_actions/replay_logs/february_40/*',
                 'output/wcci_test/scenario_0/ExpertActions_Track1_action_list_score4_reduite/*',
                 'output/wcci_test/scenario_0/agg_unitary_actions/*',
                 'ressources/*',
                 'ressources/actions/Ieee14_Sandbox_test/*',
                 'ressources/actions/neurips_track1/*',
                 'ressources/actions/rte_case14_realistic/*',
                 'ressources/actions/wcci_test/*',
                 'ressources/debug/rte_case14_realistic/scenario_000/test_unitary_actions/*',
                 'test_resourses/*',
                 'test_resourses/grids/rte_case14_realistic/chronics/000/*',
                 'test_resourses/grids/rte_case14_realistic/chronics/001/*',
                 'test_resourses/grids/rte_case14_realistic/chronics/002/*',
                 'test_resourses/grids/rte_case14_realistic_overload/chronics/000/*',
                 'test_resourses/grids/rte_case14_realistic_overload/chronics/001/*',
                 'test_resourses/grids/rte_case14_realistic_overload/chronics/002/*']}

install_requires = \
['Grid2Op>=1.5.2,<2.0.0',
 'ipykernel>=5.5.4,<6.0.0',
 'ipywidgets>=7.6.3,<8.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'networkx>=2.5.1,<3.0.0',
 'numba>=0.53.1,<0.54.0',
 'numpy==1.19.3',
 'pandas>=1.2.4,<2.0.0',
 'psutil>=5.8.0,<6.0.0',
 'pybind11>=2.5.0,<3.0.0',
 'pytest>=6.2.4,<7.0.0']

entry_points = \
{'console_scripts': ['oracle4grid = main:main']}

setup_kwargs = {
    'name': 'oracle4grid',
    'version': '1.0.2',
    'description': 'Oracle agent that finds the best course of actions aposteriori, within a given perimeter of actions',
    'long_description': None,
    'author': 'Mario Jothy',
    'author_email': 'mariojothy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
