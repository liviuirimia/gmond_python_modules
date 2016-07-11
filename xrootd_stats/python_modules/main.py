#!/usr/bin/python

import os
import xml.etree.ElementTree as ET
import lxml.etree
from collections import defaultdict

'''
comment section
-----------------------
1. ET.parse([filename]).getroot().attrib[[tag]] - get attributes from root element (one line expression)
root element attributes - [tod, ver, src, tos, pgm, ins, pid, site]
'''
d = defaultdict(list)

def main():
	xml_string = '<statistics tod="1467718493" ver="v4.3.0" src="storage02.spacescience.ro:1094" tos="1465913236" pgm="xrootd" ins="server" pid="20323" site="ALICE::ISS::FILE"><stats id="info"><host>storage02.spacescience.ro</host><port>1094</port><name>server</name></stats><stats id="buff"><reqs>294311</reqs><mem>155678720</mem><buffs>205</buffs><adj>0</adj><xlreqs>0</xlreqs><xlmem>0</xlmem><xlbuffs>0</xlbuffs></stats><stats id="link"><num>1</num><maxn>99</maxn><tot>43837</tot><in>3817131467</in><out>8477313881247</out><ctime>6759445</ctime><tmo>153038</tmo><stall>84</stall><sfps>0</sfps></stats><stats id="poll"><att>1</att><en>153045</en><ev>152898</ev><int>0</int></stats><stats id="proc"><usr><s>232</s><u>128000</u></usr><sys><s>4372</s><u>965000</u></sys></stats><stats id="xrootd"><num>43837</num><ops><open>92969</open><rf>0</rf><rd>25862125</rd><pr>0</pr><rv>1830187</rv><rs>53058131</rs><wr>795</wr><sync>14</sync><getf>0</getf><putf>0</putf><misc>168537</misc></ops><aio><num>0</num><max>0</max><rej>0</rej></aio><err>0</err><rdr>0</rdr><dly>7</dly><lgn><num>43837</num><af>0</af><au>43836</au><ua>0</ua></lgn></stats><stats id="ofs"><role>server</role><opr>0</opr><opw>0</opw><opp>-1</opp><ups>0</ups><han>0</han><rdr>0</rdr><bxq>0</bxq><rep>0</rep><err>0</err><dly>0</dly><sok>0</sok><ser>0</ser><tpc><grnt>0</grnt><deny>0</deny><err>0</err><exp>0</exp></tpc></stats><stats id="oss" v="2"><paths>1<stats id="0"><lp>"/"</lp><rp>"/storage01/xrdnamespace/home/aliprod/data/"</rp><tot>9612255148</tot><free>1290813948</free><ino>1220706304</ino><ifr>1219795431</ifr></stats></paths><space>1<stats id="0"><name>public</name><tot>19224510296</tot><free>2469531264</free><maxf>1290813948</maxf><fsn>2</fsn><usg>10214</usg></stats></space></stats><stats id="sched"><jobs>262326</jobs><inq>0</inq><maxinq>5</maxinq><threads>34</threads><idle>32</idle><tcr>44</tcr><tde>10</tde><tlimr>0</tlimr></stats><stats id="sgen"><as>1</as><et>0</et><toe>1467718493</toe></stats></statistics>'
	tree = ET.fromstring(xml_string)
	root = ET.fromstring(xml_string)

	# for i in root.iterfind('stats[@id="info"]'):
	# 	for c in i.getchildren():
	# 		print c.tag, c.text

	for i in root.iterfind('stats[@id="proc"]'):
		for usr in i.getchildren():
			if usr.tag == "usr":
				print usr.getchildren()[0].text
			if usr.tag == "sys":
				print usr.getchildren()[0].text
			# for a in usr.getchildren():
			# 	print a.text

	# a = [ (el.tag, el.text)for el in root.iter() ]
	
	# for i in a:
	# 	print i[1]
	# e = tree.xpath("//stats[@id='oss']/paths")
	# for i in e:
	# 	print i.xpath('./text()')
	# 	print i.xpath('./*/*/text()')

	#print tree.xpath('//*[count(child::*) != 0]/*/text()')
	# print tree.xpath("//stats[@id='"+'info'+"']/*/text()")
	# print tree.xpath("//stats[@id='oss']/*/text()")
	# print tree.xpath("//stats[@id='oss']/paths/./stats/*/text()")
	# print tree.xpath("//stats[@id='oss']/space/./stats/*/text()")


if __name__ == "__main__":
	main()