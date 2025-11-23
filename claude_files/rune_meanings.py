"""
Rune Meanings for the Rune Fortune Teller
Uses the Younger Futhark (16 runes), historically used in Iceland during the Viking Age.

Each rune has interpretations tailored to LOVE, HEALTH, and FINANCE categories.
Voice: Skuld (the Norn of the future) - smart, contemporary, uses modern language naturally.
"""
import random 

# Younger Futhark runes with their traditional meanings
RUNES = {
    "ᚠ": {
        "name": "Fé",
        "traditional": "Wealth, cattle, money",
        "love": "Okay so here's the thing about Fé in your love life—it's literally the wealth rune, but we're talking emotional wealth here. You're either sitting on a goldmine of affection that you're not cashing in on, or you're about to receive some serious relationship dividends. Stop hoarding your feelings like they're bitcoin. Invest in vulnerability, and watch your connection compound. The energy's there, you just gotta spend it.",
        "health": "Fé's showing up to tell you that your body is your most valuable asset, and honestly? You've been treating it like a depreciating car. Time to reinvest. This could mean better food, actual sleep, or finally using that gym membership. Your health IS your wealth, and right now the market's telling you to diversify your self-care portfolio before you crash.",
        "finance": "This is literally the money rune, so like... yeah. Wealth is coming, or it's already here and you're not seeing it. Could be a raise, a side hustle popping off, or just finally getting your budget together. Either way, Fé's energy says abundance, but also warns against hoarding. Money flows best when it moves. Don't be weird about it."
    },
    "ᚢ": {
        "name": "Úr",
        "traditional": "Drizzle, slag, endurance",
        "love": "Úr's got that steady rain energy—not the cute romantic kind, more like the kind that soaks you to the bone. Your relationship's going through something challenging, something that tests endurance. But here's the plot twist: drizzle makes things grow. This rough patch? It's either going to strengthen your bond or wash away what wasn't real. Either way, you're gonna come out of this knowing what's solid.",
        "health": "Not gonna sugarcoat it—Úr's the endurance rune, which means you're in it for the long game right now. Could be chronic stuff, could be recovery that's taking forever, could just be that you're exhausted. The lesson here is persistence. Small consistent actions over flashy quick fixes. Your body's asking for patience, not miracles.",
        "finance": "Úr in finances means the grind is real. Like, REAL real. You're in the endurance phase where progress feels slow and kinda miserable. But that's the whole point—this isn't about overnight success, it's about building something that lasts through the rough weather. Keep showing up. The breakthrough comes after you prove you won't quit."
    },
    "ᚦ": {
        "name": "Þurs",
        "traditional": "Giant, thorn, chaos",
        "love": "Þurs is the giant, the thorn, the absolute CHAOS energy in relationships. Something big and kinda scary is happening—could be conflict, could be a massive realization, could be that you're finally seeing someone's true nature. Giants aren't subtle. This rune says: brace yourself, speak your truth even if it's uncomfortable, and don't let anyone gaslight you into thinking this disruption isn't real.",
        "health": "The giant's in your health situation, which usually means something's gotten too big to ignore. That weird symptom, that persistent pain, that mental health thing you've been minimizing—yeah, Þurs says it's time. Book the appointment. Have the hard conversation. Face the thorn. Giants look scarier before you actually confront them.",
        "finance": "A giant obstacle just walked into your financial situation, or it's been there and you're finally seeing how massive it is. Could be debt, could be a career decision, could be that your whole money mindset needs renovating. Þurs doesn't do gentle. It's disruptive. But destruction comes before reconstruction, so honestly? This might be exactly what needed to happen."
    },
    "ᚬ": {
        "name": "Áss",
        "traditional": "God, mouth, communication",
        "love": "Áss is the god-rune, the communication rune, the \"your words have power\" rune. In love, this means: SAY THE THING. Whatever you've been holding back, whatever conversation you've been avoiding, whatever truth is sitting in your throat—it's time. Divine timing says speak now. Your voice is literally the tool that shifts everything right now. Use it wisely, but use it.",
        "health": "Communication is healing, and Áss is here to remind you that your body's been trying to tell you something. Maybe you need to advocate for yourself with doctors. Maybe you need to actually talk about your mental health. Maybe you just need to stop ignoring the signals your body's sending. Listen to the divine wisdom of your own system. It's smarter than you think.",
        "finance": "The mouth-rune in finances means: network, negotiate, speak up. That raise won't ask for itself. That opportunity won't knock if nobody knows you're available. Your financial breakthrough is literally waiting on the other side of a conversation you're avoiding. Stop being humble to your own detriment. Divine energy backs confident communication right now."
    },
    "ᚱ": {
        "name": "Reið",
        "traditional": "Ride, journey, movement",
        "love": "Reið is the ride, the journey, the \"things are MOVING\" rune. Your love life is in active motion right now—could be moving forward, could be moving apart, could be moving through phases. Point is: stagnation is over. If you're single, someone's heading your way. If you're coupled, the relationship's evolving. Buckle up, the journey's gonna be interesting.",
        "health": "You're entering a transition phase health-wise. Could be recovery, could be a new routine actually working, could be that you're finally getting somewhere with treatment. Reið says: trust the journey even when you can't see the destination yet. Progress isn't always linear but it IS happening. Keep moving forward.",
        "finance": "Your financial situation is about to go somewhere. Career change, new opportunity, money finally flowing after a dry spell—Reið's energy is momentum. This isn't passive wealth, this is earned-through-action wealth. The journey might be long but the destination's worth it. Stay on the path, trust the ride."
    },
    "ᚴ": {
        "name": "Kaun",
        "traditional": "Ulcer, sore, wound",
        "love": "Okay so Kaun's the wound rune and in love that's... a lot. Something hurts. Could be an old wound reopening, could be a fresh betrayal, could be that you're finally feeling pain you've been numbing. But here's the thing about wounds—they only heal if you actually treat them. Stop pretending you're fine. Address the hurt. Real love survives honest vulnerability.",
        "health": "Kaun is literally the ulcer rune, so yeah—something's inflamed, infected, or just generally not okay. This could be physical, could be mental, could be both. The wisdom here is that ignored wounds get worse. Whatever you've been putting off addressing? It's festering. Time to clean it out, even if it hurts worse before it heals.",
        "finance": "There's a financial wound here—debt that keeps growing, a bad investment that won't quit haunting you, a money belief that's actively hurting you. Kaun says: stop putting bandaids on bullet holes. This needs real treatment, maybe even professional help. The ulcer won't heal if you keep pretending it's just a scratch."
    },
    "ᚼ": {
        "name": "Hagall",
        "traditional": "Hail, disruption, uncontrolled forces",
        "love": "Hagall is the hailstorm—sudden, uncontrollable, kinda destructive but also weirdly cleansing. Your relationship's about to get hit with something you didn't see coming. Could be external drama, could be internal crisis, could be that the universe is literally testing if what you have can weather a storm. Spoiler: if it's real, it can. If it's not, the hail will reveal that too.",
        "health": "A health situation just got complicated in a way you couldn't have predicted. Hagall's the rune of uncontrolled forces, which means: this isn't your fault, but it IS your reality now. The disruption might feel unfair because honestly, it probably is. But hailstorms pass. Focus on shelter and survival first, reconstruction second.",
        "finance": "Something just disrupted your financial stability and it probably wasn't in your five-year plan. Job loss, unexpected expense, market crash, whatever—Hagall's energy is chaotic and external. You can't control the hailstorm but you CAN control how you respond to it. Emergency mode activated. Deal with the crisis first, blame later."
    },
    "ᚾ": {
        "name": "Nauð",
        "traditional": "Need, necessity, constraint",
        "love": "Nauð is the necessity rune, which in love means: you're learning what you actually need versus what you thought you wanted. This might feel restrictive, might feel like scarcity, might feel like the universe is withholding. Plot twist—it's teaching you. Sometimes we only figure out what we truly need when everything else gets stripped away. The constraint is the lesson.",
        "health": "Your health situation is teaching you about necessity right now, and it's probably not fun. Maybe you NEED rest but want productivity. Maybe you NEED treatment but want to ignore it. Maybe you NEED boundaries but feel guilty. Nauð says: constraints aren't punishments, they're redirections. Your body's needs aren't negotiable.",
        "finance": "Financial constraint is real right now—Nauð doesn't pretend otherwise. But here's the reframe: necessity teaches you what actually matters. When money's tight, you learn your real priorities fast. This isn't permanent poverty consciousness, it's temporary constraint with a lesson attached. Learn it quickly so you can move through it quickly."
    },
    "ᛁ": {
        "name": "Íss",
        "traditional": "Ice, stillness, frozen state",
        "love": "Íss is the ice rune, which means your love situation is frozen right now. Nothing's moving, nothing's changing, everything feels stuck. This could be frustrating but it's also strategic—ice preserves things. Maybe this pause is protecting you from making a move too soon. Maybe the freeze is forcing you to actually THINK instead of just react. Stillness isn't always bad.",
        "health": "Health progress is frozen, which is honestly annoying but also potentially necessary. Íss says: sometimes healing requires complete stillness. Not giving up, not backsliding, just... paused. Your body might be in preservation mode, conserving energy for what comes next. Trust the freeze. Movement will return when conditions are right.",
        "finance": "Your financial situation is iced over—no growth, no movement, no momentum. Investments aren't moving, career's stalled, money's just sitting there doing nothing. Íss reminds you that frozen isn't dead. It's preserved, it's waiting, it's building pressure for the eventual thaw. Use this stillness to plan, strategize, prepare. Spring always comes."
    },
    "ᛅ": {
        "name": "Ár",
        "traditional": "Good year, harvest, abundance",
        "love": "ÁR IS LITERALLY THE GOOD YEAR RUNE. Your love life just entered harvest season, which means: you're about to reap what you've been planting. If you've been putting in genuine effort, congrats—it's about to pay off in a major way. If you've been half-assing it, well... you harvest what you sow. Either way, this is the abundance rune. Enjoy the fruits.",
        "health": "Harvest time for your health means: all that work you've been putting in? It's about to show results. The good year is here. Your body's responding to your efforts, your energy's returning, your healing's accelerating. Ár's energy is reward, celebration, abundance. You've earned this upswing. Don't second-guess it.",
        "finance": "This is the HARVEST rune for finances which is literally what everyone wants to pull. Money's coming in, opportunities are ripe, your efforts are multiplying. This is your good year financially. But remember—harvest time requires ACTION. The crops don't pick themselves. Show up, claim what's yours, and maybe plant seeds for next year while you're at it."
    },
    "ᛋ": {
        "name": "Sól",
        "traditional": "Sun, success, vitality",
        "love": "Sól is the SUN and your love life is about to be RADIANT. This is the success rune, the vitality rune, the \"everything's coming up sunshine\" rune. If you're in a relationship, it's about to hit a golden phase. If you're single, you're about to become absolutely magnetic. The sun doesn't try to shine, it just does. That's your energy right now. Glow accordingly.",
        "health": "The sun just rose on your health situation, which means: vitality is returning. Energy's coming back. Things that felt impossible last month suddenly feel doable. Sól's the success rune, so whatever health goal you've been working toward? You're about to hit it. Your body's in its power phase. Use this solar energy while it's here.",
        "finance": "Sól in finances means SUCCESS, period. The sun's shining on your money situation—raises, opportunities, investments paying off, side hustles thriving. This is your moment to shine professionally and financially. But remember: the sun doesn't hoard its light. Share the wealth, mentor someone, pay it forward. Success multiplies when it's generous."
    },
    "ᛏ": {
        "name": "Týr",
        "traditional": "The god Týr, justice, sacrifice",
        "love": "Týr is the justice god who sacrificed his hand for the greater good, so... yeah, this rune goes hard. Something in your love life requires sacrifice or a really difficult choice that's objectively right but subjectively painful. Maybe you gotta be honest even though it'll hurt. Maybe you gotta leave even though you love them. Maybe you gotta stay even though it's hard. Honor demands it. Choose accordingly.",
        "health": "Justice in health means: you gotta make the sacrifice that leads to real healing. Maybe it's giving up the habit that's slowly killing you. Maybe it's the painful treatment that actually works. Maybe it's prioritizing your wellbeing even when others call you selfish. Týr says: the right choice isn't always the easy choice. Do it anyway.",
        "finance": "Týr in finances asks: what are you willing to sacrifice for long-term success? Could be the comfortable job that's going nowhere. Could be short-term pleasure for long-term security. Could be playing it safe versus taking the ethical risk. Justice demands balanced scales. Sometimes you gotta lose a hand to save the realm. Calculate accordingly."
    },
    "ᛒ": {
        "name": "Bjarkan",
        "traditional": "Birch, growth, new beginnings",
        "love": "Bjarkan is the birch tree—first to grow after a forest fire, symbol of new beginnings, fresh starts, that \"clean slate\" energy. Your love life's in regeneration mode. Could be a new relationship, could be a renewed relationship, could be that you're finally growing past old patterns. Birch grows fast and pretty but it also needs the right conditions. Create them.",
        "health": "New growth in health, literally. Your body's in renewal phase—could be recovery, could be that new routine finally clicking, could be that you're finally healing from something old. Bjarkan says: growth is natural when conditions are right. You're in your spring arc. Feed the new growth, protect it, let it establish before you stress-test it.",
        "finance": "Fresh start energy in finances. New job, new business, new investment strategy, new money mindset—whatever it is, it's GREEN and GROWING. Bjarkan's the pioneer plant, which means: you're building something from scratch or rebuilding after a crash. This is exciting but also vulnerable. Protect your new growth while it establishes."
    },
    "ᛘ": {
        "name": "Maðr",
        "traditional": "Human, self, mankind",
        "love": "Maðr is the HUMAN rune which in love means: you're the main character here. This is about YOU—your needs, your growth, your humanity. Stop shapeshifting to fit someone else's idea of who you should be. The relationship works best when both people show up as their actual selves. Your humanness, with all its mess and magic, is the point. Be that.",
        "health": "The human rune in health is a reminder that you're not a machine, not a productivity unit, just a human body doing its best. You're allowed to be tired, hurt, imperfect, still-healing. Maðr says: your humanity is the starting point, not the obstacle. Health looks different on every body. Honor YOURS.",
        "finance": "You are the asset. Maðr in finances means: your value isn't just your productivity or your bank account. It's your skills, your network, your humanity, your creativity, your persistence. Jobs come and go but YOU—your human capital—is the constant. Invest in yourself. You're the only resource that appreciates with age."
    },
    "ᛚ": {
        "name": "Lǫgr",
        "traditional": "Water, flow, intuition",
        "love": "Lǫgr is WATER—flow, intuition, emotional depth, that \"go with the current\" energy. Your love situation is asking you to stop forcing and start flowing. Water doesn't push through obstacles, it moves around them. Maybe you're trying too hard. Maybe you're swimming upstream. Maybe you just need to trust the current and see where it takes you. Intuition over strategy right now.",
        "health": "Water energy in health means: listen to your body's flow. Your energy ebbs and flows, your needs change like tides, your healing isn't linear. Lǫgr says: stop forcing yourself into rigid routines and start responding to what your body's actually asking for TODAY. Flexibility is strength. Flow is wisdom.",
        "finance": "Lǫgr in finances is about FLOW—money in, money out, the natural circulation. You might be blocking the flow by either hoarding or hemorrhaging. Water teaches balance. Let money move through your life naturally. Trust your intuition about opportunities. Sometimes the indirect path (around the rock) is faster than the direct one (through it)."
    },
    "ᛦ": {
        "name": "Ýr",
        "traditional": "Yew bow, endings, transformation",
        "love": "Ýr is the yew tree, the bow, the ENDING rune (because yew wood makes the best bows and bows end things). Something in your love life is completing its cycle. Could be the end of a relationship, could be the end of a pattern, could be the death of who you used to be in relationships. Endings aren't failures. They're transformations. The bow needs to be bent back before it can shoot forward.",
        "health": "The yew rune in health means: a cycle is ending. Could be the end of treatment, could be that a health phase is finally over, could be accepting that something chronic is permanent. Ýr says: endings contain new beginnings the way a seed contains a tree. What's dying is making room for what's next. Trust the transformation.",
        "finance": "Something financial is ENDING—job, income stream, business, maybe an entire career chapter. Ýr's energy is completion but also potential. The yew bow has to be drawn back before it can launch the arrow. This ending isn't the failure, it's the windup. What you're releasing is what gives you the force to shoot forward. Aim carefully."
    }
}


