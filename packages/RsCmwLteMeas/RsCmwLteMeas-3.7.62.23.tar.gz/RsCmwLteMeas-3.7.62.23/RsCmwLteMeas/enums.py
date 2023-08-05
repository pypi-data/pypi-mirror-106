from enum import Enum


# noinspection SpellCheckingInspection
class Band(Enum):
	"""61 Members, OB1 ... OB9"""
	OB1 = 0
	OB10 = 1
	OB11 = 2
	OB12 = 3
	OB13 = 4
	OB14 = 5
	OB15 = 6
	OB16 = 7
	OB17 = 8
	OB18 = 9
	OB19 = 10
	OB2 = 11
	OB20 = 12
	OB21 = 13
	OB22 = 14
	OB23 = 15
	OB24 = 16
	OB25 = 17
	OB250 = 18
	OB26 = 19
	OB27 = 20
	OB28 = 21
	OB3 = 22
	OB30 = 23
	OB31 = 24
	OB33 = 25
	OB34 = 26
	OB35 = 27
	OB36 = 28
	OB37 = 29
	OB38 = 30
	OB39 = 31
	OB4 = 32
	OB40 = 33
	OB41 = 34
	OB42 = 35
	OB43 = 36
	OB44 = 37
	OB45 = 38
	OB46 = 39
	OB47 = 40
	OB48 = 41
	OB49 = 42
	OB5 = 43
	OB50 = 44
	OB51 = 45
	OB52 = 46
	OB53 = 47
	OB6 = 48
	OB65 = 49
	OB66 = 50
	OB68 = 51
	OB7 = 52
	OB70 = 53
	OB71 = 54
	OB72 = 55
	OB73 = 56
	OB74 = 57
	OB8 = 58
	OB85 = 59
	OB9 = 60


# noinspection SpellCheckingInspection
class CarrAggrLocalOscLocation(Enum):
	"""3 Members, AUTO ... CECC"""
	AUTO = 0
	CACB = 1
	CECC = 2


# noinspection SpellCheckingInspection
class CarrAggrMaping(Enum):
	"""9 Members, INV ... SCC7"""
	INV = 0
	PCC = 1
	SCC1 = 2
	SCC2 = 3
	SCC3 = 4
	SCC4 = 5
	SCC5 = 6
	SCC6 = 7
	SCC7 = 8


# noinspection SpellCheckingInspection
class CarrAggrMode(Enum):
	"""4 Members, ICD ... OFF"""
	ICD = 0
	ICE = 1
	INTRaband = 2
	OFF = 3


# noinspection SpellCheckingInspection
class ChannelBandwidth(Enum):
	"""6 Members, B014 ... B200"""
	B014 = 0
	B030 = 1
	B050 = 2
	B100 = 3
	B150 = 4
	B200 = 5


# noinspection SpellCheckingInspection
class ChannelTypeDetection(Enum):
	"""3 Members, AUTO ... PUSCh"""
	AUTO = 0
	PUCCh = 1
	PUSCh = 2


# noinspection SpellCheckingInspection
class ChannelTypeVewFilter(Enum):
	"""4 Members, OFF ... PUSCh"""
	OFF = 0
	ON = 1
	PUCCh = 2
	PUSCh = 3


# noinspection SpellCheckingInspection
class CmwsConnector(Enum):
	"""48 Members, R11 ... RB8"""
	R11 = 0
	R12 = 1
	R13 = 2
	R14 = 3
	R15 = 4
	R16 = 5
	R17 = 6
	R18 = 7
	R21 = 8
	R22 = 9
	R23 = 10
	R24 = 11
	R25 = 12
	R26 = 13
	R27 = 14
	R28 = 15
	R31 = 16
	R32 = 17
	R33 = 18
	R34 = 19
	R35 = 20
	R36 = 21
	R37 = 22
	R38 = 23
	R41 = 24
	R42 = 25
	R43 = 26
	R44 = 27
	R45 = 28
	R46 = 29
	R47 = 30
	R48 = 31
	RA1 = 32
	RA2 = 33
	RA3 = 34
	RA4 = 35
	RA5 = 36
	RA6 = 37
	RA7 = 38
	RA8 = 39
	RB1 = 40
	RB2 = 41
	RB3 = 42
	RB4 = 43
	RB5 = 44
	RB6 = 45
	RB7 = 46
	RB8 = 47


# noinspection SpellCheckingInspection
class CyclicPrefix(Enum):
	"""2 Members, EXTended ... NORMal"""
	EXTended = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class DuplexMode(Enum):
	"""3 Members, FDD ... TDD"""
	FDD = 0
	FTDD = 1
	TDD = 2


