from fastapi import FastAPI, HTTPException

app = FastAPI()

cursos = {
    1: {
        "nome": "Dominando o Python",
        "nivel": "básico",
        "formacao": "PythonFundamentos"
    },
    2: {
        "nome": "Automação de Tarefas",
        "nivel": "intermediário",
        "formacao": "Automação"
    },
    3: {
        "nome": "Automação com Selenium",
        "nivel": "intermediário",
        "formacao": "Automação"
    }
}

# Path parameter
@app.get("/cursos/{formacao}")
async def get_curso_formacao(formacao: str):
    cursos_formacao = [
        curso for curso in cursos.values()
        if curso['formacao'].lower() == formacao.lower()
    ]
    
    return cursos_formacao

# Query Parameter
@app.get('/cursos/')
async def get_cursos_formacao_query(formacao:str):
    cursos_formacao = [
        curso for curso in cursos.values()
        if curso['formacao'].lower() ==formacao.lower()
    ]
    if not cursos_formacao:
        raise HTTPException(
            status_code=404,
            detail="Formação não encontrada"
        )
    return cursos_formacao