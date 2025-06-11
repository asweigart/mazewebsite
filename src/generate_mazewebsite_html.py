import os, sys, pprint

text = {1: '<p>. . . the entrance hall of the Maze.</p><p>They looked carefully at '
    'the bronze doors, trying to choose. The uncertainty of visitors is one of '
    'my little pleasures.</p><p>“It’s easy to get lost,” I said helpfully. '
    '“This can be a sinister place.” The sun glared at me through the '
    'gateway.</p><p>Something was ringing behind one of the doors. They spent '
    'some time trying to decide which door it was, not understanding that the '
    'silences of the Maze are as eloquent as the sounds.</p><p>“Decisions, '
    'decisions,” one said. “Too many decisions.”</p><p>“The story of my life,” '
    'said another.</p><p>“We don’t want to be late,” said a third, opening one '
    'of the doors.</p><p>“Nary a soul to be seen,” said the first, peering '
    'into the gloom.</p><p>I waited patiently for them to choose which way to '
    'go . . . </p><p>into . . .</p>',
 2: '<p>. . . a bright room whose walls were in some disrepair. The '
    'floorboards creaked and groaned; the plaster made a gritty '
    'sound.</p><p>They studied the old frescoes for clues but missed the '
    'obvious signs.</p><p>“Are we on the right path?” they '
    'asked.</p><p>Keeping in mind what a relative term “right” is, I assured '
    'them they were, indeed, on the right path. As for the “correct” path or '
    'the “most appropriate” path. . . . Well, that might be something '
    'else.</p><p>Full of confidence now they marched out to . . .</p>',
 3: '<p>. . . an entirely different kind of place.</p><p>The group complained '
    'of feeling “all turned around,” as well they might.</p><p>Because no one '
    'wanted to stay here very long they missed the real sign while looking '
    'through the obvious. People in their situation, confronted with a '
    'challenge, tend to accept the terms of the challenge as a given, without '
    'examining it from all sides. How many sides does that problem have? They '
    'don’t know.</p><p>We passed down a long flight of stairs, through some '
    'sort of pantry, and on into . . .</p>',
 4: '<p>. . . the great hall of many doors.</p><p>“What a foolish face,” I '
    'snorted. “Pay no attention.”</p><p>A sound made them all turn suddenly. A '
    'small black cat ran out of a door to my right, sniffed at us, and, before '
    'I could move, ran out of the hall. It was fortunate that I was still '
    'standing with the rest of them or they might have noticed.</p><p>Faint '
    'voices came down one of the corridors.</p><p>“Shall we toss a coin?” I '
    'asked. “Or have you made up your minds?”</p><p>They hadn’t made up their '
    'minds, and they had no coins. By a process of elimination they decided to '
    'go to . . .</p>',
 5: '<p>. . . the tree room.</p><p>“Are these real?” they asked.</p><p>I told '
    'them the trees were as real as anything else in the House. As this was an '
    'important decision I encouraged them to take their time. After all, the '
    'more they think about the possibilities the more choices they have to '
    'make.</p><p>What were their chances of choosing wisely . . . one in four? '
    'Two in four perhaps, if I was generous about it . . . and why not be '
    'generous? There are one hundred ninety doors in this part of the House, '
    'counting the gate . . . enough for everyone.</p><p>Making a choice, they '
    'entered a very long, dark corridor and at last came out into . . .</p>',
 6: '<p>. . . a gloomy, cavelike place far underground. Even I was oppressed '
    'by the weight that hung over our heads. A very small hole, high above, '
    'admitted a feeble light.</p><p>Standing in the light one of them put his '
    'hand out. “I think it may be raining out there . . .”</p><p>They didn’t '
    'like the look of the place.</p><p>“You continue to judge everything by '
    'the way it looks!” I cried, exasperated by their timidity. I knew I '
    'shouldn’t have said anything. If you think of all the deceptions '
    'practiced in my family, particularly on my father . . .</p><p>We went '
    'down the only way open to us and came to . . .</p>',
 7: '<p>. . . a pleasant room with three doors and a lamp. Looking at the '
    'picture on the wall they decided it wasn’t a very good '
    'likeness.</p><p>One of them almost fell over something on the floor. “Why '
    'don’t they pick up after themselves?” he said, sounding like an old '
    'man.</p><p>“Weren’t you ever irresponsible?” I asked, thinking of my '
    'childhood and how wild I had been.</p><p>Music was being played somewhere '
    'nearby. We stopped to listen for a moment.</p><p>Leaving the pictures '
    'looking out at an empty room we went on to . . .</p>',
 8: '<p>...a vaulted chamber lit by a single bulb.</p><p>Someone knocked a '
    'bowl off the table. The crash echoed from the ceiling and whispered away '
    'down the corridors. I broke another on purpose.</p><p>“Make sure to take '
    'that with you,” I said. “You can never tell when you might need '
    'it.”</p><p>“Take what?” they wanted to know.</p><p>“Isn’t it '
    'obvious?”</p><p>Taking a vote among themselves they went on to...</p>',
 9: '<p>...what appeared to be an old storeroom. Dust obscured a damaged '
    'paineting making it hard to understand just what the artist had '
    'intended.</p><p>“This could be a trick of some sort,” one said. “We might '
    'be going around in circles.”</p><p>“I don’t think so,” said the '
    'thoughtful one. “I think we’re supposed to think it’s a trick...that’s '
    'the trick.”</p><p>They all looked at me. “Yes,” I said. “I’m sure you’re '
    'right about that.”</p><p>With doubtful looks they left for...</p>',
 10: '<p>...a room that smelled of paint. Faint voices, apparently in an '
     'argument, came from behind the locked door.</p><p>“You know,” said one, '
     '“that sounds like us in there...”</p><p>They tried the door but, '
     'naturally, it wouldn’t open. The voices stopped when the doorknob '
     'rattled.</p><p>One picked up the umbrella. “It may rain where we’re '
     'going.”</p><p>I signaled my approval and, after a short rest, we came '
     'to...</p>',
 11: '<p>...an airy room with many doors. It was a big space, but I still felt '
     'crowded. I’ve always hated confinement.</p><p>“Whatever you do,” I '
     'warned them, “don’t touch that!”</p><p>“This must be an important room,” '
     'said one of them. “It has more doors than any of the '
     'others...”</p><p>This was not true, but I didn’t want to '
     'interrupt.</p><p>“With so many paths crossing here we must be close to '
     'the center,” she continued.</p><p>I had noticed this guest before; I '
     'would have to be careful. “This is an important choice,” I said, trying '
     'to encourage them.</p><p>Gratefully leaving the room behind we walked '
     'all the way to...</p>',
 12: '<p>...a spacious room with a hole in the floor. A ladder led down into '
     'the shadows. Outside, leaves shook in the wind. They didn’t like the '
     'look of that hole in the floor.</p><p>“Too dark down there!” they cried. '
     '“Who knows what’s at the bottom.” They looked at me '
     'again.</p><p>“Probably a room of some kind,” I volunteered quickly. “But '
     'you know what I say about appearances.” It would have been a relief to '
     'get outside for a while.</p><p>They wanted to know if they had been here '
     'before.... How could I answer that?</p><p>“I have the strangest feeling '
     'of déjà vu,” said one who, bolder than the rest, led us into...</p>',
 13: '<p>...room number 13.</p><p>They weren’t really comfortable here and I '
     'knew why.</p><p>“No, no,” they said. “We’re not all '
     'superstitious.”</p><p>“Only some of you, then?”</p><p>They were worried '
     'it might be Friday. Well it’s true that is was closer to the end of the '
     'week than they realized. It takes a great deal of experience, certainly '
     'more than they possessed, to understand how time works in the Maze. The '
     'clock thought it was six in the evening.</p><p>Quickly moving on we came '
     'to...</p>',
 14: '<p>...one of the biggest rooms in the House. All three doorways were '
     'dark.</p><p>“Afraid to go out?” I asked.</p><p>Since they tried to think '
     'of themselves as adults, they didn’t care for my question.</p><p>“Not '
     'really,” said the thoughtful one, “but that doesn’t mean we have to go '
     'running around out there just to prove something to you.”</p><p>I knew '
     'she would bear watching.</p><p>“Choose then!” I cried, as if my feelings '
     'were hurt. “Pay no attention to anything I say.” I knew they couldn’t '
     'afford not to listen to me entirely...they were so easily '
     'led.</p><p>Turning around, the group took a path that completely '
     'surprised me after all, and I followed them to...</p>',
 15: '<p>...room number 15. Just as we entered I heard a thump and the sound '
     'of footsteps hurrying away. Somewhere a door slammed.</p><p>“At least '
     'three of us can sit down here,” said one.</p><p>There were only three '
     'possible choices.</p><p>Leaning on the sacrificial tripod I was suddenly '
     'moved to say, “Perhaps these numbers relate to each other in some '
     'specific combination...” Immediately I regretted this act of '
     'charity...sometimes I think, after all these years, that I don’t really '
     'know myself.</p><p>One of them thought he had worked it out and, very '
     'pleased with himself, led us into . . .</p>',
 16: '<p>...a stone chamber which reminded me of my old neighbors.</p><p>Of '
     'course, that was a long time ago now, but would you believe their '
     'descendants are still telling stories about me and my family to their '
     'children?</p><p>Even if most of the stories are lies and exaggerations, '
     'it is immortality of a sort.</p><p>As I passed in front of an open '
     'doorway a figure, crossing the hall outside, saw me and immediately ran '
     'off.</p><p>“Who was that?” they asked.</p><p>“Another visitor, to be '
     'sure.”</p><p>“Why did he run away?”</p><p>“You probably scared him,” I '
     'said, and they apparently believed me.</p><p>With few regrets on my part '
     'we left for...</p>',
 17: '<p>...a room with a floor of sand.</p><p>“Amphorae,” I pronounced; '
     'empty, of course.</p><p>“This is an easier choice to make,” they '
     'said.</p><p>“You may think so,” I muttered to myself, “but your choices '
     'are more limited than you know.”</p><p>One should never accept the '
     'obvious here. If you think of the Maze as a machine, confusion is its '
     'product, and the machine was hard at work.</p><p>Ignoring my good advice '
     'they hurried into...</p>',
 18: '<p>... a much warmer room. Shadows danced across the floor to fire’s '
     'music.</p><p>“Someone’s lost his hat.”</p><p>“Are you sure it’s the hat '
     'that is lost?” I asked reasonably enough. No one would answer '
     'me.</p><p>Ducking behind a curtain and hurrying down a passageway we '
     'came out in ...</p>',
 19: '<p>...a shaded portico. A late afternoon sun warmed the rough blocks of '
     'stone.</p><p>“Get out of the way!” someone called. We moved into the '
     'yard, squinting at the strong light.</p><p>One of them sat on a marble '
     'bench after I politely pushed some flowers aside. “Did you pick these '
     'for me?” she asked, looking me in the eye. I had to tell her the '
     'truth.</p><p>In another part of the grounds someone was singing, but '
     'they couldn’t make out the words.</p><p>Like children they soon became '
     'restless and impatient to see something new, so we went on to...</p>',
 20: '<p>...room number 20. The ringing stopped as soon as we '
     'entered.</p><p>“What is the matter now?” I asked them.</p><p>“Too many '
     'animals for a proper house!”</p><p>They walked carefully around the '
     'edges of the room. I watched with an amusement shared, I think, by the '
     'wise old tortoise.</p><p>With backwards looks and muttered comments '
     'about turtles they left room number 20 and entered...</p>',
 21: '<p>...a yard containing shrubs trimmed in ornamental '
     'shapes.</p><p>“This,” I began, “is called...”</p><p>“We know what the '
     'name is,” they interrupted. “Why don’t you just tell us which way to '
     'go?”</p><p>“I wasn’t referring to the plants,” I said in a huff. I '
     'refused to say anything else, leaving them to find their own way '
     'to...</p>',
 22: '<p>...a gaudy room that reminded me of a theatrical backdrop. Places '
     'like this are overdone, for my taste, but some people like the '
     'exotic...well, everyone is a critic.</p><p>It’s true, I am by nature '
     'extremely critical. Although my life is a lonely one I have not spared '
     'any of my guests the rigor of my judgment.... We all have our roles to '
     'play.</p><p>This is not a bad place, really; one could spend quite some '
     'time here. However, in their restive way, the group moved on to...</p>',
 23: '<p>...a room with three other doors. Looking out the windows my feet '
     'crushed something on the floor.</p><p>“Watch your step here,” I warned '
     'them. I’m always ready to be helpful with the less important '
     'things.</p><p>“Look at those two trees out there,” one said, looking '
     'over my shoulder, which is not easy to do.</p><p>“Must be a real wind '
     'coming up.”</p><p>Now they realized that it could rain where they were '
     'going.</p><p>“We should have brought that bumbershoot with us from the '
     'coat room...”</p><p>“Which room was that?”</p><p>“You remember, the one '
     'with the animal...”</p><p>I suggested that we take the door on my right '
     'and they realized they had found the door they had been seeking for so '
     'long, the entrance to...</p>',
 24: '<p>...a place of unlimited darkness.</p><p>“Where are the doors?” they '
     'asked nerviously. “We can’t see any doors...”</p><p>“Be careful where '
     'you step!” said a cold voice. “This spot is taken.” Dozens of eyes '
     'blinked at us in the Stygian gloom.</p><p>By the time my uncertain '
     'visitors turned to ask me what to do I was already far '
     'away.</p><p>“There are no doors,” said the voice. “You are here with the '
     'rest of us now...”</p><p>Even my bellowing laughter couldn’t fill this '
     'space.</p>',
 25: '<p>...a high room with the image of a crown on the wall for everyone to '
     'see now. Though one of my parents might be lowborn, the other was close '
     'to a king.... I’ve always felt at home here.</p><p>“Which door ought we '
     'take?” they wanted to know. I rather brusquely indicated the three '
     'doors.</p><p>“Any of those is fine for my purposes.”</p><p>They were '
     'disconcerted at the apparent lack of clues. “Perhaps in another room,” '
     'they said, leaving for...</p>',
 26: '<p>...a dramatic room with four entrances and exits.</p><p>“Not enough '
     'light in here,” they remarked. “Not very tidy either.”</p><p>“Which way '
     'now, children?” I asked in my most patronizing voice.</p><p>They '
     'objected to my tone, but it distracted them from the real clues. The '
     'game usually goes as I plan it, despite the intentions of my visitors, '
     'or perhaps because of their intentions.</p><p>“What the devil is this '
     'supposed to be?” one asked. They gathered around and I realized they '
     'were close to something. I quickly picked up the bell, ringing it '
     'loudly.</p><p>“Was this what you heard outside?”</p><p>Holding their '
     'ears they ran out the door to...</p>',
 27: '<p>...a darkened chamber dominated by a large figure.</p><p>We could see '
     'that someone had been working here recently; the entrance I had so '
     'carefully hidden had been uncovered. I made a note to return as soon as '
     'I could and fill in the hole again.</p><p>The visitors were so intrigued '
     'with the entrance at the bottom of the excavation that they ignored what '
     'the figure was trying to tell them.</p><p>“Where are the '
     'workmen?”</p><p>“They must be ahead of us,” I said. “If we hurry we can '
     'catch them...I mean catch up with them.”</p><p>I herded the group '
     'through the door to...</p>',
 28: '<p>...a spacious room with a hole in the floor. A ladder led down into '
     'the shadows. Outside, leaves shook in the wind. They didn’t like the '
     'look of that hole in the floor.</p><p>“Too dark down there!” they cried. '
     '“Who knows what’s at the bottom.” They looked at me '
     'again.</p><p>“Probably a room of some kind,” I volunteered quickly. “But '
     'you what I say about appearances.” It would have been a relief to get '
     'outside for a while.</p><p>They wanted to know if they had been here '
     'before.... How could I answer that?</p><p>“I have the strangest feeling '
     'of déjà vu,” said one who, bolder than the rest, led us into...</p>',
 29: '<p>...a much smaller room.</p><p>A person with a white staff turned to '
     'face us. His associate shrugged, not an easy thing to do in his '
     'position, and went back to what he had been doing.</p><p>“Look, look,” '
     'said the person with the staff. “This is very important...”</p><p>I '
     'snatched the paper from his hand and tore it into pieces.</p><p>“How '
     'will he find his way without directions?” the group wanted to '
     'know.</p><p>“Don’t worry,” said the man, “here blindness is no '
     'disadvantage.”</p><p>I hurried my visitors out as quickly as I could '
     'to...</p>',
 30: '<p>...room number 30. “What a beautiful door...the others are so plain,” '
     'said one.</p><p>“It’s meant to influence our decision,” said '
     'another.</p><p>“Perhaps this has been done so we will not choose this '
     'door,” said the thoughtful one.</p><p>They wanted to know what the '
     'letters meant. Obviously they meant something, and I said '
     'so.</p><p>“Yes, but...why ’O’ and ’U’? What special significance can '
     'they have for us?”</p><p>The more confused they became, the more I '
     'enjoyed it. No matter how many times I’ve been through this I’m always '
     'fascinated.</p><p>Leaving the room and all that it contained behind us, '
     'we entered...</p>',
 31: '<p>...a melancholy little courtyard surrounded by a brick wall too high '
     'to see over. A dead tree lifted its bone-white branches to a sky filling '
     'with gray clouds.</p><p>“Those doors look very strange,” they '
     'said.</p><p>“You should say, ’They look very strangely,’” I '
     'corrected.</p><p>“They seem to be watching us...”</p><p>A sudden gust of '
     'wind made the branches clatter against each other like old boards. Dead '
     'leaves began to gather at our feet.</p><p>Shivering in the wind we '
     'managed to push open one of the heavy doors and make our way to...</p>',
 32: '<p>...a large square room with a hole rudely broken through one wall. It '
     'must have taken a great deal of strength to pull the heavy stones out of '
     'position.</p><p>The symmetry was also disturbed by the apparent loss of '
     'one of the room’s statues. My visitors thought a thief had broken into '
     'the room, removed the figure, and made away with it. This, of course, '
     'was one explanation.</p><p>“Another one!” they cried.</p><p>“You mean '
     'another representative of the animal kingdom?” I asked.</p><p>“What is a '
     'bird like that doing here?”</p><p>“Roosting, evidently.” Their attitude '
     'was really beginning to irritate me. I have come to think of all the '
     'inhabitants of this House as members of my little kingdom. People can be '
     'so arrogant...in a very real way we are all animals, at least in '
     'part.</p><p>I wouldn’t answer any more of their questions so we left '
     'this room to enter...</p>',
 33: '<p>...the room with no floor. They crowded each other on the narrow '
     'ledge. The bold one ventured out to the center.</p><p>Realizing that '
     'they could see all of the signs only from the center of the room, '
     'several wanted to turn back.</p><p>With exaggerated caution, considering '
     'their predicament, they finally reached the door they wanted and '
     'eventually found themselves in...</p>',
 34: '<p>...a middle-class drawing room or parlor. It was amazing how much '
     'more comfortable they felt in these surroundings.</p><p>Everyone sat '
     'down, some on the floor, and chatted about where they had been and where '
     'they should go.</p><p>“Magpies!” I said to myself. “Not a real thought '
     'in their heads.”</p><p>They were so much at ease they almost missed what '
     'the room was telling them altogether. They finally got the message, '
     'which I thought was pretty obvious, and we went on to...</p>',
 35: '<p>...what appeared to be someone’s basement. One of them sank '
     'gratefully down on an old couch which promptly collapsed.</p><p>I tried '
     'to hide my smile.</p><p>“A totem, or tribal fetish,” said one, walking '
     'around the center of the room.</p><p>“It could be a work of art,” '
     'suggested another.</p><p>“Perhaps it’s a signal to us,” the thoughtful '
     'one said. “A warning or direction?”</p><p>“Not much help when there is '
     'only one way to go,” put in another.</p><p>“I still think it’s a '
     'signal.”</p><p>“Yes,” I said right away, “I’m sure you’re '
     'right.”</p><p>She was immediately suspicious. Still, with no real choice '
     'to make, we left the thing standing alone in light and silence, and went '
     'into...</p>',
 36: '<p>...an old and ruinous part of the House. Turning a corner the music '
     'we had been hearing became louder and at last we saw the musicians '
     'themselves.</p><p>They were so involved they failed to hear us. The '
     'music was suited to the scene - a moody, romantic melody. We stopped to '
     'listen and I admit that I, too, was affected by the sound as well as by '
     'the spectacle of the masked players.</p><p>One of the visitors noticed '
     'me listening. “Beautiful music, don’t you think?”</p><p>“It’s not bad,” '
     'I said stiffly. “The viol brings the right sense of warmth to the piece, '
     'but the guitarist is overplaying his part. Still, he adds a certain '
     'plangent brio to an otherwise introspective '
     'composition...”</p><p>Unwilling to interrupt the concert we slipped past '
     'the musicians into the door to.... </p>',
 37: '<p>...a long, open room with no roof.</p><p>“What is going on here?” '
     'they wondered.</p><p>“Sometimes, important messages are couched in '
     'ambiguous terms,” I said. “That net may help you catch the answer to '
     'your question.”</p><p>They looked doubtful. “We must look at this from '
     'all sides before we make a decision.” At last, they were '
     'learning.</p><p>They really couldn’t decide which way to go; half of '
     'them wanted to go one way, half another. They were close to splitting up '
     'when there was a rattling sound and one of the doors was shaken from the '
     'other side.</p><p>They all stopped talking and moved closer together. '
     'They soon agreed on a direction and we departed for...</p>',
 38: '<p>...a narrow space where one wall boasted half-finished carving and '
     'another some sort of carnival poster. There was a little confusion as we '
     'made our entrance but we soon sorted ourselves out.</p><p>It was '
     'impossible to climb up the slippery slide and another door wouldn’t open '
     'for us, so after emptying the pebbles from our shoes, we marched on '
     'to...</p>',
 39: '<p>...what looked like a combination wine cellar and junk room. Someone '
     'had been working here as well.</p><p>“This is more to my taste,” said '
     'one, dusting off some labels. All the bottles turned out to be '
     'empty.</p><p>“I hear someone hammering,” said one.</p><p>“No, that’s a '
     'chopping sound,” said another.</p><p>None of them heard the faint '
     'jingling that came from behind the wall. “I don’t hear anything,” I said '
     'loudly and, with as much commotion as possible, hurried them out of the '
     'room to...</p>',
 40: '<p>...the foundation of the Maze. Deep underground stones had been '
     'carved and fitted; passages opened in the natural rock.</p><p>“These '
     'symbols are quite unusual,” said one. “They seem to be primitive '
     'signs...”</p><p>“Do you know what signs?” I asked him.</p><p>“Oh, you '
     'know... wind and water, hills and planets.”</p><p>It was surprising that '
     'he could identify any of the symbols, but I was relieved that he '
     'couldn’t read them correctly.</p><p>Choosing more or less at random they '
     'went through a passageway to...</p>',
 41: '<p>...a room with a special piece of furniture I thought might appeal to '
     'my guests.</p><p>“How can we trust that thing?” one remarked. “Who knows '
     'where it ends up...”</p><p>I knew naturally, but that wasn’t the point. '
     'They were pretty sure of themselves, and went right on to...</p>',
 42: '<p>...the next room.</p><p>In one corner a savage animal appeared ready '
     'to leap out, roaring, rending with tusk and claw...but it was only a bit '
     'of taxidermy after all.</p><p>I suggested they might wish to hang up '
     'their coats before going on.</p><p>“How will we find them?” one asked. '
     '“We might not pass through here again.”</p><p>I assured them I would '
     'help them to return. “You can count on me,” I said sincerely. Still, '
     'they wouldn’t leave anything behind.</p><p>Opening one of the doors we '
     'made our way to...</p>',
 43: '<p>...a great hall dominated by the entrance to room 22. The face over '
     'the door had a sly look.</p><p>“Is it good or bad to have only two '
     'choices?” they wanted to know.</p><p>It was, predictably enough, neither '
     '“good” not “bad.” These people just didn’t know how to phrase a '
     'meaningful question. You have to be very particular in this '
     'House.</p><p>We went on to...</p>',
 44: '<p>...a courtyard of palms and statues. The trees waved to each other in '
     'the breeze.</p><p>“Who left the door open?” they wanted to '
     'know.</p><p>“We came in that way,” I offered, but they were convinced we '
     'had entered by another door entirely.</p><p>They vanished through the '
     'wall and I followed them to...</p>',
 45: '<p>...the room at the center of the Maze.</p><p>My guests thought that '
     'whoever lived here was a careless person, to leave so many things '
     'around. They were wrong.</p><p>There was really only one thing for them '
     'to find: the Riddle of the Maze. They demanded that I show it to '
     'them.</p><p>“Do you think it is written on the wall for all to see? It '
     'is hidden here, somewhere, perhaps throughout the room. As far as you '
     'are concerned, what the Maze teaches can be learned in every '
     'room.”</p><p>They looked and looked...every group is the '
     'same.</p><p>“Now,” I said, after a last look around, “we must find our '
     'way back out.”</p><p>Leaving the center of the Maze we found ourselves '
     'in...</p>'}

