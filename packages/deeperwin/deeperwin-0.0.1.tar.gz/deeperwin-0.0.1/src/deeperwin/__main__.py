import argparse
import json
from deeperwin import DefaultConfig
from deeperwin.main import calculate_with_weight_sharing, calculate_without_weight_sharing
from deeperwin.utilities.utils import getCodeVersion

if __name__ == '__main__':
    # tf.config.run_functions_eagerly(True)
    parser = argparse.ArgumentParser()
    parser.add_argument("input", default="config.in", nargs='?',
                        help="Base configuration file to use (e.g. config.in). Must be a JSON-file of a config-dict. Final config is a combination of defaults and parameters set in this file.")
    args = parser.parse_args()

    with open(args.input) as f:
        config_dict = json.load(f)

    config = DefaultConfig.build_from_dict(config_dict)
    config.output.code_version = getCodeVersion()
    if config.parallel_trainer.use:
        if config.restart_dir != "":
            calculate_with_weight_sharing(config, user_config_dict=config_dict)
        else:
            calculate_with_weight_sharing(config, user_config_dict=None)
    else:
        calculate_without_weight_sharing(config, user_config_dict=config_dict)