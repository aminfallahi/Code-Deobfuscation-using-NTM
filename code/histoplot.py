import random
import numpy
from matplotlib import pyplot
import sys 
pyplot.rcParams.update({'font.size': 25})

x=[0]*6
y=[0]*6
z=[0]*6

#1
x[0]= [110.89876,110.333374,109.92326,109.13072,108.95798,107.405556,106.19795,104.20924,100.48485,98.790855,96.52365,96.21303,97.11136,95.22667,95.171005,94.9929,94.554245,91.46051,93.45661,94.31613,97.438,93.54152,91.5924,92.478455,92.98893,92.824486,91.7451,90.54636,88.20987,91.932785,93.66936,92.08043,94.77186,96.52514,93.57586,95.997086,92.58815,95.32184,90.97378,92.6884,91.51994,93.111786,88.57115,89.227615,90.48772,90.75987,91.20487,89.51729,96.9413,93.74958,93.75218,93.65816,93.87312,93.51523,95.82054,95.61388,91.590775,92.45146,90.39366,95.6753,89.79485,89.27911,91.28293,94.5211,96.09071,93.496,90.200165,94.99897,88.52568,94.50426,93.688805,91.02054,93.29948,91.54376,89.26811,99.97839,91.6172,89.79402,98.5443,85.34865,93.27325,93.93841,91.11269,94.4511,91.604355,90.86594,92.159584,90.12344,95.42851,96.43584,95.39682,90.952484,95.051414,96.77237,92.46783,92.92633,97.39024,91.586105,91.58109,90.97223]
y[0]= [42.2708333333333,43.25,40.7604166666667,44.4479166666667,43.8958333333333,43.6041666666667,42.9375,41.3958333333333,42.9895833333333,41.4791666666667,45.2708333333333,42.3020833333333,41.5729166666667,44.4895833333333,43.2291666666667,44.2083333333333,42.1041666666667,42.125,44.3958333333333,43.6354166666667,42.9166666666667,44.3958333333333,44.6354166666667,43.6354166666667,43.5729166666667,41.7604166666667,46.7604166666667,42.8229166666667,41.9166666666667,43.53125,43.6458333333333,42.9270833333333,41.75,42.1458333333333,41.8333333333333,42.125,42.1875,41.5520833333333,43.7291666666667,42.78125,42.8229166666667,45.84375,44.2916666666667,43.2708333333333,44.09375,45.375,42.2291666666667,41.9583333333333,42.03125,41.15625,42.2916666666667,43.4479166666667,42.2708333333333,42.8333333333333,44.2291666666667,42.6145833333333,43.3229166666667,42.2291666666667,43.8645833333333,43.15625,42.6666666666667,43.2083333333333,42.5104166666667,40.2083333333333,42.5520833333333,42.4479166666667,42.5833333333333,44.5208333333333,44.25,44.6979166666667,43.0104166666667,42.5833333333333,44.375,44.03125,41.6770833333333,45.5833333333333,42.6458333333333,43.9270833333333,42.4895833333333,42.78125,43.8854166666667,45.0833333333333,44.7604166666667,41.6145833333333,44.0625,43.65625,42.6458333333333,43.4166666666667,42.2708333333333,44.7604166666667,41.7083333333333,44.2604166666667,41.5833333333333,40.8645833333333,43.1041666666667,43.7708333333333,43.6354166666667,43.4583333333333,43.8333333333333,43.7291666666667]
z[0]=  [43.4876289689817,45.1897874609084,42.1713172683234,46.0238673630063,44.7886098757554,43.8901462619503,44.0208377910602,41.7894389107513,43.36857645165,41.5048520760844,45.4710192356103,42.4558614558444,42.0365737413644,45.9994189218784,45.0955403427385,46.196902181056,43.454591523159,43.4126703401881,45.48480120685,45.0051944877313,43.5505494133952,44.5708753580691,44.8118778235653,43.7426157709473,44.5773042593964,42.0688179599326,47.0797447106035,43.6997375156572,43.0091423143551,43.8869826854284,44.3053814596155,44.657640139076,42.9851989751444,43.5816804870818,42.9152526905005,43.7358383446524,42.8348577673947,42.8163214354621,43.9266797029714,43.3549584523571,44.4156669999129,45.971476339888,45.4283500904927,43.7189840132696,46.0662469713323,46.5219826510178,43.29379300133,42.4646718404487,43.6091994074083,42.9029737724811,43.2435207716423,43.9795728176933,43.1392803171244,44.773202839964,45.3273504347136,43.5343353578702,43.4948773453322,43.3970481090602,45.1802678987621,43.1865748732403,43.095211614442,44.0326169227658,44.2639309040258,40.5838766784836,43.2872320684368,42.9325043233847,43.4249800484609,44.6100027053143,44.3352428876075,45.8266388317411,44.3634813222835,44.3990585954982,44.5170494792023,44.5244904816547,43.4288658159268,46.973107954932,42.9906667243543,45.1482408411956,43.5807240820746,43.1433997283936,45.3997878104435,45.7039700165739,44.9995762854659,41.8196957690494,45.2284875187405,43.7667179269243,44.2219631539141,44.8781711893298,42.884466291918,45.3400052442898,42.3876965195317,45.7055694274761,41.6242883075203,41.6222162423066,44.0071506241163,45.4780455790243,43.6474768242193,45.014838429271,45.7541449278665,44.1687923757925]