image_maps_100_percent = {1: '<map name="image-map">\n'
    '    <area target="" alt="Room 20" title="Room 20" href="room20.html" '
    'coords="476,212,879,966" shape="rect">\n'
    '    <area target="" alt="Room 26" title="Room 26" href="room26.html" '
    'coords="954,954,1348,210" shape="rect">\n'
    '    <area target="" alt="Room 41" title="Room 41" href="room41.html" '
    'coords="1401,209,1600,181,1598,1059,1413,972" shape="poly">\n'
    '    <area target="" alt="Room 21" title="Room 21" href="room21.html" '
    'coords="1888,1213,1663,1099,1663,176,1890,143" shape="poly">\n'
    '</map>',
 2: '<map name="image-map">\n'
    '    <area target="" alt="Room 22" title="Room 22" href="room22.html" '
    'coords="751,979,1256,279" shape="rect">\n'
    '    <area target="" alt="Room 29" title="Room 29" href="room29.html" '
    'coords="203,1258,449,1094,446,240,195,210" shape="poly">\n'
    '    <area target="" alt="Room 12" title="Room 12" href="room12.html" '
    'coords="1800,1271,1551,1108,1578,220,1798,177" shape="poly">\n'
    '</map>',
 3: '<map name="image-map">\n'
    '    <area target="" alt="Room 33" title="Room 33" href="room33.html" '
    'coords="101,1383,304,1168,297,127,92,94" shape="poly">\n'
    '    <area target="" alt="Room 9" title="Room 9" href="room9.html" '
    'coords="1017,141,1357,915" shape="rect">\n'
    '    <area target="" alt="Room 18" title="Room 18" href="room18.html" '
    'coords="1792,75,1572,108,1570,1074,1770,1259" shape="poly">\n'
    '</map>',
 4: '<map name="image-map">\n'
    '    <area target="" alt="Room 44" title="Room 44" href="room44.html" '
    'coords="163,98,462,207,422,1246,149,1452" shape="poly">\n'
    '    <area target="" alt="Room 29" title="Room 29" href="room29.html" '
    'coords="557,254,688,300,667,1053,541,1142" shape="poly">\n'
    '    <area target="" alt="Room 15" title="Room 15" href="room15.html" '
    'coords="709,1019,776,965,793,340,715,314" shape="poly">\n'
    '    <area target="" alt="Room 11" title="Room 11" href="room11.html" '
    'coords="904,366,1076,896" shape="rect">\n'
    '    <area target="" alt="Room 16" title="Room 16" href="room16.html" '
    'coords="1266,1039,1194,990,1190,338,1276,305" shape="poly">\n'
    '    <area target="" alt="Room 24" title="Room 24" href="room24.html" '
    'coords="1311,297,1446,245,1430,1163,1316,1077" shape="poly">\n'
    '    <area target="" alt="Room 43" title="Room 43" href="room43.html" '
    'coords="1542,1273,1827,1437,1825,111,1539,218" shape="poly">\n'
    '</map>',
 5: '<map name="image-map">\n'
    '    <area target="" alt="Room 43" title="Room 43" href="room43.html" '
    'coords="165,309,408,978" shape="rect">\n'
    '    <area target="" alt="Room 22" title="Room 22" href="room22.html" '
    'coords="616,302,853,977" shape="rect">\n'
    '    <area target="" alt="Room 30" title="Room 30" href="room30.html" '
    'coords="1080,963,1326,315" shape="rect">\n'
    '    <area target="" alt="Room 20" title="Room 20" href="room20.html" '
    'coords="1515,975,1786,346" shape="rect">\n'
    '</map>',
 6: '<map name="image-map">\n'
    '    <area target="" alt="Room 40" title="Room 40" href="room40.html" '
    'coords="109,1393,435,1287,604,475,401,363,178,688" shape="poly">\n'
    '</map>',
 7: '<map name="image-map">\n'
    '    <area target="" alt="Room 33" title="Room 33" href="room33.html" '
    'coords="217,1284,497,1078,514,113,191,62" shape="poly">\n'
    '    <area target="" alt="Room 36" title="Room 36" href="room36.html" '
    'coords="778,1013,1188,130" shape="rect">\n'
    '    <area target="" alt="Room 16" title="Room 16" href="room16.html" '
    'coords="1744,1282,1476,1078,1471,96,1799,62" shape="poly">\n'
    '</map>',
 8: '<map name="image-map">\n'
    '    <area target="" alt="Room 31" title="Room 31" href="room31.html" '
    'coords="78,575,82,813,475,1507,703,1452,282,542" shape="poly">\n'
    '    <area target="" alt="Room 6" title="Room 6" href="room6.html" '
    'coords="606,512,467,546,796,1239,873,1123" shape="poly">\n'
    '    <area target="" alt="Room 29" title="Room 29" href="room29.html" '
    'coords="1011,994,1248,881,991,350,777,443" shape="poly">\n'
    '    <area target="" alt="Room 12" title="Room 12" href="room12.html" '
    'coords="1443,847,1649,928,1256,159,1164,260" shape="poly">\n'
    '</map>',
 9: '<map name="image-map">\n'
    '    <area target="" alt="Room 3" title="Room 3" href="room3.html" '
    'coords="217,1305,388,1184,405,454,209,355" shape="poly">\n'
    '    <area target="" alt="Room 18" title="Room 18" href="room18.html" '
    'coords="1244,1040,1546,419" shape="rect">\n'
    '</map>',
 10: '<map name="image-map">\n'
     '    <area target="" alt="Room 34" title="Room 34" href="room34.html" '
     'coords="103,153,488,942" shape="rect">\n'
     '    <area target="" alt="Room 41" title="Room 41" href="room41.html" '
     'coords="1318,157,1032,169,1055,1044,1299,1162" shape="poly">\n'
     '    <area target="" alt="Room 14" title="Room 14" href="room14.html" '
     'coords="1803,104,1417,146,1431,1229,1748,1362" shape="poly">\n'
     '</map>',
 11: '<map name="image-map">\n'
     '    <area target="" alt="Room 40" title="Room 40" href="room40.html" '
     'coords="546,502,258,1026" shape="rect">\n'
     '    <area target="" alt="Room 24" title="Room 24" href="room24.html" '
     'coords="1657,497,1376,1028" shape="rect">\n'
     '</map>',
 12: '<map name="image-map">\n'
     '    <area target="" alt="Room 2" title="Room 2" href="" '
     'coords="109,88,565,116,538,1080,228,1313" shape="poly">\n'
     '    <area target="" alt="Room 21" title="Room 21" href="" '
     'coords="1280,150,678,138,688,988,815,990,866,921,1092,920,1143,988,1246,983" '
     'shape="poly">\n'
     '    <area target="" alt="Room 39" title="Room 39" href="" '
     'coords="731,1280,796,1134,748,1155,707,1040,871,984,914,1027,1145,1066,1232,1283" '
     'shape="poly">\n'
     '    <area target="" alt="Room 8" title="Room 8" href="" '
     'coords="1827,1270,1677,1271,1437,1075,1422,110,1838,103" shape="poly">\n'
     '</map>',
 13: '<map name="image-map">\n'
     '    <area target="" alt="Room 27" title="Room 27" href="room27.html" '
     'coords="439,119,226,61,150,63,135,197,85,181,85,1350,112,1354,226,1249,533,1050" '
     'shape="poly">\n'
     '    <area target="" alt="Room 18" title="Room 18" href="room18.html" '
     'coords="684,994,1281,1056,1307,1025,1283,173,708,187" shape="poly">\n'
     '    <area target="" alt="Room 25" title="Room 25" href="room25.html" '
     'coords="1891,1345,1856,1343,1434,1068,1522,106,1765,60,1891,62" '
     'shape="poly">\n'
     '</map>',
 14: '<map name="image-map">\n'
     '    <area target="" alt="Room 10" title="Room 10" href="room10.html" '
     'coords="433,1113,70,568" shape="rect">\n'
     '    <area target="" alt="Room 43" title="Room 43" href="room43.html" '
     'coords="1108,512,793,1108" shape="rect">\n'
     '    <area target="" alt="Room 24" title="Room 24" href="room24.html" '
     'coords="1800,1123,1433,515" shape="rect">\n'
     '</map>',
 15: '<map name="image-map">\n'
     '    <area target="" alt="Room 30" title="Room 30" href="room30.html" '
     'coords="842,319,541,1015" shape="rect">\n'
     '    <area target="" alt="Room 37" title="Room 37" href="room37.html" '
     'coords="1389,320,1100,1041" shape="rect">\n'
     '    <area target="" alt="Room 3" title="Room 3" href="room3.html" '
     'coords="1751,253,1557,287,1560,442,1443,449,1438,1244,1637,1191,1757,1274" '
     'shape="poly">\n'
     '</map>',
 16: '<map name="image-map">\n'
     '    <area target="" alt="Room 36" title="Room 36" href="room36.html" '
     'coords="100,52,155,64,311,132,306,1118,100,1236,61,372" shape="poly">\n'
     '    <area target="" alt="Room 7" title="Room 7" href="room7.html" '
     'coords="1763,1246,1559,1110,1505,423,1577,108,1721,54,1820,359" '
     'shape="poly">\n'
     '</map>',
 17: '<map name="image-map">\n'
     '    <area target="" alt="Room 45" title="Room 45" href="room45.html" '
     'coords="738,61,1140,936" shape="rect">\n'
     '    <area target="" alt="Room 33" title="Room 33" href="room33.html" '
     'coords="1479,156,1801,1324" shape="rect">\n'
     '    <area target="" alt="Room 6" title="Room 6" href="room6.html" '
     'coords="66,710,324,1324" shape="rect">\n'
     '</map>',
 18: '<map name="image-map">\n'
     '    <area target="" alt="Room 13" title="Room 13" href="room13.html" '
     'coords="779,204,1127,1091" shape="rect">\n'
     '    <area target="" alt="Room 3" title="Room 3" href="room3.html" '
     'coords="1480,212,1820,1077" shape="rect">\n'
     '</map>',
 19: '<map name="image-map">\n'
     '    <area target="" alt="Room 31" title="Room 31" href="room31.html" '
     'coords="390,43,677,1158" shape="rect">\n'
     '    <area target="" alt="Room 11" title="Room 11" href="room11.html" '
     'coords="753,123,958,1025" shape="rect">\n'
     '</map>',
 20: '<map name="image-map">\n'
     '    <area target="" alt="Room 5" title="Room 5" href="room5.html" '
     'coords="72,62,325,1214" shape="rect">\n'
     '    <area target="" alt="Room 27" title="Room 27" href="room27.html" '
     'coords="1077,105,1430,979" shape="rect">\n'
     '    <area target="" alt="Room 1" title="Room 1" href="room1.html" '
     'coords="1626,95,1884,1221" shape="rect">\n'
     '</map>',
 21: '<map name="image-map">\n'
     '    <area target="" alt="Room 44" title="Room 44" href="room44.html" '
     'coords="81,396,442,1287" shape="rect">\n'
     '    <area target="" alt="Room 24" title="Room 24" href="room24.html" '
     'coords="942,488,1205,1153" shape="rect">\n'
     '    <area target="" alt="Room 31" title="Room 31" href="room31.html" '
     'coords="1549,552,1759,1052" shape="rect">\n'
     '</map>',
 22: '<map name="image-map">\n'
     '    <area target="" alt="Room 43" title="Room 43" href="room43.html" '
     'coords="370,285,641,1080" shape="rect">\n'
     '    <area target="" alt="Room 38" title="Room 38" href="room38.html" '
     'coords="1219,294,1480,1111" shape="rect">\n'
     '</map>',
 23: '<map name="image-map">\n'
     '    <area target="" alt="Room 28" title="Room 28" href="room28.html" '
     'coords="16,294,306,1050" shape="rect">\n'
     '    <area target="" alt="Room 8" title="Room 8" href="room8.html" '
     'coords="488,289,790,1030" shape="rect">\n'
     '    <area target="" alt="Room 45" title="Room 45" href="room45.html" '
     'coords="966,296,1288,1037" shape="rect">\n'
     '    <area target="" alt="Room 19" title="Room 19" href="room19.html" '
     'coords="1441,232,1783,1221" shape="rect">\n'
     '</map>',
 24: '<map name="image-map">\n</map>',
 25: '<map name="image-map">\n'
     '    <area target="" alt="Room 34" title="Room 34" href="room34.html" '
     'coords="36,406,464,1266" shape="rect">\n'
     '    <area target="" alt="Room 13" title="Room 13" href="room13.html" '
     'coords="546,399,934,1249" shape="rect">\n'
     '    <area target="" alt="Room 35" title="Room 35" href="room35.html" '
     'coords="1445,402,1804,1278" shape="rect">\n'
     '</map>',
 26: '<map name="image-map">\n'
     '    <area target="" alt="Room 30" title="Room 30" href="room30.html" '
     'coords="158,213,373,1031" shape="rect">\n'
     '    <area target="" alt="Room 36" title="Room 36" href="room36.html" '
     'coords="457,295,789,978" shape="rect">\n'
     '    <area target="" alt="Room 38" title="Room 38" href="room38.html" '
     'coords="1172,259,1504,983" shape="rect">\n'
     '    <area target="" alt="Room 1" title="Room 1" href="room1.html" '
     'coords="1598,217,1812,1039" shape="rect">\n'
     '</map>',
 27: '<map name="image-map">\n'
     '    <area target="" alt="Room 13" title="Room 13" href="room13.html" '
     'coords="194,222,530,1202" shape="rect">\n'
     '    <area target="" alt="Room 9" title="Room 9" href="room9.html" '
     'coords="791,896,1194,1381" shape="rect">\n'
     '</map>',
 28: '<map name="image-map">\n'
     '    <area target="" alt="Room 23" title="Room 23" href="room23.html" '
     'coords="191,98,468,1179" shape="rect">\n'
     '    <area target="" alt="Room 43" title="Room 43" href="room43.html" '
     'coords="746,135,1165,910" shape="rect">\n'
     '    <area target="" alt="Room 32" title="Room 32" href="room32.html" '
     'coords="679,940,1220,1288" shape="rect">\n'
     '    <area target="" alt="Room 45" title="Room 45" href="room45.html" '
     'coords="1457,109,1747,1251" shape="rect">\n'
     '</map>',
 29: '<map name="image-map">\n'
     '    <area target="" alt="Room 8" title="Room 8" href="room8.html" '
     'coords="93,311,302,1389" shape="rect">\n'
     '    <area target="" alt="Room 40" title="Room 40" href="room40.html" '
     'coords="358,281,550,1046" shape="rect">\n'
     '    <area target="" alt="Room 35" title="Room 35" href="room35.html" '
     'coords="1027,259,1350,894" shape="rect">\n'
     '    <area target="" alt="Room 2" title="Room 2" href="room2.html" '
     'coords="1396,258,1529,1056" shape="rect">\n'
     '</map>',
 30: '<map name="image-map">\n'
     '    <area target="" alt="Room 42" title="Room 42" href="room42.html" '
     'coords="336,87,507,1022" shape="rect">\n'
     '    <area target="" alt="Room 34" title="Room 34" href="room34.html" '
     'coords="786,56,1167,922" shape="rect">\n'
     '    <area target="" alt="Room 5" title="Room 5" href="room5.html" '
     'coords="1473,99,1608,1048" shape="rect">\n'
     '    <area target="" alt="Room 15" title="Room 15" href="room15.html" '
     'coords="1673,60,1872,1222" shape="rect">\n'
     '</map>',
 31: '<map name="image-map">\n'
     '    <area target="" alt="Room 44" title="Room 44" href="room44.html" '
     'coords="153,326,432,1199" shape="rect">\n'
     '    <area target="" alt="Room 19" title="Room 19" href="room19.html" '
     'coords="642,430,857,1100" shape="rect">\n'
     '    <area target="" alt="Room 21" title="Room 21" href="room21.html" '
     'coords="1494,351,1776,1231" shape="rect">\n'
     '</map>',
 32: '<map name="image-map">\n'
     '    <area target="" alt="Room 11" title="Room 11" href="room11.html" '
     'coords="93,355,373,1240" shape="rect">\n'
     '    <area target="" alt="Room 6" title="Room 6" href="room6.html" '
     'coords="783,232,1169,989" shape="rect">\n'
     '    <area target="" alt="Room 16" title="Room 16" href="room16.html" '
     'coords="506,904,652,789,725,1081,1385,1129,1407,1466,533,1470" '
     'shape="poly">\n'
     '    <area target="" alt="Room 28" title="Room 28" href="room28.html" '
     'coords="1661,527,1868,1339" shape="rect">\n'
     '</map>',
 33: '<map name="image-map">\n'
     '    <area target="" alt="Room 3" title="Room 3" href="room3.html" '
     'coords="138,185,419,1319" shape="rect">\n'
     '    <area target="" alt="Room 35" title="Room 35" href="room35.html" '
     'coords="994,168,1444,1037" shape="rect">\n'
     '    <area target="" alt="Room 7" title="Room 7" href="room7.html" '
     'coords="1499,163,1746,1303" shape="rect">\n'
     '</map>',
 34: '<map name="image-map">\n'
     '    <area target="" alt="Room 10" title="Room 10" href="room10.html" '
     'coords="59,32,424,1247" shape="rect">\n'
     '    <area target="" alt="Room 25" title="Room 25" href="room25.html" '
     'coords="495,119,840,993" shape="rect">\n'
     '</map>',
 35: '<map name="image-map">\n'
     '    <area target="" alt="Room 33" title="Room 33" href="room33.html" '
     'coords="90,252,457,943" shape="rect">\n'
     '</map>',
 36: '<map name="image-map">\n'
     '    <area target="" alt="Room 7" title="Room 7" href="room7.html" '
     'coords="70,61,344,1221" shape="rect">\n'
     '    <area target="" alt="Room 16" title="Room 16" href="room16.html" '
     'coords="521,153,850,1038" shape="rect">\n'
     '</map>',
 37: '<map name="image-map">\n'
     '    <area target="" alt="Room 15" title="Room 15" href="room15.html" '
     'coords="96,119,494,992" shape="rect">\n'
     '    <area target="" alt="Room 10" title="Room 10" href="room10.html" '
     'coords="577,145,946,971" shape="rect">\n'
     '    <area target="" alt="Room 42" title="Room 42" href="room42.html" '
     'coords="1026,140,1412,963" shape="rect">\n'
     '    <area target="" alt="Room 20" title="Room 20" href="room20.html" '
     'coords="1495,145,1864,966" shape="rect">\n'
     '</map>',
 38: '<map name="image-map">\n'
     '    <area target="" alt="Room 40" title="Room 40" href="room40.html" '
     'coords="837,256,1250,1000" shape="rect">\n'
     '    <area target="" alt="Room 22" title="Room 22" href="room22.html" '
     'coords="1374,270,1518,1137" shape="rect">\n'
     '    <area target="" alt="Room 43" title="Room 43" href="room43.html" '
     'coords="1627,206,1838,1345" shape="rect">\n'
     '</map>',
 39: '<map name="image-map">\n'
     '    <area target="" alt="Room 11" title="Room 11" href="room11.html" '
     'coords="120,158,352,1248" shape="rect">\n'
     '    <area target="" alt="Room 4" title="Room 4" href="room4.html" '
     'coords="470,190,643,902" shape="rect">\n'
     '    <area target="" alt="Room 12" title="Room 12" href="room12.html" '
     'coords="1333,187,1511,983" shape="rect">\n'
     '</map>',
 40: '<map name="image-map">\n'
     '    <area target="" alt="Room 11" title="Room 11" href="room11.html" '
     'coords="49,166,330,1285" shape="rect">\n'
     '    <area target="" alt="Room 6" title="Room 6" href="room6.html" '
     'coords="549,334,822,1208" shape="rect">\n'
     '    <area target="" alt="Room 38" title="Room 38" href="room38.html" '
     'coords="1025,377,1223,978" shape="rect">\n'
     '</map>',
 41: '<map name="image-map">\n'
     '    <area target="" alt="Room 1" title="Room 1" href="room1.html" '
     'coords="145,10,393,1091" shape="rect">\n'
     '    <area target="" alt="Room 35" title="Room 35" href="room35.html" '
     'coords="444,32,711,969" shape="rect">\n'
     '    <area target="" alt="Room 10" title="Room 10" href="room10.html" '
     'coords="785,105,1144,886" shape="rect">\n'
     '    <area target="" alt="Room 38" title="Room 38" href="room38.html" '
     'coords="1499,10,1769,1157" shape="rect">\n'
     '</map>',
 42: '<map name="image-map">\n'
     '    <area target="" alt="Room 22" title="Room 22" href="room22.html" '
     'coords="72,49,330,1304" shape="rect">\n'
     '    <area target="" alt="Room 30" title="Room 30" href="room30.html" '
     'coords="360,133,553,1102" shape="rect">\n'
     '    <area target="" alt="Room 4" title="Room 4" href="room4.html" '
     'coords="670,201,975,974" shape="rect">\n'
     '    <area target="" alt="Room 25" title="Room 25" href="room25.html" '
     'coords="1076,199,1397,983" shape="rect">\n'
     '    <area target="" alt="Room 37" title="Room 37" href="room37.html" '
     'coords="1500,196,1820,964" shape="rect">\n'
     '</map>',
 43: '<map name="image-map">\n'
     '    <area target="" alt="Room 22" title="Room 22" href="room22.html" '
     'coords="731,47,1192,928" shape="rect">\n'
     '    <area target="" alt="Room 38" title="Room 38" href="room38.html" '
     'coords="736,986,1233,1373" shape="rect">\n'
     '</map>',
 44: '<map name="image-map">\n'
     '    <area target="" alt="Room 21" title="Room 21" href="room21.html" '
     'coords="591,361,906,1027" shape="rect">\n'
     '    <area target="" alt="Room 18" title="Room 18" href="room18.html" '
     'coords="1447,369,1805,1056" shape="rect">\n'
     '</map>',
 45: '<map name="image-map">\n'
     '    <area target="" alt="Room 28" title="Room 28" href="room28.html" '
     'coords="95,113,389,1198" shape="rect">\n'
     '    <area target="" alt="Room 17" title="Room 17" href="room17.html" '
     'coords="407,85,606,948" shape="rect">\n'
     '    <area target="" alt="Room 36" title="Room 36" href="room36.html" '
     'coords="812,92,1190,903" shape="rect">\n'
     '    <area target="" alt="Room 19" title="Room 19" href="room19.html" '
     'coords="1423,101,1619,1038" shape="rect">\n'
     '    <area target="" alt="Room 23" title="Room 23" href="room23.html" '
     'coords="1664,116,1898,1267" shape="rect">\n'
     '</map>'}

