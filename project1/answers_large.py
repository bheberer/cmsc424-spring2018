import datetime
from decimal import *

correctanswers = ["" for i in range(0, 11)]

correctanswers[1] = [('Helen Gonzalez                ',),('James Gonzalez                ',),('John Green                    ',),('Joseph Garcia                 ',),('Kevin Garcia                  ',),('Lisa Garcia                   ',),('Lisa Gonzalez                 ',),('Margaret Gonzalez             ',),('Mark Garcia                   ',),('Mark Gonzalez                 ',),('Michael Garcia                ',),('Michael Green                 ',),('Paul Green                    ',),('Ronald Green                  ',),('Sharon Garcia                 ',),('Susan Garcia                  ',)]

correctanswers[2] = [('cust23    ','Barbara Roberts               ',datetime.date(1972,8,12),'VX'),('cust53    ','Brian Moore                   ',datetime.date(1986,8,10),'SW'),('cust79    ','Charles Green                 ',datetime.date(1969,8,14),'F9'),('cust98    ','Christopher Collins           ',datetime.date(1995,8,4),'UA'),('cust111   ','Christopher Williams          ',datetime.date(1974,8,14),'DL'),('cust119   ','Daniel Martin                 ',datetime.date(1992,8,4),'AA'),('cust120   ','Daniel Martinez               ',datetime.date(1974,8,11),'AS'),('cust198   ','Dorothy Rodriguez             ',datetime.date(1969,8,3),'SW'),('cust207   ','Edward Jackson                ',datetime.date(1985,8,5),'AS'),('cust219   ','Edward Wilson                 ',datetime.date(1979,8,4),'B6'),('cust249   ','Helen Baker                   ',datetime.date(1976,8,15),'UA'),('cust348   ','Karen Martinez                ',datetime.date(1980,8,9),'DL'),('cust373   ','Kevin Harris                  ',datetime.date(1997,8,10),'SW'),('cust471   ','Maria Allen                   ',datetime.date(1973,8,7),'AS'),('cust474   ','Maria Carter                  ',datetime.date(1992,8,6),'B6'),('cust480   ','Maria Johnson                 ',datetime.date(1984,8,7),'NK'),('cust512   ','Mary Scott                    ',datetime.date(1985,8,8),'AA'),('cust535   ','Michelle Baker                ',datetime.date(1989,8,11),'VX'),('cust564   ','Patricia Johnson              ',datetime.date(1979,8,9),'SW'),('cust584   ','Paul Parker                   ',datetime.date(1980,8,11),'B6'),('cust600   ','Robert Baker                  ',datetime.date(1971,8,8),'SW'),('cust606   ','Robert Green                  ',datetime.date(1989,8,8),'AS'),('cust615   ','Robert Williams               ',datetime.date(1987,8,2),'F9'),('cust625   ','Ronald Moore                  ',datetime.date(1971,8,5),'NK'),('cust651   ','Sandra Allen                  ',datetime.date(1974,8,10),'B6'),('cust683   ','Sharon Thomas                 ',datetime.date(1979,8,7),'DL'),('cust717   ','Thomas Martin                 ',datetime.date(1969,8,6),'F9')]