#2
x[1]=[110.888626,110.0026,109.240616,107.95674,105.6039,103.7869,98.800186,98.919495,92.00952,92.489265,95.21733,97.81105,93.37575,90.46675,94.70463,89.491974,92.69551,89.07344,94.49673,96.7408,93.70125,95.11145,94.765015,94.69035,93.541855,92.23588,93.59851,95.63573,90.49142,93.81741,92.82091,90.11862,92.5772,96.585365,89.12831,90.98089,96.33769,92.01982,90.48511,88.506485,90.787025,88.362854,89.702866,93.80858,95.07909,90.343056,84.985115,89.37051,93.56425,88.257034,95.98795,93.23847,88.687904,89.777756,92.082275,92.13571,99.30626,97.14928,95.253555,94.17318,92.60539,95.34859,92.83345,94.02121,86.81385,93.928055,90.190125,93.31961,86.04811,91.79152,88.8998,95.31059,90.39807,89.61494,90.43622,94.42495,93.967285,93.76645,90.425995,94.557144,92.10327,90.638176,88.539536,90.10249,94.00255,89.928795,89.61201,93.686584,94.07593,93.83367,94.609344,94.79475,92.95747,88.97797,90.68283,91.04581,93.84351,90.153336,93.67705,92.44447]
y[1]=[40.9895833333333,41.9479166666667,41.0625,44.3020833333333,43.90625,42.3333333333333,44.65625,43.1041666666667,43.125,43.4895833333333,43.3020833333333,42.6770833333333,42.9895833333333,41.5729166666667,43.90625,43.28125,45,44.2083333333333,44.3020833333333,41.6145833333333,43.3333333333333,44,41.6145833333333,40.71875,44.2916666666667,39.875,43.3958333333333,42.4895833333333,43.71875,44.1041666666667,43.375,42.3125,42.6666666666667,42.75,42.9583333333333,43.1458333333333,43.4479166666667,44.0729166666667,43.7395833333333,44.71875,42.9895833333333,41.3333333333333,43.7083333333333,45.40625,41.5729166666667,44.4583333333333,44.09375,42.5416666666667,43.5625,43.8645833333333,42.3854166666667,44.25,42.4791666666667,41.4270833333333,42.6458333333333,45.9583333333333,41.9583333333333,44.0416666666667,43.0208333333333,45.15625,43.0833333333333,45.375,44.4895833333333,44.1875,42.7604166666667,44.1875,42,43.9270833333333,40.6041666666667,43.5104166666667,45.4583333333333,44.6041666666667,44.7083333333333,46.5208333333333,39.9895833333333,41.46875,43.0208333333333,42.5104166666667,43.375,43.65625,42.6875,45.5104166666667,42.6666666666667,43.2395833333333,42.2083333333333,44.7916666666667,43.5104166666667,42.71875,42.03125,42.2083333333333,40.4479166666667,45.5208333333333,42.5729166666667,42.7291666666667,43.6666666666667,44.8125,43.0208333333333,42.0833333333333,43.875,43.8854166666667]
z[1]=[42.427522168994,43.9397163668059,41.4718612975723,44.4241148161911,43.9643978507509,43.2518550370446,46.0379076760957,44.9335948836956,43.8552752847532,43.8852033138376,44.1398530211166,43.3964347643629,44.7703584648228,42.3647572037204,45.458785783129,43.3506944020405,45.8328829636772,45.1571551847169,46.206005348646,43.0838716969674,44.2343654027504,44.7962712209122,42.3793558416273,41.1439215209078,45.3642624361947,40.1650840116531,44.7587023527749,42.9759164621245,44.9251821431131,45.8675756023496,43.6080104934375,43.2243893224311,44.3638793070309,43.4284412668945,44.5191081865376,44.8057542597086,44.2942191473584,45.3597969623741,44.6880453006527,45.4629699234264,44.89618003394,43.1769490804342,44.6241408892769,46.8481964884482,42.9004387453696,45.5881631426786,44.2512373025597,44.0083564835992,44.218487500906,44.1550585688696,42.460275675083,46.0429707103591,43.1572554777545,42.4796515572093,43.6502098968006,47.5631947282151,43.2211299202795,46.0064049642101,44.9609439090721,45.767814524822,43.7628328254725,47.0506494965326,45.5732274500645,44.6995442962466,43.0735066110357,45.1978568623569,42.9070875567998,45.7807623787612,40.7628545501891,44.9238656161033,46.0440995340503,45.1734797631717,46.0152787882026,47.7336724563063,41.3266091454918,42.815349864857,44.8446620030528,43.7692490038838,44.2885762266807,44.3073770134171,43.2182762856012,45.8167850486689,44.4772223109162,44.8160591290446,43.560465838105,45.2119623638993,44.1313054805434,42.8698029990603,42.3318970681756,43.878608977251,42.0573969479677,47.1336530242372,43.1116625642891,43.876057203866,44.3772501340596,46.3718547057121,44.391130751399,43.2783311419561,45.7528762985082,44.0709226224452]

