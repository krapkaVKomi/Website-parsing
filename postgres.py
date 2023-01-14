import psycopg2


def init(host, port, dbname, user, password):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()
    return conn, cursor


def close(cursor, conn):
    cursor.close()
    conn.close()


def get_results(cursor):
    sql = """
            select
                s.*
                , case when p.cnt is null then 'N' else 'Y' end as isPropertyPresent
                , COALESCE(p.cnt, 0) as cnt
            from
                students s
                    left join 
                    (
                        select student_id, count(*) as cnt 
                        from properties
                        group by student_id
                    ) p on s.id=p.student_id;
    """
    cursor.execute(sql)
    cur = cursor.fetchall()
    return cur


def add_student(cursor, name, dob):
    query = """
          insert into students(name, dob)
          values ('{0}', '{1}')
          returning id;
    """.format(name, dob)
    cursor.execute(query)
    row = cursor.fetchone()
    return row[0]


def add_property(cursor, student_id, property):
    query = """
          insert into properties(student_id, property)
          values ({0}, '{1}');
          commit;
    """.format(student_id, property)
    cursor.execute(query)
