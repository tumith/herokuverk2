from bottle import route, run, template, error, abort, static_file, request
#import bottle
#from bottle import *

@route('/')
def index():
    return """
        <h2>Verkefni 2</h2>
        <p><a href="/a">liður A</a></p>
        <p><a href="/b">liður B</a></p>
        """

@route('/a')
def a():
    return """
       <h2>Verkefni 2.A</h2>
       <a href="/sida/1">Síða 1.</a> -
       <a href="/sida/2">Síða 2.</a> -
       <a href="/sida/3">Síða 3.</a> -
       <a href="/">forsíða</a> -
    """

@route("/sida/<id>")
def page(id):
    if id == '1':
        return "Þetta er siða 1<br><a href='/a'>Til baka</a>"
    elif id == '2':
        return "Þetta er siða 2<br><a href='/a'>Til baka</a>"
    elif id == '3':
        return "Þetta er siða 3<br><a href='/a'>Til baka</a>"
    else:
        abort(404, "<h2 style='color:red'>Þessi siða finnst ekki</h2><h1>ERROR 404</h2>")

############################
@route('/b')
def b():
    return """
        <h2>Verkefni 2.B</h2>
        <h4>Veldu uppáhalds mynd þinn</h4>
        <a href='/sida2?allt=a'><img src='myndir/hmw.png'></a>
        <a href='/sida2?allt=b'><img src='myndir/nal.png'></a>
        <a href='/sida2?allt=c'><img src='myndir/wb.png'></a>
        <a href='/sida2?allt=d'><img src='myndir/apple.png'></a>
        <a href='/'>forsíða</a>
    """

@route('/sida2')
def page():
    l = request.query.allt
    if l == 'a':
        return "<h3>uppáhalds myndin mín er: </h3><img src='myndir/hmw.png'>"
    l = request.query.allt
    if l == 'b':
        return "<h3>uppáhalds myndin mín er: </h3><img src='myndir/nal.png'>"
    l = request.query.allt
    if l == 'c':
        return "<h3>uppáhalds myndin mín er: </h3><img src='myndir/wb.png'>"
    l = request.query.allt
    if l == 'd':
        return "<h3>uppáhalds myndin mín er: </h3><img src='myndir/apple.png'>"

############################

@route('/myndir/<skra>')
def static_skra(skra):
    return static_file(skra, root='myndir')

@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi siða finnst ekki</h2><h1>ERROR 404</h2>"

run(host='localhost' ,port='8060', debug=True)
