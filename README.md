# Guides

This is a template that allows anyone with access to the P1 Static Sites IL-2 Repo (which is practically anyone) to create their own static documentation site.

A working example from which this template derives is here: [AFOTEC OT Guide](https://oteguide.il2.dso.mil/)

The goal is to make it easy for your people to read relevant guidance for their jobs anywhere:  work, home, and on mobile.

## Stack
JS, HTML, CSS.  A React project, it is totally front end/client side, with the exception of a few dependencies and python code for document prep.
- More specifically, this project was made using [Gatsby](https://www.gatsbyjs.com/) and the [Gatsby Gitbook Starter](https://www.gatsbyjs.com/starters/hasura/gatsby-gitbook-starter)

## How to Use
This project requires a basic understanding of JavaScript, Markdown, and React (if you want to make changes).
- read the [Gatsby docs](https://www.gatsbyjs.com/docs)
  - you need to install Gatsby.  It may be as simple as `npm install -g gatsby-cli` at the command line, but to be sure you should first [read the docs](https://www.gatsbyjs.com/docs/tutorial/)
- read the [Gitbook starter](https://github.com/hasura/gatsby-gitbook-starter) docs
  - [Gitbook-readme.md](https://github.com/airmencoders/Guides/blob/master/Gitbook-readme.md) in this project's root folder has the pertinent bits
- clone this repo to your computer
- use `npm install` at the command line to install the dependencies
- change out the AFOTEC svg for one of your own
- to change and add content, follow the markdown and markdown folder conventions as seen in the folder called 'content_structure_example' 
  - the [index](https://github.com/airmencoders/Guides/blob/master/content/index.mdx) file at the root of the content folder is for your initial loading page
- to see your site as you build it, run `gatsby develop`
- to optimize your code for deployment on a server, run `gatsby build`
  - your code should land in a folder called 'public', and this will be the code you'll want to send to be served up on Platform One (not the code you use here in this repo to build it)

### How to Host on Platform One
You'll need an account.  Luckily, P1 offers free accounts for the purpose of talking on Mattermost, use of Confluence, and Jira.  I recommend joining Military Coders by [clicking here](https://chat.il4.dso.mil/signup_user_complete/?id=wdkicxm5ijrcj8uqn6n4pinzse).  Then, ask about how you can become a contributor on Repo1.  Once you have access to Repo1 (free), follow the conventions in the readme on Static Sites.  An example is [here](https://github.com/airmencoders/Guides/blob/master/route-oteguide.yaml) **but don't use this exact example, because that's my site**.  This will instruct the Repo1 server on how to process and display your site.

Note:  Static Sites on Repo1 is for public releasible information only.  There is a blog construct for CUI in the works, but this is not that project.

## Good luck!  Reach out to @agent on MatterMost if you have additional questions or would just like to show me how you are using this template