#3
x[2]=[111.02471,110.60109,109.87442,109.36541,108.18301,107.604034,104.938126,103.04042,102.06883,94.7014,90.83569,93.32794,94.63908,87.17383,92.991745,95.24301,91.017944,87.77472,91.44032,89.69223,90.48329,94.4355,97.30428,89.32338,93.640076,89.65822,90.97099,98.087074,91.69928,95.13848,89.98033,91.24518,93.41913,88.37604,90.043106,93.25784,94.937454,87.54979,85.81671,94.18448,93.93508,89.56052,86.2749,98.75771,92.37567,94.01973,93.598526,88.56664,92.53871,84.980125,91.84066,95.71294,88.47555,96.42022,94.719315,90.221725,90.20074,96.143684,89.80346,92.83592,87.525246,92.19109,90.436295,89.55835,89.10477,84.753876,97.76266,81.34506,91.03616,88.89793,85.73735,87.37053,92.98857,88.13682,90.32341,91.47658,94.22301,87.60239,92.33407,86.519356,86.973236,91.754,83.632324,91.93533,85.22621,93.58415,89.248795,90.38968,87.818855,91.66748,94.45227,92.6239,93.33301,90.07336,79.643745,89.53326,88.29399,94.26426,86.904144,91.1628]
y[2]=[44.3229166666667,43.125,41.7395833333333,41.1458333333333,44.1458333333333,44.1979166666667,43.3541666666667,42.75,40.625,42.1875,42.0625,42.5625,41.6875,41.0729166666667,42.3333333333333,42.0833333333333,40.8229166666667,41.2395833333333,42.3229166666667,41.53125,41.4375,40.6770833333333,43.0416666666667,44.1145833333333,42.71875,43.5625,41.9375,42.2708333333333,43.9791666666667,41.7916666666667,44.71875,42.09375,44,42.8541666666667,43.1770833333333,41.5625,42.2916666666667,41.9270833333333,43.7083333333333,43.625,40.9375,42.0104166666667,42.2291666666667,41.9166666666667,41.0520833333333,44.6354166666667,44.0104166666667,42.4166666666667,43.3125,43.8541666666667,40.0625,44.0625,41.4166666666667,41.625,43.40625,44.2708333333333,42.9895833333333,43.5,44.625,45.6875,43.21875,43.7291666666667,41.8854166666667,41.9479166666667,40.1979166666667,41.3645833333333,43.6458333333333,44.4375,43.0729166666667,45.7395833333333,45,43.1041666666667,40.8854166666667,41.1875,41.78125,42.28125,42.6979166666667,43.8541666666667,42.5833333333333,42.0520833333333,44.2604166666667,44.7604166666667,41.2395833333333,41.4583333333333,43.40625,43.2291666666667,42.2395833333333,41.5833333333333,41.34375,41.21875,43.9166666666667,39.40625,44.5208333333333,41.3541666666667,39.09375,41.4375,40.6979166666667,40.0520833333333,43.75,41.46875]
z[2]=[44.7202869433665,43.4283463615969,43.3957179333081,42.3218734564424,44.2545587877167,45.0592864619023,44.437888860675,42.9765733783516,41.5302529604404,42.8837681631031,43.8131851890624,43.8084789080202,43.4872837021994,41.8288274547576,42.5987542101078,42.3624628589053,42.0180396353385,42.3218416353516,44.0152980865589,41.9606591373309,43.2691828533905,41.5735643584496,43.3821057539623,45.9772323078113,44.4346726511514,44.8734751640107,43.0969050389484,43.3802041404926,45.7437775537637,42.5972007197441,45.8664656307573,43.4616854796501,44.6230373184656,44.4491921450671,44.9518405722644,43.0622200873085,42.9405442920316,42.734219444058,45.0542292596752,45.3360766446547,41.9365190107309,42.4442235231515,43.9018752525423,43.3155685751939,42.2301041112011,45.0459095801859,45.502810783134,44.3057373181762,44.7831431621424,44.9569128319968,41.5108299100327,44.9445117675046,41.5971847089358,42.9052675987585,44.6440932631663,44.8914965876344,44.3457329843656,43.6908046041545,44.6648219815435,46.5714566001385,43.3531532514548,44.5739256708892,42.3677506226161,43.6852150343247,41.0562682199847,41.9128530343424,43.7345414323293,45.9154007993641,44.1092718568215,47.3985418170814,45.1999505366893,43.369219549892,42.23681626296,41.9410511100342,41.9404948353853,44.2166894658037,43.039088892867,45.1166060761509,43.6749037686193,43.2374723113277,45.7634607091819,45.858038192921,41.8760002631788,42.9888612950739,44.1909646956029,43.455039740247,42.9635416735724,42.1564727501421,43.2192241712366,41.7858392284183,45.7496254097014,41.0011397815708,44.5390306048436,41.6287415050361,40.0125852306166,42.2303967261763,42.2162227128853,40.5363029341483,44.1806231665676,42.2857886281768]

