#

ReleaseID = {
    0: 'Rel-99',
    1: 'Rel-4',
    2: 'Rel-5',
    3: 'Rel-6',
    4: 'Rel-7',
    5: 'Rel-8',
    6: 'Rel-9',
    7: 'Beyond Rel-9',
}

ReleaseIDExt = {
    0: 'Rel-10',
    1: 'Rel-11',
    2: 'Rel-12',
}

TSNumber = {
    'Rel-11': {
        0: '32.005',
        1: '32.015',
        2: '32.205',
        3: '32.215',
        4: '32.225',
        5: '32.235',
        6: '32.250',
        7: '32.251',
        8: '32.252',
        9: '32.260',
        10: '32.270',
        11: '32.271',
        12: '32.272',
        13: '32.273',
        14: '32.275',
        15: '32.274',
    },
    'Rel-12': {
        0: '32.005',
        1: '32.015',
        2: '32.205',
        3: '32.215',
        4: '32.225',
        5: '32.235',
        6: '32.250',
        7: '32.251',
        #8: '32.252',   ###### 8 is discontinued in Release 12
        9: '32.260',
        10: '32.270',
        11: '32.271',
        12: '32.272',
        13: '32.273',
        14: '32.275',
        15: '32.274',
        16: '32277', ## added in Rel-12
    }
}

records_types = {
    0: 'moCallRecord',
    1: 'mtCallRecord',
    2: 'roamingRecord',
	3: 'incGatewayRecord',
	4: 'outGatewayRecord',
	5: 'transitCallRecord',
	6: 'moSMSRecord',
	7: 'mtSMSRecord',
	8: 'moSMSIWRecord',
	9: 'mtSMSGWRecord',
	10: 'ssActionRecord',
	11: 'hlrIntRecord',
	12: 'locUpdateHLRRecord',
	13: 'locUpdateVLRRecord',
	14: 'commonEquipRecord',
	15: 'moTraceRecord',
	16: 'mtTraceRecord',
	17: 'termCAMELRecord',
	18: 'sgsnPDPRecord',
	20: 'sgsnMMRecord',
	21: 'sgsnSMORecord',
	22: 'sgsnSMTRecord',
	23: 'mtLCSRecord',
	24: 'moLCSRecord',
	25: 'niLCSRecord',
	26: 'sgsnMTLCSRecord',
	27: 'sgsnMOLCSRecord',
	28: 'sgsnNILCSRecord',
	30: 'mMO1SRecord',
	31: 'mMO4FRqRecord',
	32: 'mMO4FRsRecord',
	33: 'mMO4DRecord',
	34: 'mMO1DRecord',
	35: 'mMO4RRecord',
	36: 'mMO1RRecord',
	37: 'mMOMDRecord',
	38: 'mMR4FRecord',
	39: 'mMR1NRqRecord',
	40: 'mMR1NRsRecord',
	41: 'mMR1RtRecord',
	42: 'mMR1AFRecord',
	43: 'mMR4DRqRecord',
	44: 'mMR4DRsRecord',
	45: 'mMR1RRRecord',
	46: 'mMR4RRqRecord',
	47: 'mMR4RRsRecord',
	48: 'mMRMDRecord',
	49: 'mMFRecord',
	50: 'mMBx1SRecord',
	51: 'mMBx1VRecord',
	52: 'mMBx1URecord',
	53: 'mMBx1DRecord',
	54: 'mM7SRecord',
	55: 'mM7DRqRecord',
	56: 'mM7DRsRecord',
	57: 'mM7CRecord',
	58: 'mM7RRecord',
	59: 'mM7DRRqRecord',
	60: 'mM7DRRsRecord',
	61: 'mM7RRqRecord',
	62: 'mM7RRsRecord',
	63: 'sCSCFRecord',
	64: 'pCSCFRecord',
	65: 'iCSCFRecord',
	66: 'mRFCRecord',
	67: 'mGCFRecord',
	68: 'bGCFRecord',
	69: 'aSRecord',
	70: 'eCSCFRecord',
	82: 'iBCFRecord',
	89: 'tRFRecord',
	90: 'tFRecord',
	91: 'aTCFRecord',
	71: 'lCSGMORecord',
	72: 'lCSRGMTRecord',
	73: 'lCSHGMTRecord',
	74: 'lCSVGMTRecord',
	75: 'lCSGNIRecord',
	76: 'sgsnMBMSRecord',
	77: 'ggsnMBMSRecord',
	86: 'gwMBMSRecord',
	78: 'sUBBMSCRecord',
	79: 'cONTENTBMSCRecord',
	80: 'pPFRecord',
	81: 'cPFRecord',
	84: 'sGWRecord',
	85: 'pGWRecord',
	92: 'tDFRecord',
	95: 'iPERecord',
	96: 'ePDGRecord',
	83: 'mMTelRecord',
	87: 'mSCsRVCCRecord',
	88: 'mMTRFRecord',
	99: 'iCSRegisterRecord',
	93: 'sCSMORecord',
	94: 'sCSMTRecord',
}

