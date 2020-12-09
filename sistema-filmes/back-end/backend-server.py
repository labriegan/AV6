from config import *
from models import Filme, Review


@app.route('/get-filmes', methods=['get'])
def get_filmes():
    db_filmes = db.session.query(Filme).all()
    json_filmes = [ filme.json() for filme in db_filmes ]
    response = jsonify(json_filmes)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/create-filmes', methods=['post'])
def create_filmes():
    response = jsonify({"status": "201", "result": "ok", "details": "Filme created"})
    data = request.get_json()
    try:
        new_filme = Filme(**data)
        db.session.add(new_filme)
        db.session.commit()
    except Exception as e:
        response = jsonify({"status": "400", "result": "error", "details ": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response 

@app.route('/delete-filmes/<int:id>', methods=['DELETE'] )
def delete_filmes(id):
    response = jsonify({"status": "200", "result": "ok", "details": "Filme deletado"})
    try:
        Filme.query.filter(Filme.id == id).delete()
        db.session.commit()
    except Exception as e:
        response = jsonify({"status": "400" , "result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/listar_reviews")
def listar_reviews():

    reviews_cadastrados = db.session.query(Review).all()
    lista_jsons = [ x.json() for x in reviews_cadastrados ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

if __name__ == '__main__':
    app.run(debug=True)