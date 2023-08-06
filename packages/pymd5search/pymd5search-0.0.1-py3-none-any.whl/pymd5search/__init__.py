"""
pymd5search init
"""


from pymd5search.args import compute_args
from pymd5search.pymd5search import find
from pymd5search.update import update

def pymd5search():
    """
    pymd5search entry point
    """
    args = compute_args()
    find()