image_map_data = {1: [('20', 'rect', '476,212,879,966'),
     ('26', 'rect', '954,954,1348,210'),
     ('41', 'poly', '1401,209,1600,181,1598,1059,1413,972'),
     ('21', 'poly', '1888,1213,1663,1099,1663,176,1890,143')],
 2: [('22', 'rect', '751,979,1256,279'),
     ('29', 'poly', '203,1258,449,1094,446,240,195,210'),
     ('12', 'poly', '1800,1271,1551,1108,1578,220,1798,177')],
 3: [('33', 'poly', '101,1383,304,1168,297,127,92,94'),
     ('9', 'rect', '1017,141,1357,915'),
     ('18', 'poly', '1792,75,1572,108,1570,1074,1770,1259')],
 4: [('44', 'poly', '163,98,462,207,422,1246,149,1452'),
     ('29', 'poly', '557,254,688,300,667,1053,541,1142'),
     ('15', 'poly', '709,1019,776,965,793,340,715,314'),
     ('11', 'rect', '904,366,1076,896'),
     ('16', 'poly', '1266,1039,1194,990,1190,338,1276,305'),
     ('24', 'poly', '1311,297,1446,245,1430,1163,1316,1077'),
     ('43', 'poly', '1542,1273,1827,1437,1825,111,1539,218')],
 5: [('43', 'rect', '165,309,408,978'),
     ('22', 'rect', '616,302,853,977'),
     ('30', 'rect', '1080,963,1326,315'),
     ('20', 'rect', '1515,975,1786,346')],
 6: [('40', 'poly', '109,1393,435,1287,604,475,401,363,178,688')],
 7: [('33', 'poly', '217,1284,497,1078,514,113,191,62'),
     ('36', 'rect', '778,1013,1188,130'),
     ('16', 'poly', '1744,1282,1476,1078,1471,96,1799,62')],
 8: [('31', 'poly', '78,575,82,813,475,1507,703,1452,282,542'),
     ('6', 'poly', '606,512,467,546,796,1239,873,1123'),
     ('29', 'poly', '1011,994,1248,881,991,350,777,443'),
     ('12', 'poly', '1443,847,1649,928,1256,159,1164,260')],
 9: [('3', 'poly', '217,1305,388,1184,405,454,209,355'),
     ('18', 'rect', '1244,1040,1546,419')],
 10: [('34', 'rect', '103,153,488,942'),
      ('41', 'poly', '1318,157,1032,169,1055,1044,1299,1162'),
      ('14', 'poly', '1803,104,1417,146,1431,1229,1748,1362')],
 11: [('40', 'rect', '546,502,258,1026'), ('24', 'rect', '1657,497,1376,1028')],
 12: [('2', 'poly', '109,88,565,116,538,1080,228,1313'),
      ('21',
       'poly',
       '1280,150,678,138,688,988,815,990,866,921,1092,920,1143,988,1246,983'),
      ('39',
       'poly',
       '731,1280,796,1134,748,1155,707,1040,871,984,914,1027,1145,1066,1232,1283'),
      ('8', 'poly', '1827,1270,1677,1271,1437,1075,1422,110,1838,103')],
 13: [('27',
       'poly',
       '439,119,226,61,150,63,135,197,85,181,85,1350,112,1354,226,1249,533,1050'),
      ('18', 'poly', '684,994,1281,1056,1307,1025,1283,173,708,187'),
      ('25', 'poly', '1891,1345,1856,1343,1434,1068,1522,106,1765,60,1891,62')],
 14: [('10', 'rect', '433,1113,70,568'),
      ('43', 'rect', '1108,512,793,1108'),
      ('24', 'rect', '1800,1123,1433,515')],
 15: [('30', 'rect', '842,319,541,1015'),
      ('37', 'rect', '1389,320,1100,1041'),
      ('3',
       'poly',
       '1751,253,1557,287,1560,442,1443,449,1438,1244,1637,1191,1757,1274')],
 16: [('36', 'poly', '100,52,155,64,311,132,306,1118,100,1236,61,372'),
      ('7', 'poly', '1763,1246,1559,1110,1505,423,1577,108,1721,54,1820,359')],
 17: [('45', 'rect', '738,61,1140,936'),
      ('33', 'rect', '1479,156,1801,1324'),
      ('6', 'rect', '66,710,324,1324')],
 18: [('13', 'rect', '779,204,1127,1091'), ('3', 'rect', '1480,212,1820,1077')],
 19: [('31', 'rect', '390,43,677,1158'), ('11', 'rect', '753,123,958,1025')],
 20: [('5', 'rect', '72,62,325,1214'),
      ('27', 'rect', '1077,105,1430,979'),
      ('1', 'rect', '1626,95,1884,1221')],
 21: [('44', 'rect', '81,396,442,1287'),
      ('24', 'rect', '942,488,1205,1153'),
      ('31', 'rect', '1549,552,1759,1052')],
 22: [('43', 'rect', '370,285,641,1080'), ('38', 'rect', '1219,294,1480,1111')],
 23: [('28', 'rect', '16,294,306,1050'),
      ('8', 'rect', '488,289,790,1030'),
      ('45', 'rect', '966,296,1288,1037'),
      ('19', 'rect', '1441,232,1783,1221')],
 24: [],
 25: [('34', 'rect', '36,406,464,1266'),
      ('13', 'rect', '546,399,934,1249'),
      ('35', 'rect', '1445,402,1804,1278')],
 26: [('30', 'rect', '158,213,373,1031'),
      ('36', 'rect', '457,295,789,978'),
      ('38', 'rect', '1172,259,1504,983'),
      ('1', 'rect', '1598,217,1812,1039')],
 27: [('13', 'rect', '194,222,530,1202'), ('9', 'rect', '791,896,1194,1381')],
 28: [('23', 'rect', '191,98,468,1179'),
      ('43', 'rect', '746,135,1165,910'),
      ('32', 'rect', '679,940,1220,1288'),
      ('45', 'rect', '1457,109,1747,1251')],
 29: [('8', 'rect', '93,311,302,1389'),
      ('40', 'rect', '358,281,550,1046'),
      ('35', 'rect', '1027,259,1350,894'),
      ('2', 'rect', '1396,258,1529,1056')],
 30: [('42', 'rect', '336,87,507,1022'),
      ('34', 'rect', '786,56,1167,922'),
      ('5', 'rect', '1473,99,1608,1048'),
      ('15', 'rect', '1673,60,1872,1222')],
 31: [('44', 'rect', '153,326,432,1199'),
      ('19', 'rect', '642,430,857,1100'),
      ('21', 'rect', '1494,351,1776,1231')],
 32: [('11', 'rect', '93,355,373,1240'),
      ('6', 'rect', '783,232,1169,989'),
      ('16', 'poly', '506,904,652,789,725,1081,1385,1129,1407,1466,533,1470'),
      ('28', 'rect', '1661,527,1868,1339')],
 33: [('3', 'rect', '138,185,419,1319'),
      ('35', 'rect', '994,168,1444,1037'),
      ('7', 'rect', '1499,163,1746,1303')],
 34: [('10', 'rect', '59,32,424,1247'), ('25', 'rect', '495,119,840,993')],
 35: [('33', 'rect', '90,252,457,943')],
 36: [('7', 'rect', '70,61,344,1221'), ('16', 'rect', '521,153,850,1038')],
 37: [('15', 'rect', '96,119,494,992'),
      ('10', 'rect', '577,145,946,971'),
      ('42', 'rect', '1026,140,1412,963'),
      ('20', 'rect', '1495,145,1864,966')],
 38: [('40', 'rect', '837,256,1250,1000'),
      ('22', 'rect', '1374,270,1518,1137'),
      ('43', 'rect', '1627,206,1838,1345')],
 39: [('11', 'rect', '120,158,352,1248'),
      ('4', 'rect', '470,190,643,902'),
      ('12', 'rect', '1333,187,1511,983')],
 40: [('11', 'rect', '49,166,330,1285'),
      ('6', 'rect', '549,334,822,1208'),
      ('38', 'rect', '1025,377,1223,978')],
 41: [('1', 'rect', '145,10,393,1091'),
      ('35', 'rect', '444,32,711,969'),
      ('10', 'rect', '785,105,1144,886'),
      ('38', 'rect', '1499,10,1769,1157')],
 42: [('22', 'rect', '72,49,330,1304'),
      ('30', 'rect', '360,133,553,1102'),
      ('4', 'rect', '670,201,975,974'),
      ('25', 'rect', '1076,199,1397,983'),
      ('37', 'rect', '1500,196,1820,964')],
 43: [('22', 'rect', '731,47,1192,928'), ('38', 'rect', '736,986,1233,1373')],
 44: [('21', 'rect', '591,361,906,1027'), ('18', 'rect', '1447,369,1805,1056')],
 45: [('28', 'rect', '95,113,389,1198'),
      ('17', 'rect', '407,85,606,948'),
      ('36', 'rect', '812,92,1190,903'),
      ('19', 'rect', '1423,101,1619,1038'),
      ('23', 'rect', '1664,116,1898,1267')]}



