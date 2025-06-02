import sqlite3

conn = sqlite3.connect('anime.db')
c = conn.cursor()

c.execute('DELETE FROM animes')

anime_list = [
    ("Fullmetal Alchemist: Brotherhood", "Action", 2009, 9.2, "fma.jpg"),
    ("Attack on Titan (Shingeki no Kyojin)", "Action", 2013, 9.1, "aot.jpg"),
    ("Death Note", "Thriller", 2006, 8.9, "deathnote.jpg"),
    ("Naruto / Naruto Shippuden", "Action", 2002, 8.3, "naruto.jpg"),
    ("One Piece", "Adventure", 1999, 8.8, "onepiece.jpg"),
    ("My Hero Academia (Boku no Hero Academia)", "Action", 2016, 8.0, "mha.jpg"),
    ("Demon Slayer (Kimetsu no Yaiba)", "Action", 2019, 8.7, "demonslayer.jpg"),
    ("Steins;Gate", "Sci-Fi", 2011, 8.6, "steinsgate.jpg"),
    ("Hunter x Hunter (2011)", "Adventure", 2011, 9.0, "hxh.jpg"),
    ("Cowboy Bebop", "Sci-Fi", 1998, 8.9, "cowboybebop.jpg"),
    ("Neon Genesis Evangelion", "Psychological", 1995, 8.4, "aaaaa.jpg"),
    ("Tokyo Ghoul", "Horror", 2014, 7.9, "tokyoghoul.jpg"),
    ("Dragon Ball Z", "Action", 1989, 8.7, "dbz.jpg"),
    ("Code Geass: Lelouch of the Rebellion", "Mecha", 2006, 8.7, "codegeass.jpg"),
    ("Your Lie in April (Shigatsu wa Kimi no Uso)", "Romance", 2014, 8.6, "yourlieinapril.jpg"),
    ("Sword Art Online", "Adventure", 2012, 7.6, "sao.jpg"),
    ("One Punch Man", "Action", 2015, 8.5, "opm.jpg"),
    ("Mob Psycho 100", "Action", 2016, 8.5, "mobpsycho.jpg"),
    ("Clannad: After Story", "Drama", 2008, 8.6, "clannad.jpg"),
    ("Violet Evergarden", "Drama", 2018, 8.4, "violet.jpg"),
    ("Haikyuu!!", "Sports", 2014, 8.7, "haikyuu.jpg"),
    ("Fate/Zero", "Fantasy", 2011, 8.3, "fatezero.jpg"),
    ("Black Clover", "Action", 2017, 7.9, "blackclover.jpg"),
    ("Made in Abyss", "Adventure", 2017, 8.4, "madeinabyss.jpg"),
    ("Jujutsu Kaisen", "Action", 2020, 8.6, "jujutsukaisen.jpg")
]

c.executemany('''
INSERT INTO animes (title, genre, release_year, rating, image)
VALUES (?, ?, ?, ?, ?)
''', anime_list)

conn.commit()
conn.close()

