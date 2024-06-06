import struct
from enum import Enum
from openmwutils import *
from openmwrecords import *

FieldType = Enum('FieldType', ['COMPULSORY', 'OPTIONAL', 'REPEATABLE'])
FieldDataType = Enum('FieldDataType', [
	'undefined', # dont use this one, it's only for debugging
	'bool8',
	'arr_zstring',
	'zstring',
	'string',
	'char',
	'arr_32_char',
	'arr_uint8',
	'uint64',
	'uint32',
	'uint16',
	'uint8',
	'int64',
	'int32',
	'float64',
	'float32',
	'rgb',
	'tes3_header',
	'skil_skill_description',
	'clas_class_data',
	'race_race_data',
	'soun_data',
	'scpt_script_header',
	'regn_weather_chances',
	'regn_sound_chances',
	'body_body_part_data',
	'fact_faction_data',
	'mgef_magic_effect_data',
	'misc_weapon_data',
	'weap_weapon_data',
	'cont_container_object',
	'spel_spell_data',
	'spel_enchantments',
	'crea_creature_data',
	'crea_creature_flags',
	'crea_carried_object',
	'crea_ai_data',
	'crea_cell_travel_destination',
	'crea_ai_activate_package',
	'crea_ai_escort_package',
	'crea_ai_follow_package',
	'crea_ai_travel_package',
	'crea_ai_wander_package',
	'ligh_light_data',
	'ench_enchantment_data',
	'ench_enchantments',
	'npc_npc_data',
	'npc_npc_flags',
	'npc_carried_object',
	'npc_spells',
	'npc_ai_data',
	'npc_cell_travel_destination',
	'npc_ai_activate_package',
	'npc_ai_escort_package',
	'npc_ai_follow_package',
	'npc_ai_travel_package',
	'npc_ai_wander_package',
	'armo_armor_data',
	'uint8_or_uint32',
	'clot_clothing_data',
	'repa_repair_item_data',
	'appa_alchemy_apparatus_data',
	'lock_lock_data',
	'prob_probe_item_data',
	'ingr_ingredient_data',
	'book_book_data',
	'alch_alchemy_data',
	'alch_enchantments',
	'cell_flags',
	'cell_ambient_light',
	'cell_moved_reference_coordinates',
	'uint32_or_float',
	'cell_cell_travel_destination',
	'cell_data_reference_position',
	'land_data_type_flags',
	'land_coordinates',
	'land_vertex_normals',
	'land_height_data',
	'land_world_map_height_data',
	'land_vertex_colors',
	'land_texture_indices',
	'pgrd_path_grid_data',
	'pgrd_path_points',
	'pgrd_connection_list',
	'info_info_data',
])

class FieldDefinition:
	def __init__(self, name, field_type, field_data_type):
		self.name = name
		self.field_type = field_type
		self.field_data_type = field_data_type

