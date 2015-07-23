# HoTPoT

Hyper-object Text Protocol of T...alent?

**Note:** Should be considered pre-experimental partially formed thought code.

## Install

Create a local [Apache CouchDB](http://couchdb.apache.org/) database named
`hotpot` (or update the code...no config yet...sorry...).

Then:
```
$ pip install -r requirements.txt
$ python app.py
```

Do some curl-ing:
```http
PUT /new-doc
Host: localhost:5984

{"some": "content"}
```

## Future

Someday, this will be a super rad Media Type and Link relationship driven
webized database thing in which you could PUT whatever sort of thing, LINK it
to other things, PATCH'em, GET'm, and DELETE'm.

Right now...it just does JSON...

## License

Apache License 2.0
