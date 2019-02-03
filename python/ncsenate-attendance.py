senator_list = '''<option value="392">Sen. J. Alexander</option>
<option value="416">Sen. T. Alexander</option>
<option value="396">Sen. Ballard</option>
<option value="64">Sen. Berger</option>
<option value="398">Sen. Bishop</option>
<option value="268">Sen. Blue</option>
<option value="399">Sen. Britt</option>
<option value="139">Sen. Brown</option>
<option value="412">Sen. Burgin</option>
<option value="395">Sen. Chaudhuri</option>
<option value="380">Sen. Clark</option>
<option value="295">Sen. Daniel</option>
<option value="230">Sen. D. Davis</option>
<option value="357">Sen. J. Davis</option>
<option value="408">Sen. deViere</option>
<option value="397">Sen. Edwards</option>
<option value="404">Sen. Fitch</option>
<option value="410">Sen. Ford</option>
<option value="383">Sen. Foushee</option>
<option value="407">Sen. Gallimore</option>
<option value="414">Sen. Garrett</option>
<option value="276">Sen. Gunn</option>
<option value="283">Sen. Harrington</option>
<option value="298">Sen. Hise</option>
<option value="400">Sen. Horner</option>
<option value="281">Sen. B. Jackson</option>
<option value="386">Sen. J. Jackson</option>
<option value="406">Sen. Johnson</option>
<option value="384">Sen. Krawiec</option>
<option value="394">Sen. Lowe</option>
<option value="411">Sen. Marcus</option>
<option value="389">Sen. McInnis</option>
<option value="228">Sen. McKissick</option>
<option value="417">Sen. Mohammed</option>
<option value="402">Sen. Newton</option>
<option value="409">Sen. Nickel</option>
<option value="273">Sen. Pate</option>
<option value="419">Sen. Perry</option>
<option value="413">Sen. Peterson</option>
<option value="303">Sen. Rabon</option>
<option value="364">Sen. Robinson</option>
<option value="375">Sen. Sanderson</option>
<option value="405">Sen. Sawyer</option>
<option value="418">Sen. Searcy</option>
<option value="391">Sen. Smith</option>
<option value="415">Sen. Steinburg</option>
<option value="99">Sen. Tillman</option>
<option value="385">Sen. Van Duyn</option>
<option value="393">Sen. Waddell</option>
<option value="388">Sen. Wells</option>
<option value="379">Sen. Woodard</option>'''.split('\n')

for senator in senator_list:
	#get ID of senator to be used to find vote records
	senator_id = senator[15:18]
	if senator_id[-1] == '"':
		senator_id = senator_id[:-1]
	goto('https://www.ncleg.gov/Legislation/Votes/MemberVoteHistory/2019/S/')