

Here's a clip of the situation:

https://clips.twitch.tv/TangentialDeterminedCockroachMoreCowbell

So Stan has lethal on board, but unfortunately there's a taunt in the way. In order to kill his opponent, Volcano would have to kill the taunt, while also not killing any of Stan's 3 minions. He has totem and portal which he can play before, or after the Volcano, to change his odds. The maelstrom will summon one of 58 one drops. The breakdown is:

37 - 1hp

15 - 2hp

5 - 3hp

1 - 4hp

To win without volcano, Stan needs to hit exactly Fire Elemental into Kalimos. Since he has 12 cards left in his deck at this point, the odds of this are 1/(12*11) = 1/132 or roughly 0.76%. Is volcano better?

The answer is yes! Here are the odds of victory for various lines:

**Totem After, Portal After:** 1.2257%

Here, the taunt can live at 1hp, and Stan still wins, since he uses portal to clear it. If he rolls spell damage, the taunt can live at 2hp, and he wins.

**Totem First, Portal After:** 1.3676%

Again, Stan can portal a 3/1 taunt after the volcano, and in this case the totem's hp makes it less likely Stan's minions die. Additionally, there is the rare case where a spell damage totem lives, and portal will clear a 3/2 as well.

**Totem First, Portal First:** 1.54876%

Here, Stan gets not only the totem's hp but also the portal minion's hp to prevent his minions from dying. Also, 1/4 of the time the elephant will take 2 damage, making it easier to kill.

**ut we can do better.**

It turns out that it doesn't make sense to portal first unless we get spell damage. With no spell damage, the portal will do 1 damage to the taunt regardless (presuming it lives). When we portal first, we are taking 3hp off the board and adding a random 1 drop (average less than 3hp). This means that we're creating a net decrease in hp on the board, leading to a higher chance that our minions die. This effects our minions more than the elephant, because our minions constitute 3 targets whereas the elephant is only one target.

**Here are some trials with the totem rolls fixed which illustrate this:**

**Roll Spell Damage, Portal First:** 2.2538%

Elephant takes 2 damage from the portal, which makes a big difference in how often it dies.

**Roll Spell Damage, Portal After:** 1.7242%

Sometimes the spell damage totem lives, so a 3/2 elephant will die.

**Roll Non Spell Damage, Portal First:** 1.302%

(Taking hp off the board unnecessarily)

**Roll Non Spell Damage, Portal After:** 1.3546%

This is roughly .05% better than using portal first.

Therefore, the best possible line is to totem first, then portal if you roll a spell damage totem.

Totem, Portal Only With Spell Damage: 1.56054%

This is .01178% better than always using portal first, i.e. it matters in roughly 1/10,000 games.

And if you're curious, in the best case scenario Stan rolls spell damage, and then a shieldbearer off of maelstrom portal, for a whopping 2.876% chance of winning.

Most of these stats were found by running 500,000 or 1,000,000 trials. The most important two scenarios, portal first totem first and portal first totem only spell damage, were run with 5,000,000 trials.

**tl;dr:** Totem First, if you get spell damage, portal. Otherwise, wait until after the volcano to portal. Roll spell damage and shieldbearer for best results :)

Feel free to point out any mistakes!

**Edit:** Ah, you're right! I forgot to mention this doesn't take into account rolling Stonetusk Boar, Patches, or Mistress of Mixtures. In the boar and patches case, I suspect the odds of winning get a lot better (trade first of course). In the mistress case the mistress has to live or you lose.

**Edit2:** In the actual game, Stan goes for the Fire Ele into Kalimos play, misses it, and loses.

**Edit3:** In case anyone's curious, it is possible to do these calculations exactly, by recursively testing every possibility for the volcano (and the totem and portal too, if you're feeling ambitious). I wasn't sure if I had the memory for it, and didn't want to code the whole thing only to learn I couldn't run it, so I went the other route. The precision with 5m trials seems to be roughly +- .001%.
