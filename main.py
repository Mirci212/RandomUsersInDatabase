from UsersToDatabase import *

load_dotenv("environment.env")
GenerateUsersInTable(os.getenv("HOST"),os.getenv("USER"),os.getenv("PASSWORD"), os.getenv("DATABASE")).writeUsersInTable("test_user",20)