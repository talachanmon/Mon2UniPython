# -*- coding: utf-8 -*-
# Converted to python code from javascript code at 
# http://paragu.parabaik.info
# This code licensed under the GPL Version 3.0 license
# This code has a few difference between paragu vesion.
# Some code that we do not understand has been skipped.
# Fixed logic error in Kinzi conversion
# Simplied the complex re-ordering script into smaller ones
# If it does not work well please write to ravi.chhabra@Geeeeemail.com
# Update Mon Character on this script to convert Mon.ttf to uni 6.0 Converter, By talachanmon@gmail.com if have problem let me know.

import re
import html_entity2utf8
#@param utf8 Mon string as the source
#@return utf8 unicode string as the output
def convert(input):
    output = input

    #Mon Sign
    tallAA = u'\u102B'
    AA = u'\u102C'
    vi = u'\u102D'
    #up-media    
    ii = u'\u102E'
    u = u'\u102F'
    uu = u'\u1030'
    ve = u'\u1031'
    ai = u'\u1032'
    ans = u'\u1036'
    db = u'\u1037'
    visarga = u'\u1038'
    asat = u'\u103A'
    ya = u'\u103B'
    ra = u'\u103C'
    zero = u'\u1040'
    # Mon consonant
    bba = u'\u105C'
    bbe = u'\u105D'
    Me = u'\u1028'
    kwatHa = u'\u103E'
    kwatna = u'\u105E'
    myie = u'\1035'
    kwatBBA = u'\u1039\u105C'
    kwatWa = u'\u103D'
    Pole = u'\u102D\u1032'
    Aao = u'\u1029'
    output = html_entity2utf8.unescape(output)
    
    # Mon reorder
    output =  output.replace( u'\u106A', u'\u1009') # ဨ။
    output = re.sub( u'\u1025(?=[\u1039\u102C])',u'\u1009',output)
    output =  output.replace( u'\u1025\u102E', u'\u1026')
    output =  output.replace( u'\u106B', u'\u100A')
    output =  output.replace( u'\u1090', u'\u101B')
    output =  output.replace( u'\u1040', zero)
    output =  output.replace( u'\u108F', u'\u1014')
    output =  output.replace( u'\u1012', u'\u1012')
    #
    output =  output.replace( u'\u105E', u'\u1039\u105C')
    output =  output.replace( u'\u103E', u'\u105E')
    output =  output.replace( u'\u103D', u'\u103E')
    output =  output.replace( u'\u103C', u'\u103D')
    output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]',ra,output)
    output =  re.sub( u'(\u103C)([\u1000-\u1021\u105A-\u105D])(\u1039[\u1000-\u1021\u105A\u105C]).',u"\\2\\3\\1",output)
    output =  output.replace( u'\u1007\u103A', u'\u105B')
    output = re.sub(u'[\u103A\u107D]',ya,output)
    output =  output.replace( u'\u1039', u'\u103A')
    
   # output =  output.replace( /(\u1031)?(\u103C)?([\u1000-\u1021])\u1064/g, "\u1064$1$2$3");
    output = re.sub(u'(\u1031|)(\u103C|)([\u1000-\u1021])\u1064',u"\u1064\\1\\2\\3",output)
   
   ## reordering kinzi
   #output =  output.replace( /(\u1031)?(\u103C)?([\u1000-\u1021])\u108B/g, "\u1064$1$2$3\u102D");
    output = re.sub(u'(\u1031)?(\u103C)?([\u1000-\u1021])\u108B',u"\u1064\\1\\2\\3\u102D",output)

   ## reordering kinzi lgt
   #output =  output.replace( /(\u1031)?(\u103C)?([\u1000-\u1021])\u108C/g, "\u1064$1$2$3\u102E");
    output = re.sub(u'(\u1031)?(\u103C)?([\u1000-\u1021])\u108C',u"\u1064\\1\\2\\3\u102E",output)
   
   ## reordering kinzi lgtsk
   #output =  output.replace( /(\u1031)?(\u103C)?([\u1000-\u1021])\u108D/g, "\u1064$1$2$3\u1036");
    output = re.sub(u'(\u1031)?(\u103C)?([\u1000-\u1021])\u108D',u"\u1064\\1\\2\\3\u1036",output)
   ## reordering kinzi AII Mon 
   #output =  output.replace( /(\u1031)?(\u103C)?([\u1000-\u1021])\u109A/g, "\u1064$1$2$3\u1033");
   #output = re.sub(u'(\u1031)?(\u103C)?([\u1000-\u1022\u1050])\u109A',u"\u1064\\1\\2\\3\u1098",output) #code not working ၚ်္ဳ  still problem
   ## reordering kinzi ttt
   ##############
    output =  output.replace( u'\u105A', tallAA + asat)
    output =  output.replace( u'\u108E', vi + ans)
    output =  output.replace( u'\u1033', u)
    output =  output.replace( u'\u1034', uu)
    output =  output.replace( u'\u1064', u'\u1004\u103A\u1039')
    output =  output.replace( u'\u104E', u'\u104E\u1004\u103A\u1038')
    output =  output.replace( u'\u1060', u'\u1039\u1000')
    output =  output.replace( u'\u1061', u'\u1039\u1001')
    output =  output.replace( u'\u1062', u'\u1039\u1002')
    output =  output.replace( u'\u1063', u'\u1039\u1003')
    output =  output.replace( u'\u1065', u'\u1039\u1005')
    output =  re.sub( u'[\u1066\u1067]',u'\u1039\u1006',output)
    output =  output.replace( u'\u1068', u'\u1039\u1007')
    output =  output.replace( u'\u1069', u'\u1039\u1008')
    output =  output.replace( u'\u106C', u'\u1039\u100B') # Mon.ttf from Linux type Mon keyboad. wrong keycode (္ဋ=္ဍ)။ 
    output =  output.replace( u'\u1070', u'\u1039\u100F')
    output = re.sub(u'[\u1071\u1072]',u'\u1039\u1010',output)
    output = re.sub(u'[\u1073\u1074]',u'\u1039\u1011',output)
    output =  output.replace( u'\u1075', u'\u1039\u1012')
    output =  output.replace( u'\u1076', u'\u1039\u1013')
    output =  output.replace( u'\u1077', u'\u1039\u1014')
    output =  output.replace( u'\u1078', u'\u1039\u1015')
    output =  output.replace( u'\u1079', u'\u1039\u1016')
    output =  output.replace( u'\u107A', u'\u1039\u1017')
    output =  output.replace( u'\u107B', u'\u1039\u1018')
    output =  output.replace( u'\u107C', u'\u1039\u1019')
    output =  output.replace( u'\u1085', u'\u1039\u101C')
    output =  output.replace( u'\u106D', u'\u1039\u100C')
    output =  output.replace( u'\u1091', u'\u100F\u1039\u100D')
    output =  output.replace( u'\u1092', u'\u100B\u1039\u100C')
    output =  output.replace( u'\u1097', u'\u100B\u1039\u100B')
    output =  output.replace( u'\u106F', u'\u100E\u1039\u100D')
    output =  output.replace( u'\u106E', u'\u100D\u1039\u100D')
    #Mon Some Reorder
    output =  output.replace( u'\u1004\u105B', u'\u105A')
    output =  output.replace( u'\u105B', u'\u1039\u105A')
    output =  output.replace( u'\u105C', u'\u1060')
    output =  output.replace( u'\u1050', u'\u105C')
    output =  output.replace( u'\u1022', u'\u105D')
    output =  output.replace( u'\u103F', u'\u105F')
    output =  output.replace( u'\u1086', u'\u103F')
    output =  output.replace( u'\u1035', u'\u1034')
    output =  output.replace( u'\u1098', u'\u1033')
    output =  output.replace( u'\u109D', u'\u1035')
    output =  output.replace( u'\u109B', u'\u1039\u100A')
    output =  output.replace( u'\u109C', u'\u1039\u100D')
    output =  output.replace( u'\u1099', u'\u102D\u1032')
    output =  output.replace( u'\u103A\u1060', u'\u1039\u105C')
    output =  output.replace( u'\u1088', u'\u103E\u102F')
    output =  output.replace( u'\u1099', Pole)
    output =  output.replace( u'\u103E\u103B', ya + kwatHa)
    #
    #output = output.replace(/(([\u1000-\u101C\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F]))(\u1040)(?=\u0020)?/g, function($0, $1)
   #{
   #   return $1 ? $1 + '\u101D' : $0 + $1;

   #}
   #);

    output = re.sub(u'(([\u1000-\u101C\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F\u1050\u1022]))(\u1040)',u'\\1\u101D',output)
   # zero and wa
   
   ## Skipping to Rewrite
       # ဘာမှန်းမသိလို့ ချန်ထားလိုက်သည်
   # output = output.replace(/((\u101D))(\u1040)(?=\u0020)?/g, function($0, $1)
   #{
   #   return $1 ? $1 + '\u101D' : $0 + $1;

   #}
   #);
   # zero and wa

   #output = output.replace(/(([\u1000-\u101C\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F\u0020]))(\u1047)/g, function($0, $1)
   #{
 #     return $1 ? $1 + '\u101B' : $0 + $1;

   #}
