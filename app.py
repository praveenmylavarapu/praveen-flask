# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:10:26 2019

@author: Praveen
"""

from flask import Flask, request
app = Flask(__name__)

people = {}

@app.route('/')
def homepage():
    return "Hello, World!"

@app.route('/people', methods=['GET'])
def getPeople():
  return "Keys on this node: %s" % '/n'.join(people.keys())

@app.route('/get/<key>', methods=['GET'])
def get(key):
  if key in people:
      val = people[key]
  else:
      val = ''
  return val

@app.route('/put/<key>/', methods=['POST', 'PUT'])
def put(key):
  #key = request.values['name']
  people[key] = request.data#['number']
  return "Added table[%s] = %s" % (key, request.data)

@app.route('/delete/<key>', methods=['DELETE'])
def delete(key):

  people.pop(key)
  return "Deleted table[%s]" % key

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)