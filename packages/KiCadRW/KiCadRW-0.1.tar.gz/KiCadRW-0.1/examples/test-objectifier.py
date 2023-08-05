####################################################################################################

from pathlib import Path

from KiCadRW.Objectifier import Objectifier, SchemaNode
from KiCadRW.Logging import setup_logging

####################################################################################################

logger = setup_logging()

####################################################################################################

schema_path = Path(
    'kicad-examples',
    # 'capacitive-half-wave-rectification-pre-zener', 'capacitive-half-wave-rectification-pre-zener.kicad_sch'
    'open-syringe-pump', 'indus', 'opensyringepump_indus.kicad_sch'
)

objectifier = Objectifier(schema_path)

# objectifier.dump()
# objectifier.get_paths()
# objectifier.get_schema()
# print(SchemaNode.NODES)

root = objectifier.root
print(root.xpath('/kicad_sch/version'))
print('---')
for node in root.xpath('/kicad_sch/lib_symbols/symbol'):
    print(f"{node.path_str}: {node.first_child}")
print('---')
for node in root.xpath('/kicad_sch/symbol/lib_id'):
    print(f"{node.path_str}: {node.first_child}")
print('---')
for node in root.xpath('/kicad_sch/symbol'):
    print(f"{node.path_str}: {node.first_child}")
    for _ in node.xpath('property'):
        print(f"    {_.path_str}: {_.childs[:2]}")
