def update():
    import requests
    import pandas as pd
    from datetime import datetime 

    URL = "https://ics.upjs.sk/~krajci/skola/alejova/septima/body.xlsx"

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

