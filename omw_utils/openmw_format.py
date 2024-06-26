from openmw_defs import RecordDefinition, FieldDefinition, FieldDataType, FieldType

ALL_RECORDS = [
	RecordDefinition('TES3', [
		FieldDefinition(
			'HEDR',
			FieldType.REPEATABLE,
			FieldDataType.tes3_header
		),
		FieldDefinition(
			'MAST',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.REPEATABLE,
			FieldDataType.uint64
		),
	]),
	RecordDefinition('GLOB', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.COMPULSORY,
			FieldDataType.char
		),
		FieldDefinition(
			'FLTV',
			FieldType.COMPULSORY,
			FieldDataType.float32
		),
	]),
	RecordDefinition('GMST', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.string,
		),
		FieldDefinition(
			'FLTV',
			FieldType.OPTIONAL,
			FieldDataType.float32,
		),
		FieldDefinition(
			'INTV',
			FieldType.OPTIONAL,
			FieldDataType.int32,
		),
		FieldDefinition(
			'STRV',
			FieldType.OPTIONAL,
			FieldDataType.string,
		),
	]),
	RecordDefinition('SKIL', [
		FieldDefinition(
			'INDX',
			FieldType.COMPULSORY,
			FieldDataType.uint32
		),
		FieldDefinition(
			'SKDT',
			FieldType.COMPULSORY,
			FieldDataType.skil_skill_description
		),
		FieldDefinition(
			'DESC',
			FieldType.OPTIONAL,
			FieldDataType.string
		)
	]),
	RecordDefinition('CLAS', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CLDT',
			FieldType.COMPULSORY,
			FieldDataType.clas_class_data
		),
		FieldDefinition(
			'DESC',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
	]),
	RecordDefinition('RACE', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'RADT',
			FieldType.COMPULSORY,
			FieldDataType.race_race_data
		),
		FieldDefinition(
			'NPCS',
			FieldType.REPEATABLE,
			FieldDataType.arr_32_char
		),
		FieldDefinition(
			'DESC',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
	]),
	RecordDefinition('SOUN', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.soun_data
		),
	]),
	RecordDefinition('SCPT', [
		FieldDefinition(
			'SCHD',
			FieldType.COMPULSORY,
			FieldDataType.scpt_script_header
		),
		FieldDefinition(
			'SCVR',
			FieldType.OPTIONAL,
			FieldDataType.arr_zstring
		),
		FieldDefinition(
			'SCDT',
			FieldType.OPTIONAL,
			FieldDataType.arr_uint8
		),
		FieldDefinition(
			'SCTX',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
	]),
	RecordDefinition('REGN', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'WEAT',
			FieldType.COMPULSORY,
			FieldDataType.regn_weather_chances
		),
		FieldDefinition(
			'BNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CNAM',
			FieldType.COMPULSORY,
			FieldDataType.rgb
		),
		FieldDefinition(
			'SNAM',
			FieldType.REPEATABLE,
			FieldDataType.regn_sound_chances
		),
	]),
	RecordDefinition('BODY', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'BYDT',
			FieldType.COMPULSORY,
			FieldDataType.body_body_part_data
		),
	]),
	RecordDefinition('FACT', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'RNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FADT',
			FieldType.OPTIONAL,
			FieldDataType.fact_faction_data
		),
		FieldDefinition(
			'ANAM',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
		FieldDefinition(
			'INTV',
			FieldType.OPTIONAL,
			FieldDataType.int32
		),
	]),
	RecordDefinition('MGEF', [
		FieldDefinition(
			'INDX',
			FieldType.COMPULSORY,
			FieldDataType.uint32
		),
		FieldDefinition(
			'MEDT',
			FieldType.COMPULSORY,
			FieldDataType.mgef_magic_effect_data
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'PTEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'BSND',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CSND',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'HSND',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ASND',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CVFX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'BVFX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'HVFX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AVFX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DESC',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
	]),
	RecordDefinition('DOOR', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ANAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('BSGN', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'NPCS',
			FieldType.REPEATABLE,
			FieldDataType.arr_32_char
		),
		FieldDefinition(
			'TNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DESC',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('LTEX', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'INTV',
			FieldType.COMPULSORY,
			FieldDataType.uint32
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('STAT', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('MISC', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MCDT',
			FieldType.COMPULSORY,
			FieldDataType.misc_weapon_data
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('WEAP', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.string
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.string
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
		FieldDefinition(
			'WPDT',
			FieldType.COMPULSORY,
			FieldDataType.weap_weapon_data
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
		FieldDefinition(
			'ENAM',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
	]),
	RecordDefinition('CONT', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CNDT',
			FieldType.COMPULSORY,
			FieldDataType.float32
		),
		FieldDefinition(
			'FLAG',
			FieldType.COMPULSORY,
			FieldDataType.uint32
		),
		FieldDefinition(
			'NPCO',
			FieldType.REPEATABLE,
			FieldDataType.cont_container_object
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('SPEL', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SPDT',
			FieldType.COMPULSORY,
			FieldDataType.spel_spell_data
		),
		FieldDefinition(
			'ENAM',
			FieldType.REPEATABLE,
			FieldDataType.spel_enchantments
		),
	]),
	RecordDefinition('CREA', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'NPDT',
			FieldType.COMPULSORY,
			FieldDataType.crea_creature_data
		),
		FieldDefinition(
			'FLAG',
			FieldType.COMPULSORY,
			FieldDataType.crea_creature_flags
		),
		FieldDefinition(
			'XSCL',
			FieldType.OPTIONAL,
			FieldDataType.float32
		),
		FieldDefinition(
			'NPCO',
			FieldType.REPEATABLE,
			FieldDataType.crea_carried_object
		),
		FieldDefinition(
			'NPCS',
			FieldType.REPEATABLE,
			FieldDataType.arr_32_char
		),
		FieldDefinition(
			'AIDT',
			FieldType.COMPULSORY,
			FieldDataType.crea_ai_data
		),
		FieldDefinition(
			'DODT',
			FieldType.REPEATABLE,
			FieldDataType.crea_cell_travel_destination
		),
		FieldDefinition(
			'DNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AI_A',
			FieldType.REPEATABLE,
			FieldDataType.crea_ai_activate_package
		),
		FieldDefinition(
			'AI_E',
			FieldType.REPEATABLE,
			FieldDataType.crea_ai_escort_package
		),
		FieldDefinition(
			'CNDT',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AI_F',
			FieldType.REPEATABLE,
			FieldDataType.crea_ai_follow_package
		),
		FieldDefinition(
			'CNDT',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AI_T',
			FieldType.REPEATABLE,
			FieldDataType.crea_ai_travel_package
		),
		FieldDefinition(
			'AI_W',
			FieldType.REPEATABLE,
			FieldDataType.crea_ai_wander_package
		),
	]),
	RecordDefinition('LIGH', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'LHDT',
			FieldType.COMPULSORY,
			FieldDataType.ligh_light_data
		),
		FieldDefinition(
			'SNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('ENCH', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ENDT',
			FieldType.COMPULSORY,
			FieldDataType.ench_enchantment_data
		),
		FieldDefinition(
			'ENAM',
			FieldType.COMPULSORY,
			FieldDataType.ench_enchantments
		),
	]),
	RecordDefinition('NPC_', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'RNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ANAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'BNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'KNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'NPDT',
			FieldType.COMPULSORY,
			FieldDataType.npc_npc_data
		),
		FieldDefinition(
			'FLAG',
			FieldType.COMPULSORY,
			FieldDataType.npc_npc_flags
		),
		FieldDefinition(
			'NPCO',
			FieldType.REPEATABLE,
			FieldDataType.npc_carried_object
		),
		FieldDefinition(
			'NPCS',
			FieldType.REPEATABLE,
			FieldDataType.npc_spells
		),
		FieldDefinition(
			'AIDT',
			FieldType.OPTIONAL,
			FieldDataType.npc_ai_data
		),
		FieldDefinition(
			'DODT',
			FieldType.REPEATABLE,
			FieldDataType.npc_cell_travel_destination
		),
		FieldDefinition(
			'DNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AI_A',
			FieldType.REPEATABLE,
			FieldDataType.npc_ai_activate_package
		),
		FieldDefinition(
			'AI_E',
			FieldType.REPEATABLE,
			FieldDataType.npc_ai_escort_package
		),
		FieldDefinition(
			'CNDT',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AI_F',
			FieldType.REPEATABLE,
			FieldDataType.npc_ai_follow_package
		),
		FieldDefinition(
			'CNDT',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AI_T',
			FieldType.REPEATABLE,
			FieldDataType.npc_ai_travel_package
		),
		FieldDefinition(
			'AI_W',
			FieldType.REPEATABLE,
			FieldDataType.npc_ai_wander_package
		),
	]),
	RecordDefinition('ARMO', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AODT',
			FieldType.COMPULSORY,
			FieldDataType.armo_armor_data
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'INDX',
			FieldType.REPEATABLE,
			FieldDataType.uint8_or_uint32
		),
		FieldDefinition(
			'BNAM',
			FieldType.REPEATABLE,
			FieldDataType.string
		),
		FieldDefinition(
			'CNAM',
			FieldType.REPEATABLE,
			FieldDataType.string
		),
		FieldDefinition(
			'ENAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('CLOT', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CTDT',
			FieldType.COMPULSORY,
			FieldDataType.clot_clothing_data
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'INDX',
			FieldType.REPEATABLE,
			FieldDataType.uint8_or_uint32
		),
		FieldDefinition(
			'BNAM',
			FieldType.REPEATABLE,
			FieldDataType.string
		),
		FieldDefinition(
			'CNAM',
			FieldType.REPEATABLE,
			FieldDataType.string
		),
		FieldDefinition(
			'ENAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('REPA', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'RIDT',
			FieldType.COMPULSORY,
			FieldDataType.repa_repair_item_data
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('ACTI', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('APPA', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'AADT',
			FieldType.OPTIONAL,
			FieldDataType.appa_alchemy_apparatus_data
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('LOCK', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'LKDT',
			FieldType.COMPULSORY,
			FieldDataType.lock_lock_data
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('PROB', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'PBDT',
			FieldType.COMPULSORY,
			FieldDataType.prob_probe_item_data
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('INGR', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'IRDT',
			FieldType.COMPULSORY,
			FieldDataType.ingr_ingredient_data
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('BOOK', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'BKDT',
			FieldType.COMPULSORY,
			FieldDataType.book_book_data
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ITEX',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'TEXT',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
		FieldDefinition(
			'ENAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('ALCH', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'MODL',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'TEXT',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SCRI',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ALDT',
			FieldType.OPTIONAL,
			FieldDataType.alch_alchemy_data
		),
		FieldDefinition(
			'ENAM',
			FieldType.REPEATABLE,
			FieldDataType.alch_enchantments
		),
	]),
	RecordDefinition('LEVI', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.uint32
		),
		FieldDefinition(
			'NNAM',
			FieldType.COMPULSORY,
			FieldDataType.uint8
		),
		FieldDefinition(
			'INDX',
			FieldType.OPTIONAL,
			FieldDataType.uint32
		),
		FieldDefinition(
			'INAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'INTV',
			FieldType.REPEATABLE,
			FieldDataType.uint16
		),
	]),
	RecordDefinition('LEVC', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.uint32
		),
		FieldDefinition(
			'NNAM',
			FieldType.COMPULSORY,
			FieldDataType.uint8
		),
		FieldDefinition(
			'INDX',
			FieldType.OPTIONAL,
			FieldDataType.uint32
		),
		FieldDefinition(
			'CNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'INTV',
			FieldType.REPEATABLE,
			FieldDataType.uint16
		),
	]),
	RecordDefinition('CELL', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.cell_flags
		),
		FieldDefinition(
			'RGNN',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'NAM5',
			FieldType.OPTIONAL,
			FieldDataType.rgb
		),
		FieldDefinition(
			'WHGT',
			FieldType.OPTIONAL,
			FieldDataType.float32
		),
		FieldDefinition(
			'AMBI',
			FieldType.OPTIONAL,
			FieldDataType.cell_ambient_light
		),
		# TODO: moved reference
		# TODO: form reference
		# TODO: form reference
		# MOVED REFERENCES
		FieldDefinition(
			'MVRF',
			FieldType.REPEATABLE,
			FieldDataType.uint32
		),
		FieldDefinition(
			'CNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CNDT',
			FieldType.REPEATABLE,
			FieldDataType.cell_moved_reference_coordinates
		),
		# FORM REFERENCE
		FieldDefinition(
			'FRMR',
			FieldType.REPEATABLE,
			FieldDataType.uint32
		),
		FieldDefinition(
			'NAME',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'UNAM',
			FieldType.REPEATABLE,
			FieldDataType.uint8
		),
		FieldDefinition(
			'XSCL',
			FieldType.REPEATABLE,
			FieldDataType.float32
		),
		FieldDefinition(
			'ANAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'BNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'INDX',
			FieldType.REPEATABLE,
			FieldDataType.uint32
		),
		FieldDefinition(
			'XSOL',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'XCHG',
			FieldType.REPEATABLE,
			FieldDataType.float32
		),
		FieldDefinition(
			'INTV',
			FieldType.REPEATABLE,
			FieldDataType.uint32_or_float
		),
		FieldDefinition(
			'NAM9',
			FieldType.REPEATABLE,
			FieldDataType.uint32
		),
		FieldDefinition(
			'DODT',
			FieldType.REPEATABLE,
			FieldDataType.cell_cell_travel_destination
		),
		FieldDefinition(
			'DNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FLTV',
			FieldType.REPEATABLE,
			FieldDataType.uint32
		),
		FieldDefinition(
			'KNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'TNAM',
			FieldType.REPEATABLE,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ZNAM',
			FieldType.REPEATABLE,
			FieldDataType.uint8
		),
		FieldDefinition(
			'DATA',
			FieldType.OPTIONAL,
			FieldDataType.cell_data_reference_position
		),
		FieldDefinition(
			'NAM0',
			FieldType.OPTIONAL,
			FieldDataType.uint32
		),
	]),
	RecordDefinition('DIAL', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.uint8
		),
	]),
	RecordDefinition('LAND', [
		FieldDefinition(
			'INTV',
			FieldType.COMPULSORY,
			FieldDataType.land_coordinates
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.land_data_type_flags
		),
		FieldDefinition(
			'VNML',
			FieldType.OPTIONAL,
			FieldDataType.land_vertex_normals
		),
		FieldDefinition(
			'VHGT',
			FieldType.OPTIONAL,
			FieldDataType.land_height_data
		),
		FieldDefinition(
			'WNAM',
			FieldType.OPTIONAL,
			FieldDataType.land_world_map_height_data
		),
		FieldDefinition(
			'VCLR',
			FieldType.OPTIONAL,
			FieldDataType.land_vertex_colors
		),
		FieldDefinition(
			'VTEX',
			FieldType.OPTIONAL,
			FieldDataType.land_texture_indices
		),
	]),

	RecordDefinition('PGRD', [
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.pgrd_path_grid_data
		),
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'PGRP',
			FieldType.OPTIONAL,
			FieldDataType.pgrd_path_points
		),
		FieldDefinition(
			'PGRC',
			FieldType.OPTIONAL,
			FieldDataType.pgrd_connection_list
		),
	]),
	RecordDefinition('SNDG', [
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.uint32
		),
		FieldDefinition(
			'CNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
	]),
	RecordDefinition('INFO', [
		FieldDefinition(
			'INAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'PNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'NNAM',
			FieldType.COMPULSORY,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DATA',
			FieldType.OPTIONAL,
			FieldDataType.info_info_data
		),
		FieldDefinition(
			'ONAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'RNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'CNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'FNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'ANAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'DNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'SNAM',
			FieldType.OPTIONAL,
			FieldDataType.zstring
		),
		FieldDefinition(
			'NAME',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
		FieldDefinition(
			'SCVR',
			FieldType.REPEATABLE,
			FieldDataType.string
		),
		FieldDefinition(
			'INTV',
			FieldType.REPEATABLE,
			FieldDataType.uint32
		),
		FieldDefinition(
			'FLTV',
			FieldType.REPEATABLE,
			FieldDataType.float32
		),
		FieldDefinition(
			'BNAM',
			FieldType.OPTIONAL,
			FieldDataType.string
		),
		FieldDefinition(
			'QSTN',
			FieldType.OPTIONAL,
			FieldDataType.bool8
		),
		FieldDefinition(
			'QSTF',
			FieldType.OPTIONAL,
			FieldDataType.bool8
		),
		FieldDefinition(
			'QSTR',
			FieldType.OPTIONAL,
			FieldDataType.bool8
		),
	]),
	RecordDefinition('SSCR', [
		FieldDefinition(
			'DATA',
			FieldType.COMPULSORY,
			FieldDataType.string
		),
		FieldDefinition(
			'NAME',
			FieldType.COMPULSORY,
			FieldDataType.string
		),
	]),
]
