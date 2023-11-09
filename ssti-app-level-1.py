#!/usr/bin/python3

from flask import Flask, request, render_template_string

app = Flask(__name__)

name_dino = ["triceratops", "stegosaurus", "diplodocus", "ankylosaurus", "iguanodon", "brachiosaurus"]

@app.route("/")
def home():
    dinosaure = request.args.get('dinosaure') or None

    Developer_BlackLIST = [ "x5f", "u005F", "U0000005F", "u0073", "subclasses", "_load_form_data", "application", "_", ".", "builtins"]

    if dinosaure == None: return "CAN Y6U H6VE THE Fl7G ? : SuperFl@G.txt"

    for x in Developer_BlackLIST:
      if x in dinosaure:
        return "Il faut toujours viser la lune, car même en cas d’échec, on atterrit dans les étoiles. - Oscar wilde", 400

    template = '''
      <p>Dino Game</p>
      {}
    '''.format(dinosaure)

    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