#4
x[3]=[110.69017,110.1805,109.47394,109.01528,108.14613,106.07309,104.86102,102.34796,100.583786,96.86296,93.50258,92.88942,94.91066,95.17127,93.96268,92.81601,91.98505,95.345924,91.116264,94.84429,91.320984,95.494774,91.38622,96.34169,91.21134,89.39113,93.24855,94.35901,95.179245,92.997025,90.15904,92.42455,89.39453,88.82382,92.16325,93.001236,91.66445,87.3214,93.06122,89.936905,95.70648,92.61143,92.4448,88.408554,90.9391,95.18737,93.69319,88.04985,93.26577,89.57489,92.18164,94.004456,90.445404,89.19296,86.255135,92.97566,93.191284,87.0132,92.064285,85.3795,91.187004,88.86075,85.4522,89.82741,85.77698,88.00006,90.10144,92.23855,89.304474,91.608215,91.83937,87.17229,84.72356,87.58544,92.56839,90.42741,90.78165,90.425995,85.728386,88.852646,85.07978,90.35647,92.68637,89.29379,89.14839,89.32566,86.52386,90.17386,86.49967,85.4332,83.346466,85.62286,91.62662,88.76579,91.69469,90.76315,94.416016,93.62213,88.85315,90.32262]
y[3]=[42.375,43.8958333333333,43.3333333333333,42.84375,43.21875,44.7916666666667,43.1770833333333,42.8645833333333,44.3020833333333,46.2708333333333,41.6770833333333,42.09375,42.5208333333333,42.7604166666667,42.8229166666667,41.96875,45.2395833333333,45.5729166666667,42.8333333333333,42.8958333333333,42.0625,43.75,44.9791666666667,43.2083333333333,40.96875,43.9270833333333,44.6041666666667,44.4583333333333,41.90625,42.9166666666667,43.2708333333333,43.3645833333333,43.1458333333333,42.4583333333333,43.1666666666667,42.2395833333333,44,42.2708333333333,41.8020833333333,46.0833333333333,43.40625,42.78125,43.0625,45.84375,41.8958333333333,42.0104166666667,44.28125,44.5416666666667,40.0208333333333,43.8854166666667,39.8229166666667,43.46875,38.3645833333333,42.2395833333333,44.75,42.4583333333333,43.2291666666667,42.84375,43.75,43.4791666666667,41.7604166666667,44.4479166666667,41.4270833333333,42.5,45.40625,41.65625,41.8541666666667,38.03125,43.8125,40.9791666666667,41.15625,43.7395833333333,43.7395833333333,43.0104166666667,40.90625,44.6979166666667,44.53125,44.5833333333333,43.875,42.6041666666667,43.2291666666667,41.40625,44.3125,42.0833333333333,43.8645833333333,42.96875,42.7395833333333,42.4895833333333,43.3333333333333,43.3125,40.2395833333333,42.0104166666667,42.0104166666667,41.6770833333333,41.9895833333333,40.3020833333333,44.875,44.1458333333333,44.9375,42.46875]
z[3]=[44.3149276690136,44.232821859973,43.6651706457979,44.4802763964458,44.7568101749804,45.3952638445505,44.4977589947225,43.4928589264915,45.9206386528138,47.1999924993001,43.506287481649,43.2233783854866,42.817898946941,44.5713112183328,43.2517938732158,42.1693022425107,45.2883197605042,46.8128066633594,44.3595541732181,44.5191645671191,42.4516200919778,44.5608904200176,46.8295696068482,44.8362671680252,41.7045807615458,44.2975758275006,44.7945010840995,45.9096069260783,43.1513814794107,44.4101257794242,44.9645901131498,43.5435741817855,44.6929611466813,43.7527474800283,45.1000150722077,43.93807851506,45.1119444308395,43.4486466421307,41.8331166893833,48.016157189713,43.7408220923651,43.3756482289491,43.4669740849676,46.4145214270254,43.5520293714416,43.7748687986739,45.7383884901474,45.3829967482211,40.2533857011276,44.5088462209304,41.6044137697425,44.6512541825237,38.5814867124671,42.4210638991464,46.5900418794062,43.6660751520783,44.2509823868044,43.0945438720374,43.9055931967526,44.0786631755082,42.1384651855418,45.2899459523806,41.6082895677574,43.9314758761129,47.3214188853901,41.7196033625597,42.5207690187419,39.980462946011,44.6186586509528,41.7937466250036,43.0518594491852,45.5095553874744,43.7897635666067,44.578135281216,41.4159017066164,46.3611077321905,44.6069868481668,46.1677338297035,45.2732505621417,42.9115903867958,43.8669434499182,42.1145041161204,44.7690251138138,42.5291744601072,43.9740940675051,44.7186825372471,43.5185968625043,43.8686447628483,44.7321588151744,44.1396590422611,40.2586932755613,43.3659282592127,42.4022127973919,43.2153469683886,42.3225450455349,41.286395125831,45.6978074705633,44.1564650525177,45.0950874992392,43.3561515240023]

