---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  - block: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Postdoctoral Researcher
          company: University of Bremen
          company_url: 'https://www.uni-bremen.de/en/'
          company_logo:
          location: Bremen, Germany
          date_start: '2023-04-01'
          date_end: ''
          description:
        - title: Assistant Lecturer
          company: IT University of Copenhagen
          company_url: 'https://en.itu.dk/'
          company_logo:
          location: Copenhagen, Denmark
          date_start: '2023-09-01'
          date_end: '2023-12-31'
          description:
        - title: PhD Fellow
          company: IT University of Copenhagen
          company_url: 'https://en.itu.dk/'
          company_logo:
          location: Copenhagen, Denmark
          date_start: '2019-08-01'
          date_end: '2022-11-03'
          description:
    design:
      columns: '2'
  - block: collection
    content:
      title: Publications
      count: 0
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  - block: collection
    id: posts
    content:
      title: Blog
      subtitle: ''
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 3
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
      filters:
          folders:
           - post
    design:
      # Choose a layout view
      view: compact
      columns: '2'
  - block: collection
    id: games
    content:
      title: Games
      filters:
         folders:
           - project
      # Choose how many pages you would like to display (0 = all pages)
      count: 0
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
       columns: '1'
       view: showcase
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text:
      # Contact (add or remove contact options as necessary)
      email: dom@domford.net
      # Automatically link email and phone or display as text?
      autolink: true
    design:
      columns: '2'
---
