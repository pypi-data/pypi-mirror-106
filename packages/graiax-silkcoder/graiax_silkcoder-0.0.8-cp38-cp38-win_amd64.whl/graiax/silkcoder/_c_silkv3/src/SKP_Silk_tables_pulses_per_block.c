/***********************************************************************
Copyright (c) 2006-2012, Skype Limited. All rights reserved. 
Redistribution and use in source and binary forms, with or without 
modification, (subject to the limitations in the disclaimer below) 
are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright 
notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution.
- Neither the name of Skype Limited, nor the names of specific 
contributors, may be used to endorse or promote products derived from 
this software without specific prior written permission.
NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED 
BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND 
CONTRIBUTORS ''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF 
USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
***********************************************************************/

#include "SKP_Silk_tables.h"

const SKP_int SKP_Silk_max_pulses_table[ 4 ] = {
         6,      8,     12,     18
};

const SKP_uint16 SKP_Silk_pulses_per_block_CDF[ 10 ][ 21 ] = 
{
{
         0,  47113,  61501,  64590,  65125,  65277,  65352,  65407,
     65450,  65474,  65488,  65501,  65508,  65514,  65516,  65520,
     65521,  65523,  65524,  65526,  65535
},
{
         0,  26368,  47760,  58803,  63085,  64567,  65113,  65333,
     65424,  65474,  65498,  65511,  65517,  65520,  65523,  65525,
     65526,  65528,  65529,  65530,  65535
},
{
         0,   9601,  28014,  45877,  57210,  62560,  64611,  65260,
     65447,  65500,  65511,  65519,  65521,  65525,  65526,  65529,
     65530,  65531,  65532,  65534,  65535
},
{
         0,   3351,  12462,  25972,  39782,  50686,  57644,  61525,
     63521,  64506,  65009,  65255,  65375,  65441,  65471,  65488,
     65497,  65505,  65509,  65512,  65535
},
{
         0,    488,   2944,   9295,  19712,  32160,  43976,  53121,
     59144,  62518,  64213,  65016,  65346,  65470,  65511,  65515,
     65525,  65529,  65531,  65534,  65535
},
{
         0,  17013,  30405,  40812,  48142,  53466,  57166,  59845,
     61650,  62873,  63684,  64223,  64575,  64811,  64959,  65051,
     65111,  65143,  65165,  65183,  65535
},
{
         0,   2994,   8323,  15845,  24196,  32300,  39340,  45140,
     49813,  53474,  56349,  58518,  60167,  61397,  62313,  62969,
     63410,  63715,  63906,  64056,  65535
},
{
         0,     88,    721,   2795,   7542,  14888,  24420,  34593,
     43912,  51484,  56962,  60558,  62760,  64037,  64716,  65069,
     65262,  65358,  65398,  65420,  65535
},
{
         0,    287,    789,   2064,   4398,   8174,  13534,  20151,
     27347,  34533,  41295,  47242,  52070,  55772,  58458,  60381,
     61679,  62533,  63109,  63519,  65535
},
{
         0,      1,      3,     91,   4521,  14708,  28329,  41955,
     52116,  58375,  61729,  63534,  64459,  64924,  65092,  65164,
     65182,  65198,  65203,  65211,  65535
}
};

const SKP_int SKP_Silk_pulses_per_block_CDF_offset = 6;


const SKP_int16 SKP_Silk_pulses_per_block_BITS_Q6[ 9 ][ 20 ] = 
{
{
        30,    140,    282,    444,    560,    625,    654,    677,
       731,    780,    787,    844,    859,    960,    896,   1024,
       960,   1024,    960,    821
},
{
        84,    103,    164,    252,    350,    442,    526,    607,
       663,    731,    787,    859,    923,    923,    960,   1024,
       960,   1024,   1024,    875
},
{
       177,    117,    120,    162,    231,    320,    426,    541,
       657,    803,    832,    960,    896,   1024,    923,   1024,
      1024,   1024,    960,   1024
},
{
       275,    182,    146,    144,    166,    207,    261,    322,
       388,    450,    516,    582,    637,    710,    762,    821,
       832,    896,    923,    734
},
{
       452,    303,    216,    170,    153,    158,    182,    220,
       274,    337,    406,    489,    579,    681,    896,    811,
       896,    960,    923,   1024
},
{
       125,    147,    170,    202,    232,    265,    295,    332,
       368,    406,    443,    483,    520,    563,    606,    646,
       704,    739,    757,    483
},
{
       285,    232,    200,    190,    193,    206,    224,    244,
       266,    289,    315,    340,    367,    394,    425,    462,
       496,    539,    561,    350
},
{
       611,    428,    319,    242,    202,    178,    172,    180,
       199,    229,    268,    313,    364,    422,    482,    538,
       603,    683,    739,    586
},
{
       501,    450,    364,    308,    264,    231,    212,    204,
       204,    210,    222,    241,    265,    295,    326,    362,
       401,    437,    469,    321
}
};