# noinspection SpellCheckingInspection
class FrameStructure(Enum):
	"""2 Members, T1 ... T2"""
	T1 = 0
	T2 = 1


# noinspection SpellCheckingInspection
class LaggingExclPeriod(Enum):
	"""3 Members, MS05 ... OFF"""
	MS05 = 0
	MS25 = 1
	OFF = 2


# noinspection SpellCheckingInspection
class LeadingExclPeriod(Enum):
	"""2 Members, MS25 ... OFF"""
	MS25 = 0
	OFF = 1


# noinspection SpellCheckingInspection
class ListMode(Enum):
	"""2 Members, ONCE ... SEGMent"""
	ONCE = 0
	SEGMent = 1


# noinspection SpellCheckingInspection
class LocalOscLocation(Enum):
	"""2 Members, CCB ... CN"""
	CCB = 0
	CN = 1


# noinspection SpellCheckingInspection
class LowHigh(Enum):
	"""2 Members, HIGH ... LOW"""
	HIGH = 0
	LOW = 1


# noinspection SpellCheckingInspection
class MeasCarrier(Enum):
	"""2 Members, PCC ... SCC1"""
	PCC = 0
	SCC1 = 1


# noinspection SpellCheckingInspection
class MeasCarrierEnhanced(Enum):
	"""4 Members, CC1 ... CC4"""
	CC1 = 0
	CC2 = 1
	CC3 = 2
	CC4 = 3


# noinspection SpellCheckingInspection
class MeasFilter(Enum):
	"""2 Members, BANDpass ... GAUSs"""
	BANDpass = 0
	GAUSs = 1


# noinspection SpellCheckingInspection
class MeasurementMode(Enum):
	"""3 Members, MELMode ... TMODe"""
	MELMode = 0
	NORMal = 1
	TMODe = 2


# noinspection SpellCheckingInspection
class MeasureSlot(Enum):
	"""3 Members, ALL ... MS1"""
	ALL = 0
	MS0 = 1
	MS1 = 2


# noinspection SpellCheckingInspection
class MevAcquisitionMode(Enum):
	"""2 Members, SLOT ... SUBFrame"""
	SLOT = 0
	SUBFrame = 1


# noinspection SpellCheckingInspection
class ModScheme(Enum):
	"""5 Members, AUTO ... QPSK"""
	AUTO = 0
	Q16 = 1
	Q256 = 2
	Q64 = 3
	QPSK = 4


# noinspection SpellCheckingInspection
class Modulation(Enum):
	"""4 Members, Q16 ... QPSK"""
	Q16 = 0
	Q256 = 1
	Q64 = 2
	QPSK = 3


# noinspection SpellCheckingInspection
class NetworkSigValue(Enum):
	"""32 Members, NS01 ... NS32"""
	NS01 = 0
	NS02 = 1
	NS03 = 2
	NS04 = 3
	NS05 = 4
	NS06 = 5
	NS07 = 6
	NS08 = 7
	NS09 = 8
	NS10 = 9
	NS11 = 10
	NS12 = 11
	NS13 = 12
	NS14 = 13
	NS15 = 14
	NS16 = 15
	NS17 = 16
	NS18 = 17
	NS19 = 18
	NS20 = 19
	NS21 = 20
	NS22 = 21
	NS23 = 22
	NS24 = 23
	NS25 = 24
	NS26 = 25
	NS27 = 26
	NS28 = 27
	NS29 = 28
	NS30 = 29
	NS31 = 30
	NS32 = 31