correctanswers[3] = [('Atlanta             ','DL',7L),('Atlanta             ','AA',2L),('Atlanta             ','SW',2L),('Atlanta             ','AS',1L),('Atlanta             ','UA',1L),('Austin              ','SW',2L),('Austin              ','B6',1L),('Baltimore           ','F9',3L),('Baltimore           ','AA',2L),('Baltimore           ','DL',1L),('Baltimore           ','VX',1L),('Boston              ','SW',3L),('Boston              ','AS',1L),('Boston              ','DL',1L),('Charlotte           ','SW',3L),('Charlotte           ','AS',1L),('Charlotte           ','UA',1L),('Chicago             ','UA',6L),('Chicago             ','AA',1L),('Chicago             ','F9',1L),('Chicago             ','SW',1L),('Cleveland           ','AA',1L),('Cleveland           ','AS',1L),('Cleveland           ','VX',1L),('Dallas-Fort Worth   ','AA',11L),('Dallas-Fort Worth   ','SW',2L),('Dallas-Fort Worth   ','B6',1L),('Denver              ','F9',6L),('Denver              ','VX',2L),('Denver              ','AA',1L),('Detroit             ','SW',1L),('Detroit             ','UA',1L),('Fort Lauderdale     ','NK',3L),('Honolulu            ','AA',1L),('Houston             ','SW',3L),('Houston             ','NK',2L),('Houston             ','AA',1L),('Houston             ','B6',1L),('Houston             ','UA',1L),('Kansas City         ','B6',1L),('Kansas City         ','SW',1L),('Las Vegas           ','SW',3L),('Las Vegas           ','AA',1L),('Los Angeles         ','UA',2L),('Los Angeles         ','DL',1L),('Los Angeles         ','VX',1L),('Miami               ','AA',1L),('Miami               ','B6',1L),('Miami               ','UA',1L),('Minneapolis         ','AA',1L),('Minneapolis         ','DL',1L),('Minneapolis         ','VX',1L),('Nashville           ','AA',2L),('Nashville           ','SW',1L),('Newark              ','AA',2L),('Newark              ','SW',2L),('Newark              ','VX',1L),('New York            ','B6',5L),('New York            ','SW',3L),('New York            ','DL',2L),('New York            ','AA',1L),('New York            ','AS',1L),('New York            ','F9',1L),('Oakland             ','SW',23L),('Oakland             ','UA',1L),('Orlando             ','SW',1L),('Philadelphia        ','AS',1L),('Phoenix             ','AA',2L),('Phoenix             ','F9',1L),('Phoenix             ','NK',1L),('Phoenix             ','SW',1L),('Portland            ','AA',1L),('Portland            ','DL',1L),('Raleigh/Durham      ','SW',2L),('Raleigh/Durham      ','AA',1L),('Sacramento          ','AS',1L),('Sacramento          ','SW',1L),('Salt Lake City      ','AA',3L),('Salt Lake City      ','F9',2L),('Salt Lake City      ','SW',2L),('Salt Lake City      ','DL',1L),('San Diego           ','SW',1L),('San Francisco       ','VX',4L),('San Francisco       ','SW',2L),('San Francisco       ','UA',2L),('San Francisco       ','DL',1L),('Santa Ana           ','AA',1L),('Santa Ana           ','F9',1L),('Seattle             ','SW',2L),('Seattle             ','AS',1L),('Seattle             ','B6',1L),('Seattle             ','UA',1L),('St Louis            ','AA',2L),('St Louis            ','SW',2L),('St Louis            ','DL',1L),('St Louis            ','F9',1L),('Tampa               ','AA',1L),('Tampa               ','DL',1L),('Tampa               ','SW',1L),('Washington          ','AA',5L),('Washington          ','B6',1L),('Washington          ','SW',1L),('Washington          ','UA',1L),('Washington          ','VX',1L)]

correctanswers[4] = [('Jeff Hernandez                ',)]

correctanswers[5] = [('DL129 ','UA241 ','SFO',datetime.timedelta(0,8280))]

