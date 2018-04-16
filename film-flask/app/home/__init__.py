#coading:uft8
from flask import Blueprint
import sys  
sys.path.append('./') 
home = Blueprint("home",__name__)
import app.home.views