senators = '''Milton F. "Toby" Fitch
Carl Ford
Valerie P. Foushee
Eddie Gallimore
Michael Garrett
Rick Gunn
Kathy Harrington
Ralph Hise
Rick Horner
Brent Jackson
Jeff Jackson
Todd Johnson
Joyce Krawiec
Paul A. Lowe
Natasha R. Marcus
Tom McInnis
Floyd B. McKissick
Mujtaba A. Mohammed
Paul Newton
Wiley Nickel
Jim Perry
Harper Peterson
Bill Rabon
Gladys A. Robinson
Norman W. Sanderson
Vickie Sawyer
Sam Searcy
Erica D. Smith
Bob Steinburg
Jerry W. Tillman
Terry Van Duyn
Joyce Waddell
Andy Wells
Mike Woodard'''.split('\n')

aye = 'Alexander; Ballard; Barefoot; Barringer; Berger; Brock; Brown; Cook; Curtis; Edwards; Gunn; Harrington; Hise; Jackson; Krawiec; McInnis; Meredith; Newton; Pate; Rabin; Rabon; Randleman; Rucho; Sanderson; Tucker; Wade'.split('; ')
nay = 'Blue; Bryant; Chaudhuri; Clark; Davis; Ford; Lowe; McKissick; Smith; Duyn; Waddell; Woodard'.split('; ')
absent = 'Foushee; Jackson; Robinson; Smith-Ingram; Bingham; Daniel; Davis; Hartsell; Lee; Tarte; Tillman; Wells'.split('; ')

for x in senators:
	if x.split(' ')[-1] in aye:
		print('Aye')
	elif x.split(' ')[-1] in nay:
		print('Nay')
	elif x.split(' ')[-1] in absent:
		print('Absent')
	else:
		print('N/A')