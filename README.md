## It's a Unix Image Gallery

You know this. You watch a movie and suddenly they *hack* or *read documents* or reveal pictures. BAMBAMBAMBAMBAM thousand files in a new window.

It makes sense. Like rest of [this](https://www.reddit.com/r/itsaunixsystem/)

This script will query Google for images for a given query, and pop open an image in a new window.

### Why does it exist?

I needed to learn Python some more. 

Plus, I always kind of wanted to write something like this.

#### Road map

##### General ideas
 * Add trigger shortcut to requery for more
 * Add query box that represents the UI
 * Requery for new link when a window closes

##### v1.1 
 * Add progress bar for total hack power
 * Open the images and position them in some order on the screen.
 

### How to use it?

##### Dependencies

Check `requirements` file. 

##### Credentials 
This is kind of complicated. You will want to get few things I do **not** supply since I do not want any quotas exceeded. 

* CX which is a custom search ID from Google. [Amalina9507@gmail.com](http://www.google.com/cse/manage/all). You want to set it up that it does *NOT* search mainly your domain, but the whole Internet.

* Get a developer key  from Google Api Console. Create a project and enable Custom Search Engine.

###### The file

Create a copy of credentials file template
`cp credentials_template.json credentials.json`

Now you can supply the file with proper CX and Dev key.

You can manually supply a different file via `--json-credentials` option

`python3 ./its_a_unix_gallery.py --json-credentials` 

###### Search query

You supply query via `-q` or `--query=` param. 

###### Example!

`python3 ./its_a_unix_gallery.py --query="cyclops amalina9507@gmail.com"`
