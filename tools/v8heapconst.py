# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "HEAP_NUMBER_TYPE",
  66: "BIGINT_TYPE",
  67: "ODDBALL_TYPE",
  68: "MAP_TYPE",
  69: "CODE_TYPE",
  70: "MUTABLE_HEAP_NUMBER_TYPE",
  71: "FOREIGN_TYPE",
  72: "BYTE_ARRAY_TYPE",
  73: "BYTECODE_ARRAY_TYPE",
  74: "FREE_SPACE_TYPE",
  75: "FIXED_INT8_ARRAY_TYPE",
  76: "FIXED_UINT8_ARRAY_TYPE",
  77: "FIXED_INT16_ARRAY_TYPE",
  78: "FIXED_UINT16_ARRAY_TYPE",
  79: "FIXED_INT32_ARRAY_TYPE",
  80: "FIXED_UINT32_ARRAY_TYPE",
  81: "FIXED_FLOAT32_ARRAY_TYPE",
  82: "FIXED_FLOAT64_ARRAY_TYPE",
  83: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  84: "FIXED_BIGINT64_ARRAY_TYPE",
  85: "FIXED_BIGUINT64_ARRAY_TYPE",
  86: "FIXED_DOUBLE_ARRAY_TYPE",
  87: "FEEDBACK_METADATA_TYPE",
  88: "FILLER_TYPE",
  89: "ACCESS_CHECK_INFO_TYPE",
  90: "ACCESSOR_INFO_TYPE",
  91: "ACCESSOR_PAIR_TYPE",
  92: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  93: "ALLOCATION_MEMENTO_TYPE",
  94: "ASM_WASM_DATA_TYPE",
  95: "ASYNC_GENERATOR_REQUEST_TYPE",
  96: "CLASS_POSITIONS_TYPE",
  97: "DEBUG_INFO_TYPE",
  98: "ENUM_CACHE_TYPE",
  99: "FUNCTION_TEMPLATE_INFO_TYPE",
  100: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  101: "INTERCEPTOR_INFO_TYPE",
  102: "INTERPRETER_DATA_TYPE",
  103: "MODULE_INFO_ENTRY_TYPE",
  104: "MODULE_TYPE",
  105: "OBJECT_TEMPLATE_INFO_TYPE",
  106: "PROMISE_CAPABILITY_TYPE",
  107: "PROMISE_REACTION_TYPE",
  108: "PROTOTYPE_INFO_TYPE",
  109: "SCRIPT_TYPE",
  110: "SOURCE_POSITION_TABLE_WITH_FRAME_CACHE_TYPE",
  111: "STACK_FRAME_INFO_TYPE",
  112: "STACK_TRACE_FRAME_TYPE",
  113: "TUPLE2_TYPE",
  114: "TUPLE3_TYPE",
  115: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  116: "WASM_DEBUG_INFO_TYPE",
  117: "WASM_EXCEPTION_TAG_TYPE",
  118: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  119: "CALLABLE_TASK_TYPE",
  120: "CALLBACK_TASK_TYPE",
  121: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  122: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  123: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  124: "FINALIZATION_GROUP_CLEANUP_JOB_TASK_TYPE",
  125: "ALLOCATION_SITE_TYPE",
  126: "EMBEDDER_DATA_ARRAY_TYPE",
  127: "FIXED_ARRAY_TYPE",
  128: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  129: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  130: "HASH_TABLE_TYPE",
  131: "ORDERED_HASH_MAP_TYPE",
  132: "ORDERED_HASH_SET_TYPE",
  133: "ORDERED_NAME_DICTIONARY_TYPE",
  134: "NAME_DICTIONARY_TYPE",
  135: "GLOBAL_DICTIONARY_TYPE",
  136: "NUMBER_DICTIONARY_TYPE",
  137: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  138: "STRING_TABLE_TYPE",
  139: "EPHEMERON_HASH_TABLE_TYPE",
  140: "SCOPE_INFO_TYPE",
  141: "SCRIPT_CONTEXT_TABLE_TYPE",
  142: "AWAIT_CONTEXT_TYPE",
  143: "BLOCK_CONTEXT_TYPE",
  144: "CATCH_CONTEXT_TYPE",
  145: "DEBUG_EVALUATE_CONTEXT_TYPE",
  146: "EVAL_CONTEXT_TYPE",
  147: "FUNCTION_CONTEXT_TYPE",
  148: "MODULE_CONTEXT_TYPE",
  149: "NATIVE_CONTEXT_TYPE",
  150: "SCRIPT_CONTEXT_TYPE",
  151: "WITH_CONTEXT_TYPE",
  152: "WEAK_FIXED_ARRAY_TYPE",
  153: "TRANSITION_ARRAY_TYPE",
  154: "CALL_HANDLER_INFO_TYPE",
  155: "CELL_TYPE",
  156: "CODE_DATA_CONTAINER_TYPE",
  157: "DESCRIPTOR_ARRAY_TYPE",
  158: "FEEDBACK_CELL_TYPE",
  159: "FEEDBACK_VECTOR_TYPE",
  160: "LOAD_HANDLER_TYPE",
  161: "PREPARSE_DATA_TYPE",
  162: "PROPERTY_ARRAY_TYPE",
  163: "PROPERTY_CELL_TYPE",
  164: "SHARED_FUNCTION_INFO_TYPE",
  165: "SMALL_ORDERED_HASH_MAP_TYPE",
  166: "SMALL_ORDERED_HASH_SET_TYPE",
  167: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  168: "STORE_HANDLER_TYPE",
  169: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  170: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  171: "WEAK_ARRAY_LIST_TYPE",
  172: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00149): (74, "FreeSpaceMap"),
  ("read_only_space", 0x00199): (68, "MetaMap"),
  ("read_only_space", 0x00219): (67, "NullMap"),
  ("read_only_space", 0x00281): (157, "DescriptorArrayMap"),
  ("read_only_space", 0x002e1): (152, "WeakFixedArrayMap"),
  ("read_only_space", 0x00331): (88, "OnePointerFillerMap"),
  ("read_only_space", 0x00381): (88, "TwoPointerFillerMap"),
  ("read_only_space", 0x00401): (67, "UninitializedMap"),
  ("read_only_space", 0x00471): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x00511): (67, "UndefinedMap"),
  ("read_only_space", 0x00571): (65, "HeapNumberMap"),
  ("read_only_space", 0x005f1): (67, "TheHoleMap"),
  ("read_only_space", 0x00699): (67, "BooleanMap"),
  ("read_only_space", 0x00771): (72, "ByteArrayMap"),
  ("read_only_space", 0x007c1): (127, "FixedArrayMap"),
  ("read_only_space", 0x00811): (127, "FixedCOWArrayMap"),
  ("read_only_space", 0x00861): (130, "HashTableMap"),
  ("read_only_space", 0x008b1): (64, "SymbolMap"),
  ("read_only_space", 0x00901): (40, "OneByteStringMap"),
  ("read_only_space", 0x00951): (140, "ScopeInfoMap"),
  ("read_only_space", 0x009a1): (164, "SharedFunctionInfoMap"),
  ("read_only_space", 0x009f1): (69, "CodeMap"),
  ("read_only_space", 0x00a41): (147, "FunctionContextMap"),
  ("read_only_space", 0x00a91): (155, "CellMap"),
  ("read_only_space", 0x00ae1): (163, "GlobalPropertyCellMap"),
  ("read_only_space", 0x00b31): (71, "ForeignMap"),
  ("read_only_space", 0x00b81): (153, "TransitionArrayMap"),
  ("read_only_space", 0x00bd1): (159, "FeedbackVectorMap"),
  ("read_only_space", 0x00c71): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x00d11): (67, "ExceptionMap"),
  ("read_only_space", 0x00db1): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x00e59): (67, "OptimizedOutMap"),
  ("read_only_space", 0x00ef9): (67, "StaleRegisterMap"),
  ("read_only_space", 0x00f69): (149, "NativeContextMap"),
  ("read_only_space", 0x00fb9): (148, "ModuleContextMap"),
  ("read_only_space", 0x01009): (146, "EvalContextMap"),
  ("read_only_space", 0x01059): (150, "ScriptContextMap"),
  ("read_only_space", 0x010a9): (142, "AwaitContextMap"),
  ("read_only_space", 0x010f9): (143, "BlockContextMap"),
  ("read_only_space", 0x01149): (144, "CatchContextMap"),
  ("read_only_space", 0x01199): (151, "WithContextMap"),
  ("read_only_space", 0x011e9): (145, "DebugEvaluateContextMap"),
  ("read_only_space", 0x01239): (141, "ScriptContextTableMap"),
  ("read_only_space", 0x01289): (129, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x012d9): (87, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x01329): (127, "ArrayListMap"),
  ("read_only_space", 0x01379): (66, "BigIntMap"),
  ("read_only_space", 0x013c9): (128, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x01419): (73, "BytecodeArrayMap"),
  ("read_only_space", 0x01469): (156, "CodeDataContainerMap"),
  ("read_only_space", 0x014b9): (86, "FixedDoubleArrayMap"),
  ("read_only_space", 0x01509): (135, "GlobalDictionaryMap"),
  ("read_only_space", 0x01559): (158, "ManyClosuresCellMap"),
  ("read_only_space", 0x015a9): (127, "ModuleInfoMap"),
  ("read_only_space", 0x015f9): (70, "MutableHeapNumberMap"),
  ("read_only_space", 0x01649): (134, "NameDictionaryMap"),
  ("read_only_space", 0x01699): (158, "NoClosuresCellMap"),
  ("read_only_space", 0x016e9): (136, "NumberDictionaryMap"),
  ("read_only_space", 0x01739): (158, "OneClosureCellMap"),
  ("read_only_space", 0x01789): (131, "OrderedHashMapMap"),
  ("read_only_space", 0x017d9): (132, "OrderedHashSetMap"),
  ("read_only_space", 0x01829): (133, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x01879): (161, "PreparseDataMap"),
  ("read_only_space", 0x018c9): (162, "PropertyArrayMap"),
  ("read_only_space", 0x01919): (154, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x01969): (154, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x019b9): (154, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x01a09): (137, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x01a59): (127, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x01aa9): (165, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x01af9): (166, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x01b49): (167, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x01b99): (138, "StringTableMap"),
  ("read_only_space", 0x01be9): (169, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x01c39): (170, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x01c89): (171, "WeakArrayListMap"),
  ("read_only_space", 0x01cd9): (139, "EphemeronHashTableMap"),
  ("read_only_space", 0x01d29): (126, "EmbedderDataArrayMap"),
  ("read_only_space", 0x01d79): (172, "WeakCellMap"),
  ("read_only_space", 0x01dc9): (58, "NativeSourceStringMap"),
  ("read_only_space", 0x01e19): (32, "StringMap"),
  ("read_only_space", 0x01e69): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x01eb9): (33, "ConsStringMap"),
  ("read_only_space", 0x01f09): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x01f59): (37, "ThinStringMap"),
  ("read_only_space", 0x01fa9): (35, "SlicedStringMap"),
  ("read_only_space", 0x01ff9): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x02049): (34, "ExternalStringMap"),
  ("read_only_space", 0x02099): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x020e9): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x02139): (0, "InternalizedStringMap"),
  ("read_only_space", 0x02189): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x021d9): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x02229): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x02279): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x022c9): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x02319): (76, "FixedUint8ArrayMap"),
  ("read_only_space", 0x02369): (75, "FixedInt8ArrayMap"),
  ("read_only_space", 0x023b9): (78, "FixedUint16ArrayMap"),
  ("read_only_space", 0x02409): (77, "FixedInt16ArrayMap"),
  ("read_only_space", 0x02459): (80, "FixedUint32ArrayMap"),
  ("read_only_space", 0x024a9): (79, "FixedInt32ArrayMap"),
  ("read_only_space", 0x024f9): (81, "FixedFloat32ArrayMap"),
  ("read_only_space", 0x02549): (82, "FixedFloat64ArrayMap"),
  ("read_only_space", 0x02599): (83, "FixedUint8ClampedArrayMap"),
  ("read_only_space", 0x025e9): (85, "FixedBigUint64ArrayMap"),
  ("read_only_space", 0x02639): (84, "FixedBigInt64ArrayMap"),
  ("read_only_space", 0x02689): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x026f1): (98, "EnumCacheMap"),
  ("read_only_space", 0x02791): (115, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x02ae1): (101, "InterceptorInfoMap"),
  ("read_only_space", 0x05119): (89, "AccessCheckInfoMap"),
  ("read_only_space", 0x05169): (90, "AccessorInfoMap"),
  ("read_only_space", 0x051b9): (91, "AccessorPairMap"),
  ("read_only_space", 0x05209): (92, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x05259): (93, "AllocationMementoMap"),
  ("read_only_space", 0x052a9): (94, "AsmWasmDataMap"),
  ("read_only_space", 0x052f9): (95, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x05349): (96, "ClassPositionsMap"),
  ("read_only_space", 0x05399): (97, "DebugInfoMap"),
  ("read_only_space", 0x053e9): (99, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05439): (100, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x05489): (102, "InterpreterDataMap"),
  ("read_only_space", 0x054d9): (103, "ModuleInfoEntryMap"),
  ("read_only_space", 0x05529): (104, "ModuleMap"),
  ("read_only_space", 0x05579): (105, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x055c9): (106, "PromiseCapabilityMap"),
  ("read_only_space", 0x05619): (107, "PromiseReactionMap"),
  ("read_only_space", 0x05669): (108, "PrototypeInfoMap"),
  ("read_only_space", 0x056b9): (109, "ScriptMap"),
  ("read_only_space", 0x05709): (110, "SourcePositionTableWithFrameCacheMap"),
  ("read_only_space", 0x05759): (111, "StackFrameInfoMap"),
  ("read_only_space", 0x057a9): (112, "StackTraceFrameMap"),
  ("read_only_space", 0x057f9): (113, "Tuple2Map"),
  ("read_only_space", 0x05849): (114, "Tuple3Map"),
  ("read_only_space", 0x05899): (116, "WasmDebugInfoMap"),
  ("read_only_space", 0x058e9): (117, "WasmExceptionTagMap"),
  ("read_only_space", 0x05939): (118, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x05989): (119, "CallableTaskMap"),
  ("read_only_space", 0x059d9): (120, "CallbackTaskMap"),
  ("read_only_space", 0x05a29): (121, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x05a79): (122, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x05ac9): (123, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x05b19): (124, "FinalizationGroupCleanupJobTaskMap"),
  ("read_only_space", 0x05b69): (125, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05bb9): (125, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05c09): (160, "LoadHandler1Map"),
  ("read_only_space", 0x05c59): (160, "LoadHandler2Map"),
  ("read_only_space", 0x05ca9): (160, "LoadHandler3Map"),
  ("read_only_space", 0x05cf9): (168, "StoreHandler0Map"),
  ("read_only_space", 0x05d49): (168, "StoreHandler1Map"),
  ("read_only_space", 0x05d99): (168, "StoreHandler2Map"),
  ("read_only_space", 0x05de9): (168, "StoreHandler3Map"),
  ("map_space", 0x00149): (1057, "ExternalMap"),
  ("map_space", 0x00199): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x001e9): "NullValue",
  ("read_only_space", 0x00269): "EmptyDescriptorArray",
  ("read_only_space", 0x002d1): "EmptyWeakFixedArray",
  ("read_only_space", 0x003d1): "UninitializedValue",
  ("read_only_space", 0x004e1): "UndefinedValue",
  ("read_only_space", 0x00561): "NanValue",
  ("read_only_space", 0x005c1): "TheHoleValue",
  ("read_only_space", 0x00659): "HoleNanValue",
  ("read_only_space", 0x00669): "TrueValue",
  ("read_only_space", 0x00719): "FalseValue",
  ("read_only_space", 0x00761): "empty_string",
  ("read_only_space", 0x00c21): "EmptyScopeInfo",
  ("read_only_space", 0x00c31): "EmptyFixedArray",
  ("read_only_space", 0x00c41): "ArgumentsMarker",
  ("read_only_space", 0x00ce1): "Exception",
  ("read_only_space", 0x00d81): "TerminationException",
  ("read_only_space", 0x00e29): "OptimizedOut",
  ("read_only_space", 0x00ec9): "StaleRegister",
  ("read_only_space", 0x026d9): "EmptyEnumCache",
  ("read_only_space", 0x02741): "EmptyPropertyArray",
  ("read_only_space", 0x02751): "EmptyByteArray",
  ("read_only_space", 0x02761): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x02779): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x027e1): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x027f1): "EmptyFixedUint8Array",
  ("read_only_space", 0x02811): "EmptyFixedInt8Array",
  ("read_only_space", 0x02831): "EmptyFixedUint16Array",
  ("read_only_space", 0x02851): "EmptyFixedInt16Array",
  ("read_only_space", 0x02871): "EmptyFixedUint32Array",
  ("read_only_space", 0x02891): "EmptyFixedInt32Array",
  ("read_only_space", 0x028b1): "EmptyFixedFloat32Array",
  ("read_only_space", 0x028d1): "EmptyFixedFloat64Array",
  ("read_only_space", 0x028f1): "EmptyFixedUint8ClampedArray",
  ("read_only_space", 0x02911): "EmptyFixedBigUint64Array",
  ("read_only_space", 0x02931): "EmptyFixedBigInt64Array",
  ("read_only_space", 0x02951): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x02971): "EmptySlowElementDictionary",
  ("read_only_space", 0x029b9): "EmptyOrderedHashMap",
  ("read_only_space", 0x029e1): "EmptyOrderedHashSet",
  ("read_only_space", 0x02a09): "EmptyFeedbackMetadata",
  ("read_only_space", 0x02a19): "EmptyPropertyCell",
  ("read_only_space", 0x02a41): "EmptyPropertyDictionary",
  ("read_only_space", 0x02a91): "NoOpInterceptorInfo",
  ("read_only_space", 0x02b31): "EmptyWeakArrayList",
  ("read_only_space", 0x02b49): "InfinityValue",
  ("read_only_space", 0x02b59): "MinusZeroValue",
  ("read_only_space", 0x02b69): "MinusInfinityValue",
  ("read_only_space", 0x02b79): "SelfReferenceMarker",
  ("read_only_space", 0x02bd1): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x02be9): "HashSeed",
  ("old_space", 0x00149): "ArgumentsIteratorAccessor",
  ("old_space", 0x001b9): "ArrayLengthAccessor",
  ("old_space", 0x00229): "BoundFunctionLengthAccessor",
  ("old_space", 0x00299): "BoundFunctionNameAccessor",
  ("old_space", 0x00309): "ErrorStackAccessor",
  ("old_space", 0x00379): "FunctionArgumentsAccessor",
  ("old_space", 0x003e9): "FunctionCallerAccessor",
  ("old_space", 0x00459): "FunctionNameAccessor",
  ("old_space", 0x004c9): "FunctionLengthAccessor",
  ("old_space", 0x00539): "FunctionPrototypeAccessor",
  ("old_space", 0x005a9): "StringLengthAccessor",
  ("old_space", 0x00619): "InvalidPrototypeValidityCell",
  ("old_space", 0x00629): "EmptyScript",
  ("old_space", 0x006a9): "ManyClosuresCell",
  ("old_space", 0x006c1): "ArrayConstructorProtector",
  ("old_space", 0x006d1): "NoElementsProtector",
  ("old_space", 0x006f9): "IsConcatSpreadableProtector",
  ("old_space", 0x00709): "ArraySpeciesProtector",
  ("old_space", 0x00731): "TypedArraySpeciesProtector",
  ("old_space", 0x00759): "RegExpSpeciesProtector",
  ("old_space", 0x00781): "PromiseSpeciesProtector",
  ("old_space", 0x007a9): "StringLengthProtector",
  ("old_space", 0x007b9): "ArrayIteratorProtector",
  ("old_space", 0x007e1): "ArrayBufferDetachingProtector",
  ("old_space", 0x00809): "PromiseHookProtector",
  ("old_space", 0x00831): "PromiseResolveProtector",
  ("old_space", 0x00841): "MapIteratorProtector",
  ("old_space", 0x00869): "PromiseThenProtector",
  ("old_space", 0x00891): "SetIteratorProtector",
  ("old_space", 0x008b9): "StringIteratorProtector",
  ("old_space", 0x008e1): "SingleCharacterStringCache",
  ("old_space", 0x010f1): "StringSplitCache",
  ("old_space", 0x01901): "RegExpMultipleCache",
  ("old_space", 0x02111): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