#   );
   # seven and ra
    output = re.sub(u'([\u1000-\u101C\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F\u0020\u1050\u1022])(\u1047)',u"\\1\u101B",output)

   #output =  output.replace( /(\u1047)( ? = [\u1000 - \u101C\u101E - \u102A\u102C\u102E - \u103F\u104C - \u109F\u0020])/g, "\u101B");
    output = re.sub(u'(\u1047)([\u1000-\u101C\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F\u0020])',u'\u101B\\2',output)
   # seven and ra
 #  // reordering storage order
   # Python RegEx not on par with holy grail of RegEx (Perl). ? lazy matching throws a NULL instead empty string!
    #output = output.replace ( /(\u1031)?([\u1000-\u1021\u105A\-\u105D])(\u1039[\u1000-\u1021\u105A\u105C])?([\u102D\u102E\u1032\u1033\u1034\u1035])?([\u1036\u1037\u1038]{0,2})([\u103B-\u103C]{0,3})([\u102F\u1030])?([\u1036\u1037\u1038]{0,2})([\u102D\u102E\u1032])?/g, "$2$3$6$1$4$9$7$5$8");
    #output =  re.sub(u'(\u1031)?([\u1000-\u1021])(\u1039[\u1000-\u1021])?([\u102D\u102E\u1032])?([\u1036\u1037\u1038]{0,2})([\u103B-\u103E]{0,3})([\u102F\u1030])?([\u1036\u1037\u1038]{0,2})([\u102D\u102E\u1032])?', "\\2\\3\\6\\1\\4\\9\\7\\5\\8",output);
   # ရရစ် ပြောင်း
    output = re.sub(u'(\u103C)([\u1000-\u1021\u105A-\u105D])',u'\\2\u103C',output)
    # ယပင့် / ယရစ် ဝဆွဲ
    output = re.sub(u'(\u103D)([\u103B\u103C])',u"\\2\\1",output)
   # သဝေထိုး ပြောင်း
   
    output = re.sub(u'\u1031([\u1000-\u1021\u105A-\u105F\u1060])',u'\\1\u1031',output)
    output = output.replace(u'\u102F\u102D',u'\u102D\u102F')
    output = output.replace(u'\u1036\u103D',u'\u103D\u1036')
    output = output.replace(ans+u, u+ans);
    output = re.sub( u'(\u103A)(\u1037)', u"\\2\\1",output);
    output = output.replace(u'\u1007\u103A',u'\u1007\u103A')
    output =  output.replace( u'\u1004', u'\u105A')
    output = re.sub(u'(\u103A)(\u1037)',u"\\2\\1",output)
    output = re.sub(u'(\u102F)(\u1035)',u"\\2\\1",output)
    output = re.sub(u'(\u1032)(\u102F)',u"\\2\\1",output)
    output = re.sub(u'(\u102F)(\u1033)',u"\\2\\1",output)
    output = re.sub(u'(\u102F)(\u102D)',u"\\2\\1",output)
    output = re.sub(u'(\u102F)(\u102E)',u"\\2\\1",output)
    output = re.sub(u'(\u102F)(\u1033)',u"\\2\\1",output)
    output = re.sub(u'(\u102F)(\u1035)',u"\\2\\1",output)
    output = re.sub(u'(\u1032)(\u103D)',u"\\2\\1",output)
    output = re.sub(u'(\u103A)(\u103E)',u"\\2\\1",output)

    #Pasint order human error
    output = re.sub(u'([\u1000-\u1060])([\u102B\u102C\u102D\u102E\u1032\u1035\u1036\u1039\u1089\u1098\u109D]){1,2}([\u103C\u1060\u1061\u1062\u1063\u105B\u105E\u1065\u1066\u1067\u1068\u1069\u1070\u1071\u1072\u1073\u1074\u1075\u1076\u1077\u1078\u1079\u107A\u107B\u107C\u1085])',u"\\1\\3\\2",output)
    #
    output =  re.sub( u'([\u102D\u102E\u1032-\u1036])([\u105E\u105F\u1060\u103D\u103E])', u"\\2\\1",output); # reorder (ဲိီဳ  ံ  ကဵု ၞၟ ၠ ှွ)။
    output =  re.sub( u'([\u102D\u102E\u1032-\u1035])(\u1039[\u1000-\u1021\u105A\u105C])', u"\\2\\1",output); # reorder (ဲိီဳ ကဵု ္ၚ္ည္ဍ္ွၜ)။   
    output =  re.sub( u'\u1031([\u103A\u103B-\u103E\u105E\u105F\u1060]+)',u'\\1\u1031',output) # Mon reorder စှ်ေ၊ သၞော် ကၠောၚ်။
    output =  re.sub( u'(\u1000-\u1021\u105A\u105C])(\u103E)(\u103A)(\u1031)', u"\\1\\2\\4\\3",output); #jaik
    output =  re.sub( u'\u1031(\u1039[\u1000-\u1021\u105A\u105C])', u"\\1\u1031",output); # # reorder (ဗ္ကေတ်ပ္ကေၚ်၊သက္ကေက်သက္ကာ)။
    output =  re.sub( u'(\u1000-\u1021\u105A\u105C])(\u103C)(\u105A\u103A\u1039)', u"\\3\\1\\2",output);
    output =  re.sub( u'\u1031([\u105B\u105D])', u"\\1\u1031",output);
    output = output.replace  ( u'\u102B\u102B', u'\u102B')
    output = output.replace  ( u'\u102C\u102C', u'\u102C')
    output = output.replace  ( u'\u102D\u102D', u'\u102D')
    output = output.replace  ( u'\u102E\u102E', u'\u102E')
    output = output.replace  ( u'\u102F\u102F', u'\u102F')
    output = output.replace  ( u'\u1030\u1030', u'\u1030')
    output = output.replace  ( u'\u1032\u1032', u'\u1032')
    output = output.replace  ( u'\u1033\u1033', u'\u1033')
    output = output.replace  ( u'\u1034\u1034', u'\u1034')
    output = output.replace  ( u'\u1035\u1035', u'\u1035')
    output = output.replace  ( u'\u1036\u1036', u'\u1036')
    output = output.replace  ( u'\u1038\u1038', u'\u1038')
    output = output.replace  ( u'\u103A\u103A', u'\u103A')
    output = output.replace  ( u'\u103B\u103B', u'\u103B')
    output = output.replace  ( u'\u103C\u103C', u'\u103C')
    output = output.replace  ( u'\u103D\u103D', u'\u103D')
    output = output.replace  ( u'\u103E\u103E', u'\u103E')
    output = output.replace  ( u'\u1039\u105A\u1039\u105A', u'\u1039\u105A')
    output = output.replace  ( u'\u105E\u105E', u'\u105E')
    output = output.replace  ( u'\u105F\u105F', u'\u105F')
    output = output.replace  ( u'\u1060\u1060', u'\u1060')
    output = output.replace ( u'\u0020\u102D', u'\u102D') 
    output = output.replace ( u'\u0020\u102E', u'\u102E') 
    output = output.replace ( u'\u0020\u102F', u'\u102F') 
    output = output.replace ( u'\u0020\u1030', u'\u1030') 
    output = output.replace ( u'\u0020\u1032', u'\u1032') 
    output = output.replace ( u'\u0020\u1033', u'\u1033') 
    output = output.replace ( u'\u0020\u1034', u'\u1034') 
    output = output.replace ( u'\u0020\u1035', u'\u1035') 
    output = output.replace ( u'\u0020\u1036', u'\u1036') 
    output = output.replace ( u'\u0020\u1038', u'\u1038') 
    output = output.replace ( u'\u0020\u103A', u'\u103A') 
    output = output.replace ( u'\u0020\u103D', u'\u103D') 
    output = output.replace ( u'\u0020\u103E', u'\u103E') 
    output = output.replace ( u'\u0020\u105E', u'\u105E') 
    output = output.replace ( u'\u0020\u105F', u'\u105F') 
    output = output.replace ( u'\u0020\u1060', u'\u1060')
    output = output.replace ( u'\u0032\u1032', u'\u1032')
    return output