records_defs = {
    'pGWRecord':{
        79: {'name': 'pGWRecord', 'type': 'SET',
             'children': {
                 0: {'name': 'recordType', 'type': 'RecordType',
                     'values': {55: 'PGWRecord'}},
                 3: {'name': 'servedIMSI', 'type': 'IMSI',  'OPTIONAL': 'yes'},
                 4: {'name': 'p-GWAddress', 'type': 'GSNAddress',
                     'children':{0:{'name': 'IPAddress', 'type': 'IPAddress'},}},
                 5: {'name': 'chargingID', 'type': 'ChargingID'},
                 6: {'name': 'servingNodeAddress', 'type': 'SEQUENCE OF GSNAddress',
                     'children':{0:{'name': 'IPAddress', 'type': 'IPAddress'},} },
                 7: {'name': 'accessPointNameNI', 'type': 'AccessPointNameNI',  'OPTIONAL': 'yes'},
                 8: {'name': 'pdpPDNType', 'type': 'PDPType',  'OPTIONAL': 'yes'},
                 9: {'name': 'servedPDPPDNAddress', 'type': 'PDPAddress',  'OPTIONAL': 'yes',
                     'children': {0: {'name': 'PDPAddress', 'type': 'IPAddress',
                                      'children': {0: {'name': 'IPAddress', 'type': 'IPAddress'}},}},},
                 11: {'name': 'dynamicAddressFlag', 'type': 'DynamicAddressFlag',  'OPTIONAL': 'yes',},
                 12: {'name': 'listOfTrafficVolumes', 'type': 'SEQUENCE OF ChangeOfCharCondition',  'OPTIONAL': 'yes'},
                 13: {'name': 'recordOpeningTime', 'type': 'TimeStamp'},
                 14: {'name': 'duration', 'type': 'CallDuration'},
                 15: {'name': 'causeForRecClosing', 'type': 'CauseForRecClosing'},
                 16: {'name': 'diagnostics', 'type': 'Diagnostics', 'OPTIONAL': 'yes',
                      'children': {0:{'name': 'gsm0408Cause', 'type' : 'INTEGER',},
                                   1:{'name': 'gsm0902MapErrorValue', 'type' : 'INTEGER',},
                                   2:{'name': 'itu-tQ767Cause', 'type' : 'INTEGER',},
                                   3:{'name': 'networkSpecificCause', 'type' : 'ManagementExtension',},
                                   4:{'name': 'manufacturerSpecificCause', 'type' : 'ManagementExtension',
                                      'children': {
                                          1: {'name': 'Unknown1', 'type' : 'INTEGER',},
                                          2: {'name': 'Unknown2', 'type' : 'INTEGER',
                                              'children': {16: {'name': 'Unknown2_16', 'type' : 'INTEGER',
                                                                'children': {
                                                                    2: {'name': 'Unknown2_16_2', 'type' : 'INTEGER',},
                                                                    1: {'name': 'Unknown2_16_1', 'type' : 'INTEGER',}
                                                                }
                                                                }
                                                           }
                                              },
                                          6: {'name': 'Unknown6', 'type' : 'INTEGER',},
                                      },
                                      },
                                   5:{'name': 'positionMethodFailureCause', 'type': 'PositionMethodFailure-Diagnostic'},
                                   6:{'name': 'unauthorizedLCSClientCause', 'type': 'UnauthorizedLCSClient-Diagnostic'},
                                   7:{'name': 'diameterResultCodeAndExperimentalResult', 'type' : 'INTEGER',}}
                      },
                 17: {'name': 'recordSequenceNumber', 'type': 'INTEGER',  'OPTIONAL': 'yes'},
                 18: {'name': 'nodeID', 'type': 'NodeID',  'OPTIONAL': 'yes'},
                 19: {'name': 'recordExtensions', 'type': 'ManagementExtensions',  'OPTIONAL': 'yes'},
                 20: {'name': 'localSequenceNumber', 'type': 'LocalSequenceNumber',  'OPTIONAL': 'yes'},
                 21: {'name': 'apnSelectionMode', 'type': 'APNSelectionMode',  'OPTIONAL': 'yes'},
                 22: {'name': 'servedMSISDN', 'type': 'MSISDN', 'OPTIONAL': 'yes'},
                 23: {'name': 'chargingCharacteristics', 'type': 'ChargingCharacteristics'},
                 24: {'name': 'chChSelectionMode', 'type': 'ChChSelectionMode',  'OPTIONAL': 'yes'},
                 25: {'name': 'iMSsignalingContext', 'type': 'NULL',  'OPTIONAL': 'yes'},
                 27: {'name': 'servingNodePLMNIdentifier', 'type': 'PLMN-Id',  'OPTIONAL': 'yes'},
                 28: {'name': 'pSFurnishChargingInformation', 'type': 'PSFurnishChargingInformation',  'OPTIONAL': 'yes'},
                 29: {'name': 'servedIMEI', 'type': 'IMEI',  'OPTIONAL': 'yes'},
                 30: {'name': 'rATType', 'type': 'RATType',  'OPTIONAL': 'yes'},
                 31: {'name': 'mSTimeZone', 'type': 'MSTimeZone',  'OPTIONAL': 'yes'},
                 32: {'name': 'userLocationInformation', 'type': 'OCTET STRING',  'OPTIONAL': 'yes'},
                 33: {'name': 'cAMELChargingInformation', 'type': 'OCTET STRING',  'OPTIONAL': 'yes'},
                 34: {'name': 'listOfServiceData', 'type': 'SEQUENCE OF ChangeOfServiceCondition',  'OPTIONAL': 'yes',
                      'children': {16: {'name': 'ChangeOfServiceCondition', 'type': 'SEQUENCE',
                                        'children': {
                                            1 : {'name': 'ratingGroup', 'type': 'RatingGroupId'} ,
                                            2 : {'name': 'chargingRuleBaseName', 'type':'ChargingRuleBaseName', 'OPTIONAL': 'yes'},
                                            3 : {'name': 'resultCode', 'type':'ResultCode', 'OPTIONAL': 'yes'},
                                            4 : {'name': 'localSequenceNumber', 'type':'LocalSequenceNumber', 'OPTIONAL': 'yes'},
                                            5 : {'name': 'timeOfFirstUsage', 'type':'TimeStamp', 'OPTIONAL': 'yes'},
                                            6 : {'name': 'timeOfLastUsage', 'type': 'TimeStamp', 'OPTIONAL': 'yes'},
                                            7 : {'name': 'timeUsage','type': 'CallDuration', 'OPTIONAL': 'yes'},
                                            8 : {'name': 'serviceConditionChange','type': 'ServiceConditionChange'},
                                            9 : {'name': 'qoSInformationNeg','type': 'EPCQoSInformation', 'OPTIONAL': 'yes',
                                                 'children': {
                                                     1: {'name': 'qCI', 'type': 'INTEGER',},
                                                     2: {'name': 'maxRequestedBandwithUL', 'type': 'INTEGER',  'OPTIONAL': 'yes',},
                                                     3: {'name': 'maxRequestedBandwithDL',  'type': 'INTEGER',  'OPTIONAL': 'yes',} ,
                                                     4: {'name': 'guaranteedBitrateUL',  'type': 'INTEGER',  'OPTIONAL': 'yes',},
                                                     5: {'name': 'guaranteedBitrateDL',  'type': 'INTEGER',  'OPTIONAL': 'yes',} ,
                                                     6: {'name': 'aRP', 'type': 'INTEGER',  'OPTIONAL': 'yes',},
                                                     7: {'name': 'aPNAggregateMaxBitrateUL', 'type': 'INTEGER',  'OPTIONAL': 'yes',} ,
                                                     8: {'name': 'aPNAggregateMaxBitrateDL',  'type': 'INTEGER',  'OPTIONAL': 'yes',} ,
                                                 }},
                                            10: {'name': 'servingNodeAddress','type': 'GSNAddress', 'OPTIONAL': 'yes',
                                                 'children': {0: {'name': 'GSNAddress', 'type': 'IPAddress'}}},
                                            12: {'name': 'datavolumeFBCUplink','type': 'DataVolumeGPRS', 'OPTIONAL': 'yes'},
                                            13: {'name': 'datavolumeFBCDownlink','type': 'DataVolumeGPRS', 'OPTIONAL': 'yes'},
                                            14: {'name': 'timeOfReport','type': 'TimeStamp'},
                                            16: {'name': 'failureHandlingContinue','type': 'FailureHandlingContinue', 'OPTIONAL': 'yes'},
                                            17: {'name': 'serviceIdentifier','type': 'ServiceIdentifier', 'OPTIONAL': 'yes'},
                                            18: {'name': 'pSFurnishChargingInformation','type': 'PSFurnishChargingInformation', 'OPTIONAL': 'yes'},
                                            19: {'name': 'aFRecordInformation','type': 'SEQUENCE OF AFRecordInformation', 'OPTIONAL': 'yes'},
                                            20: {'name': 'userLocationInformation','type': 'OCTET STRING', 'OPTIONAL': 'yes'},
                                            21: {'name': 'eventBasedChargingInformation','type': 'EventBasedChargingInformation', 'OPTIONAL': 'yes'},
                                            22: {'name': 'timeQuotaMechanism','type': 'TimeQuotaMechanism', 'OPTIONAL': 'yes'},
                                            23: {'name': 'serviceSpecificInfo','type': 'SEQUENCE OF ServiceSpecificInfo', 'OPTIONAL': 'yes'},
                                            24: {'name': 'threeGPP2UserLocationInformation','type': 'OCTET STRING', 'OPTIONAL': 'yes'},
                                            25: {'name': 'sponsorIdentity','type': 'OCTET STRING', 'OPTIONAL': 'yes'},
                                            26: {'name': 'applicationServiceProviderIdentity','type': 'OCTET STRING', 'OPTIONAL': 'yes'},
                                            27: {'name': 'aDCRuleBaseName','type': 'ADCRuleBaseName', 'OPTIONAL': 'yes'},
                                            28: {'name': 'presenceReportingAreaStatus','type': 'PresenceReportingAreaStatus', 'OPTIONAL': 'yes'},
                                            29: {'name': 'userCSGInformation', 'type': 'UserCSGInformation', 'OPTIONAL': 'yes'},
                                        },}}
                      },
                 35: {'name': 'servingNodeType', 'type': 'SEQUENCE OF ServingNodeType',
                      'children': {10: {'name': 'servingNodeType', 'type': 'ENUMERATED'}, }},
                 36: {'name': 'servedMNNAI', 'type': 'SubscriptionID',  'OPTIONAL': 'yes'},
                 37: {'name': 'p-GWPLMNIdentifier', 'type': 'PLMN-Id',  'OPTIONAL': 'yes'},
                 38: {'name': 'startTime', 'type': 'TimeStamp',  'OPTIONAL': 'yes'},
                 39: {'name': 'stopTime', 'type': 'TimeStamp',  'OPTIONAL': 'yes'},
                 40: {'name': 'served3gpp2MEID', 'type': 'OCTET STRING',  'OPTIONAL': 'yes'},
                 41: {'name': 'pDNConnectionChargingID', 'type': 'ChargingID',  'OPTIONAL': 'yes'},
                 42: {'name': 'iMSIunauthenticatedFlag', 'type': 'NULL',  'OPTIONAL': 'yes'},
                 43: {'name': 'userCSGInformation', 'type': 'UserCSGInformation',  'OPTIONAL': 'yes'},
                 44: {'name': 'threeGPP2UserLocationInformation', 'type': 'OCTET STRING',  'OPTIONAL': 'yes'},
                 45: {'name': 'servedPDPPDNAddressExt', 'type': 'PDPAddress',  'OPTIONAL': 'yes'},
                 46: {'name': 'lowPriorityIndicator', 'type': 'NULL',  'OPTIONAL': 'yes'},
                 47: {'name': 'dynamicAddressFlagExt', 'type': 'DynamicAddressFlag',  'OPTIONAL': 'yes'},
                 49: {'name': 'servingNodeiPv6Address', 'type': 'SEQUENCE OF GSNAddress',  'OPTIONAL': 'yes'},
                 50: {'name': 'p-GWiPv6AddressUsed', 'type': 'GSNAddress',  'OPTIONAL': 'yes'},
                 51: {'name': 'tWANUserLocationInformation', 'type': 'TWANUserLocationInfo',  'OPTIONAL': 'yes'},
                 52: {'name': 'retransmission', 'type': 'NULL',  'OPTIONAL': 'yes'},
                 53: {'name': 'userLocationInfoTime', 'type': 'TimeStamp',  'OPTIONAL': 'yes'},
                 54: {'name': 'cNOperatorSelectionEnt', 'type': 'CNOperatorSelectionEntity',  'OPTIONAL': 'yes'},
                 55: {'name': 'ePCQoSInformation', 'type': 'EPCQoSInformation',  'OPTIONAL': 'yes'},
                 56: {'name': 'presenceReportingAreaInfo', 'type': 'PresenceReportingAreaInfo',  'OPTIONAL': 'yes'},
                 57: {'name': 'lastUserLocationInformation', 'type': 'OCTET STRING',  'OPTIONAL': 'yes'},
                 58: {'name': 'lastMSTimeZone', 'type': 'MSTimeZone', 'OPTIONAL': 'yes'},
             }
             }
    }
}