# noinspection SpellCheckingInspection
class NetworkSigValueNoCarrAggr(Enum):
	"""288 Members, NS01 ... NS99"""
	NS01 = 0
	NS02 = 1
	NS03 = 2
	NS04 = 3
	NS05 = 4
	NS06 = 5
	NS07 = 6
	NS08 = 7
	NS09 = 8
	NS10 = 9
	NS100 = 10
	NS101 = 11
	NS102 = 12
	NS103 = 13
	NS104 = 14
	NS105 = 15
	NS106 = 16
	NS107 = 17
	NS108 = 18
	NS109 = 19
	NS11 = 20
	NS110 = 21
	NS111 = 22
	NS112 = 23
	NS113 = 24
	NS114 = 25
	NS115 = 26
	NS116 = 27
	NS117 = 28
	NS118 = 29
	NS119 = 30
	NS12 = 31
	NS120 = 32
	NS121 = 33
	NS122 = 34
	NS123 = 35
	NS124 = 36
	NS125 = 37
	NS126 = 38
	NS127 = 39
	NS128 = 40
	NS129 = 41
	NS13 = 42
	NS130 = 43
	NS131 = 44
	NS132 = 45
	NS133 = 46
	NS134 = 47
	NS135 = 48
	NS136 = 49
	NS137 = 50
	NS138 = 51
	NS139 = 52
	NS14 = 53
	NS140 = 54
	NS141 = 55
	NS142 = 56
	NS143 = 57
	NS144 = 58
	NS145 = 59
	NS146 = 60
	NS147 = 61
	NS148 = 62
	NS149 = 63
	NS15 = 64
	NS150 = 65
	NS151 = 66
	NS152 = 67
	NS153 = 68
	NS154 = 69
	NS155 = 70
	NS156 = 71
	NS157 = 72
	NS158 = 73
	NS159 = 74
	NS16 = 75
	NS160 = 76
	NS161 = 77
	NS162 = 78
	NS163 = 79
	NS164 = 80
	NS165 = 81
	NS166 = 82
	NS167 = 83
	NS168 = 84
	NS169 = 85
	NS17 = 86
	NS170 = 87
	NS171 = 88
	NS172 = 89
	NS173 = 90
	NS174 = 91
	NS175 = 92
	NS176 = 93
	NS177 = 94
	NS178 = 95
	NS179 = 96
	NS18 = 97
	NS180 = 98
	NS181 = 99
	NS182 = 100
	NS183 = 101
	NS184 = 102
	NS185 = 103
	NS186 = 104
	NS187 = 105
	NS188 = 106
	NS189 = 107
	NS19 = 108
	NS190 = 109
	NS191 = 110
	NS192 = 111
	NS193 = 112
	NS194 = 113
	NS195 = 114
	NS196 = 115
	NS197 = 116
	NS198 = 117
	NS199 = 118
	NS20 = 119
	NS200 = 120
	NS201 = 121
	NS202 = 122
	NS203 = 123
	NS204 = 124
	NS205 = 125
	NS206 = 126
	NS207 = 127
	NS208 = 128
	NS209 = 129
	NS21 = 130
	NS210 = 131
	NS211 = 132
	NS212 = 133
	NS213 = 134
	NS214 = 135
	NS215 = 136
	NS216 = 137
	NS217 = 138
	NS218 = 139
	NS219 = 140
	NS22 = 141
	NS220 = 142
	NS221 = 143
	NS222 = 144
	NS223 = 145
	NS224 = 146
	NS225 = 147
	NS226 = 148
	NS227 = 149
	NS228 = 150
	NS229 = 151
	NS23 = 152
	NS230 = 153
	NS231 = 154
	NS232 = 155
	NS233 = 156
	NS234 = 157
	NS235 = 158
	NS236 = 159
	NS237 = 160
	NS238 = 161
	NS239 = 162
	NS24 = 163
	NS240 = 164
	NS241 = 165
	NS242 = 166
	NS243 = 167
	NS244 = 168
	NS245 = 169
	NS246 = 170
	NS247 = 171
	NS248 = 172
	NS249 = 173
	NS25 = 174
	NS250 = 175
	NS251 = 176
	NS252 = 177
	NS253 = 178
	NS254 = 179
	NS255 = 180
	NS256 = 181
	NS257 = 182
	NS258 = 183
	NS259 = 184
	NS26 = 185
	NS260 = 186
	NS261 = 187
	NS262 = 188
	NS263 = 189
	NS264 = 190
	NS265 = 191
	NS266 = 192
	NS267 = 193
	NS268 = 194
	NS269 = 195
	NS27 = 196
	NS270 = 197
	NS271 = 198
	NS272 = 199
	NS273 = 200
	NS274 = 201
	NS275 = 202
	NS276 = 203
	NS277 = 204
	NS278 = 205
	NS279 = 206
	NS28 = 207
	NS280 = 208
	NS281 = 209
	NS282 = 210
	NS283 = 211
	NS284 = 212
	NS285 = 213
	NS286 = 214
	NS287 = 215
	NS288 = 216
	NS29 = 217
	NS30 = 218
	NS31 = 219
	NS32 = 220
	NS33 = 221
	NS34 = 222
	NS35 = 223
	NS36 = 224
	NS37 = 225
	NS38 = 226
	NS39 = 227
	NS40 = 228
	NS41 = 229
	NS42 = 230
	NS43 = 231
	NS44 = 232
	NS45 = 233
	NS46 = 234
	NS47 = 235
	NS48 = 236
	NS49 = 237
	NS50 = 238
	NS51 = 239
	NS52 = 240
	NS53 = 241
	NS54 = 242
	NS55 = 243
	NS56 = 244
	NS57 = 245
	NS58 = 246
	NS59 = 247
	NS60 = 248
	NS61 = 249
	NS62 = 250
	NS63 = 251
	NS64 = 252
	NS65 = 253
	NS66 = 254
	NS67 = 255
	NS68 = 256
	NS69 = 257
	NS70 = 258
	NS71 = 259
	NS72 = 260
	NS73 = 261
	NS74 = 262
	NS75 = 263
	NS76 = 264
	NS77 = 265
	NS78 = 266
	NS79 = 267
	NS80 = 268
	NS81 = 269
	NS82 = 270
	NS83 = 271
	NS84 = 272
	NS85 = 273
	NS86 = 274
	NS87 = 275
	NS88 = 276
	NS89 = 277
	NS90 = 278
	NS91 = 279
	NS92 = 280
	NS93 = 281
	NS94 = 282
	NS95 = 283
	NS96 = 284
	NS97 = 285
	NS98 = 286
	NS99 = 287


