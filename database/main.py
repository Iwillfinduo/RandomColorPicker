from db_session import global_init, create_session
from sqlalchemy import select, func
from flask import Flask
from flask_restful import Api
from flask_restful import Resource, reqparse
from db import Pallete

app = Flask(__name__)
api = Api(app)


post_parser = reqparse.RequestParser()
post_parser.add_argument('array', type = dict, required=True, action='append')


get_parser = reqparse.RequestParser()
get_parser.add_argument('type', type = str, required=True)

class GlobalDBResourse(Resource):
    def post(self):
        args = post_parser.parse_args()
        for arg in args['array']:
            unique_string = arg["first_color"] + arg["second_color"] + arg["third_color"] + arg["fourth_color"]
            with create_session() as db:
                exists = db.scalar(select(Pallete).where(Pallete.unique_string == unique_string)) is not None
            if not exists:
                with create_session() as db:
                    db.add(Pallete(first_color=arg["first_color"],
                                   second_color=arg["second_color"],
                                   third_color = arg["third_color"],
                                   fourth_color = arg["fourth_color"],
                                   unique_string = unique_string,
                                   likes = arg['likes']))
                    db.commit()
        return 200
        
    def get(self):
        args = get_parser.parse_args()
        if args["type"] == "like":
            with create_session() as db:
                max_likes = func.max(Pallete.likes)
                best_palette = db.scalar(select(Pallete).where(Pallete.likes == select(func.max(Pallete.likes)).scalar_subquery()))
                return {"first_color": best_palette.first_color,
                        "second_color": best_palette.second_color,
                        "third_color": best_palette.third_color,
                        "fourth_color": best_palette.fourth_color,
                        "likes": best_palette.likes} , 200
        else:
            return 400

api.add_resource(GlobalDBResourse, "/database/")


if __name__ == "__main__":
    global_init("data/database.db")
    app.run()