const SKP_uint16 SKP_Silk_rate_levels_CDF[ 2 ][ 10 ] = 
{
{
         0,   2005,  12717,  20281,  31328,  36234,  45816,  57753,
     63104,  65535
},
{
         0,   8553,  23489,  36031,  46295,  53519,  56519,  59151,
     64185,  65535
}
};

const SKP_int SKP_Silk_rate_levels_CDF_offset = 4;


const SKP_int16 SKP_Silk_rate_levels_BITS_Q6[ 2 ][ 9 ] = 
{
{
       322,    167,    199,    164,    239,    178,    157,    231,
       304
},
{
       188,    137,    153,    171,    204,    285,    297,    237,
       358
}
};

const SKP_uint16 SKP_Silk_shell_code_table0[ 33 ] = {
         0,  32748,  65535,      0,   9505,  56230,  65535,      0,
      4093,  32204,  61720,  65535,      0,   2285,  16207,  48750,
     63424,  65535,      0,   1709,   9446,  32026,  55752,  63876,
     65535,      0,   1623,   6986,  21845,  45381,  59147,  64186,
     65535
};

const SKP_uint16 SKP_Silk_shell_code_table1[ 52 ] = {
         0,  32691,  65535,      0,  12782,  52752,  65535,      0,
      4847,  32665,  60899,  65535,      0,   2500,  17305,  47989,
     63369,  65535,      0,   1843,  10329,  32419,  55433,  64277,
     65535,      0,   1485,   7062,  21465,  43414,  59079,  64623,
     65535,      0,      0,   4841,  14797,  31799,  49667,  61309,
     65535,  65535,      0,      0,      0,   8032,  21695,  41078,
     56317,  65535,  65535,  65535
};

const SKP_uint16 SKP_Silk_shell_code_table2[ 102 ] = {
         0,  32615,  65535,      0,  14447,  50912,  65535,      0,
      6301,  32587,  59361,  65535,      0,   3038,  18640,  46809,
     62852,  65535,      0,   1746,  10524,  32509,  55273,  64278,
     65535,      0,   1234,   6360,  21259,  43712,  59651,  64805,
     65535,      0,   1020,   4461,  14030,  32286,  51249,  61904,
     65100,  65535,      0,    851,   3435,  10006,  23241,  40797,
     55444,  63009,  65252,  65535,      0,      0,   2075,   7137,
     17119,  31499,  46982,  58723,  63976,  65535,  65535,      0,
         0,      0,   3820,  11572,  23038,  37789,  51969,  61243,
     65535,  65535,  65535,      0,      0,      0,      0,   6882,
     16828,  30444,  44844,  57365,  65535,  65535,  65535,  65535,
         0,      0,      0,      0,      0,  10093,  22963,  38779,
     54426,  65535,  65535,  65535,  65535,  65535
};

const SKP_uint16 SKP_Silk_shell_code_table3[ 207 ] = {
         0,  32324,  65535,      0,  15328,  49505,  65535,      0,
      7474,  32344,  57955,  65535,      0,   3944,  19450,  45364,
     61873,  65535,      0,   2338,  11698,  32435,  53915,  63734,
     65535,      0,   1506,   7074,  21778,  42972,  58861,  64590,
     65535,      0,   1027,   4490,  14383,  32264,  50980,  61712,
     65043,  65535,      0,    760,   3022,   9696,  23264,  41465,
     56181,  63253,  65251,  65535,      0,    579,   2256,   6873,
     16661,  31951,  48250,  59403,  64198,  65360,  65535,      0,
       464,   1783,   5181,  12269,  24247,  39877,  53490,  61502,
     64591,  65410,  65535,      0,    366,   1332,   3880,   9273,
     18585,  32014,  45928,  56659,  62616,  64899,  65483,  65535,
         0,    286,   1065,   3089,   6969,  14148,  24859,  38274,
     50715,  59078,  63448,  65091,  65481,  65535,      0,      0,
       482,   2010,   5302,  10408,  18988,  30698,  43634,  54233,
     60828,  64119,  65288,  65535,  65535,      0,      0,      0,
      1006,   3531,   7857,  14832,  24543,  36272,  47547,  56883,
     62327,  64746,  65535,  65535,  65535,      0,      0,      0,
         0,   1863,   4950,  10730,  19284,  29397,  41382,  52335,
     59755,  63834,  65535,  65535,  65535,  65535,      0,      0,
         0,      0,      0,   2513,   7290,  14487,  24275,  35312,
     46240,  55841,  62007,  65535,  65535,  65535,  65535,  65535,
         0,      0,      0,      0,      0,      0,   3606,   9573,
     18764,  28667,  40220,  51290,  59924,  65535,  65535,  65535,
     65535,  65535,  65535,      0,      0,      0,      0,      0,
         0,      0,   4879,  13091,  23376,  36061,  49395,  59315,
     65535,  65535,  65535,  65535,  65535,  65535,  65535
};

const SKP_uint16 SKP_Silk_shell_code_table_offsets[ 19 ] = {
         0,      0,      3,      7,     12,     18,     25,     33,
        42,     52,     63,     75,     88,    102,    117,    133,
       150,    168,    187
};

