from db_session import global_init, create_session
from sqlalchemy import select, func
from flask import Flask
from flask_restful import Api
from flask_restful import Resource, reqparse
from db import Pallete

app = Flask(__name__)
api = Api(app)

def FormAResponse(Pallete):
    return {"first_color": Pallete.first_color,
            "second_color": Pallete.second_color,
            "third_color": Pallete.third_color,
            "fourth_color": Pallete.fourth_color,
            "likes": Pallete.likes} , 200

post_parser = reqparse.RequestParser()
post_parser.add_argument('array', type = dict, required=True, action='append')


get_parser = reqparse.RequestParser()
get_parser.add_argument('type', type = str, required=True)

class GlobalDBResourse(Resource):
    def post(self):
        args = post_parser.parse_args()
        with create_session() as db:
            for i in range(len(args["array"]) - 1, -1, -1):
                arg = args["array"][i]
                unique_string = arg["first_color"] + arg["second_color"] + arg["third_color"] + arg["fourth_color"]
                exists = db.scalar(select(Pallete).where(Pallete.unique_string == unique_string)) is not None
                if not exists:
                        db.add(Pallete(first_color=arg["first_color"],
                                    second_color=arg["second_color"],
                                    third_color = arg["third_color"],
                                    fourth_color = arg["fourth_color"],
                                    unique_string = unique_string,
                                    likes = int(str(arg['likes']).replace(',', ''))))
                        db.commit()
                else:
                    row = db.scalar(select(Pallete).where(Pallete.unique_string == unique_string))
                    row.likes = int(str(arg['likes']).replace(',', ''))
                    db.commit()
        return 200
        
    def get(self):
        args = get_parser.parse_args()
        if args["type"] == "like":
            with create_session() as db:
                best_palette = db.scalar(select(Pallete).where(Pallete.likes == select(func.max(Pallete.likes)).scalar_subquery()))
                if best_palette != None:
                    return FormAResponse(best_palette)
                else:
                    return None, 200
        elif args["type"] == "time":
            with create_session() as db:
                last_palettes = db.query(Pallete).filter(Pallete.id == select(func.max(Pallete.id)).scalar_subquery())
                if last_palettes == None:
                    return None, 200
                else:
                    last_palette = last_palettes[0]
                    return FormAResponse(last_palette)
        else:
            return 400

api.add_resource(GlobalDBResourse, "/database/")


if __name__ == "__main__":
    global_init("data/database.db")
    app.run(port=4343, host="0.0.0.0")