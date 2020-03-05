from EvaMap.EvaMap import EvaMap
from EvaMap.examples.ontology import TTL_ONTOLOGY
from EvaMap.examples.mapping import YARRRML_MAPPING
from EvaMap.examples.data import JSON_DATA

evamap = EvaMap(TTL_ONTOLOGY, YARRRML_MAPPING, JSON_DATA)
evamap.evaluate_mapping()
print(evamap.get_total_score())
print(evamap.get_complet_result())