# noinspection SpellCheckingInspection
class ParameterSetMode(Enum):
	"""2 Members, GLOBal ... LIST"""
	GLOBal = 0
	LIST = 1


# noinspection SpellCheckingInspection
class PeriodPreamble(Enum):
	"""3 Members, MS05 ... MS20"""
	MS05 = 0
	MS10 = 1
	MS20 = 2


# noinspection SpellCheckingInspection
class PucchFormat(Enum):
	"""7 Members, F1 ... F3"""
	F1 = 0
	F1A = 1
	F1B = 2
	F2 = 3
	F2A = 4
	F2B = 5
	F3 = 6


# noinspection SpellCheckingInspection
class RbTableChannelType(Enum):
	"""7 Members, DL ... SSUB"""
	DL = 0
	NONE = 1
	PSCCh = 2
	PSSCh = 3
	PUCCh = 4
	PUSCh = 5
	SSUB = 6


# noinspection SpellCheckingInspection
class Rbw(Enum):
	"""3 Members, K030 ... M1"""
	K030 = 0
	K100 = 1
	M1 = 2


# noinspection SpellCheckingInspection
class RbwExtended(Enum):
	"""6 Members, K030 ... M1"""
	K030 = 0
	K050 = 1
	K100 = 2
	K150 = 3
	K200 = 4
	M1 = 5


# noinspection SpellCheckingInspection
class Repeat(Enum):
	"""2 Members, CONTinuous ... SINGleshot"""
	CONTinuous = 0
	SINGleshot = 1


# noinspection SpellCheckingInspection
class ResourceState(Enum):
	"""8 Members, ACTive ... RUN"""
	ACTive = 0
	ADJusted = 1
	INValid = 2
	OFF = 3
	PENDing = 4
	QUEued = 5
	RDY = 6
	RUN = 7


# noinspection SpellCheckingInspection
class ResultStatus2(Enum):
	"""10 Members, DC ... ULEU"""
	DC = 0
	INV = 1
	NAV = 2
	NCAP = 3
	OFF = 4
	OFL = 5
	OK = 6
	UFL = 7
	ULEL = 8
	ULEU = 9


