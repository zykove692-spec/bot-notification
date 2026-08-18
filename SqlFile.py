#SqlFile.py
import aiosqlite


async def init_db():
	async with aiosqlite.connect("DataBaseus.sql") as db:
		await db.execute("""
		CREATE TABLE IF NOT EXISTS users(
		name text,
		age INTEGER
		)
		""")
		
		await db.commit()
		
		
		
async def add_user(name: str, age: int):
	async with aiosqlite.connect("DataBaseus.sql") as db:
		await db.execute("INSERT INTO users (name,age) VALUES (?,?)",(name,age))
		
		await db.commit()
		
		
async def get_all():
	async with aiosqlite.connect("DataBaseus.sql") as db:
		info = await db.execute("SELECT * FROM users")
		information = await info.fetchall()
		
		res = ""
		
		for name,age in information:
			res += f"name:{name}\nage:{age}\n\n"
			
			
		return res
		
		
		
		
async def search_info(name: str):
	async with aiosqlite.connect("DataBaseus.sql") as db:
		info = await db.execute("SELECT * FROM users WHERE name = ?",(name,))
		res = await info.fetchone()
		
		if res:
			return f"name:{res[0]}\nage:{res[1]}"
			
		else:
			return "Happen error"