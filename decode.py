#!/usr/bin/env python

#--- line = '1212200805060505040201031125152114' # 2 of dials
#--- line = '05221722012002080707211817141206180918010706' # queen of disks 101
#--- line = '0505040914200805180501121518040518' # 10 of dials
# line = '2614120714241812020817021001' # Jack of skulls
# line = '072114071922011722012014010610180506' # Queen of skulls
#--- line = '2008050609181920091920080512011920' # queen of dials (goon)
#--- line = '2122060518061805091814040822180717181918010618' # 5 of disks 100
# line = '252516251814050803' # 7 of keys


# line = '01020714252510210210140117180514051825020607' # Lost's black badge (ace of skull)
#--- line = '0914200805180501121518040518200805' # Ace of dials
# line = '' # ace of keys


dials = [
(2, '1212200805060505040201031125152114', '110'),
(10, '0505040914200805180501121518040518', '111'),
('q', '2008050609181920091920080512011920', '000'), # 000 or 111?
('a', '0914200805180501121518040518200805', '001'),
('j', '0609181920091920080512011920020505', '010'),
('k', '2605181501140415140523091212020501', '101'),
(5, '2403122119092205151808011909201805', '011'),
(7, '0709192005180504200801202001160120', '100')
]

keys = [
(2, '072118062412061022', '000'),
(7, '252516251814050803', '001'),
('q', '010721220624181211', '111'),
('j', '241401171021220718', '011'),
(10, '190721181522070621', '101'),
('k', '010207220115251416', '010'),
('a', '182503120208070805', '110'),
(5, '150807062114171802', '100')
]

disks = [
(2, '16140716210721182612060718051216140716210721181705221970', '111'),
('q', '05221722012002080707211817141206180918010706', '101'),
(5, '2122060518061805091814040822180717181918010618', '100'),
(10, '07210208202121220626220117220601020719020505180107', '010'),
('k', '05020707212205071818010305021514152512220601070522202107', '000'),
('j', '161407162107211826220607161407162107211826120721', '110'),
(7, '1508070721220622061908010522202107', '001'),
('a', '170201070308072122261702100114061405050220140107', '011')
]

skulls = [
('j', '2614120714241812020817021001', '101',),
('q', '072114071922011722012014010610180506', '100'),
(7, '05020707212205071818011614011518190801', '000'),
('a', '01020714252510210210140117180514051825020607', '111'), # binary is based on others
('k', '031407210601020702190718010518031814071817', '110'),
(2, '14011712020810222525061818', '011'),
(5, '07051206022618072122012018250618', '010'),
(10, '1508070602261807222618062518141706140607051412', '001')
]

suits = [('dials: register', sorted(dials)), ('skulls: e', sorted(skulls)), ('disks: pi', sorted(disks)), ('keys: gray code', sorted(keys))]

regOrder = [7, 3, 1, 4, 2, 5, 6, 7]

def rotn(s, n):
  return [1 + (i + n - 1) % 26 for i in s]

def intToChar(i):
  return chr(i + ord('A') - 1)

# stickers = [[
# '01100100',
# '01100101',
# '01100110',
# '01100011',
# '01101111',
# '01101110'],

# [
# '01001110',
# '01001111',
# '01000011',
# '00100011',
# '01000110',
# '01000101',
# '01000111'
# ]]


for (name, suit) in suits:
  print('%s' % name)
  cards = dict()
  for stuff in suit:
    card = stuff[0]
    line = stuff[1]
    binary = stuff[2]

    decoded = [line[i:i+2] for i in range(0, len(line), 2)]
    rot = 13
    if name == 'dials: register':
      rot = 0
    ints = [int(str(c)) for c in decoded]
    chars = [intToChar(i) for i in rotn(ints, rot)]

    asString = reduce(lambda l, r: l + r, chars, '')
    cards[binary] = (asString, card)

  for (binary, (asString, card)) in sorted(cards.items()):
    print('%4s %s %s' % (str(card), binary, asString))


# for s in stickers:
#   data = [intToChar(int(st, 2)) for st in s]
#   print(data)