#5
x[4]=[111.20932,107.95475,90.49347,90.78822,97.2444,93.07074,90.234116,92.91953,96.58745,92.88783,93.80832,89.74263,91.130264,94.33232,96.6927,97.53424,94.41931,97.03146,95.47928,96.530594,94.691284,88.33983,92.26243,88.990295,88.24577,92.9728,86.94634,88.50588,93.78171,98.281425,91.80436,96.59096,95.84117,92.11803,91.96629,91.568146,93.98534,90.101974,80.68161,90.90794,88.931076,89.46132,90.34205,90.504326,89.93941,95.17085,93.17387,95.4337,93.708954,91.9303,89.592026,92.46715,93.384575,94.58543,89.69487,94.812744,91.03836,87.99623,89.70386,94.325356,94.128815,91.88251,94.834564,92.57817,89.65976,89.45387,90.48552,86.50901,93.52191,87.16214,93.4845,97.426575,96.58777,95.49968,94.265854,89.697174,96.85205,91.134186,89.267456,92.66751,98.64934,89.53798,94.903915,91.58966,91.59962,94.889694,93.81727,90.07829,88.465675,95.9463,90.49216,87.83376,89.700935,92.65811,93.049255,93.30132,89.81769,95.22212,87.38684,89.884735]
y[4]=[44.1770833333333,43.75,44.125,43.1354166666667,45.1041666666667,43.15625,41.3229166666667,43.8854166666667,41.7916666666667,42.65625,45.03125,43.3229166666667,42.3541666666667,43.9791666666667,44.34375,42.40625,46.5625,41.40625,42.1354166666667,43.0833333333333,45.09375,44.4166666666667,43.5833333333333,44.3541666666667,44.59375,41.7604166666667,42.09375,42.5,44.2291666666667,44.0416666666667,41.1041666666667,41.2708333333333,43.4791666666667,42.8125,40.7916666666667,46.8229166666667,43.6041666666667,42.8541666666667,44.28125,41.4583333333333,44.6979166666667,44.2395833333333,44.2395833333333,44.0625,43.1458333333333,42.3645833333333,42.75,42.4583333333333,43.3229166666667,45.3645833333333,43.9479166666667,43.7395833333333,42.2395833333333,43.3333333333333,43.9895833333333,43.0520833333333,41.28125,44.0104166666667,42.25,42.6979166666667,43.0208333333333,44.6666666666667,43.6145833333333,42.9791666666667,41.5,42.3020833333333,44.2291666666667,43.2291666666667,45.7291666666667,40.90625,43.40625,42.9166666666667,43.4270833333333,43.15625,44.8125,43.2708333333333,43.28125,42.2708333333333,43.15625,44.2083333333333,43.125,41.1979166666667,43.15625,42.1458333333333,42.46875,42.3229166666667,44.1041666666667,41.3333333333333,42.9479166666667,40.71875,42.1145833333333,40.9270833333333,42.8958333333333,44.4166666666667,40.9791666666667,43.1979166666667,46.2395833333333,39.875,44.7916666666667,45.625]
z[4]=[45.5576575256345,44.9770669349723,45.7787073737913,45.0992843758304,46.6703882744544,43.1821810030627,42.0183206902034,45.7240940511055,41.8624663267551,42.7997515564899,45.7895799326491,43.7845789449621,42.8517439222771,45.7289846236376,45.7727147365622,43.1367649371957,48.0647468136185,41.5212750039074,42.3049368621741,43.8217738206533,46.5321202523074,45.5977618586599,44.3901699867575,44.8617669260965,44.7841434048272,41.9696188735704,42.0938609920838,44.0480543581736,45.3561548240401,44.7875720237679,41.935702138772,42.1058839942661,43.9863913497295,43.3074640269526,42.7771909435475,47.2306346182675,43.8611627579382,44.3630088715646,44.7166893961155,41.856243494175,44.918350920133,44.6430500171382,44.479715931001,44.7225048253619,43.2091094570984,44.162929298273,43.1193835568092,44.3388463815459,44.5456668521554,47.344057561073,44.590301342392,45.048137453899,43.9556029720688,44.3393313825353,45.5185158155882,43.15554547463,42.7806092256862,44.0960435184514,42.7667850969383,42.7821728143628,44.9101494723958,45.0431601459279,44.6539897281629,43.9115370278175,43.2941240153096,44.0773530675734,44.3049910940802,43.4144917233877,47.6798470053938,41.2196872995909,43.8930136208938,44.6680290417538,44.021024244351,44.7663876594974,46.3190729963805,43.3544397799638,44.0014892202536,42.9583752853886,44.5920891147679,45.725732888116,43.2200858993009,41.9819704172237,44.1235614122262,43.2090725983485,44.3298275117451,43.8735765855715,45.4632370433184,43.0308597140423,44.4441111551214,41.2341773246536,42.92149423186,42.8537608505925,44.5583441983376,45.293091367932,42.7200598469677,44.2622246003666,48.209482065994,40.6855288929681,45.2055864958225,45.9039642724274]