correctanswers[6] = [('AA149 ',Decimal('0.01')),('AA157 ',Decimal('0.01')),('DL138 ',Decimal('0.01')),('DL166 ',Decimal('0.01')),('F9198 ',Decimal('0.01')),('NK174 ',Decimal('0.01')),('SW167 ',Decimal('0.01')),('SW176 ',Decimal('0.01')),('SW179 ',Decimal('0.01')),('SW190 ',Decimal('0.01')),('SW193 ',Decimal('0.01')),('SW196 ',Decimal('0.01')),('UA160 ',Decimal('0.01')),('UA173 ',Decimal('0.01')),('AA159 ',Decimal('0.00')),('AA182 ',Decimal('0.00')),('AA197 ',Decimal('0.00')),('AA204 ',Decimal('0.00')),('AA207 ',Decimal('0.00')),('AA212 ',Decimal('0.00')),('AA219 ',Decimal('0.00')),('AA226 ',Decimal('0.00')),('AA231 ',Decimal('0.00')),('AA237 ',Decimal('0.00')),('AA242 ',Decimal('0.00')),('AA244 ',Decimal('0.00')),('AA247 ',Decimal('0.00')),('AA248 ',Decimal('0.00')),('AA250 ',Decimal('0.00')),('AA252 ',Decimal('0.00')),('AA258 ',Decimal('0.00')),('AA265 ',Decimal('0.00')),('AA267 ',Decimal('0.00')),('AA271 ',Decimal('0.00')),('AA277 ',Decimal('0.00')),('AA280 ',Decimal('0.00')),('AA282 ',Decimal('0.00')),('AA290 ',Decimal('0.00')),('AA300 ',Decimal('0.00')),('AS262 ',Decimal('0.00')),('AS273 ',Decimal('0.00')),('AS283 ',Decimal('0.00')),('AS284 ',Decimal('0.00')),('B6214 ',Decimal('0.00')),('B6270 ',Decimal('0.00')),('B6276 ',Decimal('0.00')),('B6285 ',Decimal('0.00')),('B6286 ',Decimal('0.00')),('B6289 ',Decimal('0.00')),('DL202 ',Decimal('0.00')),('DL229 ',Decimal('0.00')),('DL235 ',Decimal('0.00')),('DL236 ',Decimal('0.00')),('DL239 ',Decimal('0.00')),('DL263 ',Decimal('0.00')),('DL268 ',Decimal('0.00')),('DL272 ',Decimal('0.00')),('DL293 ',Decimal('0.00')),('F9146 ',Decimal('0.00')),('F9203 ',Decimal('0.00')),('F9223 ',Decimal('0.00')),('F9255 ',Decimal('0.00')),('F9264 ',Decimal('0.00')),('F9275 ',Decimal('0.00')),('F9291 ',Decimal('0.00')),('F9294 ',Decimal('0.00')),('F9298 ',Decimal('0.00')),('NK227 ',Decimal('0.00')),('NK230 ',Decimal('0.00')),('NK297 ',Decimal('0.00')),('SW155 ',Decimal('0.00')),('SW161 ',Decimal('0.00')),('SW180 ',Decimal('0.00')),('SW201 ',Decimal('0.00')),('SW205 ',Decimal('0.00')),('SW206 ',Decimal('0.00')),('SW208 ',Decimal('0.00')),('SW210 ',Decimal('0.00')),('SW211 ',Decimal('0.00')),('SW213 ',Decimal('0.00')),('SW215 ',Decimal('0.00')),('SW216 ',Decimal('0.00')),('SW218 ',Decimal('0.00')),('SW220 ',Decimal('0.00')),('SW221 ',Decimal('0.00')),('SW222 ',Decimal('0.00')),('SW224 ',Decimal('0.00')),('SW225 ',Decimal('0.00')),('SW233 ',Decimal('0.00')),('SW234 ',Decimal('0.00')),('SW240 ',Decimal('0.00')),('SW245 ',Decimal('0.00')),('SW246 ',Decimal('0.00')),('SW251 ',Decimal('0.00')),('SW254 ',Decimal('0.00')),('SW257 ',Decimal('0.00')),('SW261 ',Decimal('0.00')),('SW266 ',Decimal('0.00')),('SW274 ',Decimal('0.00')),('SW278 ',Decimal('0.00')),('SW281 ',Decimal('0.00')),('SW288 ',Decimal('0.00')),('SW292 ',Decimal('0.00')),('SW295 ',Decimal('0.00')),('SW296 ',Decimal('0.00')),('SW299 ',Decimal('0.00')),('UA217 ',Decimal('0.00')),('UA228 ',Decimal('0.00')),('UA232 ',Decimal('0.00')),('UA241 ',Decimal('0.00')),('UA243 ',Decimal('0.00')),('UA249 ',Decimal('0.00')),('UA259 ',Decimal('0.00')),('UA260 ',Decimal('0.00')),('UA279 ',Decimal('0.00')),('VX209 ',Decimal('0.00')),('VX238 ',Decimal('0.00')),('VX253 ',Decimal('0.00')),('VX256 ',Decimal('0.00')),('VX269 ',Decimal('0.00')),('VX287 ',Decimal('0.00'))]

