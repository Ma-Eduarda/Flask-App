@app.get("/instituicoesensino")
def getInstituicoesEnsino():
    conn = sqlite3.connect (DATABASE_NAME)
    cursor = conn.cursor()
    statement = "select * from tb_instituicao"
    cursor.execute(statement)
    resulset = cursor.fetchall()
    for linha in resulset:
        id = linha[0]
        codigo = linha[1]
        nome = linha[2]
        

    conn.close
