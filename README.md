# YAYDL
**Y**et **A**nother **Y**outube **D**own**L**oader is a silly name, but does
exactly what it says on the tin. This can search for a youtube video by name,
and then ideally, you can select one of the resulting videos, and download
a corresponding video or audio file from it, in whatever possible quality
and file format.

Motivation for reinventing the wheel is just a demonstration of ability
and refresh of web development skills. For example, PostgreSQL is just used
to store a local database of whatever video or audio files are downloaded, 
there is really no productive purpose of this at the moment. However, I 
was hoping to ultimately create something that was a notch above the other
youtube downloader pages.

How to use locally:
```
git clone https://github.com/jesskas/YAYDL.git
[name of python executable] manage.py runserver
```
Hopefully, provided the expected ports are available, you should simply
be able to visit `http://localhost:8000` and see the page.
