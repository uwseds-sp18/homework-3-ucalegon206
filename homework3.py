import sqlite3
import pandas as pd
import os.path


def create_dataframe(db_path):
    
    if not os.path.exists(db_path):
        raise ValueError('path to database not found')

    conn = sqlite3.connect(database_name)
    lang = ['us', 'gb', 'fr', 'de', 'ca']
    df = pd.DataFrame([])
    for l in lang:
        table_name = str.upper(l) + "videos"
        sql = "select video_id, category_id, '%s' as language from %s;" % (l, table_name)
        df_new = pd.read_sql(sql, conn)
        df = pd.concat([df, df_new], axis=0)
    return df
