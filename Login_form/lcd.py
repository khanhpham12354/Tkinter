from gtts import gTTS
import sqlite3 as sql
data_word = {}
def load_data():
	path  = "database\\data_newword.db";
	con = sql.connect(path);
	with con:
		cur  = con.cursor();
		cur.execute("SELECT* FROM data123");
		rows = cur.fetchall();
		for i in range(1,len(rows)+ 1):
			data_word[str(i)] = rows[i-1][1];
			speak = gTTS(text = data_word[str(i)], lang='en', slow=False)
			speak.save("speak\\" + str(data_word[str(i)]) + ".mp3")
			#data_translate[str(i)] = rows[i-1][2];
		# print(data_word)
		# print(data_translate)
	con.close();
load_data();