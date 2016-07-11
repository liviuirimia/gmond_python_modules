import os
import xml.etree.ElementTree as ET

xml_string = '<statistics tod="1467718493" ver="v4.3.0" src="storage02.spacescience.ro:1094" tos="1465913236" pgm="xrootd" ins="server" pid="20323" site="ALICE::ISS::FILE"><stats id="info"><host>storage02.spacescience.ro</host><port>1094</port><name>server</name></stats><stats id="buff"><reqs>294311</reqs><mem>155678720</mem><buffs>205</buffs><adj>0</adj><xlreqs>0</xlreqs><xlmem>0</xlmem><xlbuffs>0</xlbuffs></stats><stats id="link"><num>1</num><maxn>99</maxn><tot>43837</tot><in>3817131467</in><out>8477313881247</out><ctime>6759445</ctime><tmo>153038</tmo><stall>84</stall><sfps>0</sfps></stats><stats id="poll"><att>1</att><en>153045</en><ev>152898</ev><int>0</int></stats><stats id="proc"><usr><s>232</s><u>128000</u></usr><sys><s>4372</s><u>965000</u></sys></stats><stats id="xrootd"><num>43837</num><ops><open>92969</open><rf>0</rf><rd>25862125</rd><pr>0</pr><rv>1830187</rv><rs>53058131</rs><wr>795</wr><sync>14</sync><getf>0</getf><putf>0</putf><misc>168537</misc></ops><aio><num>0</num><max>0</max><rej>0</rej></aio><err>0</err><rdr>0</rdr><dly>7</dly><lgn><num>43837</num><af>0</af><au>43836</au><ua>0</ua></lgn></stats><stats id="ofs"><role>server</role><opr>0</opr><opw>0</opw><opp>-1</opp><ups>0</ups><han>0</han><rdr>0</rdr><bxq>0</bxq><rep>0</rep><err>0</err><dly>0</dly><sok>0</sok><ser>0</ser><tpc><grnt>0</grnt><deny>0</deny><err>0</err><exp>0</exp></tpc></stats><stats id="oss" v="2"><paths>1<stats id="0"><lp>"/"</lp><rp>"/storage01/xrdnamespace/home/aliprod/data/"</rp><tot>9612255148</tot><free>1290813948</free><ino>1220706304</ino><ifr>1219795431</ifr></stats></paths><space>1<stats id="0"><name>public</name><tot>19224510296</tot><free>2469531264</free><maxf>1290813948</maxf><fsn>2</fsn><usg>10214</usg></stats></space></stats><stats id="sched"><jobs>262326</jobs><inq>0</inq><maxinq>5</maxinq><threads>34</threads><idle>32</idle><tcr>44</tcr><tde>10</tde><tlimr>0</tlimr></stats><stats id="sgen"><as>1</as><et>0</et><toe>1467718493</toe></stats></statistics>'
descriptors = []
mapping = {}
Desc_Skel = {}
sts = {}

NAME_PREFIX = 'xrootd_stats_'
metric_list = {
	NAME_PREFIX + 'src'	: { 'type' : 'string', 
							'format' : '%s', 
							'description' : 'description for src string'
							},
	NAME_PREFIX + 'ver'	: { 'type' : 'string', 
							'format' : '%s', 
							'description' : 'description for ver string'},
	NAME_PREFIX + 'tos'	: { 'type' : 'uint', 
							'format' : '%d', 
							'description' : 'description for tos number'},

}

def get_root_attrib(name):
	root = ET.fromstring(xml_string)
	for i in root.attrib:
		sts[i] = root.attrib[i]
	return sts[name]

def metric_init(params):
	global descriptors, Desc_Skel

	Desc_Skel = {
		'name'			: 'XXX',
		'call_back'		: get_root_attrib,
		'time_max'		: 60,
		'value_type'	: 'uint',
		'format'		: '%d',
		'description'	: 'XXX',
		'groups'		: 'xrootd_stats'

	}

	for k,v in metric_list.iteritems():
		descriptors.append(create_desc(Desc_Skel, {
				'name': k,
				'call_back' : get_root_attrib,
				'value_type': v['type'],
				'format': v['format'],
				'description': v['description']
			}))
	return descriptors

def create_desc(skel, prop):
	d = skel.copy()
	for k,v in prop.iteritems():
		d[k] = v
	return d

def metric_cleanup():
	pass

if __name__ == "__main__":
	metric_init(None)
	for d in descriptors:
		v = d['call_back'](d['name'])
		print v