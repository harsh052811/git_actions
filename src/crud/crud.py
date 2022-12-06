from ..util.db import Database
db = Database()
cursor = db.get_cursor()


def retrive(yesterday_dt, yesterday_dt1):
    links = {}
    query = "SELECT id,audio_url FROM ctm_call_activities WHERE audio_url IS NOT NULL and created_at > %s and created_at < %s limit 50"
    dates = (yesterday_dt, yesterday_dt1)
    cursor.execute(query,dates)
    for row in cursor:
        links[row[0]] = row[1]
    return links


def dump(transcription: dict):
    id = transcription["id"]
    transcript = transcription["transcript"]
    result={}
    try:
        print('Running update for id={}'.format(id))
        query = '''UPDATE ctm_call_activities 
        set transcription = %s where id = %s'''
        params = (transcript, id)
        cursor.execute(query, params)
        db.con.commit()
        result['status']='success'
    except Exception as e:
        print("database:dump exception = {}".format(e))
        result['status']='failed'
        result['exception']=e
    return result