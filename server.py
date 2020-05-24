from flask import Flask
from flask_graphql import GraphQLView
from database import read_data
from api.schemas.schema import schema
from api.routes import app

read_data.load_data()

app.add_url_rule(
    '/',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
app.run(debug=True)
