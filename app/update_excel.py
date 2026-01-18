import requests
import pandas as pd
from datetime import datetime 
    def update():
    

    URL = "https://ics.upjs.sk/~krajci/skola/alejova/septima/body.xlsx"




   
    try:
        last_update = datetime.strptime(
            status_path.read_text().strip(),
            "%Y-%m-%d %H:%M:%S"
        )
            if datetime.now() - last_update < timedelta(hours=1):
                return

    r = requests.get(URL, timeout=30)
    r.raise_for_status()

    df = pd.read_excel(r.content, header=None)

    df = df.dropna(axis=1, how="all")  # remove columns where all values are empty
    dummy_headers = [i+1 for i in range(df.shape[1])]
    df.columns = dummy_headers

    df = df.fillna("")

    df.to_json("data/latest.json", orient="records")

    f = open( "data/status.txt", "w" )
    formatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(formatted)