ChChSelectionModes = {
 0: 'servingNodeSupplied',
 1: 'subscriptionSpecific',
 2: 'aPNSpecific',
 3: 'homeDefault',
 4: 'roamingDefault',
 5: 'visitingDefault',
 6: 'fixedDefault',
}

APNSelectionModes = {
 0: 'mSorNetworkProvidedSubscriptionVerified',
 1: 'mSProvidedSubscriptionNotVerified',
 2: 'networkProvidedSubscriptionNotVerified',
}

ServiceConditionChanges = {
 0: 'qoSChange (0), -- bearer modification',
 1: 'sGSNChange (1), -- bearer modification: -- apply to Gn-SGSN /SGW Change',
 2: 'sGSNPLMNIDChange (2), -- bearer modification',
 3: 'tariffTimeSwitch (3), -- tariff time change',
 4: 'pDPContextRelease (4), -- bearer release',
 5: 'rATChange (5), -- bearer modification',
 6: 'serviceIdledOut (6), -- IP flow idle out, DCCA QHT expiry',
 7: 'reserved (7), -- old: QCTexpiry is no report event',
 8: 'configurationChange (8), -- configuration change',
 9: 'serviceStop (9), -- IP flow termination.From "Service Stop" in -- Change-Condition AVP',
 10: 'dCCATimeThresholdReached (10), -- DCCA quota reauthorization',
 11: 'dCCAVolumeThresholdReached (11), -- DCCA quota reauthorization',
 12: 'dCCAServiceSpecificUnitThresholdReached (12), -- DCCA quota reauthorization',
 13: 'dCCATimeExhausted (13), -- DCCA quota reauthorization',
 14: 'dCCAVolumeExhausted (14), -- DCCA quota reauthorization',
 15: 'dCCAValidityTimeout (15), -- DCCA quota validity time (QVT expiry)',
 16: 'reserved1 (16), -- reserved due to no use case, -- old: return Requested is covered by (17),(18)',
 17: 'dCCAReauthorisationRequest (17), -- DCCA quota reauthorization request by OCS',
 18: 'dCCAContinueOngoingSession (18), -- DCCA failure handling (CCFH), -- continue IP flow',
 19: 'dCCARetryAndTerminateOngoingSession (19), -- DCCA failure handling (CCFH), -- terminate IP flow after DCCA retry',
 20: 'dCCATerminateOngoingSession (20), -- DCCA failure handling, -- terminate IP flow',
 21: 'cGI-SAIChange (21), -- bearer modification. "CGI-SAI Change"',
 22: 'rAIChange (22), -- bearer modification. "RAI Change"',
 23: 'dCCAServiceSpecificUnitExhausted (23), -- DCCA quota reauthorization',
 24: 'recordClosure (24), -- PGW-CDR closure',
 25: 'timeLimit (25), -- intermediate recording. From "Service Data --Time Limit" Change-Condition AVP value',
 26: 'volumeLimit (26), -- intermediate recording.From "Service Data --Volume Limit" Change-Condition AVP value',
 27: 'serviceSpecificUnitLimit (27), -- intermediate recording',
 28: 'envelopeClosure (28),',
 29: 'eCGIChange (29), -- bearer modification. "ECGI Change"',
 30: 'tAIChange (30), -- bearer modification. "TAI Change"',
 31: 'userLocationChange (31), -- bearer modification. "User Location Change"',
 32: 'userCSGInformationChange (32) -- bearer modification. "User CSG info Change"',
}

