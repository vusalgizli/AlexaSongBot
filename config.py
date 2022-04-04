import os
API_ID = int(os.getenv("16602040"))
API_HASH = os.getenv("a969618f49b2b2e0e33fc745e266bf17")
BOT_TOKEN = os.getenv("5266578609:AAGWX-5owgJ9TxDyK0lz5aDK37UGJIXsdes")
DATABASE_URL = os.getenv("mongodb+srv://aylak:aylak@cluster0.cd5my.mongodb.net/Cluster0?retryWrites=true&w=majority")
OWNER_ID = list({int(x) for x in os.environ.get("5266934814", "").split()})
