from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://tcfuqwk2y469zc7hw4c5:pscale_pw_Hms7HWZfNFdBacqZnazLZGbI98gm4pP0g7HY6KepL1n@ap-south.connect.psdb.cloud/lungcancer?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca":"/etc/ssl/cert.pem"
                       }})


def load_db():

  with engine.connect() as conn:
    result = conn.execute(text("select * from hospitals"))

    result_dicts = []
    for row in result.all():
      result_dicts.append(row._mapping)

  return result_dicts