servingNodeTypes = {
    0: 'sGSN',
    1: 'pMIPSGW',
    2: 'gTPSGW',
    3: 'ePDG',
    4: 'hSGW',
    5: 'mME',
    6: 'tWAN',
}

ratypes = {
    0: 'Reserved',
    1: 'UTRAN',
    2: 'GERAN',
    3: 'WLAN',
    4: 'GAN',
    5: 'HSPA-Evolution',
    6: 'EUTRAN (WB-E-UTRAN)',
    7: 'Virtual',
    8: 'EUTRAN-NB-IOT',
}

FileClosureTriggerReasons = {
    0: 'Normal closure (Undefined normal closure reason).',
    1: 'File size limit reached (OA&M configured).',
    2: 'File open-time limit reached (OA&M configured).',
    3: 'Maximum number of CDRs in file reached (OA&M configured).',
    4: 'File closed by manual intervention.',
    5: 'CDR release, version or encoding change.',
    128: 'Abnormal file closure (Undefined error closure reason).',
    129: 'File system error.',
    130: 'File system storage exhausted.',
    131: 'File integrity error.',
}

RecordClosingCause = {
    0: 'normalRelease',
    4: 'abnormalRelease',
    5: 'cAMELInitCallRelease',
    16: 'volumeLimit',
    17: 'timeLimit',
    18: 'servingNodeChange',
    19: 'maxChangeCond',
    20: 'managementIntervention',
    21: 'intraSGSNIntersystemChange',
    22: 'rATChange',
    23: 'mSTimeZoneChange',
    24: 'sGSNPLMNIDChange',
    52: 'unauthorizedRequestingNetwork',
    53: 'unauthorizedLCSClient',
    54: 'positionMethodFailure',
    58: 'unknownOrUnreachableLCSClient',
    59: 'listofDownstreamNodeChange',
	}