class RecordDefinition:
	def __init__(self, name, fields):
		self.name = name
		self.fields = fields

	def convert_field(self, field):
		matched_field_definition = next((x for x in self.fields if x.name == field.name), None)

		if matched_field_definition == None:
			raise Exception(f"This record ({self.name}) doesn't contain a field definition for field type {field.name}")

		if matched_field_definition.field_data_type == FieldDataType.bool8:
			if field.data[0] == 0:
				return 'false'
			elif field.data[0] == 1:
				return 'true'
			else:
				raise Exception('invalid bool8 value: ' + str(field.data[0]))

		if matched_field_definition.field_data_type == FieldDataType.uint64:
			number = struct.unpack('<Q', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.uint32:
			number = struct.unpack('<L', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.uint16:
			number = struct.unpack('<H', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.uint8:
			number = struct.unpack('<B', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"

		if matched_field_definition.field_data_type == FieldDataType.int64:
			number = struct.unpack('<q', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.int32:
			number = struct.unpack('<l', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"

		elif matched_field_definition.field_data_type == FieldDataType.float64:
			number = struct.unpack('d', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.float32:
			number = struct.unpack('f', field.data)[0]
			return f"[{matched_field_definition.name}:{number}]\n"

		elif matched_field_definition.field_data_type == FieldDataType.rgb:
			return f"[{matched_field_definition.name}:{field.data[0]}:{field.data[1]}:{field.data[2]}]\n"

		elif matched_field_definition.field_data_type == FieldDataType.zstring:
			string = sanitize_string(field.data.decode('cp1252'))
			return f"[{matched_field_definition.name}:{string}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.string:
			string = sanitize_string(field.data.decode('cp1252'))
			return f"[{matched_field_definition.name}:{string}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.char:
			return f"[{matched_field_definition.name}:{field.data.decode('cp1252')}]\n"
		elif matched_field_definition.field_data_type == FieldDataType.arr_32_char:
			return f"[{matched_field_definition.name}:{field.data.decode('cp1252')}]\n"

		elif matched_field_definition.field_data_type == FieldDataType.uint8_or_uint32:
			return '[TODO:uint8_or_uint32]\n'
		elif matched_field_definition.field_data_type == FieldDataType.uint32_or_float:
			return '[TODO:uint32_or_float]\n'

		elif matched_field_definition.field_data_type == FieldDataType.tes3_header:
			return '[TODO:tes3_header]\n'

		elif matched_field_definition.field_data_type == FieldDataType.skil_skill_description:
			return '[TODO:skil_skill_description]\n'

		elif matched_field_definition.field_data_type == FieldDataType.clas_class_data:
			return '[TODO:clas_class_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.race_race_data:
			return '[TODO:race_race_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.soun_data:
			return '[TODO:soun_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.scpt_script_header:
			return '[TODO:scpt_script_header]\n'

		elif matched_field_definition.field_data_type == FieldDataType.arr_zstring:
			return '[TODO:arr_zstring]\n'
		elif matched_field_definition.field_data_type == FieldDataType.arr_uint8:
			return '[TODO:arr_uint8]\n'

		elif matched_field_definition.field_data_type == FieldDataType.regn_sound_chances:
			return '[TODO:regn_sound_chances]\n'
		elif matched_field_definition.field_data_type == FieldDataType.regn_weather_chances:
			return '[TODO:regn_weather_chances]\n'

		elif matched_field_definition.field_data_type == FieldDataType.body_body_part_data:
			return '[TODO:body_body_part_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.fact_faction_data:
			return '[TODO:fact_faction_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.mgef_magic_effect_data:
			return '[TODO:mgef_magic_effect_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.misc_weapon_data:
			return '[TODO:misc_weapon_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.weap_weapon_data:
			return '[TODO:weap_weapon_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.cont_container_object:
			return '[TODO:cont_container_object]\n'

		elif matched_field_definition.field_data_type == FieldDataType.spel_spell_data:
			return '[TODO:spel_spell_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.spel_enchantments:
			return '[TODO:spel_enchantments]\n'

		elif matched_field_definition.field_data_type == FieldDataType.crea_creature_data:
			return '[TODO:crea_creature_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_creature_flags:
			return '[TODO:crea_creature_flags]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_carried_object:
			return '[TODO:crea_carried_object]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_ai_data:
			return '[TODO:crea_ai_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_cell_travel_destination:
			return '[TODO:crea_cell_travel_destination]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_ai_activate_package:
			return '[TODO:crea_ai_activate_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_ai_escort_package:
			return '[TODO:crea_ai_escort_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_ai_follow_package:
			return '[TODO:crea_ai_follow_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_ai_travel_package:
			return '[TODO:crea_ai_travel_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.crea_ai_wander_package:
			return '[TODO:crea_ai_wander_package]\n'

		elif matched_field_definition.field_data_type == FieldDataType.ligh_light_data:
			return '[TODO:ligh_light_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.ench_enchantment_data:
			return '[TODO:ench_enchantment_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.ench_enchantments:
			return '[TODO:ench_enchantments]\n'

		elif matched_field_definition.field_data_type == FieldDataType.npc_npc_data:
			return '[TODO:npc_npc_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_npc_flags:
			return '[TODO:npc_npc_flags]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_carried_object:
			return '[TODO:npc_carried_object]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_spells:
			return '[TODO:npc_spells]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_ai_data:
			return '[TODO:npc_ai_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_cell_travel_destination:
			return '[TODO:npc_cell_travel_destination]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_ai_activate_package:
			return '[TODO:npc_ai_activate_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_ai_escort_package:
			return '[TODO:npc_ai_escort_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_ai_follow_package:
			return '[TODO:npc_ai_follow_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_ai_travel_package:
			return '[TODO:npc_ai_travel_package]\n'
		elif matched_field_definition.field_data_type == FieldDataType.npc_ai_wander_package:
			return '[TODO:npc_ai_wander_package]\n'

		elif matched_field_definition.field_data_type == FieldDataType.armo_armor_data:
			return '[TODO:armo_armor_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.clot_clothing_data:
			return '[TODO:clot_clothing_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.repa_repair_item_data:
			return '[TODO:repa_repair_item_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.appa_alchemy_apparatus_data:
			return '[TODO:appa_alchemy_apparatus_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.lock_lock_data:
			return '[TODO:lock_lock_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.prob_probe_item_data:
			return '[TODO:prob_probe_item_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.ingr_ingredient_data:
			return '[TODO:ingr_ingredient_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.book_book_data:
			return '[TODO:book_book_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.alch_alchemy_data:
			return '[TODO:alch_alchemy_data]\n'

		elif matched_field_definition.field_data_type == FieldDataType.alch_enchantments:
			return '[TODO:alch_enchantments]\n'

		elif matched_field_definition.field_data_type == FieldDataType.cell_flags:
			return '[TODO:cell_flags]\n'
		elif matched_field_definition.field_data_type == FieldDataType.cell_ambient_light:
			return '[TODO:cell_ambient_light]\n'
		elif matched_field_definition.field_data_type == FieldDataType.cell_moved_reference_coordinates:
			return '[TODO:cell_moved_reference_coordinates]\n'
		elif matched_field_definition.field_data_type == FieldDataType.cell_cell_travel_destination:
			return '[TODO:cell_cell_travel_destination]\n'
		elif matched_field_definition.field_data_type == FieldDataType.cell_data_reference_position:
			return '[TODO:cell_data_reference_position]\n'

		elif matched_field_definition.field_data_type == FieldDataType.land_data_type_flags:
			return '[TODO:land_data_type_flags]\n'
		elif matched_field_definition.field_data_type == FieldDataType.land_coordinates:
			return '[TODO:land_coordinates]\n'
		elif matched_field_definition.field_data_type == FieldDataType.land_vertex_normals:
			return '[TODO:land_vertex_normals]\n'
		elif matched_field_definition.field_data_type == FieldDataType.land_height_data:
			return '[TODO:land_height_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.land_world_map_height_data:
			return '[TODO:land_world_map_height_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.land_vertex_colors:
			return '[TODO:land_vertex_colors]\n'
		elif matched_field_definition.field_data_type == FieldDataType.land_texture_indices:
			return '[TODO:land_texture_indices]\n'

		elif matched_field_definition.field_data_type == FieldDataType.pgrd_path_grid_data:
			return '[TODO:pgrd_path_grid_data]\n'
		elif matched_field_definition.field_data_type == FieldDataType.pgrd_path_points:
			return '[TODO:pgrd_path_points]\n'
		elif matched_field_definition.field_data_type == FieldDataType.pgrd_connection_list:
			return '[TODO:pgrd_connection_list]\n'

		elif matched_field_definition.field_data_type == FieldDataType.info_info_data:
			return '[TODO:info_info_data]\n'

		else:
			raise Exception(f"Field data type {matched_field_definition.field_data_type} isn't defined!")
		return ""
