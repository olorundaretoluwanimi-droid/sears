#!/usr/bin/env python3
"""The script, line by line → audio/lines.json (for the AI33 narrator) and script.md (readable).
Each entry: id, chapter, text (spoken, numbers as words), subs (caption lines, digits, one line each ≤ ~56 characters).
Speaks to "you" in the open, the ending and about once per chapter. Every fact is in FACTS.md."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = 'elevenlabs_0dPqNXnhg2bmxQv1WKDp'   # Storyteller Oxley (AI33 Pro / ElevenLabs)
C = []
def L(ch, i, spoken, *subs): C.append((ch, i, spoken, list(subs)))

# ── cold open: your house ──
L('open', 'n01', "Take a look around your house.", "Take a look around your house.")
L('open', 'n02', "Maybe there's a wrench in the garage that says Craftsman. A washing machine that says Kenmore.",
  "Maybe there's a wrench in the garage that says Craftsman.", "A washing machine that says Kenmore.")
L('open', 'n03', "And maybe, a few streets away, there's a house that arrived by train, in thousands of pieces, with a book of instructions to put it together.",
  "And maybe, a few streets away, there's a house", "that arrived by train, in thousands of pieces,", "with a book of instructions to put it together.")
L('open', 'n04', "All of it came from the same place. A company in Chicago called Sears, Roebuck.", "All of it came from the same place.", "A company in Chicago called Sears, Roebuck.")
L('open', 'n05', "In eighteen eighty-six, a railroad station agent in Minnesota started selling watches by mail, at fourteen dollars apiece.",
  "In 1886, a railroad station agent in Minnesota", "started selling watches by mail, at $14 apiece.")
L('open', 'n06', "Within a few decades, his company would sell you almost anything. A dress. A plow. A doll for Christmas. A whole house.",
  "Within a few decades, his company would sell you almost anything.", "A dress. A plow. A doll for Christmas. A whole house.")
L('open', 'n07', "For millions of families on farms and in small towns, the Sears catalog was the store.",
  "For millions of families on farms and in small towns,", "the Sears catalog was the store.")
L('open', 'n08', "People like to call Sears the Amazon of its time.", "People like to call Sears the Amazon of its time.")
L('open', 'n09', "Then, in nineteen ninety-three, Sears stopped printing its big catalog. The next year, Amazon was founded.",
  "Then, in 1993, Sears stopped printing its big catalog.", "The next year, Amazon was founded.")
L('open', 'n10', "This is the story of what happened to Sears. Every photograph you'll see is real, every number has a source, and you'll see the actual catalog pages.",
  "This is the story of what happened to Sears.", "Every photograph you'll see is real, every number has a source,", "and you'll see the actual catalog pages.")
L('open', 'n11', "We'll tell it through seven things Sears sold. A watch. The catalog. A house. A store. A tower. The last catalog. And a closing-sale sign.",
  "We'll tell it through seven things Sears sold.", "A watch. The catalog. A house. A store.", "A tower. The last catalog. And a closing-sale sign.")
L('open', 'n12', "If you ever waited for the Christmas catalog to arrive, and circled the toys you wanted, this one is for you.",
  "If you ever waited for the Christmas catalog to arrive,", "and circled the toys you wanted, this one is for you.")

# ── 1. a gold watch · 1886 · $14 ──
L('c1', 'n13', "North Redwood, Minnesota. Eighteen eighty-six. Richard Warren Sears is twenty-two years old, and he's the agent at the railroad station.",
  "North Redwood, Minnesota. 1886.", "Richard Warren Sears is 22 years old,", "and he's the agent at the railroad station.")
L('c1', 'n14', "One day, a shipment of watches arrives for a jeweler in a nearby town. The jeweler refuses it.",
  "One day, a shipment of watches arrives for a jeweler", "in a nearby town. The jeweler refuses it.")
L('c1', 'n15', "Instead of sending the watches back, Sears buys them himself. He offers them to other station agents up and down the line, at fourteen dollars each, and they sell them on.",
  "Instead of sending the watches back, Sears buys them himself.", "He offers them to other station agents up and down the line,", "at $14 each, and they sell them on.")
L('c1', 'n16', "Within six months, he has made five thousand dollars. So he leaves the railroad, and starts a watch company.",
  "Within six months, he has made $5,000.", "So he leaves the railroad, and starts a watch company.")
L('c1', 'n17', "In eighteen eighty-seven, he moves it to Chicago, where the railroads meet, and hires a young watch repairman from Indiana. His name is Alvah Curtis Roebuck.",
  "In 1887, he moves it to Chicago, where the railroads meet,", "and hires a young watch repairman from Indiana.", "His name is Alvah Curtis Roebuck.")
L('c1', 'n18', "This is one of their advertisements, from a newspaper in Winchester, Indiana, in January eighteen eighty-eight. Look at the promise at the bottom. We send it for examination. You could see the watch before you paid for it.",
  "This is one of their advertisements, from a newspaper", "in Winchester, Indiana, in January 1888.", "Look at the promise at the bottom.", "You could see the watch before you paid for it.")
L('c1', 'n19', "In eighteen ninety-three, the company takes both their names. Sears, Roebuck and Company.", "In 1893, the company takes both their names.", "Sears, Roebuck and Company.")
L('c1', 'n20', "Sears writes the advertising, almost all of it himself. And he finds that people far from any city will buy almost anything by mail, as long as they trust who's sending it.",
  "Sears writes the advertising, almost all of it himself.", "And he finds that people far from any city will buy", "almost anything by mail, as long as they trust the sender.")
L('c1', 'n21', "In eighteen ninety-five, Roebuck sells out. A Chicago clothing man named Julius Rosenwald buys in, and turns a brilliant salesman's business into a machine.",
  "In 1895, Roebuck sells out. A Chicago clothing man", "named Julius Rosenwald buys in, and turns a brilliant", "salesman's business into a machine.")
L('c1', 'n22', "Here are the men in charge that year. Sears, the president. Aaron Nusbaum, the manager. And Rosenwald.",
  "Here are the men in charge that year.", "Sears, the president. Aaron Nusbaum, the manager. And Rosenwald.")
L('c1', 'n23', "Between eighteen ninety-five and nineteen-oh-seven, sales grow from seven hundred and fifty thousand dollars a year to more than fifty million.",
  "Between 1895 and 1907, sales grow from $750,000 a year", "to more than $50 million.")
L('c1', 'n24', "So if a watch could travel by mail to a farm in Minnesota, what else could?", "So if a watch could travel by mail to a farm in Minnesota,", "what else could?")

# ── 2. the catalog · 1897 ──
L('c2', 'n25', "This is the Sears catalog for the spring of eighteen ninety-seven. The company called it the Consumers Guide.",
  "This is the Sears catalog for the spring of 1897.", "The company called it the Consumers Guide.")
L('c2', 'n26', "Not long before, it had been a little book of watches and jewelry. By eighteen ninety-four, it ran to three hundred and twenty-two pages. A year later, five hundred and thirty-two.",
  "Not long before, it had been a little book of watches and jewelry.", "By 1894, it ran to 322 pages.", "A year later, 532.")
L('c2', 'n27', "Groceries. Stoves. Dolls. Medicines. Bicycles. Clothing. Plows.", "Groceries. Stoves. Dolls. Medicines.", "Bicycles. Clothing. Plows.")
L('c2', 'n28', "And it reached people where the stores couldn't. In eighteen ninety-six, the Post Office began Rural Free Delivery. For the first time, a farm family's mail came to its own gate, instead of waiting for them in town.",
  "And it reached people where the stores couldn't.", "In 1896, the Post Office began Rural Free Delivery.", "For the first time, a farm family's mail came to its own gate,", "instead of waiting for them in town.")
L('c2', 'n29', "In nineteen thirteen came Parcel Post, and the mail carrier could bring the packages too.",
  "In 1913 came Parcel Post,", "and the mail carrier could bring the packages too.")
L('c2', 'n30', "By nineteen-oh-eight, more than one in five Americans received the Sears catalog. At its peak, it offered a hundred thousand items, on fourteen hundred pages.",
  "By 1908, more than one in five Americans received the catalog.", "At its peak, it offered 100,000 items, on 1,400 pages.")
L('c2', 'n31', "To fill the orders, Sears built a plant on Chicago's West Side. When it opened in nineteen-oh-six, its mail-order building was the largest commercial building in the world.",
  "To fill the orders, Sears built a plant on Chicago's West Side.", "When it opened in 1906, its mail-order building", "was the largest commercial building in the world.")
L('c2', 'n32', "Railroad tracks ran right into it. Orders rode on belts and chutes from floor to floor, and parcels left by the carload.",
  "Railroad tracks ran right into it.", "Orders rode on belts and chutes from floor to floor,", "and parcels left by the carload.")
L('c2', 'n33', "And the catalog printed its customers' letters. Here's one, from Chapel Hill, North Carolina, January eighteen ninety-seven.",
  "And the catalog printed its customers' letters.", "Here's one, from Chapel Hill, North Carolina, January 1897.")
L('c2', 'q01', "I am much pleased. So far it is all you claim for it. It keeps splendid time.", "“I am much pleased. So far it is all you claim for it.", "It keeps splendid time.”")
L('c2', 'n34', "At the bottom of the page, Sears printed a dare. If you think mail-order buying doesn't pay, give us one trial.",
  "At the bottom of the page, Sears printed a dare.", "If you think mail-order buying doesn't pay, give us one trial.")
L('c2', 'n35', "And every autumn, the catalog grew a Christmas section. Toys. Dolls. Stockings stuffed with presents, ready to mail.",
  "And every autumn, the catalog grew a Christmas section.", "Toys. Dolls. Stockings stuffed with presents, ready to mail.")
L('c2', 'n36', "In nineteen thirty-three, Sears printed its first separate Christmas catalog. Families had their own name for it, and in nineteen sixty-eight Sears made it official. The Wish Book.",
  "In 1933, Sears printed its first separate Christmas catalog.", "Families had their own name for it,", "and in 1968 Sears made it official. The Wish Book.")
L('c2', 'n37', "Maybe you remember it. The toys at the back. The corners folded down. The circles you drew around the things you hoped for.",
  "Maybe you remember it. The toys at the back.", "The corners folded down.", "The circles you drew around the things you hoped for.")
L('c2', 'n38', "So, if you could buy the stove and the sewing machine by mail, could you buy the house to put them in?",
  "So, if you could buy the stove and the sewing machine by mail,", "could you buy the house to put them in?")

# ── 3. a house in a box · 1918 · $1,172 ──
L('c3', 'n39', "In nineteen-oh-eight, Sears began selling houses. Not just the plans. The houses.", "In 1908, Sears began selling houses.", "Not just the plans. The houses.")
L('c3', 'n40', "You picked one from a catalog called Modern Homes, and Sears sent it by rail. The lumber, cut to size and numbered. The nails, the doors, the windows, the paint. As many as thirty thousand parts, and a book of instructions.",
  "You picked one from a catalog called Modern Homes,", "and Sears sent it by rail. The lumber, cut to size and numbered.", "The nails, the doors, the windows, the paint.", "As many as 30,000 parts, and a book of instructions.")
L('c3', 'n41', "Sears said a man of average abilities could put one together in about ninety days.", "Sears said a man of average abilities", "could put one together in about 90 days.")
L('c3', 'n42', "Between nineteen-oh-eight and nineteen forty, Sears sold somewhere between seventy and seventy-five thousand of them. No one knows exactly, because Sears didn't keep the sales records.",
  "Between 1908 and 1940, Sears sold somewhere between", "70,000 and 75,000 of them. No one knows exactly,", "because Sears didn't keep the sales records.")
L('c3', 'n43', "Which brings us to a small town in Illinois.", "Which brings us to a small town in Illinois.")
L('c3', 'n44', "Carlinville sits about forty miles south of Springfield, in the coal country of Macoupin County.",
  "Carlinville sits about 40 miles south of Springfield,", "in the coal country of Macoupin County.")
L('c3', 'n45', "In nineteen eighteen, Standard Oil of Indiana opened coal mines near the town, and the miners needed somewhere to live. So the company ordered houses from Sears. Lots of them.",
  "In 1918, Standard Oil of Indiana opened coal mines near the town,", "and the miners needed somewhere to live.", "So the company ordered houses from Sears. Lots of them.")
L('c3', 'n46', "One hundred and ninety-two houses, for about a million dollars. It's the largest order for Sears houses anyone knows of.",
  "192 houses, for about a million dollars.", "It's the largest order for Sears houses anyone knows of.")
L('c3', 'n47', "Most of them went to Carlinville, onto a new neighborhood of about a dozen blocks. People called it the Standard Addition.",
  "Most of them went to Carlinville,", "onto a new neighborhood of about a dozen blocks.", "People called it the Standard Addition.")
L('c3', 'n48', "Here's one of the designs Sears was selling that year. The Carlin. Five rooms, a porch, and a balcony upstairs. One thousand, one hundred and seventy-two dollars.",
  "Here's one of the designs Sears was selling that year.", "The Carlin. Five rooms, a porch, and a balcony upstairs.", "$1,172.")
L('c3', 'n49', "And Sears was proud of Carlinville. A few years later, it put the town in its own catalog. We sell houses, the page says. In any quantity.",
  "And Sears was proud of Carlinville.", "A few years later, it put the town in its own catalog.", "“We sell houses,” the page says. “In any quantity.”")
L('c3', 'n50', "These are the street views it printed. The Standard Addition, new, around nineteen twenty.",
  "These are the street views it printed.", "The Standard Addition, new, around 1920.")
L('c3', 'n51', "But the coal didn't last. In nineteen twenty-five, Standard Oil closed its mines near Carlinville.",
  "But the coal didn't last.", "In 1925, Standard Oil closed its mines near Carlinville.")
L('c3', 'n52', "At the mining camp of Schoper nearby, local historians say most of the Sears houses were taken apart and loaded back onto boxcars, and left the way they came. Schoper is a ghost town today.",
  "At the mining camp of Schoper nearby, local historians say", "most of the Sears houses were taken apart, loaded back", "onto boxcars, and left the way they came.", "Schoper is a ghost town today.")
L('c3', 'n53', "But in Carlinville, the houses stayed. About a hundred and fifty of them are still standing. It's thought to be the largest group of Sears houses in one place in the country.",
  "But in Carlinville, the houses stayed.", "About 150 of them are still standing.", "It's thought to be the largest group of Sears houses", "in one place in the country.")
L('c3', 'n54', "And there are Sears houses all over America whose owners have no idea. If your house was built between nineteen-oh-eight and nineteen forty, look in the basement or the attic, for numbers stamped on the beams.",
  "And there are Sears houses all over America", "whose owners have no idea.", "If your house was built between 1908 and 1940,", "look in the basement or the attic,", "for numbers stamped on the beams.")
L('c3', 'n55', "There's a harder part of the story, too. From about nineteen twelve, Sears lent buyers the money. When the Depression came, many couldn't pay. Sears had to sell off about eleven million dollars in loans gone bad, and at the end of nineteen thirty-three, it stopped lending.",
  "There's a harder part of the story, too.", "From about 1912, Sears lent buyers the money.", "When the Depression came, many couldn't pay.", "Sears had to sell off about $11 million in loans gone bad,", "and at the end of 1933, it stopped lending.")
L('c3', 'n56', "The house catalog ended in nineteen forty. By then, Sears had found a new way to sell. And this one didn't need the mail at all.",
  "The house catalog ended in 1940.", "By then, Sears had found a new way to sell.", "And this one didn't need the mail at all.")

# ── 4. a store down the street · 1925 ──
L('c4', 'n57', "By the nineteen twenties, the farm family had a car. And the car could take them to town.",
  "By the 1920s, the farm family had a car.", "And the car could take them to town.")
L('c4', 'n58', "A retired Army general named Robert Wood joined Sears, and he believed the future was stores.",
  "A retired Army general named Robert Wood joined Sears,", "and he believed the future was stores.")
L('c4', 'n59', "On the second of February, nineteen twenty-five, the first Sears store opened, inside the catalog plant in Chicago.",
  "On 2 February 1925, the first Sears store opened,", "inside the catalog plant in Chicago.")
L('c4', 'n60', "By the end of nineteen twenty-seven, there were twenty-seven. By nineteen thirty-two, more than three hundred.",
  "By the end of 1927, there were 27.", "By 1932, more than 300.")
L('c4', 'n61', "And in nineteen thirty-one, for the first time, the stores sold more than the catalog.",
  "And in 1931, for the first time,", "the stores sold more than the catalog.")
L('c4', 'n62', "Here's the Sears building in Allentown, Pennsylvania, in nineteen twenty-nine.", "Here's the Sears building in Allentown, Pennsylvania, in 1929.")
L('c4', 'n63', "In town after town, Sears became the store on Main Street. Later, the big store at the end of the mall.",
  "In town after town, Sears became the store on Main Street.", "Later, the big store at the end of the mall.")
L('c4', 'n64', "It sold its own names. Kenmore had first appeared on a sewing machine in nineteen thirteen. In nineteen twenty-seven, it went on a washing machine. The same year, Sears started selling Craftsman tools.",
  "It sold its own names. Kenmore had first appeared", "on a sewing machine in 1913.", "In 1927, it went on a washing machine.", "The same year, Sears started selling Craftsman tools.")
L('c4', 'n65', "Maybe that's the wrench in your garage.", "Maybe that's the wrench in your garage.")
L('c4', 'n66', "So how big could one company get?", "So how big could one company get?")

# ── 5. the tallest building · 1973 ──
L('c5', 'n67', "By the nineteen sixties, Sears was the biggest retailer in America. And in nineteen seventy, it started building a headquarters to match.",
  "By the 1960s, Sears was the biggest retailer in America.", "And in 1970, it started building a headquarters to match.")
L('c5', 'n68', "When it opened in nineteen seventy-three, the Sears Tower in Chicago was the tallest building in the world. Fourteen hundred and fifty-one feet. It would hold the title for nearly twenty-five years.",
  "When it opened in 1973, the Sears Tower in Chicago", "was the tallest building in the world. 1,451 feet.", "It would hold the title for nearly 25 years.")
L('c5', 'n69', "Sears moved its offices out of the old catalog plant on the West Side, and up into the sky.",
  "Sears moved its offices out of the old catalog plant", "on the West Side, and up into the sky.")
L('c5', 'n70', "But down on the ground, shopping was changing again.", "But down on the ground, shopping was changing again.")
L('c5', 'n71', "A discount chain from Arkansas called Walmart was growing fast, in exactly the kind of small towns Sears had built its business on. And new stores that sold just one thing, like Home Depot, sold more of it, for less.",
  "A discount chain from Arkansas called Walmart was growing fast,", "in exactly the kind of small towns", "Sears had built its business on.", "And new stores that sold just one thing, like Home Depot,", "sold more of it, for less.")
L('c5', 'n72', "Sears tried to be everything at once. It owned Allstate insurance. It bought a stockbroker, Dean Witter. It launched the Discover card. Its stores kept losing ground.",
  "Sears tried to be everything at once. It owned Allstate insurance.", "It bought a stockbroker, Dean Witter.", "It launched the Discover card. Its stores kept losing ground.")
L('c5', 'n73', "By the start of the nineteen nineties, Walmart had passed Sears as the biggest retailer in America.",
  "By the start of the 1990s, Walmart had passed Sears", "as the biggest retailer in America.")
L('c5', 'n74', "What would Sears give up to survive?", "What would Sears give up to survive?")

# ── 6. the last catalog · 25 Jan 1993 ──
L('c6', 'n75', "In nineteen ninety-two, Sears lost three point nine billion dollars. It was the biggest loss a North American retailer had ever reported.",
  "In 1992, Sears lost $3.9 billion.", "It was the biggest loss a North American retailer", "had ever reported.")
L('c6', 'n76', "The catalog was part of the problem. By one account, it was losing as much as a million dollars a day. Printing a book of some fifteen hundred pages and mailing it to millions of homes had become too expensive.",
  "The catalog was part of the problem. By one account,", "it was losing as much as a million dollars a day.", "Printing a book of some 1,500 pages and mailing it", "to millions of homes had become too expensive.")
L('c6', 'n77', "On the twenty-fifth of January, nineteen ninety-three, Sears announced the end. No more Big Book. A hundred and thirteen stores would close, and fifty thousand jobs would go.",
  "On 25 January 1993, Sears announced the end.", "No more Big Book.", "113 stores would close, and 50,000 jobs would go.")
L('c6', 'n78', "That year, Sears also began moving out of its tower, to new offices in the suburbs of Chicago.",
  "That year, Sears also began moving out of its tower,", "to new offices in the suburbs of Chicago.")
L('c6', 'n79', "And on the fifth of July, nineteen ninety-four, a man in Washington State started a company to sell books over the internet. It would become Amazon.",
  "And on 5 July 1994, a man in Washington State", "started a company to sell books over the internet.", "It would become Amazon.")
L('c6', 'n80', "It's easy now to say Sears threw the future away. But in nineteen ninety-three, almost nobody shopped online. The danger Sears could see was Walmart and Home Depot, not the internet. Ending the catalog was a decision to save the stores.",
  "It's easy now to say Sears threw the future away.", "But in 1993, almost nobody shopped online.", "The danger Sears could see was Walmart and Home Depot,", "not the internet.", "Ending the catalog was a decision to save the stores.")
L('c6', 'n81', "Could the stores alone keep Sears alive?", "Could the stores alone keep Sears alive?")

# ── 7. the closing-sale sign · 2018 ──
L('c7', 'n82', "In two thousand four, Kmart announced it would buy Sears. Kmart was controlled by an investor named Eddie Lampert. The deal closed in March two thousand five. Together, Sears and Kmart had about three and a half thousand stores.",
  "In 2004, Kmart announced it would buy Sears.", "Kmart was controlled by an investor named Eddie Lampert.", "The deal closed in March 2005.", "Together, Sears and Kmart had about 3,500 stores.")
L('c7', 'n83', "Lampert cut costs and looked for value in the real estate under the stores. His critics said too little went back into the stores themselves. His supporters said the shoppers had already gone.",
  "Lampert cut costs and looked for value in the real estate", "under the stores. His critics said too little", "went back into the stores themselves.", "His supporters said the shoppers had already gone.")
L('c7', 'n84', "One by one, the famous names were sold. Craftsman went to Stanley Black and Decker in two thousand seventeen. DieHard batteries, two years later.",
  "One by one, the famous names were sold.", "Craftsman went to Stanley Black & Decker in 2017.", "DieHard batteries, two years later.")
L('c7', 'n85', "On the fifteenth of October, two thousand eighteen, Sears Holdings filed for bankruptcy. It had six hundred and eighty-seven Sears and Kmart stores left.",
  "On 15 October 2018, Sears Holdings filed for bankruptcy.", "It had 687 Sears and Kmart stores left.")
L('c7', 'n86', "Lampert bought what remained at auction, through a new company. And the closing-sale signs kept going up.",
  "Lampert bought what remained at auction, through a new company.", "And the closing-sale signs kept going up.")
L('c7', 'n87', "This is the Sears in Hialeah, Florida, in February twenty twenty. Last five days.",
  "This is the Sears in Hialeah, Florida, in February 2020.", "Last five days.")
L('c7', 'n88', "By the end of twenty twenty-five, there were five Sears stores left in the United States.",
  "By the end of 2025, there were five Sears stores", "left in the United States.")
L('c7', 'n89', "So what's left?", "So what's left?")

# ── epilogue: your house, today ──
L('end', 'n90', "Go back to Carlinville.", "Go back to Carlinville.")
L('end', 'n91', "The coal mines are long gone. The trains still stop at the little station, and the courthouse still stands over the square.",
  "The coal mines are long gone.", "The trains still stop at the little station,", "and the courthouse still stands over the square.")
L('end', 'n92', "And in the Standard Addition, about a hundred and fifty Sears houses are still somebody's home. More than a hundred years after they came in on the train.",
  "And in the Standard Addition, about 150 Sears houses", "are still somebody's home.", "More than a hundred years after they came in on the train.")
L('end', 'n93', "Look around your own house again. The Craftsman wrench still turns. Kenmore is still a name on appliances. And in Chicago, the tower Sears built still stands, though since two thousand nine it's been called the Willis Tower.",
  "Look around your own house again.", "The Craftsman wrench still turns.", "Kenmore is still a name on appliances.", "And in Chicago, the tower Sears built still stands,", "though since 2009 it's been called the Willis Tower.")
L('end', 'n94', "Sears had the future in its hands more than once. It brought the city store to the farm gate, by mail. It brought the store to the end of the road, when the car arrived.",
  "Sears had the future in its hands more than once.", "It brought the city store to the farm gate, by mail.", "It brought the store to the end of the road, when the car arrived.")
L('end', 'n95', "The third time, it let go.", "The third time, it let go.")
L('end', 'n96', "But a lot of it is still here. In the houses. In the toolboxes. And in the memory of a book that came in the mail, with the whole world inside it.",
  "But a lot of it is still here. In the houses. In the toolboxes.", "And in the memory of a book that came in the mail,", "with the whole world inside it.")
L('end', 'n97', "Did your family order from the catalog, or live in a Sears house? Tell us in the comments. Next time: Rochester, and Kodak.",
  "Did your family order from the catalog, or live in a Sears house?", "Tell us in the comments. Next time: Rochester, and Kodak.")

os.makedirs(os.path.join(D, 'audio'), exist_ok=True)
json.dump([{'id': i, 'chapter': ch, 'voice': V, 'text': sp, 'subs': su} for ch, i, sp, su in C], open(os.path.join(D, 'audio', 'lines.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
names = {'open': 'Cold open — your house', 'c1': '1 · A gold watch · 1886 · $14', 'c2': '2 · The catalog · 1897', 'c3': '3 · A house in a box · 1918 · $1,172',
         'c4': '4 · A store down the street · 1925', 'c5': '5 · The tallest building · 1973', 'c6': '6 · The last catalog · 25 Jan 1993',
         'c7': '7 · The closing-sale sign · 2018', 'end': 'Epilogue — your house, today'}
out, last = ['# What Happened to Sears? The Catalog That Built Small-Town America — script', ''], None
for ch, i, sp, su in C:
    if ch != last: out += ['', f'## {names[ch]}', '']; last = ch
    out.append(f'**{i}** {" ".join(su)}')
open(os.path.join(D, 'script.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
w = sum(len(sp.split()) for _, _, sp, _ in C); print(len(C), 'lines', w, 'words', f'~{w / 150:.1f} min of speech')
long = [(i, s) for _, i, _, su in C for s in su if len(s) > 66]; print('long caption lines:', long)
