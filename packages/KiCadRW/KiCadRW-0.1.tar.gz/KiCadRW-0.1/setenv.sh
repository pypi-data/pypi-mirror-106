export KiCadRW_source_path=${PWD}
export KiCadRW_examples_path=${KiCadRW_source_path}/examples

source /opt/python-virtual-env/py38/bin/activate
append_to_python_path_if_not ${KiCadRW_source_path}
append_to_python_path_if_not ${KiCadRW_source_path}/tools
append_to_python_path_if_not ${KiCadRW_source_path}/KiCadRW