# noinspection SpellCheckingInspection
class RetriggerFlag(Enum):
	"""3 Members, IFPower ... ON"""
	IFPower = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class RxConnector(Enum):
	"""154 Members, I11I ... RH8"""
	I11I = 0
	I13I = 1
	I15I = 2
	I17I = 3
	I21I = 4
	I23I = 5
	I25I = 6
	I27I = 7
	I31I = 8
	I33I = 9
	I35I = 10
	I37I = 11
	I41I = 12
	I43I = 13
	I45I = 14
	I47I = 15
	IF1 = 16
	IF2 = 17
	IF3 = 18
	IQ1I = 19
	IQ3I = 20
	IQ5I = 21
	IQ7I = 22
	R11 = 23
	R11C = 24
	R12 = 25
	R12C = 26
	R12I = 27
	R13 = 28
	R13C = 29
	R14 = 30
	R14C = 31
	R14I = 32
	R15 = 33
	R16 = 34
	R17 = 35
	R18 = 36
	R21 = 37
	R21C = 38
	R22 = 39
	R22C = 40
	R22I = 41
	R23 = 42
	R23C = 43
	R24 = 44
	R24C = 45
	R24I = 46
	R25 = 47
	R26 = 48
	R27 = 49
	R28 = 50
	R31 = 51
	R31C = 52
	R32 = 53
	R32C = 54
	R32I = 55
	R33 = 56
	R33C = 57
	R34 = 58
	R34C = 59
	R34I = 60
	R35 = 61
	R36 = 62
	R37 = 63
	R38 = 64
	R41 = 65
	R41C = 66
	R42 = 67
	R42C = 68
	R42I = 69
	R43 = 70
	R43C = 71
	R44 = 72
	R44C = 73
	R44I = 74
	R45 = 75
	R46 = 76
	R47 = 77
	R48 = 78
	RA1 = 79
	RA2 = 80
	RA3 = 81
	RA4 = 82
	RA5 = 83
	RA6 = 84
	RA7 = 85
	RA8 = 86
	RB1 = 87
	RB2 = 88
	RB3 = 89
	RB4 = 90
	RB5 = 91
	RB6 = 92
	RB7 = 93
	RB8 = 94
	RC1 = 95
	RC2 = 96
	RC3 = 97
	RC4 = 98
	RC5 = 99
	RC6 = 100
	RC7 = 101
	RC8 = 102
	RD1 = 103
	RD2 = 104
	RD3 = 105
	RD4 = 106
	RD5 = 107
	RD6 = 108
	RD7 = 109
	RD8 = 110
	RE1 = 111
	RE2 = 112
	RE3 = 113
	RE4 = 114
	RE5 = 115
	RE6 = 116
	RE7 = 117
	RE8 = 118
	RF1 = 119
	RF1C = 120
	RF2 = 121
	RF2C = 122
	RF2I = 123
	RF3 = 124
	RF3C = 125
	RF4 = 126
	RF4C = 127
	RF4I = 128
	RF5 = 129
	RF5C = 130
	RF6 = 131
	RF6C = 132
	RF7 = 133
	RF8 = 134
	RFAC = 135
	RFBC = 136
	RFBI = 137
	RG1 = 138
	RG2 = 139
	RG3 = 140
	RG4 = 141
	RG5 = 142
	RG6 = 143
	RG7 = 144
	RG8 = 145
	RH1 = 146
	RH2 = 147
	RH3 = 148
	RH4 = 149
	RH5 = 150
	RH6 = 151
	RH7 = 152
	RH8 = 153


# noinspection SpellCheckingInspection
class RxConverter(Enum):
	"""40 Members, IRX1 ... RX44"""
	IRX1 = 0
	IRX11 = 1
	IRX12 = 2
	IRX13 = 3
	IRX14 = 4
	IRX2 = 5
	IRX21 = 6
	IRX22 = 7
	IRX23 = 8
	IRX24 = 9
	IRX3 = 10
	IRX31 = 11
	IRX32 = 12
	IRX33 = 13
	IRX34 = 14
	IRX4 = 15
	IRX41 = 16
	IRX42 = 17
	IRX43 = 18
	IRX44 = 19
	RX1 = 20
	RX11 = 21
	RX12 = 22
	RX13 = 23
	RX14 = 24
	RX2 = 25
	RX21 = 26
	RX22 = 27
	RX23 = 28
	RX24 = 29
	RX3 = 30
	RX31 = 31
	RX32 = 32
	RX33 = 33
	RX34 = 34
	RX4 = 35
	RX41 = 36
	RX42 = 37
	RX43 = 38
	RX44 = 39


# noinspection SpellCheckingInspection
class Scenario(Enum):
	"""4 Members, CSPath ... SALone"""
	CSPath = 0
	MAPRotocol = 1
	NAV = 2
	SALone = 3


# noinspection SpellCheckingInspection
class SegmentChannelTypeExtended(Enum):
	"""5 Members, AUTO ... PUSCh"""
	AUTO = 0
	PSCCh = 1
	PSSCh = 2
	PUCCh = 3
	PUSCh = 4


# noinspection SpellCheckingInspection
class SidelinkChannelType(Enum):
	"""2 Members, PSCCh ... PSSCh"""
	PSCCh = 0
	PSSCh = 1


# noinspection SpellCheckingInspection
class SignalSlope(Enum):
	"""2 Members, FEDGe ... REDGe"""
	FEDGe = 0
	REDGe = 1


# noinspection SpellCheckingInspection
class SignalType(Enum):
	"""2 Members, SL ... UL"""
	SL = 0
	UL = 1


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""2 Members, NONE ... SLFail"""
	NONE = 0
	SLFail = 1


# noinspection SpellCheckingInspection
class SyncMode(Enum):
	"""2 Members, ENHanced ... NORMal"""
	ENHanced = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class TimeMask(Enum):
	"""3 Members, GOO ... SBLanking"""
	GOO = 0
	PPSRs = 1
	SBLanking = 2


# noinspection SpellCheckingInspection
class UplinkChannelType(Enum):
	"""2 Members, PUCCh ... PUSCh"""
	PUCCh = 0
	PUSCh = 1
