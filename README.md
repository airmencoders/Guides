# Guides

This is a template that allows anyone with access to the P1 Static Sites IL-2 Repo (which is practically anyone) to create their own static documentation site.

A working example from which this template derives is here: [AFOTEC OT Guide](https://oteguide.il2.dso.mil/)

The goal is to make it easy for your people to read relevant guidance for their jobs anywhere:  work, home, and on mobile.

Stack:  JS, HTML, CSS.  A React project, it is totally front end/client side, with the exception of a few dependencies and python code for document prep.
- More specifically, this project was made using [Gatsby](https://www.gatsbyjs.com/) and the [Gatsby Gitbook Starter](https://www.gatsbyjs.com/starters/hasura/gatsby-gitbook-starter)

This project requires a basic understanding of JavaScript and React.  The rest is fairly simple:
- read the Gatsby docs
- read the Gitbook starter docs
  - 'Gitbook-readme.md' in this project's root folder has the pertinent bits
- use 'npm install' at the command line to install the dependencies after you've cloned the files onto your machine
- change out the AFOTEC svg for one of your own
- to change and add content, follow the markdown and markdown folder conventions as seen in the folder called 'content_structure_example'
- follow the convention in 'route-otguide.yaml' to instruct the Repo1 server on how to process and display your site

**If this topic interests you, please contact me by raising an issue above**