PAGE_LINKS = ['<a href="index.html">Home</a>']
for i in range(1, 46):
    PAGE_LINKS.append(f'<a href="room{i}.html">{i}</a>')
PAGE_LINKS = ' | '.join(PAGE_LINKS)


for i in range(1, 46):
    print(f'Generating room #{i}...')
    image_map_html = ''
    for data in image_map_data[i]:
        dest, shape, coords = data
        # Thumbnails are 25% resized
        coords = ','.join([str(int(c) // 4) for c in coords.split(',')])
        image_map_html += f'<area target="" alt="Room {dest}" title="Room {dest}" href="room{dest}.html" coords="{coords}" shape="{shape}">\n'

    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Room {i}</title>
    <link rel="stylesheet" href="css/maze.css">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container">
  <div class="row">
    <div class="col-12 col-lg-6">
    {text[i]}
    </div>
    <div class="col-12 col-lg-6">
    <img src="images/room{i}_thumb.jpg" class="maze-room-img-thumb" usemap="#image-map"><br>
    <a href="images/room{i}.jpg" class="zoom-icon">&#128269;</a>
    <map name="image-map">
        {image_map_html}
    </map>
    </div>
  </div>

  <div class="row">
    <div class="col-12">
      <p class="bottom-page-links">{PAGE_LINKS}</p>
    </div>
  </div>
</div>
</body>
</html>
'''

    print(f'Generating room{i}.html...')
    with open(f'../mazewebsite/room{i}.html', 'w') as fo:
        fo.write(content)








