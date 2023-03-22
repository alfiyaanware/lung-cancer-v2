from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from hospitals"))

    result_dicts = []
    for row in result.all():
      result_dicts.append(row._mapping)

  return result_dicts


def load_hospital_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from hospitals where id= :val"), {"val": id})
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