#6
x[5]=[55.424572,54.982544,54.519936,54.09685,53.42336,52.43547,51.267204,49.315567,47.42028,45.344925,45.373005,42.287483,40.456047,41.994217,41.448986,43.621902,42.596703,42.711304,43.665787,40.965534,42.005707,45.22668,44.918564,43.81123,40.178677,39.85341,42.419647,42.187603,39.194664,41.13075,40.283775,45.82704,42.97547,42.96257,41.03932,42.86949,41.421516,43.531578,43.53755,40.73854,41.07377,45.217796,43.142113,43.5607,42.222206,42.468266,44.5075,42.649597,42.210728,41.554375,41.05185,43.436172,42.529015,42.550694,41.152275,45.49884,43.095295,41.17367,41.12123,43.809464,42.85617,41.798042,43.345478,41.63986,43.973377,40.626045,42.623844,42.445858,42.797585,40.686924,41.210186,42.8605,41.30522,43.139904,42.81299,43.10598,44.504112,38.63012,43.64263,44.33552,43.408707,43.83982,41.889206,45.068985,42.691982,43.80712,42.837296,40.753365,43.27206,43.415398,41.9384,43.099625,41.46867,42.70356,42.08908,44.58658,39.711243,41.57855,43.96022,42.96718]
y[5]=[17.1666666666667,17.9270833333333,17.9166666666667,17.5416666666667,18.4166666666667,18.5,18.0104166666667,17.4166666666667,18.4479166666667,17.28125,17.3125,18.1145833333333,17.2395833333333,17.4791666666667,17.9166666666667,17.0104166666667,17.8958333333333,17.5520833333333,17.3333333333333,17.5833333333333,18.4791666666667,18.3020833333333,16.1979166666667,18.1041666666667,18.3958333333333,17.5416666666667,18.3854166666667,17.5625,17.1979166666667,18.75,18.1354166666667,18.7291666666667,18.2395833333333,18.8333333333333,17.59375,17.59375,18.0416666666667,17.9583333333333,17.15625,17.9583333333333,17.5729166666667,18.0520833333333,18.6979166666667,18.21875,17.8333333333333,18.8333333333333,18.0208333333333,18.125,17.8333333333333,17.6979166666667,17.1979166666667,17.2083333333333,17.5208333333333,16.71875,17.2395833333333,17.5729166666667,18.6875,17.1875,17.21875,17.4270833333333,18.1145833333333,18.0520833333333,17.2291666666667,17.2708333333333,17.6041666666667,17.1041666666667,18.0833333333333,16.90625,18.1354166666667,18.0104166666667,18.1458333333333,18.1354166666667,17.5208333333333,17.7708333333333,17.2291666666667,17.1979166666667,18.0520833333333,16.3125,17.2395833333333,18.0104166666667,17.59375,17.9166666666667,17.40625,17.21875,17.1770833333333,17.84375,17.9791666666667,17.0416666666667,18.2395833333333,17.7395833333333,17.1875,16.6875,16.8645833333333,16.65625,18.2708333333333,18.1354166666667,17.5104166666667,17.8125,17.8854166666667,17.03125]
z[5]=[18.8935835025579,18.1091997353566,18.2452165517642,19.3699392005753,18.8838595922765,19.638840417663,19.570575222041,18.1997284246158,18.920809583782,17.9073277519122,17.3821915485715,18.2440220565191,18.1355753316419,17.7695942943384,19.8769810904007,18.8384913779857,19.8497520991332,18.7252360129934,18.5045312178329,19.4696760031991,20.1070065386652,18.7969978752014,17.3879915190791,19.9581369698764,19.3272560538267,17.5660702117508,19.9795853603032,18.7445815783735,17.2687107241273,20.7310449697306,19.6913405157533,20.6670675675028,18.292740080161,19.5199754217785,18.5539513706788,19.0871972218301,19.5305354830775,18.376537947471,18.6812060154832,18.4663839573676,18.0633356456709,18.5845193496072,18.7812031949211,19.8635796539415,19.1005368247963,19.646056632464,19.5646383602298,19.4185886639439,18.7380574926125,18.0224784614937,18.617911161182,17.9945814016352,19.211430117263,16.9062843894353,17.3726755039289,19.5179800609433,19.7611367200096,19.1711641376693,17.8323709442111,19.1501020740612,19.0866373552378,18.1219092995688,18.1790238267999,17.5117608069792,19.409445946986,17.5945932098551,19.7578931191184,17.3085745654127,18.7434887839433,18.50069590279,18.7265598154835,19.4160673166808,18.089483063618,19.0695160361522,17.6143140788599,18.653907544925,19.5943923335069,16.6769047599902,18.2889743351577,18.8002372571054,17.8745249394802,18.3065216582517,18.435158608823,17.3911085714122,17.4376615300028,18.0615030518488,18.5571997700375,17.5119514292664,19.6205284807431,18.2703280385752,17.3475969227369,18.1243815069498,17.5921231985001,17.1063026032904,20.0178566714586,18.2226152536568,18.5700649245128,19.5419594627897,18.6799154356846,18.8216996960478]


bins = numpy.linspace(15, 60, 100)
pyplot.xlabel("Loss")
pyplot.hist(y[int(sys.argv[1])], bins, alpha=0.7, label='Testing with Same Size')
pyplot.hist(x[int(sys.argv[1])], bins, alpha=0.7, label='Training')
pyplot.hist(z[int(sys.argv[1])], bins, alpha=0.7, label='Testing with Different Size')
pyplot.legend(loc='upper right')
pyplot.show()
