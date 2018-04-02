###########################################################
# This file is generated using extract.py using pycparser
###########################################################
# revision:
#	wireless-drivers-next-for-davem-2018-03-29-781-ga07a0eb
###########################################################
CMD_UNSPEC = 0
CMD_GET_WIPHY = 1
CMD_SET_WIPHY = 2
CMD_NEW_WIPHY = 3
CMD_DEL_WIPHY = 4
CMD_GET_INTERFACE = 5
CMD_SET_INTERFACE = 6
CMD_NEW_INTERFACE = 7
CMD_DEL_INTERFACE = 8
CMD_GET_KEY = 9
CMD_SET_KEY = 10
CMD_NEW_KEY = 11
CMD_DEL_KEY = 12
CMD_GET_BEACON = 13
CMD_SET_BEACON = 14
CMD_START_AP = 15
CMD_NEW_BEACON = CMD_START_AP
CMD_STOP_AP = 16
CMD_DEL_BEACON = CMD_STOP_AP
CMD_GET_STATION = 17
CMD_SET_STATION = 18
CMD_NEW_STATION = 19
CMD_DEL_STATION = 20
CMD_GET_MPATH = 21
CMD_SET_MPATH = 22
CMD_NEW_MPATH = 23
CMD_DEL_MPATH = 24
CMD_SET_BSS = 25
CMD_SET_REG = 26
CMD_REQ_SET_REG = 27
CMD_GET_MESH_CONFIG = 28
CMD_SET_MESH_CONFIG = 29
CMD_SET_MGMT_EXTRA_IE = 30
CMD_GET_REG = 31
CMD_GET_SCAN = 32
CMD_TRIGGER_SCAN = 33
CMD_NEW_SCAN_RESULTS = 34
CMD_SCAN_ABORTED = 35
CMD_REG_CHANGE = 36
CMD_AUTHENTICATE = 37
CMD_ASSOCIATE = 38
CMD_DEAUTHENTICATE = 39
CMD_DISASSOCIATE = 40
CMD_MICHAEL_MIC_FAILURE = 41
CMD_REG_BEACON_HINT = 42
CMD_JOIN_IBSS = 43
CMD_LEAVE_IBSS = 44
CMD_TESTMODE = 45
CMD_CONNECT = 46
CMD_ROAM = 47
CMD_DISCONNECT = 48
CMD_SET_WIPHY_NETNS = 49
CMD_GET_SURVEY = 50
CMD_NEW_SURVEY_RESULTS = 51
CMD_SET_PMKSA = 52
CMD_DEL_PMKSA = 53
CMD_FLUSH_PMKSA = 54
CMD_REMAIN_ON_CHANNEL = 55
CMD_CANCEL_REMAIN_ON_CHANNEL = 56
CMD_SET_TX_BITRATE_MASK = 57
CMD_REGISTER_FRAME = 58
CMD_REGISTER_ACTION = CMD_REGISTER_FRAME
CMD_FRAME = 59
CMD_ACTION = CMD_FRAME
CMD_FRAME_TX_STATUS = 60
CMD_ACTION_TX_STATUS = CMD_FRAME_TX_STATUS
CMD_SET_POWER_SAVE = 61
CMD_GET_POWER_SAVE = 62
CMD_SET_CQM = 63
CMD_NOTIFY_CQM = 64
CMD_SET_CHANNEL = 65
CMD_SET_WDS_PEER = 66
CMD_FRAME_WAIT_CANCEL = 67
CMD_JOIN_MESH = 68
CMD_LEAVE_MESH = 69
CMD_UNPROT_DEAUTHENTICATE = 70
CMD_UNPROT_DISASSOCIATE = 71
CMD_NEW_PEER_CANDIDATE = 72
CMD_GET_WOWLAN = 73
CMD_SET_WOWLAN = 74
CMD_START_SCHED_SCAN = 75
CMD_STOP_SCHED_SCAN = 76
CMD_SCHED_SCAN_RESULTS = 77
CMD_SCHED_SCAN_STOPPED = 78
CMD_SET_REKEY_OFFLOAD = 79
CMD_PMKSA_CANDIDATE = 80
CMD_TDLS_OPER = 81
CMD_TDLS_MGMT = 82
CMD_UNEXPECTED_FRAME = 83
CMD_PROBE_CLIENT = 84
CMD_REGISTER_BEACONS = 85
CMD_UNEXPECTED_4ADDR_FRAME = 86
CMD_SET_NOACK_MAP = 87
CMD_CH_SWITCH_NOTIFY = 88
CMD_START_P2P_DEVICE = 89
CMD_STOP_P2P_DEVICE = 90
CMD_CONN_FAILED = 91
CMD_SET_MCAST_RATE = 92
CMD_SET_MAC_ACL = 93
CMD_RADAR_DETECT = 94
CMD_GET_PROTOCOL_FEATURES = 95
CMD_UPDATE_FT_IES = 96
CMD_FT_EVENT = 97
CMD_CRIT_PROTOCOL_START = 98
CMD_CRIT_PROTOCOL_STOP = 99
CMD_GET_COALESCE = 100
CMD_SET_COALESCE = 101
CMD_CHANNEL_SWITCH = 102
CMD_VENDOR = 103
CMD_SET_QOS_MAP = 104
CMD_ADD_TX_TS = 105
CMD_DEL_TX_TS = 106
CMD_GET_MPP = 107
CMD_JOIN_OCB = 108
CMD_LEAVE_OCB = 109
CMD_CH_SWITCH_STARTED_NOTIFY = 110
CMD_TDLS_CHANNEL_SWITCH = 111
CMD_TDLS_CANCEL_CHANNEL_SWITCH = 112
CMD_WIPHY_REG_CHANGE = 113
CMD_ABORT_SCAN = 114
CMD_START_NAN = 115
CMD_STOP_NAN = 116
CMD_ADD_NAN_FUNCTION = 117
CMD_DEL_NAN_FUNCTION = 118
CMD_CHANGE_NAN_CONFIG = 119
CMD_NAN_MATCH = 120
CMD_SET_MULTICAST_TO_UNICAST = 121
CMD_UPDATE_CONNECT_PARAMS = 122
CMD_SET_PMK = 123
CMD_DEL_PMK = 124
CMD_PORT_AUTHORIZED = 125
CMD_RELOAD_REGDB = 126
CMD_EXTERNAL_AUTH = 127
CMD_STA_OPMODE_CHANGED = 128
CMD_CONTROL_PORT_FRAME = 129
CMD_AFTER_LAST = 130
CMD_MAX = CMD_AFTER_LAST - 1
ATTR_UNSPEC = 0
ATTR_WIPHY = 1
ATTR_WIPHY_NAME = 2
ATTR_IFINDEX = 3
ATTR_IFNAME = 4
ATTR_IFTYPE = 5
ATTR_MAC = 6
ATTR_KEY_DATA = 7
ATTR_KEY_IDX = 8
ATTR_KEY_CIPHER = 9
ATTR_KEY_SEQ = 10
ATTR_KEY_DEFAULT = 11
ATTR_BEACON_INTERVAL = 12
ATTR_DTIM_PERIOD = 13
ATTR_BEACON_HEAD = 14
ATTR_BEACON_TAIL = 15
ATTR_STA_AID = 16
ATTR_STA_FLAGS = 17
ATTR_STA_LISTEN_INTERVAL = 18
ATTR_STA_SUPPORTED_RATES = 19
ATTR_STA_VLAN = 20
ATTR_STA_INFO = 21
ATTR_WIPHY_BANDS = 22
ATTR_MNTR_FLAGS = 23
ATTR_MESH_ID = 24
ATTR_STA_PLINK_ACTION = 25
ATTR_MPATH_NEXT_HOP = 26
ATTR_MPATH_INFO = 27
ATTR_BSS_CTS_PROT = 28
ATTR_BSS_SHORT_PREAMBLE = 29
ATTR_BSS_SHORT_SLOT_TIME = 30
ATTR_HT_CAPABILITY = 31
ATTR_SUPPORTED_IFTYPES = 32
ATTR_REG_ALPHA2 = 33
ATTR_REG_RULES = 34
ATTR_MESH_CONFIG = 35
ATTR_BSS_BASIC_RATES = 36
ATTR_WIPHY_TXQ_PARAMS = 37
ATTR_WIPHY_FREQ = 38
ATTR_WIPHY_CHANNEL_TYPE = 39
ATTR_KEY_DEFAULT_MGMT = 40
ATTR_MGMT_SUBTYPE = 41
ATTR_IE = 42
ATTR_MAX_NUM_SCAN_SSIDS = 43
ATTR_SCAN_FREQUENCIES = 44
ATTR_SCAN_SSIDS = 45
ATTR_GENERATION = 46
ATTR_BSS = 47
ATTR_REG_INITIATOR = 48
ATTR_REG_TYPE = 49
ATTR_SUPPORTED_COMMANDS = 50
ATTR_FRAME = 51
ATTR_SSID = 52
ATTR_AUTH_TYPE = 53
ATTR_REASON_CODE = 54
ATTR_KEY_TYPE = 55
ATTR_MAX_SCAN_IE_LEN = 56
ATTR_CIPHER_SUITES = 57
ATTR_FREQ_BEFORE = 58
ATTR_FREQ_AFTER = 59
ATTR_FREQ_FIXED = 60
ATTR_WIPHY_RETRY_SHORT = 61
ATTR_WIPHY_RETRY_LONG = 62
ATTR_WIPHY_FRAG_THRESHOLD = 63
ATTR_WIPHY_RTS_THRESHOLD = 64
ATTR_TIMED_OUT = 65
ATTR_USE_MFP = 66
ATTR_STA_FLAGS2 = 67
ATTR_CONTROL_PORT = 68
ATTR_TESTDATA = 69
ATTR_PRIVACY = 70
ATTR_DISCONNECTED_BY_AP = 71
ATTR_STATUS_CODE = 72
ATTR_CIPHER_SUITES_PAIRWISE = 73
ATTR_CIPHER_SUITE_GROUP = 74
ATTR_WPA_VERSIONS = 75
ATTR_AKM_SUITES = 76
ATTR_REQ_IE = 77
ATTR_RESP_IE = 78
ATTR_PREV_BSSID = 79
ATTR_KEY = 80
ATTR_KEYS = 81
ATTR_PID = 82
ATTR_4ADDR = 83
ATTR_SURVEY_INFO = 84
ATTR_PMKID = 85
ATTR_MAX_NUM_PMKIDS = 86
ATTR_DURATION = 87
ATTR_COOKIE = 88
ATTR_WIPHY_COVERAGE_CLASS = 89
ATTR_TX_RATES = 90
ATTR_FRAME_MATCH = 91
ATTR_ACK = 92
ATTR_PS_STATE = 93
ATTR_CQM = 94
ATTR_LOCAL_STATE_CHANGE = 95
ATTR_AP_ISOLATE = 96
ATTR_WIPHY_TX_POWER_SETTING = 97
ATTR_WIPHY_TX_POWER_LEVEL = 98
ATTR_TX_FRAME_TYPES = 99
ATTR_RX_FRAME_TYPES = 100
ATTR_FRAME_TYPE = 101
ATTR_CONTROL_PORT_ETHERTYPE = 102
ATTR_CONTROL_PORT_NO_ENCRYPT = 103
ATTR_SUPPORT_IBSS_RSN = 104
ATTR_WIPHY_ANTENNA_TX = 105
ATTR_WIPHY_ANTENNA_RX = 106
ATTR_MCAST_RATE = 107
ATTR_OFFCHANNEL_TX_OK = 108
ATTR_BSS_HT_OPMODE = 109
ATTR_KEY_DEFAULT_TYPES = 110
ATTR_MAX_REMAIN_ON_CHANNEL_DURATION = 111
ATTR_MESH_SETUP = 112
ATTR_WIPHY_ANTENNA_AVAIL_TX = 113
ATTR_WIPHY_ANTENNA_AVAIL_RX = 114
ATTR_SUPPORT_MESH_AUTH = 115
ATTR_STA_PLINK_STATE = 116
ATTR_WOWLAN_TRIGGERS = 117
ATTR_WOWLAN_TRIGGERS_SUPPORTED = 118
ATTR_SCHED_SCAN_INTERVAL = 119
ATTR_INTERFACE_COMBINATIONS = 120
ATTR_SOFTWARE_IFTYPES = 121
ATTR_REKEY_DATA = 122
ATTR_MAX_NUM_SCHED_SCAN_SSIDS = 123
ATTR_MAX_SCHED_SCAN_IE_LEN = 124
ATTR_SCAN_SUPP_RATES = 125
ATTR_HIDDEN_SSID = 126
ATTR_IE_PROBE_RESP = 127
ATTR_IE_ASSOC_RESP = 128
ATTR_STA_WME = 129
ATTR_SUPPORT_AP_UAPSD = 130
ATTR_ROAM_SUPPORT = 131
ATTR_SCHED_SCAN_MATCH = 132
ATTR_MAX_MATCH_SETS = 133
ATTR_PMKSA_CANDIDATE = 134
ATTR_TX_NO_CCK_RATE = 135
ATTR_TDLS_ACTION = 136
ATTR_TDLS_DIALOG_TOKEN = 137
ATTR_TDLS_OPERATION = 138
ATTR_TDLS_SUPPORT = 139
ATTR_TDLS_EXTERNAL_SETUP = 140
ATTR_DEVICE_AP_SME = 141
ATTR_DONT_WAIT_FOR_ACK = 142
ATTR_FEATURE_FLAGS = 143
ATTR_PROBE_RESP_OFFLOAD = 144
ATTR_PROBE_RESP = 145
ATTR_DFS_REGION = 146
ATTR_DISABLE_HT = 147
ATTR_HT_CAPABILITY_MASK = 148
ATTR_NOACK_MAP = 149
ATTR_INACTIVITY_TIMEOUT = 150
ATTR_RX_SIGNAL_DBM = 151
ATTR_BG_SCAN_PERIOD = 152
ATTR_WDEV = 153
ATTR_USER_REG_HINT_TYPE = 154
ATTR_CONN_FAILED_REASON = 155
ATTR_AUTH_DATA = 156
ATTR_VHT_CAPABILITY = 157
ATTR_SCAN_FLAGS = 158
ATTR_CHANNEL_WIDTH = 159
ATTR_CENTER_FREQ1 = 160
ATTR_CENTER_FREQ2 = 161
ATTR_P2P_CTWINDOW = 162
ATTR_P2P_OPPPS = 163
ATTR_LOCAL_MESH_POWER_MODE = 164
ATTR_ACL_POLICY = 165
ATTR_MAC_ADDRS = 166
ATTR_MAC_ACL_MAX = 167
ATTR_RADAR_EVENT = 168
ATTR_EXT_CAPA = 169
ATTR_EXT_CAPA_MASK = 170
ATTR_STA_CAPABILITY = 171
ATTR_STA_EXT_CAPABILITY = 172
ATTR_PROTOCOL_FEATURES = 173
ATTR_SPLIT_WIPHY_DUMP = 174
ATTR_DISABLE_VHT = 175
ATTR_VHT_CAPABILITY_MASK = 176
ATTR_MDID = 177
ATTR_IE_RIC = 178
ATTR_CRIT_PROT_ID = 179
ATTR_MAX_CRIT_PROT_DURATION = 180
ATTR_PEER_AID = 181
ATTR_COALESCE_RULE = 182
ATTR_CH_SWITCH_COUNT = 183
ATTR_CH_SWITCH_BLOCK_TX = 184
ATTR_CSA_IES = 185
ATTR_CSA_C_OFF_BEACON = 186
ATTR_CSA_C_OFF_PRESP = 187
ATTR_RXMGMT_FLAGS = 188
ATTR_STA_SUPPORTED_CHANNELS = 189
ATTR_STA_SUPPORTED_OPER_CLASSES = 190
ATTR_HANDLE_DFS = 191
ATTR_SUPPORT_5_MHZ = 192
ATTR_SUPPORT_10_MHZ = 193
ATTR_OPMODE_NOTIF = 194
ATTR_VENDOR_ID = 195
ATTR_VENDOR_SUBCMD = 196
ATTR_VENDOR_DATA = 197
ATTR_VENDOR_EVENTS = 198
ATTR_QOS_MAP = 199
ATTR_MAC_HINT = 200
ATTR_WIPHY_FREQ_HINT = 201
ATTR_MAX_AP_ASSOC_STA = 202
ATTR_TDLS_PEER_CAPABILITY = 203
ATTR_SOCKET_OWNER = 204
ATTR_CSA_C_OFFSETS_TX = 205
ATTR_MAX_CSA_COUNTERS = 206
ATTR_TDLS_INITIATOR = 207
ATTR_USE_RRM = 208
ATTR_WIPHY_DYN_ACK = 209
ATTR_TSID = 210
ATTR_USER_PRIO = 211
ATTR_ADMITTED_TIME = 212
ATTR_SMPS_MODE = 213
ATTR_OPER_CLASS = 214
ATTR_MAC_MASK = 215
ATTR_WIPHY_SELF_MANAGED_REG = 216
ATTR_EXT_FEATURES = 217
ATTR_SURVEY_RADIO_STATS = 218
ATTR_NETNS_FD = 219
ATTR_SCHED_SCAN_DELAY = 220
ATTR_REG_INDOOR = 221
ATTR_MAX_NUM_SCHED_SCAN_PLANS = 222
ATTR_MAX_SCAN_PLAN_INTERVAL = 223
ATTR_MAX_SCAN_PLAN_ITERATIONS = 224
ATTR_SCHED_SCAN_PLANS = 225
ATTR_PBSS = 226
ATTR_BSS_SELECT = 227
ATTR_STA_SUPPORT_P2P_PS = 228
ATTR_PAD = 229
ATTR_IFTYPE_EXT_CAPA = 230
ATTR_MU_MIMO_GROUP_DATA = 231
ATTR_MU_MIMO_FOLLOW_MAC_ADDR = 232
ATTR_SCAN_START_TIME_TSF = 233
ATTR_SCAN_START_TIME_TSF_BSSID = 234
ATTR_MEASUREMENT_DURATION = 235
ATTR_MEASUREMENT_DURATION_MANDATORY = 236
ATTR_MESH_PEER_AID = 237
ATTR_NAN_MASTER_PREF = 238
ATTR_BANDS = 239
ATTR_NAN_FUNC = 240
ATTR_NAN_MATCH = 241
ATTR_FILS_KEK = 242
ATTR_FILS_NONCES = 243
ATTR_MULTICAST_TO_UNICAST_ENABLED = 244
ATTR_BSSID = 245
ATTR_SCHED_SCAN_RELATIVE_RSSI = 246
ATTR_SCHED_SCAN_RSSI_ADJUST = 247
ATTR_TIMEOUT_REASON = 248
ATTR_FILS_ERP_USERNAME = 249
ATTR_FILS_ERP_REALM = 250
ATTR_FILS_ERP_NEXT_SEQ_NUM = 251
ATTR_FILS_ERP_RRK = 252
ATTR_FILS_CACHE_ID = 253
ATTR_PMK = 254
ATTR_SCHED_SCAN_MULTI = 255
ATTR_SCHED_SCAN_MAX_REQS = 256
ATTR_WANT_1X_4WAY_HS = 257
ATTR_PMKR0_NAME = 258
ATTR_PORT_AUTHORIZED = 259
ATTR_EXTERNAL_AUTH_ACTION = 260
ATTR_EXTERNAL_AUTH_SUPPORT = 261
ATTR_NSS = 262
ATTR_ACK_SIGNAL = 263
ATTR_CONTROL_PORT_OVER_NL80211 = 264
ATTR_AFTER_LAST = 265
NUM_NL80211_ATTR = ATTR_AFTER_LAST
ATTR_MAX = ATTR_AFTER_LAST - 1
IFTYPE_UNSPECIFIED = 0
IFTYPE_ADHOC = 1
IFTYPE_STATION = 2
IFTYPE_AP = 3
IFTYPE_AP_VLAN = 4
IFTYPE_WDS = 5
IFTYPE_MONITOR = 6
IFTYPE_MESH_POINT = 7
IFTYPE_P2P_CLIENT = 8
IFTYPE_P2P_GO = 9
IFTYPE_P2P_DEVICE = 10
IFTYPE_OCB = 11
IFTYPE_NAN = 12
NUM_NL80211_IFTYPES = 13
IFTYPE_MAX = NUM_NL80211_IFTYPES - 1
STA_FLAG_INVALID = 0
STA_FLAG_AUTHORIZED = 1
STA_FLAG_SHORT_PREAMBLE = 2
STA_FLAG_WME = 3
STA_FLAG_MFP = 4
STA_FLAG_AUTHENTICATED = 5
STA_FLAG_TDLS_PEER = 6
STA_FLAG_ASSOCIATED = 7
STA_FLAG_AFTER_LAST = 8
STA_FLAG_MAX = STA_FLAG_AFTER_LAST - 1
P2P_PS_UNSUPPORTED = 0
P2P_PS_SUPPORTED = 0
NUM_NL80211_P2P_PS_STATUS = 1
RATE_INFO_INVALID = 0
RATE_INFO_BITRATE = 1
RATE_INFO_MCS = 2
RATE_INFO_40_MHZ_WIDTH = 3
RATE_INFO_SHORT_GI = 4
RATE_INFO_BITRATE32 = 5
RATE_INFO_VHT_MCS = 6
RATE_INFO_VHT_NSS = 7
RATE_INFO_80_MHZ_WIDTH = 8
RATE_INFO_80P80_MHZ_WIDTH = 9
RATE_INFO_160_MHZ_WIDTH = 10
RATE_INFO_10_MHZ_WIDTH = 11
RATE_INFO_5_MHZ_WIDTH = 12
RATE_INFO_AFTER_LAST = 13
RATE_INFO_MAX = RATE_INFO_AFTER_LAST - 1
STA_BSS_PARAM_INVALID = 0
STA_BSS_PARAM_CTS_PROT = 1
STA_BSS_PARAM_SHORT_PREAMBLE = 2
STA_BSS_PARAM_SHORT_SLOT_TIME = 3
STA_BSS_PARAM_DTIM_PERIOD = 4
STA_BSS_PARAM_BEACON_INTERVAL = 5
STA_BSS_PARAM_AFTER_LAST = 6
STA_BSS_PARAM_MAX = STA_BSS_PARAM_AFTER_LAST - 1
STA_INFO_INVALID = 0
STA_INFO_INACTIVE_TIME = 1
STA_INFO_RX_BYTES = 2
STA_INFO_TX_BYTES = 3
STA_INFO_LLID = 4
STA_INFO_PLID = 5
STA_INFO_PLINK_STATE = 6
STA_INFO_SIGNAL = 7
STA_INFO_TX_BITRATE = 8
STA_INFO_RX_PACKETS = 9
STA_INFO_TX_PACKETS = 10
STA_INFO_TX_RETRIES = 11
STA_INFO_TX_FAILED = 12
STA_INFO_SIGNAL_AVG = 13
STA_INFO_RX_BITRATE = 14
STA_INFO_BSS_PARAM = 15
STA_INFO_CONNECTED_TIME = 16
STA_INFO_STA_FLAGS = 17
STA_INFO_BEACON_LOSS = 18
STA_INFO_T_OFFSET = 19
STA_INFO_LOCAL_PM = 20
STA_INFO_PEER_PM = 21
STA_INFO_NONPEER_PM = 22
STA_INFO_RX_BYTES64 = 23
STA_INFO_TX_BYTES64 = 24
STA_INFO_CHAIN_SIGNAL = 25
STA_INFO_CHAIN_SIGNAL_AVG = 26
STA_INFO_EXPECTED_THROUGHPUT = 27
STA_INFO_RX_DROP_MISC = 28
STA_INFO_BEACON_RX = 29
STA_INFO_BEACON_SIGNAL_AVG = 30
STA_INFO_TID_STATS = 31
STA_INFO_RX_DURATION = 32
STA_INFO_PAD = 33
STA_INFO_ACK_SIGNAL = 34
STA_INFO_AFTER_LAST = 35
STA_INFO_MAX = STA_INFO_AFTER_LAST - 1
TID_STATS_INVALID = 0
TID_STATS_RX_MSDU = 1
TID_STATS_TX_MSDU = 2
TID_STATS_TX_MSDU_RETRIES = 3
TID_STATS_TX_MSDU_FAILED = 4
TID_STATS_PAD = 5
NUM_NL80211_TID_STATS = 6
TID_STATS_MAX = NUM_NL80211_TID_STATS - 1
MPATH_FLAG_ACTIVE = 1 << 0
MPATH_FLAG_RESOLVING = 1 << 1
MPATH_FLAG_SN_VALID = 1 << 2
MPATH_FLAG_FIXED = 1 << 3
MPATH_FLAG_RESOLVED = 1 << 4
MPATH_INFO_INVALID = 0
MPATH_INFO_FRAME_QLEN = 1
MPATH_INFO_SN = 2
MPATH_INFO_METRIC = 3
MPATH_INFO_EXPTIME = 4
MPATH_INFO_FLAGS = 5
MPATH_INFO_DISCOVERY_TIMEOUT = 6
MPATH_INFO_DISCOVERY_RETRIES = 7
MPATH_INFO_AFTER_LAST = 8
MPATH_INFO_MAX = MPATH_INFO_AFTER_LAST - 1
BAND_ATTR_INVALID = 0
BAND_ATTR_FREQS = 1
BAND_ATTR_RATES = 2
BAND_ATTR_HT_MCS_SET = 3
BAND_ATTR_HT_CAPA = 4
BAND_ATTR_HT_AMPDU_FACTOR = 5
BAND_ATTR_HT_AMPDU_DENSITY = 6
BAND_ATTR_VHT_MCS_SET = 7
BAND_ATTR_VHT_CAPA = 8
BAND_ATTR_AFTER_LAST = 9
BAND_ATTR_MAX = BAND_ATTR_AFTER_LAST - 1
FREQUENCY_ATTR_INVALID = 0
FREQUENCY_ATTR_FREQ = 1
FREQUENCY_ATTR_DISABLED = 2
FREQUENCY_ATTR_NO_IR = 3
FREQUENCY_ATTR_NO_IBSS = 4
FREQUENCY_ATTR_RADAR = 5
FREQUENCY_ATTR_MAX_TX_POWER = 6
FREQUENCY_ATTR_DFS_STATE = 7
FREQUENCY_ATTR_DFS_TIME = 8
FREQUENCY_ATTR_NO_HT40_MINUS = 9
FREQUENCY_ATTR_NO_HT40_PLUS = 10
FREQUENCY_ATTR_NO_80MHZ = 11
FREQUENCY_ATTR_NO_160MHZ = 12
FREQUENCY_ATTR_DFS_CAC_TIME = 13
FREQUENCY_ATTR_INDOOR_ONLY = 14
FREQUENCY_ATTR_IR_CONCURRENT = 15
FREQUENCY_ATTR_NO_20MHZ = 16
FREQUENCY_ATTR_NO_10MHZ = 17
FREQUENCY_ATTR_AFTER_LAST = 18
FREQUENCY_ATTR_MAX = FREQUENCY_ATTR_AFTER_LAST - 1
BITRATE_ATTR_INVALID = 0
BITRATE_ATTR_RATE = 1
BITRATE_ATTR_2GHZ_SHORTPREAMBLE = 2
BITRATE_ATTR_AFTER_LAST = 3
BITRATE_ATTR_MAX = BITRATE_ATTR_AFTER_LAST - 1
REGDOM_SET_BY_CORE = 0
REGDOM_SET_BY_USER = 1
REGDOM_SET_BY_DRIVER = 2
REGDOM_SET_BY_COUNTRY_IE = 3
REGDOM_TYPE_COUNTRY = 0
REGDOM_TYPE_WORLD = 1
REGDOM_TYPE_CUSTOM_WORLD = 2
REGDOM_TYPE_INTERSECTION = 3
REG_RULE_ATTR_INVALID = 0
ATTR_REG_RULE_FLAGS = 1
ATTR_FREQ_RANGE_START = 2
ATTR_FREQ_RANGE_END = 3
ATTR_FREQ_RANGE_MAX_BW = 4
ATTR_POWER_RULE_MAX_ANT_GAIN = 5
ATTR_POWER_RULE_MAX_EIRP = 6
ATTR_DFS_CAC_TIME = 7
REG_RULE_ATTR_AFTER_LAST = 8
REG_RULE_ATTR_MAX = REG_RULE_ATTR_AFTER_LAST - 1
SCHED_SCAN_MATCH_ATTR_INVALID = 0
SCHED_SCAN_MATCH_ATTR_SSID = 1
SCHED_SCAN_MATCH_ATTR_RSSI = 2
SCHED_SCAN_MATCH_ATTR_RELATIVE_RSSI = 3
SCHED_SCAN_MATCH_ATTR_RSSI_ADJUST = 4
SCHED_SCAN_MATCH_ATTR_BSSID = 5
SCHED_SCAN_MATCH_ATTR_AFTER_LAST = 6
SCHED_SCAN_MATCH_ATTR_MAX = SCHED_SCAN_MATCH_ATTR_AFTER_LAST - 1
RRF_NO_OFDM = 1 << 0
RRF_NO_CCK = 1 << 1
RRF_NO_INDOOR = 1 << 2
RRF_NO_OUTDOOR = 1 << 3
RRF_DFS = 1 << 4
RRF_PTP_ONLY = 1 << 5
RRF_PTMP_ONLY = 1 << 6
RRF_NO_IR = 1 << 7
RRF_NO_IBSS = 1 << 8
RRF_AUTO_BW = 1 << 11
RRF_IR_CONCURRENT = 1 << 12
RRF_NO_HT40MINUS = 1 << 13
RRF_NO_HT40PLUS = 1 << 14
RRF_NO_80MHZ = 1 << 15
RRF_NO_160MHZ = 1 << 16
DFS_UNSET = 0
DFS_FCC = 1
DFS_ETSI = 2
DFS_JP = 3
USER_REG_HINT_USER = 0
USER_REG_HINT_CELL_BASE = 1
USER_REG_HINT_INDOOR = 2
SURVEY_INFO_INVALID = 0
SURVEY_INFO_FREQUENCY = 1
SURVEY_INFO_NOISE = 2
SURVEY_INFO_IN_USE = 3
SURVEY_INFO_TIME = 4
SURVEY_INFO_TIME_BUSY = 5
SURVEY_INFO_TIME_EXT_BUSY = 6
SURVEY_INFO_TIME_RX = 7
SURVEY_INFO_TIME_TX = 8
SURVEY_INFO_TIME_SCAN = 9
SURVEY_INFO_PAD = 10
SURVEY_INFO_AFTER_LAST = 11
SURVEY_INFO_MAX = SURVEY_INFO_AFTER_LAST - 1
MNTR_FLAG_INVALID = 0
MNTR_FLAG_FCSFAIL = 1
MNTR_FLAG_PLCPFAIL = 2
MNTR_FLAG_CONTROL = 3
MNTR_FLAG_OTHER_BSS = 4
MNTR_FLAG_COOK_FRAMES = 5
MNTR_FLAG_ACTIVE = 6
MNTR_FLAG_AFTER_LAST = 7
MNTR_FLAG_MAX = MNTR_FLAG_AFTER_LAST - 1
MESH_POWER_UNKNOWN = 0
MESH_POWER_ACTIVE = 1
MESH_POWER_LIGHT_SLEEP = 2
MESH_POWER_DEEP_SLEEP = 3
MESH_POWER_AFTER_LAST = 4
MESH_POWER_MAX = MESH_POWER_AFTER_LAST - 1
MESHCONF_INVALID = 0
MESHCONF_RETRY_TIMEOUT = 1
MESHCONF_CONFIRM_TIMEOUT = 2
MESHCONF_HOLDING_TIMEOUT = 3
MESHCONF_MAX_PEER_LINKS = 4
MESHCONF_MAX_RETRIES = 5
MESHCONF_TTL = 6
MESHCONF_AUTO_OPEN_PLINKS = 7
MESHCONF_HWMP_MAX_PREQ_RETRIES = 8
MESHCONF_PATH_REFRESH_TIME = 9
MESHCONF_MIN_DISCOVERY_TIMEOUT = 10
MESHCONF_HWMP_ACTIVE_PATH_TIMEOUT = 11
MESHCONF_HWMP_PREQ_MIN_INTERVAL = 12
MESHCONF_HWMP_NET_DIAM_TRVS_TIME = 13
MESHCONF_HWMP_ROOTMODE = 14
MESHCONF_ELEMENT_TTL = 15
MESHCONF_HWMP_RANN_INTERVAL = 16
MESHCONF_GATE_ANNOUNCEMENTS = 17
MESHCONF_HWMP_PERR_MIN_INTERVAL = 18
MESHCONF_FORWARDING = 19
MESHCONF_RSSI_THRESHOLD = 20
MESHCONF_SYNC_OFFSET_MAX_NEIGHBOR = 21
MESHCONF_HT_OPMODE = 22
MESHCONF_HWMP_PATH_TO_ROOT_TIMEOUT = 23
MESHCONF_HWMP_ROOT_INTERVAL = 24
MESHCONF_HWMP_CONFIRMATION_INTERVAL = 25
MESHCONF_POWER_MODE = 26
MESHCONF_AWAKE_WINDOW = 27
MESHCONF_PLINK_TIMEOUT = 28
MESHCONF_ATTR_AFTER_LAST = 29
MESHCONF_ATTR_MAX = MESHCONF_ATTR_AFTER_LAST - 1
MESH_SETUP_INVALID = 0
MESH_SETUP_ENABLE_VENDOR_PATH_SEL = 1
MESH_SETUP_ENABLE_VENDOR_METRIC = 2
MESH_SETUP_IE = 3
MESH_SETUP_USERSPACE_AUTH = 4
MESH_SETUP_USERSPACE_AMPE = 5
MESH_SETUP_ENABLE_VENDOR_SYNC = 6
MESH_SETUP_USERSPACE_MPM = 7
MESH_SETUP_AUTH_PROTOCOL = 8
MESH_SETUP_ATTR_AFTER_LAST = 9
MESH_SETUP_ATTR_MAX = MESH_SETUP_ATTR_AFTER_LAST - 1
TXQ_ATTR_INVALID = 0
TXQ_ATTR_AC = 1
TXQ_ATTR_TXOP = 2
TXQ_ATTR_CWMIN = 3
TXQ_ATTR_CWMAX = 4
TXQ_ATTR_AIFS = 5
TXQ_ATTR_AFTER_LAST = 6
TXQ_ATTR_MAX = TXQ_ATTR_AFTER_LAST - 1
AC_VO = 0
AC_VI = 1
AC_BE = 2
AC_BK = 3
NUM_ACS = 4
CHAN_NO_HT = 0
CHAN_HT20 = 1
CHAN_HT40MINUS = 2
CHAN_HT40PLUS = 3
CHAN_WIDTH_20_NOHT = 0
CHAN_WIDTH_20 = 1
CHAN_WIDTH_40 = 2
CHAN_WIDTH_80 = 3
CHAN_WIDTH_80P80 = 4
CHAN_WIDTH_160 = 5
CHAN_WIDTH_5 = 6
CHAN_WIDTH_10 = 7
BSS_CHAN_WIDTH_20 = 0
BSS_CHAN_WIDTH_10 = 1
BSS_CHAN_WIDTH_5 = 2
BSS_INVALID = 0
BSS_BSSID = 1
BSS_FREQUENCY = 2
BSS_TSF = 3
BSS_BEACON_INTERVAL = 4
BSS_CAPABILITY = 5
BSS_INFORMATION_ELEMENTS = 6
BSS_SIGNAL_MBM = 7
BSS_SIGNAL_UNSPEC = 8
BSS_STATUS = 9
BSS_SEEN_MS_AGO = 10
BSS_BEACON_IES = 11
BSS_CHAN_WIDTH = 12
BSS_BEACON_TSF = 13
BSS_PRESP_DATA = 14
BSS_LAST_SEEN_BOOTTIME = 15
BSS_PAD = 16
BSS_PARENT_TSF = 17
BSS_PARENT_BSSID = 18
BSS_CHAIN_SIGNAL = 19
BSS_AFTER_LAST = 20
BSS_MAX = BSS_AFTER_LAST - 1
BSS_STATUS_AUTHENTICATED = 0
BSS_STATUS_ASSOCIATED = 1
BSS_STATUS_IBSS_JOINED = 2
AUTHTYPE_OPEN_SYSTEM = 0
AUTHTYPE_SHARED_KEY = 1
AUTHTYPE_FT = 2
AUTHTYPE_NETWORK_EAP = 3
AUTHTYPE_SAE = 4
AUTHTYPE_FILS_SK = 5
AUTHTYPE_FILS_SK_PFS = 6
AUTHTYPE_FILS_PK = 7
AUTHTYPE_NUM = 8
AUTHTYPE_MAX = AUTHTYPE_NUM - 1
AUTHTYPE_AUTOMATIC = 9
KEYTYPE_GROUP = 0
KEYTYPE_PAIRWISE = 1
KEYTYPE_PEERKEY = 2
NUM_NL80211_KEYTYPES = 3
MFP_NO = 0
MFP_REQUIRED = 1
MFP_OPTIONAL = 2
WPA_VERSION_1 = 1 << 0
WPA_VERSION_2 = 1 << 1
KEY_DEFAULT_TYPE_INVALID = 0
KEY_DEFAULT_TYPE_UNICAST = 1
KEY_DEFAULT_TYPE_MULTICAST = 2
NUM_NL80211_KEY_DEFAULT_TYPES = 3
KEY_INVALID = 0
KEY_DATA = 1
KEY_IDX = 2
KEY_CIPHER = 3
KEY_SEQ = 4
KEY_DEFAULT = 5
KEY_DEFAULT_MGMT = 6
KEY_TYPE = 7
KEY_DEFAULT_TYPES = 8
KEY_AFTER_LAST = 9
KEY_MAX = KEY_AFTER_LAST - 1
TXRATE_INVALID = 0
TXRATE_LEGACY = 1
TXRATE_HT = 2
TXRATE_VHT = 3
TXRATE_GI = 4
TXRATE_AFTER_LAST = 5
TXRATE_MAX = TXRATE_AFTER_LAST - 1
TXRATE_DEFAULT_GI = 0
TXRATE_FORCE_SGI = 1
TXRATE_FORCE_LGI = 2
BAND_2GHZ = 0
BAND_5GHZ = 1
BAND_60GHZ = 2
NUM_NL80211_BANDS = 3
PS_DISABLED = 0
PS_ENABLED = 1
ATTR_CQM_INVALID = 0
ATTR_CQM_RSSI_THOLD = 1
ATTR_CQM_RSSI_HYST = 2
ATTR_CQM_RSSI_THRESHOLD_EVENT = 3
ATTR_CQM_PKT_LOSS_EVENT = 4
ATTR_CQM_TXE_RATE = 5
ATTR_CQM_TXE_PKTS = 6
ATTR_CQM_TXE_INTVL = 7
ATTR_CQM_BEACON_LOSS_EVENT = 8
ATTR_CQM_RSSI_LEVEL = 9
ATTR_CQM_AFTER_LAST = 10
ATTR_CQM_MAX = ATTR_CQM_AFTER_LAST - 1
CQM_RSSI_THRESHOLD_EVENT_LOW = 0
CQM_RSSI_THRESHOLD_EVENT_HIGH = 1
CQM_RSSI_BEACON_LOSS_EVENT = 2
TX_POWER_AUTOMATIC = 0
TX_POWER_LIMITED = 1
TX_POWER_FIXED = 2
PKTPAT_INVALID = 0
PKTPAT_MASK = 1
PKTPAT_PATTERN = 2
PKTPAT_OFFSET = 3
NUM_NL80211_PKTPAT = 4
MAX_NL80211_PKTPAT = NUM_NL80211_PKTPAT - 1
WOWLAN_TRIG_INVALID = 0
WOWLAN_TRIG_ANY = 1
WOWLAN_TRIG_DISCONNECT = 2
WOWLAN_TRIG_MAGIC_PKT = 3
WOWLAN_TRIG_PKT_PATTERN = 4
WOWLAN_TRIG_GTK_REKEY_SUPPORTED = 5
WOWLAN_TRIG_GTK_REKEY_FAILURE = 6
WOWLAN_TRIG_EAP_IDENT_REQUEST = 7
WOWLAN_TRIG_4WAY_HANDSHAKE = 8
WOWLAN_TRIG_RFKILL_RELEASE = 9
WOWLAN_TRIG_WAKEUP_PKT_80211 = 10
WOWLAN_TRIG_WAKEUP_PKT_80211_LEN = 11
WOWLAN_TRIG_WAKEUP_PKT_8023 = 12
WOWLAN_TRIG_WAKEUP_PKT_8023_LEN = 13
WOWLAN_TRIG_TCP_CONNECTION = 14
WOWLAN_TRIG_WAKEUP_TCP_MATCH = 15
WOWLAN_TRIG_WAKEUP_TCP_CONNLOST = 16
WOWLAN_TRIG_WAKEUP_TCP_NOMORETOKENS = 17
WOWLAN_TRIG_NET_DETECT = 18
WOWLAN_TRIG_NET_DETECT_RESULTS = 19
NUM_NL80211_WOWLAN_TRIG = 20
MAX_NL80211_WOWLAN_TRIG = NUM_NL80211_WOWLAN_TRIG - 1
WOWLAN_TCP_INVALID = 0
WOWLAN_TCP_SRC_IPV4 = 1
WOWLAN_TCP_DST_IPV4 = 2
WOWLAN_TCP_DST_MAC = 3
WOWLAN_TCP_SRC_PORT = 4
WOWLAN_TCP_DST_PORT = 5
WOWLAN_TCP_DATA_PAYLOAD = 6
WOWLAN_TCP_DATA_PAYLOAD_SEQ = 7
WOWLAN_TCP_DATA_PAYLOAD_TOKEN = 8
WOWLAN_TCP_DATA_INTERVAL = 9
WOWLAN_TCP_WAKE_PAYLOAD = 10
WOWLAN_TCP_WAKE_MASK = 11
NUM_NL80211_WOWLAN_TCP = 12
MAX_NL80211_WOWLAN_TCP = NUM_NL80211_WOWLAN_TCP - 1
COALESCE_RULE_INVALID = 0
ATTR_COALESCE_RULE_DELAY = 1
ATTR_COALESCE_RULE_CONDITION = 2
ATTR_COALESCE_RULE_PKT_PATTERN = 3
NUM_NL80211_ATTR_COALESCE_RULE = 4
ATTR_COALESCE_RULE_MAX = NUM_NL80211_ATTR_COALESCE_RULE - 1
COALESCE_CONDITION_MATCH = 0
COALESCE_CONDITION_NO_MATCH = 1
IFACE_LIMIT_UNSPEC = 0
IFACE_LIMIT_MAX = 1
IFACE_LIMIT_TYPES = 2
NUM_NL80211_IFACE_LIMIT = 3
MAX_NL80211_IFACE_LIMIT = NUM_NL80211_IFACE_LIMIT - 1
IFACE_COMB_UNSPEC = 0
IFACE_COMB_LIMITS = 1
IFACE_COMB_MAXNUM = 2
IFACE_COMB_STA_AP_BI_MATCH = 3
IFACE_COMB_NUM_CHANNELS = 4
IFACE_COMB_RADAR_DETECT_WIDTHS = 5
IFACE_COMB_RADAR_DETECT_REGIONS = 6
IFACE_COMB_BI_MIN_GCD = 7
NUM_NL80211_IFACE_COMB = 8
MAX_NL80211_IFACE_COMB = NUM_NL80211_IFACE_COMB - 1
PLINK_LISTEN = 0
PLINK_OPN_SNT = 1
PLINK_OPN_RCVD = 2
PLINK_CNF_RCVD = 3
PLINK_ESTAB = 4
PLINK_HOLDING = 5
PLINK_BLOCKED = 6
NUM_NL80211_PLINK_STATES = 7
MAX_NL80211_PLINK_STATES = NUM_NL80211_PLINK_STATES - 1
PLINK_ACTION_NO_ACTION = 0
PLINK_ACTION_OPEN = 1
PLINK_ACTION_BLOCK = 2
NUM_NL80211_PLINK_ACTIONS = 3
REKEY_DATA_INVALID = 0
REKEY_DATA_KEK = 1
REKEY_DATA_KCK = 2
REKEY_DATA_REPLAY_CTR = 3
NUM_NL80211_REKEY_DATA = 4
MAX_NL80211_REKEY_DATA = NUM_NL80211_REKEY_DATA - 1
HIDDEN_SSID_NOT_IN_USE = 0
HIDDEN_SSID_ZERO_LEN = 1
HIDDEN_SSID_ZERO_CONTENTS = 2
STA_WME_INVALID = 0
STA_WME_UAPSD_QUEUES = 1
STA_WME_MAX_SP = 2
STA_WME_AFTER_LAST = 3
STA_WME_MAX = STA_WME_AFTER_LAST - 1
PMKSA_CANDIDATE_INVALID = 0
PMKSA_CANDIDATE_INDEX = 1
PMKSA_CANDIDATE_BSSID = 2
PMKSA_CANDIDATE_PREAUTH = 3
NUM_NL80211_PMKSA_CANDIDATE = 4
MAX_NL80211_PMKSA_CANDIDATE = NUM_NL80211_PMKSA_CANDIDATE - 1
TDLS_DISCOVERY_REQ = 0
TDLS_SETUP = 1
TDLS_TEARDOWN = 2
TDLS_ENABLE_LINK = 3
TDLS_DISABLE_LINK = 4
FEATURE_SK_TX_STATUS = 1 << 0
FEATURE_HT_IBSS = 1 << 1
FEATURE_INACTIVITY_TIMER = 1 << 2
FEATURE_CELL_BASE_REG_HINTS = 1 << 3
FEATURE_P2P_DEVICE_NEEDS_CHANNEL = 1 << 4
FEATURE_SAE = 1 << 5
FEATURE_LOW_PRIORITY_SCAN = 1 << 6
FEATURE_SCAN_FLUSH = 1 << 7
FEATURE_AP_SCAN = 1 << 8
FEATURE_VIF_TXPOWER = 1 << 9
FEATURE_NEED_OBSS_SCAN = 1 << 10
FEATURE_P2P_GO_CTWIN = 1 << 11
FEATURE_P2P_GO_OPPPS = 1 << 12
FEATURE_ADVERTISE_CHAN_LIMITS = 1 << 14
FEATURE_FULL_AP_CLIENT_STATE = 1 << 15
FEATURE_USERSPACE_MPM = 1 << 16
FEATURE_ACTIVE_MONITOR = 1 << 17
FEATURE_AP_MODE_CHAN_WIDTH_CHANGE = 1 << 18
FEATURE_DS_PARAM_SET_IE_IN_PROBES = 1 << 19
FEATURE_WFA_TPC_IE_IN_PROBES = 1 << 20
FEATURE_QUIET = 1 << 21
FEATURE_TX_POWER_INSERTION = 1 << 22
FEATURE_ACKTO_ESTIMATION = 1 << 23
FEATURE_STATIC_SMPS = 1 << 24
FEATURE_DYNAMIC_SMPS = 1 << 25
FEATURE_SUPPORTS_WMM_ADMISSION = 1 << 26
FEATURE_MAC_ON_CREATE = 1 << 27
FEATURE_TDLS_CHANNEL_SWITCH = 1 << 28
FEATURE_SCAN_RANDOM_MAC_ADDR = 1 << 29
FEATURE_SCHED_SCAN_RANDOM_MAC_ADDR = 1 << 30
FEATURE_ND_RANDOM_MAC_ADDR = 1 << 31
EXT_FEATURE_VHT_IBSS = 0
EXT_FEATURE_RRM = 1
EXT_FEATURE_MU_MIMO_AIR_SNIFFER = 2
EXT_FEATURE_SCAN_START_TIME = 3
EXT_FEATURE_BSS_PARENT_TSF = 4
EXT_FEATURE_SET_SCAN_DWELL = 5
EXT_FEATURE_BEACON_RATE_LEGACY = 6
EXT_FEATURE_BEACON_RATE_HT = 7
EXT_FEATURE_BEACON_RATE_VHT = 8
EXT_FEATURE_FILS_STA = 9
EXT_FEATURE_MGMT_TX_RANDOM_TA = 10
EXT_FEATURE_MGMT_TX_RANDOM_TA_CONNECTED = 11
EXT_FEATURE_SCHED_SCAN_RELATIVE_RSSI = 12
EXT_FEATURE_CQM_RSSI_LIST = 13
EXT_FEATURE_FILS_SK_OFFLOAD = 14
EXT_FEATURE_4WAY_HANDSHAKE_STA_PSK = 15
EXT_FEATURE_4WAY_HANDSHAKE_STA_1X = 16
EXT_FEATURE_FILS_MAX_CHANNEL_TIME = 17
EXT_FEATURE_ACCEPT_BCAST_PROBE_RESP = 18
EXT_FEATURE_OCE_PROBE_REQ_HIGH_TX_RATE = 19
EXT_FEATURE_OCE_PROBE_REQ_DEFERRAL_SUPPRESSION = 20
EXT_FEATURE_MFP_OPTIONAL = 21
EXT_FEATURE_LOW_SPAN_SCAN = 22
EXT_FEATURE_LOW_POWER_SCAN = 23
EXT_FEATURE_HIGH_ACCURACY_SCAN = 24
EXT_FEATURE_DFS_OFFLOAD = 25
EXT_FEATURE_CONTROL_PORT_OVER_NL80211 = 26
NUM_NL80211_EXT_FEATURES = 27
MAX_NL80211_EXT_FEATURES = NUM_NL80211_EXT_FEATURES - 1
PROBE_RESP_OFFLOAD_SUPPORT_WPS = 1 << 0
PROBE_RESP_OFFLOAD_SUPPORT_WPS2 = 1 << 1
PROBE_RESP_OFFLOAD_SUPPORT_P2P = 1 << 2
PROBE_RESP_OFFLOAD_SUPPORT_80211U = 1 << 3
CONN_FAIL_MAX_CLIENTS = 0
CONN_FAIL_BLOCKED_CLIENT = 1
TIMEOUT_UNSPECIFIED = 0
TIMEOUT_SCAN = 1
TIMEOUT_AUTH = 2
TIMEOUT_ASSOC = 3
SCAN_FLAG_LOW_PRIORITY = 1 << 0
SCAN_FLAG_FLUSH = 1 << 1
SCAN_FLAG_AP = 1 << 2
SCAN_FLAG_RANDOM_ADDR = 1 << 3
SCAN_FLAG_FILS_MAX_CHANNEL_TIME = 1 << 4
SCAN_FLAG_ACCEPT_BCAST_PROBE_RESP = 1 << 5
SCAN_FLAG_OCE_PROBE_REQ_HIGH_TX_RATE = 1 << 6
SCAN_FLAG_OCE_PROBE_REQ_DEFERRAL_SUPPRESSION = 1 << 7
SCAN_FLAG_LOW_SPAN = 1 << 8
SCAN_FLAG_LOW_POWER = 1 << 9
SCAN_FLAG_HIGH_ACCURACY = 1 << 10
ACL_POLICY_ACCEPT_UNLESS_LISTED = 0
ACL_POLICY_DENY_UNLESS_LISTED = 1
SMPS_OFF = 0
SMPS_STATIC = 1
SMPS_DYNAMIC = 2
SMPS_AFTER_LAST = 3
SMPS_MAX = SMPS_AFTER_LAST - 1
RADAR_DETECTED = 0
RADAR_CAC_FINISHED = 1
RADAR_CAC_ABORTED = 2
RADAR_NOP_FINISHED = 3
RADAR_PRE_CAC_EXPIRED = 4
RADAR_CAC_STARTED = 5
DFS_USABLE = 0
DFS_UNAVAILABLE = 1
DFS_AVAILABLE = 2
PROTOCOL_FEATURE_SPLIT_WIPHY_DUMP = 1 << 0
CRIT_PROTO_UNSPEC = 0
CRIT_PROTO_DHCP = 1
CRIT_PROTO_EAPOL = 2
CRIT_PROTO_APIPA = 3
NUM_NL80211_CRIT_PROTO = 4
RXMGMT_FLAG_ANSWERED = 1 << 0
TDLS_PEER_HT = 1 << 0
TDLS_PEER_VHT = 1 << 1
TDLS_PEER_WMM = 1 << 2
SCHED_SCAN_PLAN_INVALID = 0
SCHED_SCAN_PLAN_INTERVAL = 1
SCHED_SCAN_PLAN_ITERATIONS = 2
SCHED_SCAN_PLAN_AFTER_LAST = 3
SCHED_SCAN_PLAN_MAX = SCHED_SCAN_PLAN_AFTER_LAST - 1
BSS_SELECT_ATTR_INVALID = 0
BSS_SELECT_ATTR_RSSI = 1
BSS_SELECT_ATTR_BAND_PREF = 2
BSS_SELECT_ATTR_RSSI_ADJUST = 3
BSS_SELECT_ATTR_AFTER_LAST = 4
BSS_SELECT_ATTR_MAX = BSS_SELECT_ATTR_AFTER_LAST - 1
NAN_FUNC_PUBLISH = 0
NAN_FUNC_SUBSCRIBE = 1
NAN_FUNC_FOLLOW_UP = 2
NAN_FUNC_TYPE_AFTER_LAST = 3
NAN_FUNC_MAX_TYPE = NAN_FUNC_TYPE_AFTER_LAST - 1
NAN_SOLICITED_PUBLISH = 1 << 0
NAN_UNSOLICITED_PUBLISH = 1 << 1
NAN_FUNC_TERM_REASON_USER_REQUEST = 0
NAN_FUNC_TERM_REASON_TTL_EXPIRED = 1
NAN_FUNC_TERM_REASON_ERROR = 2
NAN_FUNC_INVALID = 0
NAN_FUNC_TYPE = 1
NAN_FUNC_SERVICE_ID = 2
NAN_FUNC_PUBLISH_TYPE = 3
NAN_FUNC_PUBLISH_BCAST = 4
NAN_FUNC_SUBSCRIBE_ACTIVE = 5
NAN_FUNC_FOLLOW_UP_ID = 6
NAN_FUNC_FOLLOW_UP_REQ_ID = 7
NAN_FUNC_FOLLOW_UP_DEST = 8
NAN_FUNC_CLOSE_RANGE = 9
NAN_FUNC_TTL = 10
NAN_FUNC_SERVICE_INFO = 11
NAN_FUNC_SRF = 12
NAN_FUNC_RX_MATCH_FILTER = 13
NAN_FUNC_TX_MATCH_FILTER = 14
NAN_FUNC_INSTANCE_ID = 15
NAN_FUNC_TERM_REASON = 16
NUM_NL80211_NAN_FUNC_ATTR = 17
NAN_FUNC_ATTR_MAX = NUM_NL80211_NAN_FUNC_ATTR - 1
NAN_SRF_INVALID = 0
NAN_SRF_INCLUDE = 1
NAN_SRF_BF = 2
NAN_SRF_BF_IDX = 3
NAN_SRF_MAC_ADDRS = 4
NUM_NL80211_NAN_SRF_ATTR = 5
NAN_SRF_ATTR_MAX = NUM_NL80211_NAN_SRF_ATTR - 1
NAN_MATCH_INVALID = 0
NAN_MATCH_FUNC_LOCAL = 1
NAN_MATCH_FUNC_PEER = 2
NUM_NL80211_NAN_MATCH_ATTR = 3
NAN_MATCH_ATTR_MAX = NUM_NL80211_NAN_MATCH_ATTR - 1
EXTERNAL_AUTH_START = 0
EXTERNAL_AUTH_ABORT = 1