def get_rune_interpretation(rune_symbol, category):
    """
    Get the interpretation for a specific rune based on the user's emotional category.
    
    Parameters:
    -----------
    rune_symbol : str
        The rune symbol (e.g., "ᚠ", "ᚢ", etc.)
    category : str
        The emotional category: "LOVE", "HEALTH", or "FINANCE"
        
    Returns:
    --------
    str
        Skuld's interpretation of the rune for that category
    """
    if rune_symbol not in RUNES:
        return "Error: Rune not found in database."
    
    category_lower = category.lower()
    if category_lower not in ["love", "health", "finance"]:
        return "Error: Category must be 'LOVE', 'HEALTH', or 'FINANCE'."
    
    rune_data = RUNES[rune_symbol]
    return rune_data[category_lower]


def get_rune_name(rune_symbol):
    """
    Get the traditional name of a rune.
    
    Parameters:
    -----------
    rune_symbol : str
        The rune symbol (e.g., "ᚠ", "ᚢ", etc.)
        
    Returns:
    --------
    str
        The rune's traditional name
    """
    if rune_symbol not in RUNES:
        return "Unknown rune"
    return RUNES[rune_symbol]["name"]


def draw_a_random_rune():
    """
    Get a list of all available rune symbols.
    
    Returns:
    --------
    list
        List of all rune symbols in the database
    """
    list(RUNES.keys())
    drawn_rune = random.choice(list(RUNES.keys()))
    return drawn_rune


# Testing
if __name__ == "__main__":
    print("Testing rune_meanings.py")
    print("=" * 60)
    
    # Test with first rune
    test_rune = "ᚠ"
    print(f"Rune: {test_rune}")
    print(f"Name: {get_rune_name(test_rune)}")
    print()
    print("LOVE interpretation:")
    print(get_rune_interpretation(test_rune, "LOVE"))
    print()
    print(f"Total runes available: {len(get_all_rune_symbols())}")
    print()
    print("✓ rune_meanings.py is ready!")
