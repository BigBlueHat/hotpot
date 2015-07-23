# /

...the one URL you'll have the hardest time overriding...

# /{url}

Seriously, any URL you want. Include `/`'s, etc.

## GET

Guess.

## POST

That's going to depend on the Media Type of both `/{url}` and what you're
sending, but in theory, it will *append* to the `/{url}` you POSTed to.

If it's an Atom feed...or an email inbox, the result is obvious(-ish).

## PUT

Makes a thing. If that thing exists, and you send an `If-Match` header that
...matches...then you update te thing.

## DELETE

Seriously? You need docs for this?

Well...OK.

Be sure to send a `If-Match` or you'll get an error. It's for your own good.
Trust me.

## PATCH

Heh. Later.

## LINK

Actually...this isn't a joke.

Send just `Link` headers (the body gets ignored), and link relationships will
be stored for the resource. Yeah, I know right! Like backlinks on the Web!
Circa...1996 or some such. http://relify.com/