correctanswers[7] = [('cust0     ','Anthony Allen                 '),('cust10    ','Anthony Robinson              '),('cust100   ','Christopher Evans             '),('cust101   ','Christopher Garcia            '),('cust104   ','Christopher Jones             '),('cust107   ','Christopher Robinson          '),('cust108   ','Christopher Rodriguez         '),('cust109   ','Christopher Taylor            '),('cust11    ','Anthony Turner                '),('cust110   ','Christopher Walker            '),('cust111   ','Christopher Williams          '),('cust118   ','Daniel Lopez                  '),('cust120   ','Daniel Martinez               '),('cust121   ','Daniel Moore                  '),('cust122   ','Daniel Parker                 '),('cust124   ','Daniel Rodriguez              '),('cust125   ','Daniel Walker                 '),('cust126   ','Daniel Williams               '),('cust128   ','David Baker                   '),('cust131   ','David Harris                  '),('cust132   ','David Jackson                 '),('cust138   ','David Scott                   '),('cust14    ','Barbara Adams                 '),('cust141   ','David Thompson                '),('cust142   ','David White                   '),('cust143   ','Deborah Adams                 '),('cust144   ','Deborah Anderson              '),('cust146   ','Deborah Carter                '),('cust150   ','Deborah Johnson               '),('cust151   ','Deborah Lee                   '),('cust153   ','Deborah Moore                 '),('cust154   ','Deborah Phillips              '),('cust155   ','Deborah Scott                 '),('cust156   ','Deborah Smith                 '),('cust157   ','Deborah Young                 '),('cust158   ','Donald Adams                  '),('cust159   ','Donald Anderson               '),('cust163   ','Donald Hill                   '),('cust164   ','Donald Jackson                '),('cust165   ','Donald King                   '),('cust166   ','Donald Miller                 '),('cust17    ','Barbara Jones                 '),('cust170   ','Donald Thomas                 '),('cust173   ','Donald Wright                 '),('cust174   ','Donna Adams                   '),('cust175   ','Donna Campbell                '),('cust177   ','Donna Collins                 '),('cust181   ','Donna Robinson                '),('cust182   ','Donna Rodriguez               '),('cust184   ','Donna Walker                  '),('cust186   ','Donna Young                   '),('cust187   ','Dorothy Adams                 '),('cust189   ','Dorothy Carter                '),('cust191   ','Dorothy Collins               '),('cust195   ','Dorothy Martin                '),('cust196   ','Dorothy Nelson                '),('cust201   ','Edward Anderson               '),('cust202   ','Edward Campbell               '),('cust204   ','Edward Davis                  '),('cust206   ','Edward Gonzalez               '),('cust21    ','Barbara Parker                '),('cust210   ','Edward Lewis                  '),('cust214   ','Edward Robinson               '),('cust217   ','Edward Turner                 '),('cust222   ','Elizabeth Brown               '),('cust223   ','Elizabeth Campbell            '),('cust229   ','Elizabeth Phillips            '),('cust230   ','Elizabeth Thompson            '),('cust232   ','Elizabeth Wilson              '),('cust233   ','Elizabeth Wright              '),('cust236   ','George Evans                  '),('cust237   ','George Hall                   '),('cust238   ','George Hill                   '),('cust241   ','George Parker                 '),('cust243   ','George Thompson               '),('cust244   ','George Turner                 '),('cust246   ','George Williams               '),('cust247   ','Helen Allen                   '),('cust248   ','Helen Anderson                '),('cust249   ','Helen Baker                   '),('cust250   ','Helen Collins                 '),('cust253   ','Helen Johnson                 '),('cust254   ','Helen Mitchell                '),('cust255   ','Helen Nelson                  '),('cust257   ','Helen Thompson                '),('cust258   ','Helen Walker                  '),('cust261   ','James Carter                  '),('cust263   ','James Edwards                 '),('cust264   ','James Garcia                  '),('cust266   ','James Hernandez               '),('cust269   ','James King                    '),('cust270   ','James Martin                  '),('cust273   ','James Rodriguez               '),('cust275   ','James Walker                  '),('cust276   ','James White                   '),('cust278   ','Jason Allen                   '),('cust279   ','Jason Campbell                '),('cust281   ','Jason Mitchell                '),('cust282   ','Jason Moore                   '),('cust283   ','Jason Perez                   '),('cust284   ','Jason Phillips                '),('cust285   ','Jason Robinson                '),('cust289   ','Jeff Clark                    '),('cust290   ','Jeff Davis                    '),('cust291   ','Jeff Edwards                  '),('cust292   ','Jeff Gonzalez                 '),('cust294   ','Jeff Johnson                  '),('cust296   ','Jeff Nelson                   '),('cust299   ','Jeff Turner                   '),('cust3     ','Anthony Garcia                '),('cust300   ','Jennifer Allen                '),('cust305   ','Jennifer Garcia               '),('cust307   ','Jennifer Harris               '),('cust309   ','Jennifer Mitchell             '),('cust310   ','Jennifer Smith                '),('cust311   ','Jennifer Thomas               '),('cust313   ','Jennifer Wright               '),('cust316   ','John Campbell                 '),('cust317   ','John Green                    '),('cust318   ','John Hall                     '),('cust319   ','John Harris                   '),('cust32    ','Betty Hall                    '),('cust321   ','John Lopez                    '),('cust324   ','John Parker                   '),('cust327   ','John Robinson                 '),('cust329   ','John Thomas                   '),('cust33    ','Betty Mitchell                '),('cust330   ','John Turner                   '),('cust331   ','John Wilson                   '),('cust333   ','Joseph Brown                  '),('cust334   ','Joseph Evans                  '),('cust335   ','Joseph Garcia                 '),('cust336   ','Joseph Green                  '),('cust337   ','Joseph Hall                   '),('cust338   ','Joseph Lee                    '),('cust339   ','Joseph Martinez               '),('cust340   ','Joseph Miller                 '),('cust341   ','Joseph Moore                  '),('cust342   ','Joseph Parker                 '),('cust343   ','Joseph Perez                  '),('cust344   ','Joseph Phillips               '),('cust345   ','Joseph Thomas                 '),('cust346   ','Karen Anderson                '),('cust347   ','Karen Campbell                '),('cust348   ','Karen Martinez                '),('cust349   ','Karen Mitchell                '),('cust35    ','Betty Scott                   '),('cust352   ','Karen Taylor                  '),('cust353   ','Karen Williams                '),('cust354   ','Kenneth Baker                 '),('cust359   ','Kenneth Lopez                 '),('cust36    ','Betty Turner                  '),('cust360   ','Kenneth Moore                 '),('cust362   ','Kenneth Robinson              '),('cust365   ','Kenneth Smith                 '),('cust367   ','Kenneth Turner                '),('cust371   ','Kevin Evans                   '),('cust372   ','Kevin Garcia                  '),('cust374   ','Kevin King                    '),('cust375   ','Kevin Lewis                   '),('cust378   ','Kevin Roberts                 '),('cust379   ','Kevin Rodriguez               '),('cust382   ','Kevin Walker                  '),('cust384   ','Kimberly Anderson             '),('cust386   ','Kimberly Collins              '),('cust391   ','Kimberly King                 '),('cust392   ','Kimberly Lee                  '),('cust393   ','Kimberly Martinez             '),('cust397   ','Kimberly Taylor               '),('cust399   ','Kimberly Turner               '),('cust402   ','Laura Adams                   '),('cust406   ','Laura Evans                   '),('cust408   ','Laura Harris                  '),('cust409   ','Laura Hernandez               '),('cust410   ','Laura Johnson                 '),('cust411   ','Laura Martinez                '),('cust412   ','Laura Nelson                  '),('cust413   ','Laura Scott                   '),('cust416   ','Laura Turner                  '),('cust418   ','Laura Wilson                  '),('cust420   ','Laura Young                   '),('cust423   ','Linda Collins                 '),('cust424   ','Linda Evans                   '),('cust425   ','Linda Hall                    '),('cust426   ','Linda Lopez                   '),('cust428   ','Linda Phillips                '),('cust429   ','Linda Roberts                 '),('cust43    ','Brian Clark                   '),('cust431   ','Linda Smith                   '),('cust432   ','Linda Taylor                  '),('cust434   ','Linda Walker                  '),('cust436   ','Linda Young                   '),('cust437   ','Lisa Adams                    '),('cust438   ','Lisa Brown                    '),('cust439   ','Lisa Clark                    '),('cust440   ','Lisa Davis                    '),('cust441   ','Lisa Edwards                  '),('cust443   ','Lisa Garcia                   '),('cust444   ','Lisa Gonzalez                 '),('cust445   ','Lisa Jones                    '),('cust446   ','Lisa Lee                      '),('cust449   ','Lisa Thompson                 '),('cust45    ','Brian Edwards                 '),('cust452   ','Lisa Wilson                   '),('cust454   ','Margaret Clark                '),('cust456   ','Margaret Gonzalez             '),('cust461   ','Margaret Mitchell             '),('cust462   ','Margaret Parker               '),('cust466   ','Margaret Smith                '),('cust467   ','Margaret Taylor               '),('cust468   ','Margaret White                '),('cust469   ','Margaret Wright               '),('cust47    ','Brian Hall                    '),('cust470   ','Margaret Young                '),('cust471   ','Maria Allen                   '),('cust474   ','Maria Carter                  '),('cust475   ','Maria Clark                   '),('cust476   ','Maria Garcia                  '),('cust478   ','Maria Hernandez               '),('cust480   ','Maria Johnson                 '),('cust481   ','Maria King                    '),('cust485   ','Maria Rodriguez               '),('cust487   ','Maria Turner                  '),('cust488   ','Maria White                   '),('cust489   ','Mark Campbell                 '),('cust490   ','Mark Collins                  '),('cust491   ','Mark Garcia                   '),('cust492   ','Mark Gonzalez                 '),('cust493   ','Mark Lee                      '),('cust494   ','Mark Lopez                    '),('cust496   ','Mark Phillips                 '),('cust497   ','Mark Roberts                  '),('cust498   ','Mark Robinson                 '),('cust499   ','Mark Rodriguez                '),('cust50    ','Brian Lopez                   '),('cust500   ','Mark Taylor                   '),('cust503   ','Mark Wright                   '),('cust504   ','Mary Allen                    '),('cust507   ','Mary Edwards                  '),('cust508   ','Mary Gonzalez                 '),('cust511   ','Mary Parker                   '),('cust514   ','Mary Thomas                   '),('cust518   ','Michael Garcia                '),('cust519   ','Michael Green                 '),('cust52    ','Brian Miller                  '),('cust520   ','Michael Hernandez             '),('cust521   ','Michael Jones                 '),('cust522   ','Michael King                  '),('cust524   ','Michael Moore                 '),('cust525   ','Michael Nelson                '),('cust526   ','Michael Parker                '),('cust527   ','Michael Roberts               '),('cust528   ','Michael Taylor                '),('cust529   ','Michael Thompson              '),('cust531   ','Michael Wilson                '),('cust532   ','Michael Wright                '),('cust533   ','Michelle Allen                '),('cust535   ','Michelle Baker                '),('cust537   ','Michelle Collins              '),('cust538   ','Michelle Edwards              '),('cust54    ','Brian Nelson                  '),('cust541   ','Michelle Lewis                '),('cust542   ','Michelle Nelson               '),('cust543   ','Michelle Phillips             '),('cust546   ','Michelle Thomas               '),('cust547   ','Michelle Turner               '),('cust549   ','Nancy Clark                   '),('cust550   ','Nancy Collins                 '),('cust552   ','Nancy Garcia                  '),('cust553   ','Nancy Gonzalez                '),('cust554   ','Nancy Hernandez               '),('cust555   ','Nancy Lee                     '),('cust556   ','Nancy Moore                   '),('cust558   ','Nancy Taylor                  '),('cust559   ','Nancy White                   '),('cust56    ','Brian Perez                   '),('cust561   ','Nancy Wilson                  '),('cust562   ','Patricia Davis                '),('cust563   ','Patricia Edwards              '),('cust565   ','Patricia Miller               '),('cust566   ','Patricia Parker               '),('cust567   ','Patricia Phillips             '),('cust568   ','Patricia Thomas               '),('cust569   ','Patricia Thompson             '),('cust57    ','Brian Scott                   '),('cust571   ','Patricia Walker               '),('cust572   ','Patricia Wilson               '),('cust573   ','Paul Anderson                 '),('cust576   ','Paul Green                    '),('cust577   ','Paul Hernandez                '),('cust58    ','Brian Taylor                  '),('cust580   ','Paul Johnson                  '),('cust581   ','Paul Jones                    '),('cust582   ','Paul Lee                      '),('cust583   ','Paul Miller                   '),('cust584   ','Paul Parker                   '),('cust585   ','Paul Phillips                 '),('cust589   ','Richard Garcia                '),('cust59    ','Brian Wright                  '),('cust591   ','Richard Hill                  '),('cust592   ','Richard Lee                   '),('cust593   ','Richard Lewis                 '),('cust594   ','Richard Miller                '),('cust597   ','Richard Perez                 '),('cust598   ','Richard Scott                 '),('cust599   ','Robert Anderson               '),('cust60    ','Carol Adams                   '),('cust601   ','Robert Campbell               '),('cust603   ','Robert Edwards                '),('cust604   ','Robert Evans                  '),('cust605   ','Robert Gonzalez               '),('cust606   ','Robert Green                  '),('cust608   ','Robert Hernandez              '),('cust609   ','Robert King                   '),('cust61    ','Carol Allen                   '),('cust611   ','Robert Perez                  '),('cust612   ','Robert Roberts                '),('cust613   ','Robert Scott                  '),('cust616   ','Robert Wright                 '),('cust617   ','Ronald Adams                  '),('cust618   ','Ronald Baker                  '),('cust619   ','Ronald Clark                  '),('cust62    ','Carol Campbell                '),('cust621   ','Ronald Green                  '),('cust622   ','Ronald Johnson                '),('cust623   ','Ronald Martinez               '),('cust624   ','Ronald Miller                 '),('cust625   ','Ronald Moore                  '),('cust626   ','Ronald Perez                  '),('cust628   ','Ronald Smith                  '),('cust629   ','Ronald Thomas                 '),('cust63    ','Carol Carter                  '),('cust630   ','Ronald Walker                 '),('cust633   ','Ruth Adams                    '),('cust635   ','Ruth Anderson                 '),('cust636   ','Ruth Baker                    '),('cust637   ','Ruth Davis                    '),('cust638   ','Ruth Garcia                   '),('cust64    ','Carol Edwards                 '),('cust640   ','Ruth Jackson                  '),('cust643   ','Ruth Parker                   '),('cust645   ','Ruth Smith                    '),('cust646   ','Ruth Taylor                   '),('cust648   ','Ruth Thompson                 '),('cust651   ','Sandra Allen                  '),('cust652   ','Sandra Brown                  '),('cust653   ','Sandra Campbell               '),('cust654   ','Sandra Clark                  '),('cust656   ','Sandra Hill                   '),('cust659   ','Sandra Perez                  '),('cust660   ','Sandra Scott                  '),('cust661   ','Sandra Wilson                 '),('cust662   ','Sarah Anderson                '),('cust663   ','Sarah Brown                   '),('cust665   ','Sarah Hall                    '),('cust667   ','Sarah Lopez                   '),('cust668   ','Sarah Mitchell                '),('cust669   ','Sarah Turner                  '),('cust670   ','Sarah Walker                  '),('cust672   ','Sharon Evans                  '),('cust673   ','Sharon Garcia                 '),('cust675   ','Sharon Jackson                '),('cust676   ','Sharon Lee                    '),('cust678   ','Sharon Lopez                  '),('cust679   ','Sharon Martinez               '),('cust68    ','Carol Moore                   '),('cust680   ','Sharon Moore                  '),('cust682   ','Sharon Taylor                 '),('cust683   ','Sharon Thomas                 '),('cust684   ','Sharon Walker                 '),('cust685   ','Sharon Young                  '),('cust686   ','Steven Brown                  '),('cust687   ','Steven Evans                  '),('cust688   ','Steven Green                  '),('cust689   ','Steven Harris                 '),('cust69    ','Carol Roberts                 '),('cust691   ','Steven Lewis                  '),('cust692   ','Steven Martin                 '),('cust693   ','Steven Mitchell               '),('cust697   ','Steven Scott                  '),('cust698   ','Steven Williams               '),('cust699   ','Susan Allen                   '),('cust700   ','Susan Brown                   '),('cust702   ','Susan Clark                   '),('cust704   ','Susan Garcia                  '),('cust705   ','Susan Hall                    '),('cust706   ','Susan Miller                  '),('cust708   ','Susan Williams                '),('cust71    ','Carol Thomas                  '),('cust710   ','Thomas Anderson               '),('cust712   ','Thomas Collins                '),('cust713   ','Thomas Garcia                 '),('cust714   ','Thomas Jones                  '),('cust715   ','Thomas King                   '),('cust716   ','Thomas Lee                    '),('cust717   ','Thomas Martin                 '),('cust719   ','Thomas Mitchell               '),('cust72    ','Carol Thompson                '),('cust720   ','Thomas Nelson                 '),('cust721   ','Thomas Phillips               '),('cust723   ','Thomas Smith                  '),('cust726   ','Thomas Young                  '),('cust73    ','Carol White                   '),('cust730   ','William Johnson               '),('cust731   ','William Lee                   '),('cust732   ','William Lopez                 '),('cust733   ','William Martinez              '),('cust735   ','William Moore                 '),('cust736   ','William Parker                '),('cust737   ','William Roberts               '),('cust738   ','William Robinson              '),('cust740   ','William Wright                '),('cust75    ','Carol Wright                  '),('cust76    ','Charles Adams                 '),('cust79    ','Charles Green                 '),('cust8     ','Anthony Perez                 '),('cust80    ','Charles Harris                '),('cust81    ','Charles Jackson               '),('cust82    ','Charles Johnson               '),('cust83    ','Charles Jones                 '),('cust85    ','Charles Martin                '),('cust86    ','Charles Parker                '),('cust88    ','Charles Scott                 '),('cust9     ','Anthony Roberts               '),('cust94    ','Charles Wright                '),('cust96    ','Christopher Anderson          '),('cust98    ','Christopher Collins           ')]

correctanswers[8] = []

correctanswers[9] = [('Las Vegas           ',)]

correctanswers[10] = [('AA101 ',1L),('SW102 ',2L),('F9103 ',3L),('NK104 ',4L),('SW105 ',5L),('SW106 ',6L),('F9107 ',7L),('DL108 ',8L),('SW109 ',9L),('F9110 ',10L),('AA111 ',11L),('VX114 ',12L),('AS118 ',13L),('B6116 ',14L),('B6112 ',15L),('B6125 ',16L),('AS117 ',17L),('B6115 ',18L),('SW113 ',18L),('AA119 ',20L),('AA121 ',20L),('SW123 ',20L)]

