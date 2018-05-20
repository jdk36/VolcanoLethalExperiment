import random;

def map_minions(minions_hp):
    minion_map = dict();
    count = 1;
    for minion in minions_hp.keys():
        minion_map[count] = minion;
        count+=1;
    return minion_map;

def handle_deaths(minions_hp):
    to_delete = None;
    for minion in minions_hp.keys():
        if minions_hp[minion] == 0:
            to_delete = minion;
    if to_delete:
        del minions_hp[to_delete];
    return minions_hp;

def all_keys_in_dict(key_list, dictionary):
    return_val = True;
    for key in key_list:
        if not key in dictionary:
            return_val = False;
    return return_val;

TRIALS = 1000000;
portal_first = True;
totem_first = True;
portal_spell_dmg_only = False;
fix_spell_dmg_roll = False;
fix_no_spell_dmg = False;
fix_shieldbearer = True;
successes = 0;

for i in range(0,TRIALS):

    ## setup the board
    minions_hp = dict();
    portal = 0;
    spell_dmg = False;

    ## roll a totem
    if totem_first:
        totem = random.randint(1,4);
        if fix_no_spell_dmg:
            totem = random.randint(2,4);
        if totem == 1 or fix_spell_dmg_roll:
            minions_hp["totem"]= 2;
            if portal_spell_dmg_only:
                portal_first = True;
            spell_dmg = True;
        elif totem == 2 or totem == 3:
            minions_hp["totem"] = 2;
        else:
            minions_hp["totem"] = 1;

    ## use maelstrom portal
    if portal_first:
        portal = 1;
        if spell_dmg:
            portal = 2;
        ## 37 minions with 1hp
        ## 15 minions with 2hp
        ## 5 minions with 3hp
        ## shieldbearer EleGiggle
        sel = random.randint(1, 58);
        if sel <= 37:
            hp = 1;
        elif sel <= 52:
            hp = 2;
        elif sel <= 57:
            hp = 3;
        else:
            hp = 4;
        if fix_shieldbearer:
            hp = 4;
        minions_hp["portal_minion"] = hp;

    non_random_minions = {
      "elephant": 6 - portal,
      "fandral": 3 - portal,
      "6/6 jade": 6 - portal,
      "hammer thing":2,
      "3/3 jade": 3,
      "flametongue": 3,
    }

    minions_hp.update(non_random_minions);

    ## Volcano!
    for j in range(0, 15):
        minion_map = map_minions(minions_hp);
        dmg = random.randint(1, len(minions_hp));
        minion_hurt = minion_map[dmg];
        minions_hp[minion_hurt] -= 1;
        minions_hp = handle_deaths(minions_hp);

    ## Is it lethal?
    if portal_first:
        elephant_died = not "elephant" in minions_hp
    else:
        elephant_died = not "elephant" in minions_hp or \
        minions_hp["elephant"] == 1;
        if totem_first:
            if spell_dmg and "totem" in minions_hp:
                elephant_died = elephant_died or minions_hp["elephant"] == 2;
        else:
            totem = random.randint(1, 4);
            if totem == 1:
                elephant_died = elephant_died or minions_hp["elephant"] == 2;

    attackers_lived = all_keys_in_dict(list(["3/3 jade", \
    "hammer thing", "flametongue"]), minions_hp);

    success = elephant_died and attackers_lived;

    ## Print success/failure
    if success:
        successes+=1;

success_rate = float(successes) / TRIALS;
print(successes);
print(success_rate);

print(minions_hp);
